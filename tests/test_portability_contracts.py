import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PortabilityContractTests(unittest.TestCase):
    def test_generic_profile_version_matches_release_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        profile = json.loads((ROOT / "profiles/generic-business/folderdesk.example.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["folderdesk_version"], version)
        self.assertEqual(profile["repositories"][0]["role"], "workspace")


if __name__ == "__main__":
    unittest.main()
