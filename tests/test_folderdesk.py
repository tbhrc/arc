import contextlib
import importlib.util
import io
import json
from pathlib import Path
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "folderdesk.py"
spec = importlib.util.spec_from_file_location("folderdesk_cli", MODULE_PATH)
folderdesk = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folderdesk)


class FolderDeskV2Tests(unittest.TestCase):
    def data(self):
        return folderdesk.build_onboarding_config(
            business_name="Acme Holdings",
            owner="acme",
            domains=["Sales", "Delivery"],
        )

    def test_onboarding_is_single_repo_first(self):
        data = self.data()
        self.assertEqual(data["folderdesk_version"], "2.0.0")
        self.assertEqual(len(data["repositories"]), 1)
        self.assertEqual(data["repositories"][0]["name"], "acme-holdings")
        self.assertEqual(data["repositories"][0]["role"], "workspace")
        self.assertEqual([d["name"] for d in data["domains"]], ["sales", "delivery"])
        self.assertEqual([r["name"] for r in folderdesk.repos_from_config(data)], ["acme-holdings"])

    def test_expansion_repositories_are_explicit_and_supported(self):
        data = self.data()
        data["repositories"].append({
            "name": "research",
            "description": "Explicit research expansion.",
            "role": "research",
            "required": False,
        })
        folderdesk.validate_config(data)
        self.assertEqual([r["name"] for r in folderdesk.repos_from_config(data)], ["acme-holdings", "research"])

    def test_exactly_one_primary_workspace_is_required(self):
        data = self.data()
        data["repositories"][0]["role"] = "research"
        with self.assertRaises(folderdesk.FolderDeskError):
            folderdesk.validate_config(data)

    def test_generated_router_routes_six_local_core_skills(self):
        data = self.data()
        repo = folderdesk.primary_workspace(data)
        agents = folderdesk.generated_agents(data, repo)
        self.assertIn("# AGENTS.md — FolderDesk Router", agents)
        self.assertIn("Domains are local context/folder concerns", agents)
        self.assertIn("Additional repositories are optional expansion", agents)
        for skill in folderdesk.BASELINE_SKILLS:
            self.assertIn(f".folderdesk/skills/{skill}/SKILL.md", agents)
        self.assertIn("Issues are optional continuity", agents)
        self.assertIn("not a recurring gate", agents)
        self.assertNotIn("ARC", agents)
        self.assertNotIn("tbhrc/arc", agents)

    def test_baseline_skill_files_are_self_contained_and_complete(self):
        rows = folderdesk.starter_skill_files()
        self.assertEqual([path for path, _ in rows], [f"{skill}/SKILL.md" for skill in folderdesk.BASELINE_SKILLS])
        self.assertEqual(folderdesk.BASELINE_SKILLS, (
            "structure",
            "skill-builder",
            "lessons",
            "auditor",
            "document-intake",
            "client-experience",
        ))

    def test_managed_marker_uses_folderdesk_identity(self):
        repo = folderdesk.primary_workspace(self.data())
        marker = json.loads(folderdesk.generated_managed_marker(repo))
        self.assertEqual(marker["managed_by"], "FolderDesk")
        self.assertEqual(marker["folderdesk_version"], "2.0.0")
        self.assertEqual(marker["role"], "workspace")

    def test_repository_inspection_refuses_redirected_owner_identity(self):
        data = self.data()
        with mock.patch.object(folderdesk, "gh_authenticated", return_value=True), \
             mock.patch.object(folderdesk, "gh_repo_identity", return_value={
                 "requested": "acme/acme-holdings",
                 "resolved": "old-owner/acme-holdings",
                 "url": "https://github.com/old-owner/acme-holdings",
             }):
            rows = folderdesk.inspect_repository_state(data)
        self.assertEqual(rows[0]["action"], "OWNER_MISMATCH")
        self.assertEqual(rows[0]["resolved_name"], "old-owner/acme-holdings")

    def test_user_target_operability_requires_exact_active_identity(self):
        data = self.data()
        data["target"]["owner_type"] = "user"
        with mock.patch.object(folderdesk, "gh_active_login", return_value="someone-else"):
            ok, detail = folderdesk.gh_target_operability(data)
        self.assertFalse(ok)
        self.assertIn("target user acme", detail)

    def test_verify_does_not_call_unmanaged_exact_repo_broken(self):
        data = self.data()
        identity = {"requested": "acme/acme-holdings", "resolved": "acme/acme-holdings", "url": "u"}
        out = io.StringIO()
        with mock.patch.object(folderdesk, "gh_authenticated", return_value=True), \
             mock.patch.object(folderdesk, "gh_repo_identity", return_value=identity), \
             mock.patch.object(folderdesk, "gh_path_exists", return_value=False), \
             contextlib.redirect_stdout(out):
            rc = folderdesk.command_verify(data)
        self.assertEqual(rc, 0)
        self.assertIn("REUSED/UNMANAGED", out.getvalue())

    def test_verify_requires_all_baseline_skills_for_managed_repo(self):
        data = self.data()
        identity = {"requested": "acme/acme-holdings", "resolved": "acme/acme-holdings", "url": "u"}
        def exists(_full: str, path: str) -> bool:
            if path == ".folderdesk/managed.json":
                return True
            return path != ".folderdesk/skills/auditor/SKILL.md"
        with mock.patch.object(folderdesk, "gh_authenticated", return_value=True), \
             mock.patch.object(folderdesk, "gh_repo_identity", return_value=identity), \
             mock.patch.object(folderdesk, "gh_path_exists", side_effect=exists):
            rc = folderdesk.command_verify(data)
        self.assertEqual(rc, 1)

    def test_manifest_round_trip_uses_folderdesk_names(self):
        data = self.data()
        manifest = folderdesk.manifest_from_config(data)
        self.assertEqual(manifest["manifest_schema"], "2.0")
        self.assertEqual(manifest["folderdesk_version"], "2.0.0")
        self.assertNotIn("arc_version", manifest)
        restored = folderdesk.config_from_manifest(manifest)
        self.assertEqual(restored["folderdesk_version"], "2.0.0")
        self.assertEqual(restored["repositories"][0]["role"], "workspace")
        self.assertEqual(restored["domains"][0]["name"], "sales")

    def test_example_profile_matches_release_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        profile = json.loads((ROOT / "profiles/generic-business/folderdesk.example.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["folderdesk_version"], version)
        self.assertEqual(len(profile["repositories"]), 1)
        self.assertEqual(profile["repositories"][0]["role"], "workspace")


if __name__ == "__main__":
    unittest.main()
