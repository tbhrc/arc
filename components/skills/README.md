# Skills Component

Skills are ARC's reusable HOW layer.

A deployed organisation should nominate one editable canonical Skills home (this repo's own: `.github/skills/`). Runtime copies/adapters may exist, but should not become independently edited canon.

`scripts/sync_agent_skills.py` is the concrete adapter: it mirrors the canonical Skills home into each local AI CLI's own native discovery path — `.claude/skills/`, `.codex/skills/` (both symlinks) and `.agents/skills.json` (Antigravity's documented per-repo manifest, written best-effort — verify live with `agy --print` before relying on it). Re-run it after adding, renaming or removing a Skill.

Prefer concise instructions for capable agents. Add deterministic scripts only for proven fragile or machine-interface requirements.

A good Skill answers:

- when it applies;
- what inputs/truth owners it uses;
- what action/outcome it produces;
- safety/approval boundaries;
- how to verify success;
- where to hand off when another capability owns the next step.
