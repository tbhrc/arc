import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PortabilityContractTests(unittest.TestCase):
    def test_generic_profile_version_matches_release_version(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        profile = json.loads((ROOT / "profiles/generic-business/arc.example.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["arc_version"], version)


if __name__ == "__main__":
    unittest.main()
