import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Issue52ClientExperienceTests(unittest.TestCase):
    def test_readme_is_concise_front_door_and_handoff(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Start here — Give this to your agent", text)
        self.assertIn("You do not need GitHub experience", text)
        self.assertIn("Open https://github.com/tbhrc/folderdesk", text)
        self.assertIn("Read the root AGENTS.md first", text)
        self.assertIn("Confirm the exact GitHub identity and target owner/path", text)
        self.assertIn("Start with one private workspace repository", text)
        self.assertIn("six core local Skills", text)
        self.assertIn("Do not copy TBHRC private business data or secrets", text)
        self.assertIn("Prove the deployment with one useful real workflow", text)
        self.assertIn("GitHub Platform Capabilities", text)
        self.assertIn("not a first-day FolderDesk requirement", text)
        self.assertNotIn("FolderDesk V5", text)
        self.assertNotIn("showing the remaining-time estimate during bootstrap", text)

    def test_bootstrap_discovers_brand_connectors_tone_and_output(self):
        text = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("representative documents", text)
        self.assertIn("Communication and output preferences", text)
        self.assertIn("Infer, then connect", text)
        self.assertIn("smallest useful connector set", text)
        self.assertIn("our documents are in Google", text)
        self.assertIn("Google Workspace / Google Drive", text)
        self.assertIn("polished DOCX and/or PDF", text)
        self.assertIn("one repository", text.lower())
        self.assertIn("self-contained workspace", text.lower())
        self.assertIn("six local foundational Skills", text)
        self.assertIn("Auditor is not a deployment gate", text)
        self.assertIn("REUSED/UNMANAGED", (ROOT / "VERIFY.md").read_text(encoding="utf-8"))

    def test_client_experience_starter_skill_is_seeded_locally_by_default(self):
        skill = (ROOT / "starter/skills/client-experience/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Assume zero GitHub knowledge", skill)
        self.assertIn("representative documents", skill)
        self.assertIn("polished DOCX", skill)
        self.assertIn("documents are in Google", skill)
        self.assertIn("Google Workspace / Drive", skill)
        self.assertIn("Avoid status theatre", skill)
        seed_spec = importlib.util.spec_from_file_location("folderdesk_seed52", ROOT / "scripts" / "seed_foundation.py")
        seed = importlib.util.module_from_spec(seed_spec)
        assert seed_spec.loader is not None
        seed_spec.loader.exec_module(seed)
        self.assertIn("client-experience", seed.STARTER_SKILLS)
        self.assertIn("auditor", seed.STARTER_SKILLS)
        self.assertIn("structure", seed.STARTER_SKILLS)
        config = {
            "target": {"owner": "acme"},
            "repositories": [{"name": "acme", "role": "workspace"}],
        }
        self.assertEqual(seed.resolve_target(config), ("acme", "acme", ".folderdesk/skills/"))

    def test_features_capture_product_behaviour(self):
        text = (ROOT / "FEATURES.md").read_text(encoding="utf-8")
        self.assertIn("Non-technical client onboarding with GitHub hidden as agent backend", text)
        self.assertIn("Brand learning from formal guidelines or representative documents", text)
        self.assertIn("Communication tone/terminology/detail adaptation", text)
        self.assertIn("Proactive connector inference from client clues", text)
        self.assertIn("Google Workspace / Drive priority", text)
        self.assertIn("Existing-system/connector discovery", text)
        self.assertIn("Polished DOCX/PDF default", text)
        self.assertIn("Backend technical evidence separated", text)


if __name__ == "__main__":
    unittest.main()
