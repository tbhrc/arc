import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync_public_skills.py"
spec = importlib.util.spec_from_file_location("sync_public_skills", MODULE_PATH)
sync = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(sync)


class PublicSkillSyncTests(unittest.TestCase):
    def make_skill(self, root: Path, name: str, body: str = "# Test\n") -> None:
        path = root / name
        path.mkdir(parents=True)
        (path / "SKILL.md").write_text(body, encoding="utf-8")

    def test_allowlisted_skill_copies_exactly_and_preserves_local_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "dest"
            self.make_skill(source, "public-one", "# Canonical\n")
            self.make_skill(dest, "atlas", "# Local\n")
            sync.validate_sources(source, ["public-one"])
            sync.apply_sync(source, dest, ["public-one"])
            unexpected, drift = sync.inspect(source, dest, ["atlas"], ["public-one"])
            self.assertEqual(unexpected, [])
            self.assertEqual(drift, [])
            self.assertEqual((dest / "atlas" / "SKILL.md").read_text(), "# Local\n")

    def test_unexpected_public_skill_fails_boundary_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "dest"
            self.make_skill(source, "public-one")
            self.make_skill(dest, "atlas")
            self.make_skill(dest, "talent-bridge-internal")
            unexpected, drift = sync.inspect(source, dest, ["atlas"], ["public-one"])
            self.assertEqual(unexpected, ["talent-bridge-internal"])
            self.assertEqual(drift, ["public-one"])

    def test_selected_skill_drift_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source"
            dest = root / "dest"
            self.make_skill(source, "public-one", "# New\n")
            self.make_skill(dest, "public-one", "# Old\n")
            unexpected, drift = sync.inspect(source, dest, [], ["public-one"])
            self.assertEqual(unexpected, [])
            self.assertEqual(drift, ["public-one"])

    def test_manifest_rejects_preserve_sync_overlap(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            path.write_text(json.dumps({"destination": ".github/skills", "preserve": ["atlas"], "skills": ["atlas"]}), encoding="utf-8")
            with self.assertRaises(sync.SyncError):
                sync.load_manifest(path)


if __name__ == "__main__":
    unittest.main()
