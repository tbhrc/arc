import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue51", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class Issue51ClientUxTests(unittest.TestCase):
    def data(self):
        return arc.build_onboarding_config(business_name="Acme", owner="acme")

    def test_bootstrap_streams_progress_and_remaining_time(self):
        out = io.StringIO()
        ticks = iter([100.0, 102.0, 104.0, 106.0, 108.0, 108.0])
        with mock.patch.object(arc, "gh_authenticated", return_value=True), \
             mock.patch.object(arc, "create_repo", return_value=True), \
             mock.patch.object(arc.time, "monotonic", side_effect=lambda: next(ticks)), \
             contextlib.redirect_stdout(out):
            rc = arc.command_bootstrap(self.data(), True)
        rendered = out.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("FolderDesk bootstrap starting", rendered)
        self.assertIn("GitHub connection: confirmed", rendered)
        self.assertIn("Work ahead: 4 configured repositories", rendered)
        self.assertIn("[1/4] Checking acme/skills", rendered)
        self.assertIn("estimated remaining", rendered)
        self.assertIn("[4/4] Complete", rendered)
        self.assertIn("FolderDesk bootstrap complete", rendered)

    def test_bootstrap_requires_github_in_human_language(self):
        with mock.patch.object(arc, "gh_authenticated", return_value=False):
            with self.assertRaisesRegex(arc.ArcError, "GitHub is FolderDesk's first requirement"):
                arc.command_bootstrap(self.data(), True)

    def test_public_front_door_is_human_first(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Step 1 — Connect GitHub", readme)
        self.assertIn("Give this to your agent", readme)
        self.assertIn("[Ultimate Features](FEATURES.md)", readme)
        self.assertIn("what you get", readme.lower())

    def test_release_contract_uses_folderdesk_product_name(self):
        releases = (ROOT / "RELEASES.md").read_text(encoding="utf-8")
        self.assertTrue(releases.startswith("# FolderDesk Release Contract"))
        self.assertNotIn("# ARC Release Contract", releases)
        self.assertIn("formal FolderDesk release/tag", releases)


if __name__ == "__main__":
    unittest.main()
