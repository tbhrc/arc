import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "sync_agent_skills.py"
spec = importlib.util.spec_from_file_location("sync_agent_skills", MODULE_PATH)
sync = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(sync)


class AgentSkillSyncTests(unittest.TestCase):
    def make_skill(self, source: Path, name: str) -> None:
        path = source / name
        path.mkdir(parents=True)
        (path / "SKILL.md").write_text(f"# {name}\n", encoding="utf-8")

    def test_finds_only_dirs_with_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            (source / "not-a-skill").mkdir(parents=True)
            self.assertEqual(sync.find_skills(source), ["atlas"])

    def test_symlinks_point_into_workspace_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            sync.sync_symlink_target(root, source, ".claude/skills", ["atlas"])
            link = root / ".claude" / "skills" / "atlas"
            self.assertTrue(link.is_symlink())
            self.assertEqual(link.readlink(), Path("../../.folderdesk/skills/atlas"))
            self.assertEqual((link / "SKILL.md").read_text(), "# atlas\n")

    def test_stale_symlink_removed_when_skill_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            sync.sync_symlink_target(root, source, ".claude/skills", ["atlas"])
            sync.sync_symlink_target(root, source, ".claude/skills", [])
            self.assertFalse((root / ".claude" / "skills" / "atlas").exists())

    def test_real_file_never_touched(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            dest = root / ".claude" / "skills"
            dest.mkdir(parents=True)
            (dest / "atlas").mkdir()
            (dest / "atlas" / "local.md").write_text("local\n", encoding="utf-8")
            sync.sync_symlink_target(root, source, ".claude/skills", ["atlas"])
            self.assertFalse((dest / "atlas").is_symlink())
            self.assertEqual((dest / "atlas" / "local.md").read_text(), "local\n")

    def test_agy_manifest_points_at_workspace_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            sync.write_agy_manifest(root, source)
            manifest = json.loads((root / ".agents" / "skills.json").read_text())
            self.assertEqual(manifest, {"entries": [{"path": ".folderdesk/skills"}]})

    def test_idempotent_rerun_produces_no_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            sync.sync_symlink_target(root, source, ".claude/skills", ["atlas"])
            sync.sync_symlink_target(root, source, ".claude/skills", ["atlas"])
            entries = list((root / ".claude" / "skills").iterdir())
            self.assertEqual(len(entries), 1)


if __name__ == "__main__":
    unittest.main()
