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
            "target": {"owner": "example-org", "owner_type": "org", "default_visibility": "private"},
            "repositories": [{"name": "skills", "role": "skills", "required": True}],
            "domains": [{"name": "sales"}],
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
        data["integrations"] = {"api_token": "do-not-store-secrets-here"}
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
            exists_fn=lambda full_name: full_name == "example-org/skills",
        )
        states = {row["name"]: row["action"] for row in rows}
        self.assertEqual(states["skills"], "REUSE")
        self.assertEqual(states["sales"], "CREATE")

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


if __name__ == "__main__":
    unittest.main()
