# Skills Component

Skills are ARC's reusable HOW layer.

A deployed FolderDesk workspace has one editable local Skills home: `.folderdesk/skills/`. Put a Skill directory there (for example `.folderdesk/skills/uae-corporate-tax/SKILL.md`) and keep runtime discovery paths derived; do not edit runtime copies independently. The FolderDesk framework repository itself may keep framework-owned Skills in `.github/skills/`.

`scripts/sync_agent_skills.py` is the concrete adapter. With no arguments it exposes both framework-owned `.github/skills/` and workspace-owned `.folderdesk/skills/`; a workspace Skill wins if the same name exists in both. It mirrors the selected source into each local AI CLI's native discovery path — `.claude/skills/`, `.codex/skills/` (both symlinks) and `.agents/skills.json` (Antigravity's documented per-repo manifest, written best-effort — verify live with `agy --print` before relying on it). Re-run it after adding, renaming or removing a Skill:

```bash
python3 .folderdesk/scripts/sync_agent_skills.py
```

Use `--source <path>` only when a deployment intentionally keeps canonical local Skills somewhere else.

Prefer concise instructions for capable agents. Add deterministic scripts only for proven fragile or machine-interface requirements.

A good Skill answers:

- when it applies;
- what inputs/truth owners it uses;
- what action/outcome it produces;
- safety/approval boundaries;
- how to verify success;
- where to hand off when another capability owns the next step.
