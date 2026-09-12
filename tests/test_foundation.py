import importlib.util
from pathlib import Path
import unittest

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
                {"name": "example-business", "role": "workspace"},
            ],
        }

    def test_defaults_to_workspace_local_skills(self):
        self.assertEqual(
            foundation.resolve_target(self.config()),
            ("example-org", "example-business", ".folderdesk/skills/"),
        )

    def test_explicit_skills_repo_remains_supported(self):
        data = self.config()
        data["repositories"].append({"name": "playbooks", "role": "skills"})
        self.assertEqual(foundation.resolve_target(data), ("example-org", "playbooks", ""))

    def test_rejects_placeholder_owner(self):
        data = self.config()
        data["target"]["owner"] = "YOUR-GITHUB-ORG"
        with self.assertRaises(foundation.FoundationError):
            foundation.resolve_target(data)

    def test_rejects_missing_workspace_or_skills_owner(self):
        data = self.config()
        data["repositories"] = [{"name": "research", "role": "research"}]
        with self.assertRaises(foundation.FoundationError):
            foundation.resolve_target(data)

    def test_starter_skill_files_are_self_contained_baseline(self):
        rows = foundation.starter_files()
        self.assertEqual(len(rows), 6)
        paths = {path for path, _ in rows}
        self.assertEqual(paths, {
            "structure/SKILL.md",
            "skill-builder/SKILL.md",
            "lessons/SKILL.md",
            "auditor/SKILL.md",
            "document-intake/SKILL.md",
            "client-experience/SKILL.md",
        })
        self.assertNotIn("owner-router/SKILL.md", paths)
        self.assertNotIn("github-workflow/SKILL.md", paths)
        self.assertNotIn("research-escalation/SKILL.md", paths)

    def test_plan_is_non_mutating(self):
        self.assertEqual(foundation.command_plan(self.config()), 0)


if __name__ == "__main__":
    unittest.main()
