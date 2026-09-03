import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "seed_foundation.py"
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

    def test_plan_is_non_mutating(self):
        self.assertEqual(foundation.command_plan(self.config()), 0)


if __name__ == "__main__":
    unittest.main()
