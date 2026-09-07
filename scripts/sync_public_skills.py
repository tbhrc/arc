#!/usr/bin/env python3
"""Selectively sync explicitly public-safe Skills into public ARC.

The manifest is an allowlist. Any public Skill directory that is neither allowlisted
nor explicitly preserved is treated as unexpected exposure and fails verification.
The script never decides that a private Skill is safe to publish; humans do that by
editing the manifest.
"""
from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "profiles" / "tbhrc-reference" / "public-skill-export.json"


class SyncError(RuntimeError):
    pass


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SyncError("Manifest root must be an object")
    for key in ("destination", "preserve", "skills"):
        if key not in data:
            raise SyncError(f"Manifest missing required key: {key}")
    if not isinstance(data["preserve"], list) or not all(isinstance(x, str) and x for x in data["preserve"]):
        raise SyncError("preserve must be a list of non-empty Skill names")
    if not isinstance(data["skills"], list) or not all(isinstance(x, str) and x for x in data["skills"]):
        raise SyncError("skills must be a list of non-empty Skill names")
    overlap = set(data["preserve"]) & set(data["skills"])
    if overlap:
        raise SyncError(f"Skill cannot be both preserved and synced: {', '.join(sorted(overlap))}")
    return data


def skill_dirs(root: Path) -> set[str]:
    if not root.exists():
        return set()
    return {p.name for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")}


def validate_sources(source: Path, skills: list[str]) -> None:
    for name in skills:
        skill = source / name
        if not skill.is_dir():
            raise SyncError(f"Selected source Skill does not exist: {skill}")
        if not (skill / "SKILL.md").is_file():
            raise SyncError(f"Selected source Skill has no SKILL.md: {skill}")


def trees_equal(left: Path, right: Path) -> bool:
    if not left.is_dir() or not right.is_dir():
        return False
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(trees_equal(left / name, right / name) for name in comparison.common_dirs)


def inspect(source: Path, destination: Path, preserve: list[str], skills: list[str]) -> tuple[list[str], list[str]]:
    allowed = set(preserve) | set(skills)
    unexpected = sorted(skill_dirs(destination) - allowed)
    drift = sorted(name for name in skills if not trees_equal(source / name, destination / name))
    return unexpected, drift


def apply_sync(source: Path, destination: Path, skills: list[str]) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for name in skills:
        target = destination / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source / name, target)
        print(f"SYNC {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync explicitly approved public-safe Skills into ARC")
    parser.add_argument("--source", type=Path, required=True, help="Local checkout/root of the canonical Skills repository")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--apply", action="store_true", help="Copy allowlisted Skills before verifying")
    args = parser.parse_args()

    try:
        manifest = load_manifest(args.manifest)
        source = args.source.resolve()
        destination = (ROOT / manifest["destination"]).resolve()
        skills = manifest["skills"]
        preserve = manifest["preserve"]
        validate_sources(source, skills)

        if args.apply:
            apply_sync(source, destination, skills)

        unexpected, drift = inspect(source, destination, preserve, skills)
        result = {
            "status": "GREEN" if not unexpected and not drift else "DRIFT",
            "selected": skills,
            "preserved": preserve,
            "unexpected_public_skills": unexpected,
            "selected_skill_drift": drift,
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        if unexpected:
            print("ARC PUBLIC-SKILL ERROR: unexpected public Skill directories detected", file=sys.stderr)
        if drift:
            print("ARC PUBLIC-SKILL ERROR: selected public Skills are not in canonical parity", file=sys.stderr)
        return 0 if result["status"] == "GREEN" else 1
    except (SyncError, OSError, json.JSONDecodeError) as exc:
        print(f"ARC PUBLIC-SKILL ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
