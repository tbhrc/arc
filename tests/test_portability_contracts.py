import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PortabilityContractTests(unittest.TestCase):
    def test_generic_profile_version_matches_release_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        profile = json.loads((ROOT / "profiles/generic-business/arc.example.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["arc_version"], version)

    def test_provider_contract_is_not_single_vendor(self):
        text = (ROOT / "providers/README.md").read_text(encoding="utf-8")
        for provider in ("ChatGPT", "Codex", "Claude", "GitHub Copilot"):
            self.assertIn(provider, text)
        self.assertIn("provider-neutral", text.lower())

    def test_runtime_contract_has_normal_and_trusted_routes(self):
        text = (ROOT / "runtimes/README.md").read_text(encoding="utf-8")
        self.assertIn("GitHub-hosted Actions", text)
        self.assertIn("Self-hosted Mac/Linux", text)
        self.assertIn("VPS", text)
        self.assertIn("least privileged", text)

    def test_module_catalogue_is_optional(self):
        text = (ROOT / "modules/README.md").read_text(encoding="utf-8")
        self.assertIn("optional ownership patterns", text)
        self.assertIn("CRM / Sales", text)
        self.assertIn("Recruitment / HR", text)
        self.assertIn("Reporting / BI", text)

    def test_public_readme_tracks_current_release(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"ARC v{version}", text)
        self.assertIn("scripts/seed_foundation.py", text)
        self.assertIn("modules/README.md", text)
        self.assertIn("providers/README.md", text)
        self.assertIn("runtimes/README.md", text)


if __name__ == "__main__":
    unittest.main()
