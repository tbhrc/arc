#!/usr/bin/env python3
"""Seed ARC's minimal generic Skills foundation into a target Skills repository.

Plan-first by default. Mutation requires --apply. Existing target files are never overwritten.
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


def resolve_target(data: dict[str, Any]) -> tuple[str, str]:
    target = data.get("target", {})
    owner = target.get("owner")
    if not isinstance(owner, str) or not owner.strip() or owner == "YOUR-GITHUB-ORG":
        raise FoundationError("A real target.owner is required")
    for repo in data.get("repositories", []):
        if isinstance(repo, dict) and repo.get("role") == "skills":
            name = repo.get("name")
            if isinstance(name, str) and name.strip():
                return owner, name
    raise FoundationError("No repository with role 'skills' is configured")


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
    result = run(["gh", "api", f"repos/{full_repo}/contents/{path}"])
    return result.returncode == 0


def put_new_file(full_repo: str, path: str, content: str) -> None:
    payload = {
        "message": f"Seed ARC foundational Skill {path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    result = run(
        ["gh", "api", f"repos/{full_repo}/contents/{path}", "-X", "PUT", "--input", "-"],
        input_text=json.dumps(payload),
    )
    if result.returncode != 0:
        raise FoundationError(result.stderr.strip() or result.stdout.strip() or f"Failed to create {path}")


def command_plan(data: dict[str, Any]) -> int:
    owner, skills_repo = resolve_target(data)
    print(f"ARC Skills foundation plan for {owner}/{skills_repo}")
    for path, _ in starter_files():
        print(f"- {path}: create only if missing")
    print("No mutation performed.")
    return 0


def command_apply(data: dict[str, Any]) -> int:
    if not gh_available():
        raise FoundationError("GitHub CLI (gh) is required for --apply")
    auth = run(["gh", "auth", "status"])
    if auth.returncode != 0:
        raise FoundationError("GitHub CLI is not authenticated")
    owner, skills_repo = resolve_target(data)
    full_repo = f"{owner}/{skills_repo}"
    for path, content in starter_files():
        if remote_path_exists(full_repo, path):
            print(f"REUSE {full_repo}/{path}")
            continue
        put_new_file(full_repo, path, content)
        print(f"CREATE {full_repo}/{path}")
    print("ARC foundational Skills seeding complete. Existing target files were not overwritten.")
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="ARC foundational Skills seeder")
    p.add_argument("--config", required=True)
    p.add_argument("--apply", action="store_true", help="Create missing foundational Skill files")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        data = load_config(args.config)
        return command_apply(data) if args.apply else command_plan(data)
    except (FoundationError, json.JSONDecodeError) as exc:
        print(f"ARC FOUNDATION ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
