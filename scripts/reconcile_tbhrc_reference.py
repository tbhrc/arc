#!/usr/bin/env python3
"""Verify the public ARC TBHRC reference against current canonical Skills truth.

Checks are deliberately bounded:
1. Router repository membership parity.
2. Material ARC Fast Links into tbhrc/skills resolve to real paths.
3. One consolidated report with ARC + Skills source SHAs.

The script reports drift; it does not invent role/visibility metadata or mutate source truth.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REFERENCE = ROOT / "profiles" / "tbhrc-reference" / "arc.reference.json"
MATERIAL_DOCS = (
    ROOT / "AGENTS.md",
    ROOT / "README.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "MANIFEST.md",
    ROOT / "VERIFY.md",
    ROOT / "profiles" / "tbhrc-reference" / "README.md",
)
SKILLS_URL_RE = re.compile(
    r"https://github\.com/tbhrc/skills/(?P<kind>tree|blob)/main/(?P<path>[^)\s>#]+)(?:#[^)\s>]*)?"
)


class ReconcileError(RuntimeError):
    pass


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ReconcileError(f"Missing required file: {path}") from exc


def git_sha(path: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise ReconcileError(f"Not a readable Git checkout: {path}")
    return result.stdout.strip()


def router_repositories(router_path: Path) -> set[str]:
    data = load_json(router_path)
    if not isinstance(data, dict):
        raise ReconcileError("Router registry root must be an object")
    repos = set()
    for key in data:
        if not isinstance(key, str) or "/" not in key:
            raise ReconcileError(f"Invalid Router repository key: {key!r}")
        repos.add(key)
    return repos


def reference_repositories(reference_path: Path) -> tuple[str, set[str]]:
    data = load_json(reference_path)
    if not isinstance(data, dict):
        raise ReconcileError("Reference profile root must be an object")
    target = data.get("target")
    if not isinstance(target, dict) or not isinstance(target.get("owner"), str):
        raise ReconcileError("Reference profile requires target.owner")
    owner = target["owner"]
    rows = data.get("repositories")
    if not isinstance(rows, list):
        raise ReconcileError("Reference profile repositories must be a list")
    repos: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("name"), str):
            raise ReconcileError("Every reference repository requires a name")
        repos.add(f"{owner}/{row['name']}")
    return owner, repos


def material_skill_links(docs: tuple[Path, ...] = MATERIAL_DOCS) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for doc in docs:
        if not doc.exists():
            continue
        text = doc.read_text(encoding="utf-8")
        for match in SKILLS_URL_RE.finditer(text):
            kind = match.group("kind")
            rel = unquote(urlsplit(match.group(0)).path.split("/main/", 1)[1]).strip("/")
            document = str(doc.relative_to(ROOT)) if doc.is_relative_to(ROOT) else doc.name
            key = (document, kind, rel)
            if key in seen:
                continue
            seen.add(key)
            links.append({
                "document": document,
                "kind": kind,
                "path": rel,
                "url": match.group(0),
            })
    return links


def verify_skill_links(skills_source: Path, links: list[dict[str, str]]) -> list[dict[str, str]]:
    broken: list[dict[str, str]] = []
    for link in links:
        target = skills_source / link["path"]
        ok = target.is_dir() if link["kind"] == "tree" else target.is_file()
        if not ok:
            broken.append(link)
    return broken


def build_report(skills_source: Path, reference_path: Path = DEFAULT_REFERENCE) -> dict[str, object]:
    router_path = skills_source / "templates" / "agents-repositories.json"
    router = router_repositories(router_path)
    _, reference = reference_repositories(reference_path)
    missing = sorted(router - reference)
    extra = sorted(reference - router)
    links = material_skill_links()
    broken = verify_skill_links(skills_source, links)
    status = "GREEN" if not missing and not extra and not broken else "DRIFT"
    return {
        "status": status,
        "arc_sha": git_sha(ROOT),
        "skills_sha": git_sha(skills_source),
        "router_repository_count": len(router),
        "reference_repository_count": len(reference),
        "missing_in_reference": missing,
        "extra_in_reference": extra,
        "checked_skill_fast_links": len(links),
        "broken_skill_fast_links": broken,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Reconcile ARC TBHRC reference parity")
    parser.add_argument("--skills-source", required=True, type=Path)
    parser.add_argument("--reference", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    try:
        report = build_report(args.skills_source.resolve(), args.reference.resolve())
        rendered = json.dumps(report, indent=2, sort_keys=True)
        print(rendered)
        if args.report:
            args.report.write_text(rendered + "\n", encoding="utf-8")
        return 0 if report["status"] == "GREEN" else 1
    except (ReconcileError, OSError, json.JSONDecodeError) as exc:
        print(f"ARC RECONCILE ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
