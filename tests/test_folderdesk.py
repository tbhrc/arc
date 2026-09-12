import importlib.util
import json
from pathlib import Path
import unittest

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

    def test_generated_router_is_folderdesk_native_and_single_repo_first(self):
        data = self.data()
        repo = folderdesk.primary_workspace(data)
        agents = folderdesk.generated_agents(data, repo)
        self.assertIn("# AGENTS.md — FolderDesk Router", agents)
        self.assertIn("Domains are local context/folder concerns", agents)
        self.assertIn("Additional repositories are optional expansion", agents)
        self.assertIn(".folderdesk/", agents)
        self.assertNotIn("ARC", agents)
        self.assertNotIn("tbhrc/arc", agents)

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
