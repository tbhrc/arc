#!/usr/bin/env python3
"""ARC plan-first bootstrap and verification CLI.

No secret handling is implemented by design.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SELF_FILES = [
    "README.md", "AGENTS.md", "ATLAS.md", "ARCHITECTURE.md", "MANIFEST.md",
    "BOOTSTRAP.md", "VERIFY.md", "VERSION", "LICENSE",
    ".github/skills/atlas/SKILL.md", ".github/prompts/atlas.prompt.md",
    "profiles/generic-business/arc.example.json",
]
VALID_VISIBILITY = {"public", "private", "internal"}
VALID_OWNER_TYPES = {"org", "user"}


class ArcError(RuntimeError):
    pass


def load_config(path: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise ArcError(f"Config not found: {path}")
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ArcError(f"Invalid JSON in {path}: {exc}") from exc
    validate_config(data)
    return data


def validate_config(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ArcError("Config root must be a JSON object")
    target = data.get("target")
    if not isinstance(target, dict):
        raise ArcError("Config must contain target object")
    owner = target.get("owner")
    if not isinstance(owner, str) or not owner.strip():
        raise ArcError("target.owner must be a non-empty string")
    if owner == "YOUR-GITHUB-ORG":
        raise ArcError("Replace target.owner placeholder before deployment")
    owner_type = target.get("owner_type", "org")
    if owner_type not in VALID_OWNER_TYPES:
        raise ArcError(f"target.owner_type must be one of {sorted(VALID_OWNER_TYPES)}")
    visibility = target.get("default_visibility", "private")
    if visibility not in VALID_VISIBILITY:
        raise ArcError(f"target.default_visibility must be one of {sorted(VALID_VISIBILITY)}")
    repos = data.get("repositories", [])
    if not isinstance(repos, list) or not repos:
        raise ArcError("repositories must be a non-empty list")
    names: set[str] = set()
    for repo in repos:
        if not isinstance(repo, dict):
            raise ArcError("each repositories item must be an object")
        name = repo.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ArcError("each repository requires a non-empty name")
        if name in names:
            raise ArcError(f"duplicate repository name: {name}")
        names.add(name)
        vis = repo.get("visibility", visibility)
        if vis not in VALID_VISIBILITY:
            raise ArcError(f"invalid visibility for {name}: {vis}")
    domains = data.get("domains", [])
    if not isinstance(domains, list):
        raise ArcError("domains must be a list")
    for domain in domains:
        if not isinstance(domain, dict) or not isinstance(domain.get("name"), str) or not domain["name"].strip():
            raise ArcError("each domain requires a non-empty name")
        if domain["name"] in names:
            raise ArcError(f"domain repository duplicates core repository: {domain['name']}")
        names.add(domain["name"])


def repos_from_config(data: dict[str, Any]) -> list[dict[str, Any]]:
    target = data["target"]
    default_visibility = target.get("default_visibility", "private")
    rows: list[dict[str, Any]] = []
    for repo in data.get("repositories", []):
        rows.append({
            "name": repo["name"],
            "description": repo.get("description", f"ARC {repo.get('role', 'component')} repository."),
            "role": repo.get("role", "component"),
            "required": bool(repo.get("required", True)),
            "visibility": repo.get("visibility", default_visibility),
        })
    for domain in data.get("domains", []):
        rows.append({
            "name": domain["name"],
            "description": domain.get("description", "ARC business/domain truth owner."),
            "role": "business-domain",
            "required": True,
            "visibility": domain.get("visibility", default_visibility),
        })
    return rows


def run(cmd: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=check)


def gh_available() -> bool:
    return shutil.which("gh") is not None


def gh_repo_exists(full_name: str) -> bool:
    result = run(["gh", "repo", "view", full_name, "--json", "nameWithOwner"], check=False)
    return result.returncode == 0


def command_doctor(data: dict[str, Any]) -> int:
    print(f"ARC doctor for {data['target']['owner']}")
    ok = True
    if sys.version_info < (3, 10):
        print("FAIL Python 3.10+ required")
        ok = False
    else:
        print(f"PASS Python {sys.version_info.major}.{sys.version_info.minor}")
    if not gh_available():
        print("FAIL GitHub CLI (gh) not found")
        ok = False
    else:
        print("PASS GitHub CLI found")
        auth = run(["gh", "auth", "status"], check=False)
        if auth.returncode == 0:
            print("PASS GitHub CLI authentication available")
        else:
            print("FAIL GitHub CLI is not authenticated for the intended target")
            ok = False
    print("PASS configuration schema")
    return 0 if ok else 1


def command_plan(data: dict[str, Any]) -> int:
    target = data["target"]
    print("ARC deployment plan")
    print(f"Target: {target['owner']} ({target.get('owner_type', 'org')})")
    print(f"Default visibility: {target.get('default_visibility', 'private')}")
    print("Repositories:")
    for repo in repos_from_config(data):
        marker = "required" if repo["required"] else "optional"
        print(f"- {repo['name']}: {repo['role']} | {repo['visibility']} | {marker}")
    integrations = data.get("integrations", {})
    print("Integrations (manual/declared, not secret bootstrap):")
    print(f"- private files: {integrations.get('private_files', 'not declared')}")
    systems = integrations.get("specialist_systems", [])
    print(f"- specialist systems: {', '.join(systems) if systems else 'none declared'}")
    print(f"- memory: {integrations.get('memory', 'optional')}")
    print("No mutation performed.")
    return 0


def create_repo(owner: str, owner_type: str, repo: dict[str, Any]) -> None:
    full = f"{owner}/{repo['name']}"
    if gh_repo_exists(full):
        print(f"REUSE {full}")
        return
    cmd = ["gh", "repo", "create", full, f"--{repo['visibility']}", "--description", repo["description"]]
    if owner_type == "org":
        pass
    result = run(cmd, check=False)
    if result.returncode != 0:
        raise ArcError(f"Failed to create {full}: {result.stderr.strip() or result.stdout.strip()}")
    print(f"CREATE {full}")


def command_bootstrap(data: dict[str, Any], apply: bool) -> int:
    if not apply:
        print("ARC bootstrap is in PLAN-ONLY mode. Add --apply to create missing repositories.")
        return command_plan(data)
    if not gh_available():
        raise ArcError("GitHub CLI (gh) is required for --apply")
    auth = run(["gh", "auth", "status"], check=False)
    if auth.returncode != 0:
        raise ArcError("GitHub CLI is not authenticated")
    target = data["target"]
    owner = target["owner"]
    owner_type = target.get("owner_type", "org")
    for repo in repos_from_config(data):
        create_repo(owner, owner_type, repo)
    print("Repository bootstrap complete. Secrets and specialist-system integrations were intentionally not modified.")
    return 0


def command_verify(data: dict[str, Any]) -> int:
    if not gh_available():
        raise ArcError("GitHub CLI (gh) is required for target verification")
    owner = data["target"]["owner"]
    failed = False
    for repo in repos_from_config(data):
        full = f"{owner}/{repo['name']}"
        result = run(["gh", "repo", "view", full, "--json", "nameWithOwner,visibility,url"], check=False)
        if result.returncode != 0:
            state = "MISSING"
            if repo["required"]:
                failed = True
        else:
            state = "OK"
        print(f"{state} {full}")
    print("Target repository verification complete. Finish the human/agent gates in VERIFY.md.")
    return 1 if failed else 0


def command_verify_self() -> int:
    missing = [path for path in REQUIRED_SELF_FILES if not (ROOT / path).exists()]
    if missing:
        raise ArcError("Missing required ARC files: " + ", ".join(missing))
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version or version.count(".") != 2:
        raise ArcError("VERSION must contain semantic version X.Y.Z")
    atlas = (ROOT / ".github/skills/atlas/SKILL.md").read_text(encoding="utf-8")
    if not atlas.startswith("---\nname: atlas\n"):
        raise ArcError("Atlas Skill frontmatter missing or malformed")
    example = json.loads((ROOT / "profiles/generic-business/arc.example.json").read_text(encoding="utf-8"))
    clone = json.loads(json.dumps(example))
    if clone.get("target", {}).get("owner") == "YOUR-GITHUB-ORG":
        clone["target"]["owner"] = "example-org"
    validate_config(clone)
    print(f"ARC self-verification PASS (v{version})")
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="ARC plan-first deployment utility")
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("doctor", "plan", "verify"):
        sp = sub.add_parser(name)
        sp.add_argument("--config", required=True)
    sp = sub.add_parser("bootstrap")
    sp.add_argument("--config", required=True)
    sp.add_argument("--apply", action="store_true", help="Create missing configured repositories")
    sub.add_parser("verify-self")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "verify-self":
            return command_verify_self()
        data = load_config(args.config)
        if args.command == "doctor":
            return command_doctor(data)
        if args.command == "plan":
            return command_plan(data)
        if args.command == "bootstrap":
            return command_bootstrap(data, args.apply)
        if args.command == "verify":
            return command_verify(data)
        raise ArcError(f"Unknown command: {args.command}")
    except ArcError as exc:
        print(f"ARC ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
