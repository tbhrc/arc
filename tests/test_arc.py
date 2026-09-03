import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "arc.py"
spec = importlib.util.spec_from_file_location("arc_cli", MODULE_PATH)
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class ArcConfigTests(unittest.TestCase):
    def base(self):
        return {
            "target": {"owner": "example-org", "owner_type": "org", "default_visibility": "private"},
            "repositories": [{"name": "skills", "role": "skills", "required": True}],
            "domains": [{"name": "sales"}],
        }

    def test_valid_config(self):
        arc.validate_config(self.base())

    def test_placeholder_rejected_for_real_deploy(self):
        data = self.base()
        data["target"]["owner"] = "YOUR-GITHUB-ORG"
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_duplicate_repository_rejected(self):
        data = self.base()
        data["domains"] = [{"name": "skills"}]
        with self.assertRaises(arc.ArcError):
            arc.validate_config(data)

    def test_bootstrap_without_apply_is_plan_only(self):
        data = self.base()
        self.assertEqual(arc.command_bootstrap(data, False), 0)


if __name__ == "__main__":
    unittest.main()
