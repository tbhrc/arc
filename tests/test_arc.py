import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

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

    def test_bootstrap_without_apply_is_plan_only(self):
        data = self.base()
        self.assertEqual(arc.command_bootstrap(data, False), 0)

    def test_generated_repository_contract_links_core_owners(self):
        repo = {"name": "sales", "role": "business-domain", "description": "Sales owner.", "required": True, "visibility": "private"}
        navigation = {"skills": "playbooks", "research": "lab"}
        readme = arc.generated_readme("acme", repo, navigation)
        agents = arc.generated_agents("acme", repo, navigation)
        self.assertIn("acme/playbooks", readme)
        self.assertIn("acme/lab", agents)
        self.assertIn("Atlas", agents)


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

    def test_restore_without_apply_is_plan_only(self):
        manifest = arc.manifest_from_config(self.base())
        self.assertEqual(arc.command_restore(manifest, apply=False), 0)


if __name__ == "__main__":
    unittest.main()
