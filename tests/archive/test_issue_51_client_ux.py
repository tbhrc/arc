import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue51", ROOT / "scripts" / "folderdesk.py")
folderdesk = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(folderdesk)


class Issue51ClientUxTests(unittest.TestCase):
    def data(self):
        return folderdesk.build_onboarding_config(business_name="Acme", owner="acme")

    def test_bootstrap_streams_progress_and_remaining_time(self):
        out = io.StringIO()
        ticks = iter([100.0, 102.0])
        state = [{"name": "acme", "full_name": "acme/acme", "resolved_name": "", "action": "CREATE"}]
        with mock.patch.object(folderdesk, "gh_authenticated", return_value=True), \
             mock.patch.object(folderdesk, "inspect_repository_state", return_value=state), \
             mock.patch.object(folderdesk, "gh_target_operability", return_value=(True, "confirmed")), \
             mock.patch.object(folderdesk, "create_repo", return_value=True), \
             mock.patch.object(folderdesk.time, "monotonic", side_effect=lambda: next(ticks)), \
             contextlib.redirect_stdout(out):
            rc = folderdesk.command_bootstrap(self.data(), True)
        rendered = out.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("GitHub target access: confirmed", rendered)
        self.assertIn("FolderDesk bootstrap starting with 1 configured repository", rendered)
        self.assertIn("[1/1] Checking acme/acme", rendered)
        self.assertIn("estimated remaining", rendered)
        self.assertIn("self-contained baseline Skills", rendered)

    def test_bootstrap_requires_github_in_human_language(self):
        with mock.patch.object(folderdesk, "gh_authenticated", return_value=False):
            with self.assertRaisesRegex(folderdesk.FolderDeskError, "GitHub must be connected/authenticated"):
                folderdesk.command_bootstrap(self.data(), True)

    def test_public_front_door_is_human_first(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("You do not need GitHub experience", readme)
        self.assertIn("Give this to your agent", readme)
        self.assertIn("[Ultimate Features](FEATURES.md)", readme)
        self.assertIn("what you get", readme.lower())

    def test_release_contract_uses_folderdesk_product_name(self):
        releases = (ROOT / "RELEASES.md").read_text(encoding="utf-8")
        self.assertTrue(releases.startswith("# FolderDesk Release Contract"))
        self.assertNotIn("# ARC Release Contract", releases)
        self.assertNotIn("scripts/arc.py", releases)
        self.assertIn("formal FolderDesk release/tag", releases)


if __name__ == "__main__":
    unittest.main()
