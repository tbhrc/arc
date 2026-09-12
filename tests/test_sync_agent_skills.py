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
    def make_skill(self, source: Path, name: str, body: str | None = None) -> None:
        path = source / name
        path.mkdir(parents=True)
        (path / "SKILL.md").write_text(body or f"# {name}\n", encoding="utf-8")

    def test_finds_only_dirs_with_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            (source / "not-a-skill").mkdir(parents=True)
            self.assertEqual(sync.find_skills(source), ["atlas"])

    def test_framework_and_workspace_skills_are_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            framework = root / ".github" / "skills"
            workspace = root / ".folderdesk" / "skills"
            self.make_skill(framework, "atlas")
            self.make_skill(workspace, "tax")
            found = sync.collect_skills([framework, workspace])
            self.assertEqual(set(found), {"atlas", "tax"})
            self.assertEqual(found["atlas"], framework)
            self.assertEqual(found["tax"], workspace)

    def test_workspace_skill_wins_name_collision(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            framework = root / ".github" / "skills"
            workspace = root / ".folderdesk" / "skills"
            self.make_skill(framework, "atlas", "framework\n")
            self.make_skill(workspace, "atlas", "workspace\n")
            found = sync.collect_skills([framework, workspace])
            self.assertEqual(found["atlas"], workspace)

    def test_symlinks_point_to_each_owning_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            framework = root / ".github" / "skills"
            workspace = root / ".folderdesk" / "skills"
            self.make_skill(framework, "atlas")
            self.make_skill(workspace, "tax")
            found = sync.collect_skills([framework, workspace])
            sync.sync_symlink_target(root, found, ".claude/skills")
            self.assertEqual((root / ".claude/skills/atlas").readlink(), Path("../../.github/skills/atlas"))
            self.assertEqual((root / ".claude/skills/tax").readlink(), Path("../../.folderdesk/skills/tax"))

    def test_stale_symlink_removed_when_skill_deleted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            sync.sync_symlink_target(root, {"atlas": source}, ".claude/skills")
            sync.sync_symlink_target(root, {}, ".claude/skills")
            self.assertFalse((root / ".claude/skills/atlas").exists())

    def test_real_file_never_touched(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            dest = root / ".claude" / "skills"
            dest.mkdir(parents=True)
            (dest / "atlas").mkdir()
            (dest / "atlas" / "local.md").write_text("local\n", encoding="utf-8")
            sync.sync_symlink_target(root, {"atlas": source}, ".claude/skills")
            self.assertFalse((dest / "atlas").is_symlink())
            self.assertEqual((dest / "atlas/local.md").read_text(), "local\n")

    def test_agy_manifest_lists_both_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            framework = root / ".github" / "skills"
            workspace = root / ".folderdesk" / "skills"
            self.make_skill(framework, "atlas")
            self.make_skill(workspace, "tax")
            sync.write_agy_manifest(root, [framework, workspace])
            manifest = json.loads((root / ".agents/skills.json").read_text())
            self.assertEqual(manifest, {"entries": [{"path": ".github/skills"}, {"path": ".folderdesk/skills"}]})

    def test_idempotent_rerun_produces_no_duplicates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / ".folderdesk" / "skills"
            self.make_skill(source, "atlas")
            found = {"atlas": source}
            sync.sync_symlink_target(root, found, ".claude/skills")
            sync.sync_symlink_target(root, found, ".claude/skills")
            entries = list((root / ".claude/skills").iterdir())
            self.assertEqual(len(entries), 1)


if __name__ == "__main__":
    unittest.main()
