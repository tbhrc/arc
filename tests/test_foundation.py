import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "seed_foundation.py"
spec = importlib.util.spec_from_file_location("seed_foundation", MODULE_PATH)
foundation = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(foundation)


class FoundationTests(unittest.TestCase):
    def config(self):
        return {
            "target": {"owner": "example-org"},
            "repositories": [
                {"name": "playbooks", "role": "skills"},
                {"name": "research", "role": "research"},
            ],
        }

    def test_resolves_configured_skills_owner(self):
        self.assertEqual(foundation.resolve_target(self.config()), ("example-org", "playbooks"))

    def test_rejects_placeholder_owner(self):
        data = self.config()
        data["target"]["owner"] = "YOUR-GITHUB-ORG"
        with self.assertRaises(foundation.FoundationError):
            foundation.resolve_target(data)

    def test_rejects_missing_skills_role(self):
        data = self.config()
        data["repositories"] = [{"name": "research", "role": "research"}]
        with self.assertRaises(foundation.FoundationError):
            foundation.resolve_target(data)

    def test_starter_skill_files_exist(self):
        rows = foundation.starter_files()
        self.assertEqual(len(rows), 4)
        paths = {path for path, _ in rows}
        self.assertIn("owner-router/SKILL.md", paths)
        self.assertIn("research-escalation/SKILL.md", paths)

    def test_starter_routing_contract_has_north_star_and_fast_links(self):
        owner_router = (ROOT / "starter/skills/owner-router/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("North Star", owner_router)
        self.assertIn("Fast Links", owner_router)

    def test_starter_github_workflow_has_anti_drift_and_issue_contract(self):
        workflow = (ROOT / "starter/skills/github-workflow/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Anti-Drift — Original Objective", workflow)
        for heading in (
            "North Star",
            "Local Objective",
            "Checklist",
            "Acceptance Criteria",
            "Current Status",
            "Exact Next Action",
        ):
            self.assertIn(heading, workflow)

    def test_repository_durable_work_template_has_canonical_sections(self):
        template = (ROOT / ".github/ISSUE_TEMPLATE/durable-work.md").read_text(encoding="utf-8")
        required = (
            "## North Star",
            "## Anti-Drift — Original Objective",
            "## Local Objective",
            "## Checklist",
            "## Acceptance Criteria",
            "## Current Status",
            "## Exact Next Action",
        )
        for heading in required:
            self.assertIn(heading, template)

    def test_repository_issue_template_does_not_hard_code_tbhrc_top_five(self):
        template = (ROOT / ".github/ISSUE_TEMPLATE/durable-work.md").read_text(encoding="utf-8")
        self.assertNotIn("CREATE VALUE", template)
        self.assertNotIn("GENERATE REVENUE", template)
        self.assertNotIn("EXECUTE THE MISSION", template)

    def test_plan_is_non_mutating(self):
        self.assertEqual(foundation.command_plan(self.config()), 0)


if __name__ == "__main__":
    unittest.main()
