import contextlib
import importlib.util
import io
import pathlib
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue50", ROOT / "scripts" / "folderdesk.py")
folderdesk = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folderdesk)


class Issue50LastMileTests(unittest.TestCase):
    def test_seeded_router_is_folderdesk_native_and_workspace_first(self):
        data = folderdesk.build_onboarding_config(business_name="Acme", owner="acme")
        repo = folderdesk.primary_workspace(data)
        agents = folderdesk.generated_agents(data, repo)
        self.assertIn("https://github.com/tbhrc/folderdesk", agents)
        self.assertIn("Domains are local context/folder concerns", agents)
        self.assertIn("Additional repositories are optional expansion", agents)
        self.assertNotIn("https://github.com/tbhrc/arc", agents)
        self.assertNotIn("ARC", agents)

    def test_atlas_pointer_uses_folderdesk_upstream(self):
        pointer = folderdesk.generated_atlas_pointer()
        self.assertIn("tbhrc/folderdesk", pointer)
        self.assertNotIn("tbhrc/arc", pointer)
        self.assertNotIn("ARC", pointer)

    def test_doctor_connectors_exposes_declared_last_mile_without_gate(self):
        data = folderdesk.build_onboarding_config(
            business_name="Acme",
            owner="acme",
            private_files="SharePoint",
            specialist_systems=["HubSpot", "Composio MCP"],
            memory="Hindsight",
        )
        out = io.StringIO()
        with mock.patch.object(folderdesk, "gh_available", return_value=True), \
             mock.patch.object(folderdesk, "gh_authenticated", return_value=True), \
             contextlib.redirect_stdout(out):
            rc = folderdesk.command_doctor(data, connectors=True)
        rendered = out.getvalue()
        self.assertEqual(0, rc)
        self.assertIn("Connection readiness (read-only; not a deployment gate)", rendered)
        self.assertIn("GitHub: WIRED", rendered)
        self.assertIn("DECLARED SharePoint", rendered)
        self.assertIn("DECLARED HubSpot", rendered)
        self.assertIn("DECLARED Composio MCP", rendered)
        self.assertIn("external wiring UNVERIFIED", rendered)


if __name__ == "__main__":
    unittest.main()
