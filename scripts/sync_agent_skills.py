#!/usr/bin/env python3
"""Expose FolderDesk Skills through each local agent's native discovery path.

A deployed workspace keeps editable local Skills under `.folderdesk/skills/`.
Framework-owned pointer Skills may also live under `.github/skills/`. With no
`--source`, both homes are exposed and a workspace Skill wins if the same name
exists in both places. `--source` selects one explicit non-standard source.

Derived targets:

    .claude/skills/<name>   Claude Code — symlink
    .codex/skills/<name>    Codex       — symlink
    .agents/skills.json     Antigravity — per-repo manifest (best-effort;
                            verify live with `agy --print` before relying on it)

Idempotent: safe to re-run after adding, renaming or removing a Skill. Runtime
adapters are derived; never edit them as Skill canon.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def find_skills(source: Path) -> list[str]:
    if not source.is_dir():
        return []
    return sorted(
        p.name for p in source.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    )


def collect_skills(sources: list[Path]) -> dict[str, Path]:
    """Return name -> source directory; later sources take precedence."""
    found: dict[str, Path] = {}
    for source in sources:
        for name in find_skills(source):
            found[name] = source
    return found


def sync_symlink_target(repo_root: Path, skill_sources: dict[str, Path], dest_name: str) -> None:
    dest = repo_root / dest_name
    dest.mkdir(parents=True, exist_ok=True)

    for name, source in sorted(skill_sources.items()):
        link = dest / name
        target = Path("..", "..", source.relative_to(repo_root), name)
        if link.is_symlink() or link.exists():
            if link.is_symlink():
                link.unlink()
            else:
                continue  # never touch a real file/dir that isn't our symlink
        link.symlink_to(target)

    # Remove stale managed symlinks for Skills no longer exposed by any source.
    for link in dest.iterdir():
        if link.is_symlink() and link.name not in skill_sources:
            link.unlink()


def write_agy_manifest(repo_root: Path, sources: list[Path]) -> None:
    agents_dir = repo_root / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "entries": [
            {"path": str(source.relative_to(repo_root))}
            for source in sources
            if find_skills(source)
        ]
    }
    (agents_dir / "skills.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--source",
        default=None,
        help="Explicit Skills home. Default: merge .github/skills then .folderdesk/skills (workspace wins on name collision)",
    )
    ap.add_argument("--root", default=".", help="Repository root (default: current directory)")
    args = ap.parse_args()

    repo_root = Path(args.root).resolve()
    if args.source:
        sources = [(repo_root / args.source).resolve()]
    else:
        sources = [
            (repo_root / ".github/skills").resolve(),
            (repo_root / ".folderdesk/skills").resolve(),
        ]

    skill_sources = collect_skills(sources)
    if not skill_sources:
        shown = ", ".join(str(source.relative_to(repo_root)) for source in sources)
        print(f"No Skills found under {shown} — nothing to sync.")
        return 0

    sync_symlink_target(repo_root, skill_sources, ".claude/skills")
    sync_symlink_target(repo_root, skill_sources, ".codex/skills")
    write_agy_manifest(repo_root, sources)

    source_labels = ", ".join(
        str(source.relative_to(repo_root)) for source in sources if find_skills(source)
    )
    print(f"synced {len(skill_sources)} skill(s) from {source_labels}: {' '.join(sorted(skill_sources))}")
    print("claude=.claude/skills codex=.codex/skills agy=.agents/skills.json (manifest, unverified live)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
