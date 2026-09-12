import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocumentIntakeDefaultTests(unittest.TestCase):
    def test_starter_document_intake_skill_exists_and_requires_retrieval(self):
        text = (ROOT / "starter/skills/document-intake/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("by default whenever a user gives the agent a file/document", text)
        self.assertIn("FILE SOURCE", text)
        self.assertIn("VERIFY RETRIEVAL", text)
        self.assertIn("inventory, not ingestion", text.lower())
        self.assertIn("provenance", text.lower())

    def test_foundation_seeds_document_intake_into_workspace_by_default(self):
        spec = importlib.util.spec_from_file_location("folderdesk_seed", ROOT / "scripts" / "seed_foundation.py")
        seed = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(seed)
        self.assertIn("document-intake", seed.STARTER_SKILLS)
        paths = [path for path, _ in seed.starter_files()]
        self.assertIn("document-intake/SKILL.md", paths)
        config = {
            "target": {"owner": "acme"},
            "repositories": [{"name": "acme", "role": "workspace"}],
        }
        self.assertEqual(seed.resolve_target(config), ("acme", "acme", ".folderdesk/skills/"))

    def test_public_product_surfaces_file_task_memory_behaviour(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        features = (ROOT / "FEATURES.md").read_text(encoding="utf-8")
        bootstrap = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("filing/retrieval", readme)
        self.assertIn("If I give you a file/document", readme)
        self.assertIn("verify I can retrieve it later", readme)
        self.assertIn("file source/output", bootstrap)
        self.assertIn("verify retrieval", bootstrap)
        self.assertIn("Default client file/document intake", features)
        self.assertIn("Retrieve source documents and derived organisational knowledge later", features)
        self.assertIn("Admin-chaos reduction", features)


if __name__ == "__main__":
    unittest.main()
