# FolderDesk Repository Seed

When `scripts/folderdesk.py bootstrap --apply` creates a **new** workspace repository, it immediately seeds:

- a workspace `README.md`;
- a compact root `AGENTS.md` Router;
- `work/`, `knowledge/`, `outputs/` and `archive/`;
- `.folderdesk/` for agent support and local reusable Skills;
- a thin `.github/skills/atlas/SKILL.md` pointer to current FolderDesk;
- a `.github/prompts/atlas.prompt.md` entrypoint.

Existing repositories are never overwritten by bootstrap. Additional repositories are created only when they are explicitly present in the FolderDesk profile.

The generated text lives in `scripts/folderdesk.py` so the executable bootstrap and its seed contract cannot silently diverge.
