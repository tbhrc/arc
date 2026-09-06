import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "arc.py"
spec = importlib.util.spec_from_file_location("arc_cli", MODULE_PATH)
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class ArcConfigTests(unittest.TestCase):
    def base(self):
        return {
            "arc_version": "0.3.0",
            "target": {
                "business_name": "Example Business",
                "owner": "example-org",
                "owner_type": "org",
                "default_visibility": "private",
            },
            "repositories": [
                {"name": "skills", "role": "skills", "required": True},
                {"name": "research", "role": "research", "required": True},
            ],
            "domains": [{"name": "sales"}],
            "integrations": {
                "private_files": "SharePoint",
                "specialist_systems": ["HubSpot", "Xero"],
                "memory": "optional",
            },
        }

    def test_valid_config(self):
        arc.validate_config(self.base())

    def test_placeholder_rejected_for_real_deploy(self):
        data = self.base()
        data["target"]["owner"] = "YOUR-GITHUB-ORG"
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_duplicate_repository_rejected(self):
        data = self.base()
        data["domains"] = [{"name": "skills"}]
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_secret_like_field_rejected(self):
        data = self.base()
        data["integrations"]["api_token"] = "do-not-store-secrets-here"
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_known_credential_value_pattern_rejected(self):
        data = self.base()
        data["integrations"]["private_files"] = "github_pat_123456789012345678901234567890"
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_onboarding_config_is_valid_and_slugs_domains(self):
        data = arc.build_onboarding_config(
            business_name="Example Business",
            owner="example-org",
            domains=["Sales & Marketing", "Client Delivery"],
            private_files="SharePoint",
            specialist_systems=["HubSpot", "Xero"],
        )
        arc.validate_config(data)
        self.assertEqual(data["target"]["business_name"], "Example Business")
        self.assertEqual([row["name"] for row in data["domains"]], ["sales-marketing", "client-delivery"])
        self.assertEqual(data["integrations"]["specialist_systems"], ["HubSpot", "Xero"])

    def test_write_config_refuses_implicit_overwrite(self):
        data = self.base()
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "arc.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(arc.ArcError):
                arc.write_config(data, str(path))
            arc.write_config(data, str(path), overwrite=True)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["target"]["owner"], "example-org")

    def test_repository_inspection_classifies_reuse_and_create(self):
        data = self.base()
        rows = arc.inspect_repository_state(
            data,
            exists_fn=lambda full_name: full_name in {"example-org/skills", "example-org/sales"},
        )
        states = {row["name"]: row["action"] for row in rows}
        self.assertEqual(states["skills"], "REUSE")
        self.assertEqual(states["research"], "CREATE")
        self.assertEqual(states["sales"], "REUSE")

    def test_atlas_modes_are_stable(self):
        self.assertEqual(
            set(arc.ATLAS_MODES),
            {"onboard", "adopt", "audit", "health", "upgrade", "recover", "next"},
        )

    def test_bootstrap_without_apply_is_preview(self):
        data = self.base()
        with mock.patch("builtins.print") as print_mock:
            self.assertEqual(arc.command_bootstrap(data, False), 0)
        messages = [call.args[0] for call in print_mock.call_args_list]
        self.assertEqual(
            messages[0],
            "ARC bootstrap preview: no mutation selected. Use --apply to create missing repositories.",
        )
        self.assertNotIn("approval", " ".join(messages).lower())
        self.assertNotIn("plan-only", " ".join(messages).lower())

    def test_generated_repository_router_links_core_owners_and_routes_conditionally(self):
        repo = {"name": "sales", "role": "business-domain", "description": "Sales owner.", "required": True, "visibility": "private"}
        navigation = {"skills": "playbooks", "research": "lab"}
        readme = arc.generated_readme("acme", repo, navigation)
        agents = arc.generated_agents("acme", repo, navigation)
        self.assertIn("acme/playbooks", readme)
        self.assertTrue(agents.startswith("# AGENTS.md — Repository Router\n"))
        self.assertIn("https://github.com/acme/playbooks", agents)
        self.assertIn("acme/lab", agents)
        self.assertIn("https://github.com/acme/sales/issues", agents)
        self.assertIn("Known owner + bounded task", agents)
        self.assertIn("Owner or source unclear", agents)
        self.assertIn("Level 0 Direct", agents)
        self.assertIn("Ordinary already-authorised bounded work executes directly; do not ask twice", agents)
        self.assertIn("only when Hybrid or Controlled may be needed", agents)
        self.assertIn("Multiple agents, specialist delegation or genuine parallel work", agents)
        self.assertIn("Onboarding, adoption or recovery", agents)
        self.assertIn("it is not the daily routing layer", agents)
        self.assertNotIn("ARC Agent Contract", agents)
        self.assertNotIn("## Operating loop", agents)

    def test_generated_atlas_surfaces_use_direct_authority_semantics(self):
        pointer = arc.generated_atlas_pointer()
        prompt = arc.generated_atlas_prompt()
        for surface in (pointer, prompt):
            self.assertIn("Inspect/plan when useful", surface)
            self.assertIn("current instruction is sufficient authority for ordinary bounded work", surface)
            self.assertIn("`--apply` is a deliberate mutation-mode selector", surface)
            self.assertIn(
                "Fresh authority is required only at real destructive/root/private-data/spend/legal/client-commitment boundaries",
                surface,
            )
            self.assertNotIn("start in plan mode", surface)
            self.assertNotIn("start in non-mutating plan mode", surface)

    def test_cli_description_is_not_plan_first(self):
        description = arc.parser().description
        self.assertEqual(description, "ARC deployment and recovery utility")
        self.assertNotIn("plan-first", description.lower())


class ArcSafeHarbourTests(unittest.TestCase):
    def base(self):
        return ArcConfigTests().base()

    def test_manifest_round_trip_preserves_topology_and_external_owner_names(self):
        data = self.base()
        manifest = arc.manifest_from_config(
            data,
            inspect_target=True,
            exists_fn=lambda full_name: full_name in {"example-org/skills", "example-org/sales"},
        )
        arc.validate_manifest(manifest)
        restored = arc.config_from_manifest(manifest)
        arc.validate_config(restored)

        self.assertEqual(manifest["manifest_schema"], "1.0")
        self.assertEqual(manifest["target"]["owner"], "example-org")
        self.assertEqual(manifest["integrations"]["private_files"], "SharePoint")
        self.assertEqual(manifest["integrations"]["specialist_systems"], ["HubSpot", "Xero"])
        self.assertEqual(restored["target"]["owner"], data["target"]["owner"])
        self.assertEqual({r["name"] for r in restored["repositories"]}, {"skills", "research"})
        self.assertEqual({d["name"] for d in restored["domains"]}, {"sales"})

        states = {row["name"]: row["observed_action"] for row in manifest["repositories"]}
        self.assertEqual(states["skills"], "REUSE")
        self.assertEqual(states["research"], "CREATE")
        self.assertEqual(states["sales"], "REUSE")

    def test_manifest_has_explicit_recovery_exclusions(self):
        manifest = arc.manifest_from_config(self.base())
        exclusions = set(manifest["recovery"]["excluded_material"])
        self.assertIn("credential values", exclusions)
        self.assertIn("private-file contents", exclusions)
        self.assertIn("CRM/ERP/ATS/accounting records", exclusions)
        self.assertFalse(manifest["observation"]["repository_state_observed"])

    def test_manifest_rejects_secret_like_extension(self):
        manifest = arc.manifest_from_config(self.base())
        manifest["integrations"]["access_token"] = "bad"
        with self.assertRaises(arc.ArcError):
            arc.validate_manifest(manifest)

    def test_manifest_rejects_unsupported_schema(self):
        manifest = arc.manifest_from_config(self.base())
        manifest["manifest_schema"] = "2.0"
        with self.assertRaises(arc.ArcError):
            arc.validate_manifest(manifest)

    def test_write_manifest_refuses_implicit_overwrite(self):
        manifest = arc.manifest_from_config(self.base())
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "estate.json"
            arc.write_manifest(manifest, str(path))
            with self.assertRaises(arc.ArcError):
                arc.write_manifest(manifest, str(path))
            arc.write_manifest(manifest, str(path), overwrite=True)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["manifest_schema"], "1.0")

    def test_restore_without_apply_is_destructive_boundary_preview(self):
        manifest = arc.manifest_from_config(self.base())
        with mock.patch("builtins.print") as print_mock:
            self.assertEqual(arc.command_restore(manifest, apply=False), 0)
        messages = [call.args[0] for call in print_mock.call_args_list]
        self.assertEqual(
            messages[0],
            "ARC recovery preview: no mutation selected. Destructive repository reconstruction requires explicit authority before `restore --apply`.",
        )
        self.assertIn("destructive", messages[0].lower())


if __name__ == "__main__":
    unittest.main()
