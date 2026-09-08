import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue52", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class Issue52ClientExperienceTests(unittest.TestCase):
    def test_readme_starts_from_agent_not_client_github_operation(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Start here — Give this to your agent", text)
        self.assertIn("You do not need GitHub experience", text)
        self.assertIn("Assume I have never used GitHub", text)
        self.assertIn("Do not teach me GitHub unless I ask", text)
        self.assertNotIn("## Step 1 — Connect GitHub", text)

    def test_bootstrap_discovers_brand_connectors_tone_and_output(self):
        text = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("representative documents", text)
        self.assertIn("Communication and output preferences", text)
        self.assertIn("Infer, then connect, the systems", text)
        self.assertIn("smallest useful connector set", text)
        self.assertIn("documents are in Google", text)
        self.assertIn("Google Workspace / Google Drive", text)
        self.assertIn("before asking the client to manually reproduce that context", text)
        self.assertIn("polished DOCX and/or PDF", text)

    def test_client_experience_starter_skill_is_seeded(self):
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

    def test_generated_router_inherits_client_experience(self):
        repo = {"name": "sales", "role": "business-domain", "description": "Sales", "required": True, "visibility": "private"}
        agents = arc.generated_agents("acme", repo, {"skills": "skills", "research": "research"})
        self.assertIn("[Client Experience](https://github.com/acme/skills/tree/main/client-experience)", agents)
        self.assertIn("Client-facing onboarding, status or business artifact", agents)
        self.assertIn("polished DOCX/PDF", agents)
        self.assertIn("keep technical evidence behind the scenes", agents)

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
