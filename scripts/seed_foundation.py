#!/usr/bin/env python3
"""Seed FolderDesk's minimal generic Skills foundation.

Single-repository deployments place starter Skills under `.folderdesk/skills/` in the
primary workspace. A separately configured repository with role `skills` remains a
supported explicit expansion. Existing target files are never overwritten.
"""
from __future__ import annotations

import argparse
import base64
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STARTER_ROOT = ROOT / "starter" / "skills"
STARTER_SKILLS = (
    "owner-router",
    "github-workflow",
    "skill-authoring",
    "research-escalation",
    "document-intake",
    "client-experience",
)


class FoundationError(RuntimeError):
    pass


def load_config(path: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FoundationError(f"Config not found: {path}")
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise FoundationError("Config root must be an object")
    return data


def resolve_target(data: dict[str, Any]) -> tuple[str, str, str]:
    target = data.get("target", {})
    owner = target.get("owner")
    if not isinstance(owner, str) or not owner.strip() or owner == "YOUR-GITHUB-ORG":
        raise FoundationError("A real target.owner is required")

    repos = [repo for repo in data.get("repositories", []) if isinstance(repo, dict)]
    for repo in repos:
        if repo.get("role") == "skills" and isinstance(repo.get("name"), str) and repo["name"].strip():
            return owner, repo["name"], ""
    for repo in repos:
        if repo.get("role") == "workspace" and isinstance(repo.get("name"), str) and repo["name"].strip():
            return owner, repo["name"], ".folderdesk/skills/"
    raise FoundationError("No primary workspace repository is configured")


def starter_files() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for skill in STARTER_SKILLS:
        path = STARTER_ROOT / skill / "SKILL.md"
        if not path.exists():
            raise FoundationError(f"Missing starter Skill: {path.relative_to(ROOT)}")
        rows.append((f"{skill}/SKILL.md", path.read_text(encoding="utf-8")))
    return rows


def run(cmd: list[str], *, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, input=input_text, capture_output=True)


def gh_available() -> bool:
    return shutil.which("gh") is not None


def remote_path_exists(full_repo: str, path: str) -> bool:
    return run(["gh", "api", f"repos/{full_repo}/contents/{path}"]).returncode == 0


def put_new_file(full_repo: str, path: str, content: str) -> None:
    payload = {
        "message": f"Seed FolderDesk foundational Skill {path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    result = run(
        ["gh", "api", f"repos/{full_repo}/contents/{path}", "-X", "PUT", "--input", "-"],
        input_text=json.dumps(payload),
    )
    if result.returncode != 0:
        raise FoundationError(result.stderr.strip() or result.stdout.strip() or f"Failed to create {path}")


def command_plan(data: dict[str, Any]) -> int:
    owner, repository, prefix = resolve_target(data)
    location = f"{owner}/{repository}/{prefix}".rstrip("/")
    print(f"FolderDesk Skills foundation preview for {location}")
    for path, _ in starter_files():
        print(f"- {prefix}{path}: create only if missing")
    print("No mutation selected. Use --apply when the current instruction authorises bounded seeding.")
    return 0


def command_apply(data: dict[str, Any]) -> int:
    if not gh_available():
        raise FoundationError("GitHub CLI (gh) is required for --apply")
    auth = run(["gh", "auth", "status"])
    if auth.returncode != 0:
        raise FoundationError("GitHub CLI is not authenticated")
    owner, repository, prefix = resolve_target(data)
    full_repo = f"{owner}/{repository}"
    for path, content in starter_files():
        remote_path = f"{prefix}{path}"
        if remote_path_exists(full_repo, remote_path):
            print(f"REUSE {full_repo}/{remote_path}")
            continue
        put_new_file(full_repo, remote_path, content)
        print(f"CREATE {full_repo}/{remote_path}")
    print("FolderDesk foundational Skills seeding complete. Existing target files were not overwritten.")
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="FolderDesk foundational Skills seeder")
    p.add_argument("--config", required=True)
    p.add_argument("--apply", action="store_true", help="Create missing foundational Skill files")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        data = load_config(args.config)
        return command_apply(data) if args.apply else command_plan(data)
    except (FoundationError, json.JSONDecodeError) as exc:
        print(f"FOLDERDESK FOUNDATION ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
