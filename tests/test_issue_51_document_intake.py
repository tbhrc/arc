import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_doc_intake", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class DocumentIntakeDefaultTests(unittest.TestCase):
    def test_starter_document_intake_skill_exists_and_requires_retrieval(self):
        text = (ROOT / "starter/skills/document-intake/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("by default whenever a user gives the agent a file/document", text)
        self.assertIn("FILE SOURCE", text)
        self.assertIn("VERIFY RETRIEVAL", text)
        self.assertIn("inventory, not ingestion", text.lower())
        self.assertIn("provenance", text.lower())

    def test_foundation_seeds_document_intake(self):
        spec2 = importlib.util.spec_from_file_location("folderdesk_seed", ROOT / "scripts" / "seed_foundation.py")
        seed = importlib.util.module_from_spec(spec2)
        assert spec2.loader is not None
        spec2.loader.exec_module(seed)
        self.assertIn("document-intake", seed.STARTER_SKILLS)
        paths = [path for path, _ in seed.starter_files()]
        self.assertIn("document-intake/SKILL.md", paths)

    def test_generated_agent_router_has_default_file_route(self):
        repo = {"name": "ops", "role": "operations", "description": "Ops", "required": True, "visibility": "private"}
        agents = arc.generated_agents("acme", repo, {"skills": "skills", "research": "research"})
        self.assertIn("[Document Intake](https://github.com/acme/skills/tree/main/document-intake)", agents)
        self.assertIn("User gives you a file/document", agents)
        self.assertIn("verify the source and derived knowledge can be retrieved later", agents)
        self.assertIn("Inventory alone is not ingestion", agents)

    def test_public_product_surfaces_file_task_memory_positioning(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        features = (ROOT / "FEATURES.md").read_text(encoding="utf-8")
        self.assertIn("task-management, filing and organisational-memory system", readme)
        self.assertIn("Give FolderDesk a file", readme)
        self.assertIn("find it again later", readme)
        self.assertIn("Default client file/document intake", features)
        self.assertIn("Retrieve source documents and derived organisational knowledge later", features)
        self.assertIn("Admin-chaos reduction", features)


if __name__ == "__main__":
    unittest.main()
