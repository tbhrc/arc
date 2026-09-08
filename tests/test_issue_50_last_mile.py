import contextlib
import importlib.util
import io
import pathlib
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("arc_issue50", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)

class Issue50LastMileTests(unittest.TestCase):
    def test_seeded_router_uses_target_owner_skills_and_folderdesk_upstream(self):
        repo = {"name": "sales", "role": "business-domain", "description": "Sales owner.", "required": True, "visibility": "private"}
        navigation = {"skills": "playbooks", "research": "lab"}
        agents = arc.generated_agents("acme", repo, navigation)
        self.assertIn("https://github.com/acme/playbooks/tree/main/github-agent-workflow", agents)
        self.assertIn("https://github.com/acme/playbooks/blob/main/human-ai-operations-map/references/ai-sniper-entry-map.md", agents)
        self.assertIn("https://github.com/acme/playbooks/tree/main/github-multi-agent-orchestrator", agents)
        self.assertIn("https://github.com/tbhrc/folderdesk", agents)
        self.assertNotIn("https://github.com/tbhrc/arc", agents)

    def test_atlas_pointer_uses_folderdesk_upstream(self):
        pointer = arc.generated_atlas_pointer()
        self.assertIn("tbhrc/folderdesk", pointer)
        self.assertNotIn("tbhrc/arc", pointer)

    def test_doctor_connectors_exposes_declared_last_mile_without_gate(self):
        data = arc.build_onboarding_config(business_name="Acme", owner="acme", private_files="SharePoint", specialist_systems=["HubSpot", "Composio MCP"], memory="Hindsight")
        data["runtimes"] = ["github-hosted-actions"]
        out = io.StringIO()
        with mock.patch.object(arc, "gh_available", return_value=True), mock.patch.object(arc, "gh_authenticated", return_value=True), contextlib.redirect_stdout(out):
            rc = arc.command_doctor(data, connectors=True)
        rendered = out.getvalue()
        self.assertEqual(0, rc)
        self.assertIn("Connection readiness (read-only; not a deployment gate)", rendered)
        self.assertIn("GitHub: WIRED", rendered)
        self.assertIn("DECLARED SharePoint", rendered)
        self.assertIn("DECLARED HubSpot", rendered)
        self.assertIn("DECLARED Composio MCP", rendered)
        self.assertIn("DECLARED github-hosted-actions", rendered)
        self.assertIn("external wiring UNVERIFIED", rendered)

if __name__ == "__main__":
    unittest.main()
