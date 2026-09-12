#!/usr/bin/env python3
"""Mirror the canonical Skills home into each local AI CLI's own native
discovery path, so Claude Code, Codex, and Antigravity (agy) all see the
same one-editable-canon Skills without duplicating them.

Canonical source is auto-detected: deployed FolderDesk workspaces prefer
`.folderdesk/skills/`; the FolderDesk framework repository falls back to
`.github/skills/`. Use `--source` only for an explicit non-standard source.

Targets (see `components/agents/README.md` — runtime copies/adapters may
exist, but must never become independently edited canon):

    .claude/skills/<name>   Claude Code   — symlink
    .codex/skills/<name>    Codex         — symlink; confirmed live via a
                            `codex exec` discovery test that Codex reads a
                            project-local .codex/skills/ in addition to its
                            global $CODEX_HOME/skills.
    .agents/skills.json     Antigravity (agy) — agy's own documented per-repo
                            manifest convention. NOT verified live as of this
                            writing (a live agy 1.2.1 test did not pick it up;
                            only its global ~/.gemini/config/skills/ showed).
                            Written anyway as forward-compatible best-effort —
                            verify with `agy --print` before relying on it.

Idempotent: safe to re-run after adding, renaming or removing a Skill.
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


def sync_symlink_target(repo_root: Path, source: Path, dest_name: str, skills: list[str]) -> None:
    dest = repo_root / dest_name
    dest.mkdir(parents=True, exist_ok=True)

    for name in skills:
        link = dest / name
        target = Path("..", "..", source.relative_to(repo_root), name)
        if link.is_symlink() or link.exists():
            if link.is_symlink():
                link.unlink()
            else:
                continue  # never touch a real file/dir that isn't our symlink
        link.symlink_to(target)

    # Remove stale symlinks for Skills that no longer exist
    for link in dest.iterdir():
        if not link.is_symlink():
            continue
        if link.name not in skills:
            link.unlink()


def write_agy_manifest(repo_root: Path, source: Path) -> None:
    agents_dir = repo_root / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    manifest = {"entries": [{"path": str(source.relative_to(repo_root))}]}
    (agents_dir / "skills.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default=None, help="Canonical Skills home (default: auto-detect .folderdesk/skills, then .github/skills)")
    ap.add_argument("--root", default=".", help="Repository root (default: current directory)")
    args = ap.parse_args()

    repo_root = Path(args.root).resolve()
    if args.source:
        source = (repo_root / args.source).resolve()
    else:
        workspace_source = (repo_root / ".folderdesk/skills").resolve()
        framework_source = (repo_root / ".github/skills").resolve()
        source = workspace_source if find_skills(workspace_source) else framework_source

    skills = find_skills(source)
    if not skills:
        print(f"No Skills found under {source} — nothing to sync.")
        return 0

    sync_symlink_target(repo_root, source, ".claude/skills", skills)
    sync_symlink_target(repo_root, source, ".codex/skills", skills)
    write_agy_manifest(repo_root, source)

    print(f"synced {len(skills)} skill(s) from {source.relative_to(repo_root)}: {' '.join(skills)}")
    print("claude=.claude/skills codex=.codex/skills agy=.agents/skills.json (manifest, unverified live)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
