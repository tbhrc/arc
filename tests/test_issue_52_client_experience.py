import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class Issue52ClientExperienceTests(unittest.TestCase):
    def test_readme_is_concise_front_door_and_handoff(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Start here — Give this to your agent", text)
        self.assertIn("You do not need GitHub experience", text)
        self.assertIn("Open https://github.com/tbhrc/folderdesk and help me deploy FolderDesk into my GitHub organisation.", text)
        self.assertIn("Read the root AGENTS.md first", text)
        self.assertIn("First confirm that you can access and operate on my target GitHub organisation/account.", text)
        self.assertIn("showing the remaining-time estimate during bootstrap", text)
        self.assertIn("Do not copy TBHRC private business data or secrets", text)
        self.assertIn("treat it as a FolderDesk intake event", text)
        self.assertIn("verification status, connection readiness and the next useful capability to activate", text)
        self.assertIn("detailed deployment behaviour belongs in [Get Started / Bootstrap](BOOTSTRAP.md)", text)
        self.assertNotIn("Assume I have never used GitHub", text)
        self.assertNotIn("documents are in Google", text)
        self.assertNotIn("Avoid status theatre", text)

    def test_bootstrap_discovers_brand_connectors_tone_and_output(self):
        text = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("representative documents", text)
        self.assertIn("Communication and output preferences", text)
        self.assertIn("Infer, then connect", text)
        self.assertIn("smallest useful connector set", text)
        self.assertIn("documents are in Google", text)
        self.assertIn("Google Workspace / Google Drive", text)
        self.assertIn("before asking the client to manually reproduce that context", text)
        self.assertIn("polished DOCX and/or PDF", text)
        self.assertIn("The client should not need to know or operate GitHub", text)
        self.assertIn("single repository", text.lower())

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
