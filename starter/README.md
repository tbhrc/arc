# ARC Repository Seed

When `scripts/arc.py bootstrap --apply` creates a **new** repository, it immediately seeds:

- a role-aware `README.md`;
- a root `AGENTS.md`;
- a thin `.github/skills/atlas/SKILL.md` pointer to current ARC;
- a `.github/prompts/atlas.prompt.md` entrypoint.

Existing repositories are never overwritten by bootstrap. Atlas inventories them and proposes integration/migration separately.

The generated text lives in `scripts/arc.py` so the executable bootstrap and its seed contract cannot silently diverge.
