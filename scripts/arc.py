#!/usr/bin/env python3
"""ARC onboarding, deployment, export and recovery CLI.

ARC intentionally handles portable architecture metadata, never secret values or copied
external business data.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_SCHEMA = "1.0"
REQUIRED_SELF_FILES = [
    "README.md",
    "AGENTS.md",
    "ATLAS.md",
    "ARCHITECTURE.md",
    "MANIFEST.md",
    "BOOTSTRAP.md",
    "VERIFY.md",
    "VERSION",
    "LICENSE",
    "contracts/safe-harbour.md",
    ".github/skills/atlas/SKILL.md",
    ".github/skills/atlas/agents/openai.yaml",
    ".github/skills/atlas/references/modes.md",
    ".github/prompts/atlas.prompt.md",
    "profiles/generic-business/arc.example.json",
    "scripts/package_atlas.py",
]
VALID_VISIBILITY = {"public", "private", "internal"}
VALID_OWNER_TYPES = {"org", "user"}
VALID_DEPLOYMENT_SCOPES = {"shared", "tenant"}
ATLAS_MODES = ("onboard", "adopt", "audit", "health", "upgrade", "recover", "next")
SECRET_KEY_FRAGMENTS = (
    "password",
    "passwd",
    "token",
    "secret",
    "api_key",
    "apikey",
    "private_key",
    "access_key",
)
SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


class ArcError(RuntimeError):
    pass


def read_arc_version() -> str:
    path = ROOT / "VERSION"
    if path.exists():
        value = path.read_text(encoding="utf-8").strip()
        if value:
            return value
    return "0.3.0"


def _load_json(path: str, label: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise ArcError(f"{label} not found: {path}")
    try:
        value = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ArcError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ArcError(f"{label} root must be a JSON object")
    return value


def load_config(path: str) -> dict[str, Any]:
    data = _load_json(path, "Config")
    validate_config(data)
    return data


def _walk_secret_like_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            path = f"{prefix}.{key_text}" if prefix else key_text
            lowered = key_text.lower()
            if any(fragment in lowered for fragment in SECRET_KEY_FRAGMENTS):
                found.append(path)
            found.extend(_walk_secret_like_keys(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            path = f"{prefix}[{index}]" if prefix else f"[{index}]"
            found.extend(_walk_secret_like_keys(child, path))
    return found


def _walk_sensitive_values(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            found.extend(_walk_sensitive_values(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            path = f"{prefix}[{index}]" if prefix else f"[{index}]"
            found.extend(_walk_sensitive_values(child, path))
    elif isinstance(value, str):
        if any(pattern.search(value) for pattern in SENSITIVE_VALUE_PATTERNS):
            found.append(prefix or "<root>")
    return found


def assert_no_sensitive_material(value: Any, label: str) -> None:
    secret_keys = _walk_secret_like_keys(value)
    if secret_keys:
        raise ArcError(f"{label} must never contain secret-like fields: " + ", ".join(secret_keys))
    sensitive_values = _walk_sensitive_values(value)
    if sensitive_values:
        raise ArcError(f"{label} appears to contain credential values at: " + ", ".join(sensitive_values))


def validate_config(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise ArcError("Config root must be a JSON object")
    assert_no_sensitive_material(data, "ARC configuration")

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

    deployment_context = data.get("deployment_context", {"scope": "shared"})
    if not isinstance(deployment_context, dict):
        raise ArcError("deployment_context must be an object")
    scope = deployment_context.get("scope", "shared")
    if scope not in VALID_DEPLOYMENT_SCOPES:
        raise ArcError(f"deployment_context.scope must be one of {sorted(VALID_DEPLOYMENT_SCOPES)}")
    tenant_id = deployment_context.get("tenant_id")
    entity_ref = deployment_context.get("entity_ref")
    if scope == "tenant":
        if not isinstance(tenant_id, str) or not tenant_id.strip():
            raise ArcError("tenant-scoped deployment requires deployment_context.tenant_id")
        if entity_ref is not None and (not isinstance(entity_ref, str) or not entity_ref.strip()):
            raise ArcError("deployment_context.entity_ref must be a non-empty string when provided")
    elif tenant_id not in (None, "") or entity_ref not in (None, ""):
        raise ArcError("shared deployment_context must not declare tenant_id or entity_ref")

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
        vis = domain.get("visibility", visibility)
        if vis not in VALID_VISIBILITY:
            raise ArcError(f"invalid visibility for {domain['name']}: {vis}")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise ArcError(f"Cannot derive repository name from: {value!r}")
    return slug


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def build_onboarding_config(
    *,
    business_name: str,
    owner: str,
    owner_type: str = "org",
    visibility: str = "private",
    domains: list[str] | None = None,
    private_files: str = "not-declared",
    specialist_systems: list[str] | None = None,
    memory: str = "optional",
    tenant_id: str | None = None,
    entity_ref: str | None = None,
) -> dict[str, Any]:
    domain_rows = [
        {"name": slugify(domain), "description": f"{domain.strip()} business/domain truth owner."}
        for domain in (domains or [])
    ]
    deployment_context: dict[str, Any] = {"scope": "shared"}
    if tenant_id:
        deployment_context = {"scope": "tenant", "tenant_id": tenant_id.strip()}
        if entity_ref:
            deployment_context["entity_ref"] = entity_ref.strip()
    elif entity_ref:
        raise ArcError("entity_ref requires tenant_id for tenant-scoped deployment")

    data: dict[str, Any] = {
        "arc_version": read_arc_version(),
        "target": {
            "business_name": business_name.strip(),
            "owner": owner.strip(),
            "owner_type": owner_type,
            "default_visibility": visibility,
        },
        "deployment_context": deployment_context,
        "repositories": [
            {"name": "skills", "description": "Canonical reusable AI Skills and operating HOW.", "role": "skills", "required": True},
            {"name": "research", "description": "External research, technology discovery and proving evidence.", "role": "research", "required": True},
            {"name": "ops", "description": "Business-wide operating architecture and cross-domain control.", "role": "operations", "required": True},
            {"name": "ai-engine", "description": "Optional privileged execution infrastructure for genuine runtime gaps.", "role": "trusted-runtime", "required": False},
        ],
        "domains": domain_rows,
        "integrations": {
            "private_files": private_files.strip() or "not-declared",
            "specialist_systems": specialist_systems or [],
            "memory": memory.strip() or "optional",
        },
    }
    validate_config(data)
    return data


def write_config(data: dict[str, Any], path: str, *, overwrite: bool = False) -> Path:
    validate_config(data)
    target = Path(path)
    if target.exists() and not overwrite:
        raise ArcError(f"Refusing to overwrite existing config: {path}. Use --overwrite explicitly.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return target


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


def navigation_from_config(data: dict[str, Any]) -> dict[str, str]:
    nav: dict[str, str] = {}
    for repo in repos_from_config(data):
        role = repo["role"]
        if role in {"skills", "research", "operations", "trusted-runtime"} and role not in nav:
            nav[role] = repo["name"]
    return nav


def run(cmd: list[str], *, check: bool = True, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, input=input_text, capture_output=True, check=check)


def gh_available() -> bool:
    return shutil.which("gh") is not None


def gh_authenticated() -> bool:
    if not gh_available():
        return False
    return run(["gh", "auth", "status"], check=False).returncode == 0


def gh_repo_exists(full_name: str) -> bool:
    result = run(["gh", "repo", "view", full_name, "--json", "nameWithOwner"], check=False)
    return result.returncode == 0


def inspect_repository_state(
    data: dict[str, Any], exists_fn: Callable[[str], bool] | None = None
) -> list[dict[str, str]]:
    owner = data["target"]["owner"]
    repos = repos_from_config(data)
    if exists_fn is None and not gh_authenticated():
        return [
            {"name": repo["name"], "full_name": f"{owner}/{repo['name']}", "action": "UNKNOWN"}
            for repo in repos
        ]
    checker = exists_fn or gh_repo_exists
    return [
        {
            "name": repo["name"],
            "full_name": f"{owner}/{repo['name']}",
            "action": "REUSE" if checker(f"{owner}/{repo['name']}") else "CREATE",
        }
        for repo in repos
    ]


def command_onboard(args: argparse.Namespace) -> int:
    if args.non_interactive:
        if not args.business_name or not args.owner:
            raise ArcError("--non-interactive requires --business-name and --owner")
        business_name, owner = args.business_name, args.owner
        domains = parse_csv(args.domains)
        specialist_systems = parse_csv(args.specialist_systems)
    else:
        business_name = args.business_name or input("Business name: ").strip()
        owner = args.owner or input("GitHub organisation/user: ").strip()
        domains_text = args.domains if args.domains is not None else input("Business domains (comma-separated, optional): ").strip()
        domains = parse_csv(domains_text)
        if args.private_files == "not-declared":
            args.private_files = input("Private-file store (optional): ").strip() or "not-declared"
        specialist_text = args.specialist_systems if args.specialist_systems is not None else input("Specialist systems (comma-separated, optional): ").strip()
        specialist_systems = parse_csv(specialist_text)

    data = build_onboarding_config(
        business_name=business_name,
        owner=owner,
        owner_type=args.owner_type,
        visibility=args.visibility,
        domains=domains,
        private_files=args.private_files,
        specialist_systems=specialist_systems,
        memory=args.memory,
        tenant_id=args.tenant_id,
        entity_ref=args.entity_ref,
    )
    path = write_config(data, args.output, overwrite=args.overwrite)
    print(f"FolderDesk onboarding profile written: {path}")
    print("No remote mutation performed. Doctor and plan remain available when useful.")
    return 0


def command_connection_readiness(data: dict[str, Any]) -> int:
    owner = data["target"]["owner"]
    navigation = navigation_from_config(data)
    skills = navigation.get("skills", "skills")
    integrations = data.get("integrations", {})
    print("Connection readiness (read-only; not a deployment gate)")
    print("Selected modules:")
    for repo in repos_from_config(data):
        print(f"- {repo['name']} ({repo['role']}): GitHub repository + {owner}/{skills} Skills routing")
    print("Observed portable surfaces:")
    if gh_available() and gh_authenticated():
        print("- GitHub: WIRED (gh authenticated)")
    elif gh_available():
        print("- GitHub: NOT WIRED (gh present but unauthenticated)")
    else:
        print("- GitHub: NOT WIRED (gh unavailable)")
    private_files = integrations.get("private_files", "not-declared")
    print(f"- Private files connector: DECLARED {private_files}; external wiring UNVERIFIED")
    systems = integrations.get("specialist_systems", [])
    if systems:
        for system in systems:
            print(f"- Specialist connector/MCP: DECLARED {system}; external wiring UNVERIFIED")
    else:
        print("- Specialist connector/MCP: none declared")
    memory = integrations.get("memory", "optional")
    print(f"- Memory: DECLARED {memory}; external wiring UNVERIFIED")
    runtimes = data.get("runtimes", [])
    if runtimes:
        for runtime in runtimes:
            print(f"- Runtime: DECLARED {runtime}; external wiring UNVERIFIED")
    else:
        print("- Runtime: none declared")
    print("External connector/MCP/runtime credentials are intentionally not inspected. Confirm provider-side wiring before calling the deployment operationally ready.")
    return 0


def command_doctor(data: dict[str, Any], *, connectors: bool = False) -> int:
    print(f"FolderDesk doctor for {data['target']['owner']}")
    ok = True
    print(f"PASS Python {sys.version_info.major}.{sys.version_info.minor}")
    if not gh_available():
        print("FAIL GitHub CLI (gh) not found")
        ok = False
    elif gh_authenticated():
        print("PASS GitHub CLI found and authenticated")
    else:
        print("FAIL GitHub CLI is not authenticated for the intended target")
        ok = False
    print("PASS configuration schema")
    if connectors:
        command_connection_readiness(data)
    return 0 if ok else 1


def command_plan(data: dict[str, Any], inspect_target: bool = False) -> int:
    target = data["target"]
    print("FolderDesk deployment plan")
    if target.get("business_name"):
        print(f"Business: {target['business_name']}")
    print(f"Target: {target['owner']} ({target.get('owner_type', 'org')})")
    print(f"Default visibility: {target.get('default_visibility', 'private')}")
    deployment_context = data.get("deployment_context", {"scope": "shared"})
    print(f"Deployment scope: {deployment_context.get('scope', 'shared')}")
    if deployment_context.get("scope") == "tenant":
        print(f"Tenant: {deployment_context['tenant_id']}")
        if deployment_context.get("entity_ref"):
            print(f"Canonical entity ref: {deployment_context['entity_ref']}")
    state_by_name = {}
    if inspect_target:
        state_by_name = {row["name"]: row["action"] for row in inspect_repository_state(data)}
    print("Repositories:")
    for repo in repos_from_config(data):
        marker = "required" if repo["required"] else "optional"
        action = state_by_name.get(repo["name"], "PLANNED")
        print(f"- {repo['name']}: {repo['role']} | {repo['visibility']} | {marker} | {action}")
    integrations = data.get("integrations", {})
    print("Integrations (declared ownership; never secret bootstrap):")
    print(f"- private files: {integrations.get('private_files', 'not declared')}")
    systems = integrations.get("specialist_systems", [])
    print(f"- specialist systems: {', '.join(systems) if systems else 'none declared'}")
    print(f"- memory: {integrations.get('memory', 'optional')}")
    if inspect_target and any(value == "UNKNOWN" for value in state_by_name.values()):
        print("Target inspection unavailable because GitHub CLI is unavailable or unauthenticated.")
    print("No mutation performed.")
    return 0


def role_label(role: str) -> str:
    return {
        "skills": "Reusable HOW / Skills canon",
        "research": "External discovery and proving evidence",
        "operations": "Cross-business operating architecture and control",
        "trusted-runtime": "Privileged execution infrastructure for genuine runtime gaps",
        "business-domain": "Business/domain truth owner",
    }.get(role, role.replace("-", " ").title())


def generated_readme(owner: str, repo: dict[str, Any], navigation: dict[str, str]) -> str:
    skills = navigation.get("skills", "skills")
    research = navigation.get("research", "research")
    return f"""# {repo['name']}\n\n**FolderDesk role:** {role_label(repo['role'])}\n\n{repo['description']}\n\nThis repository was bootstrapped from [FolderDesk](https://github.com/tbhrc/folderdesk). Its live facts and decisions belong here only where this repository is the declared owner. Reusable operating method belongs in `{owner}/{skills}`; external discovery/proving belongs in `{owner}/{research}`.\n\n## Start\n\n1. Read `AGENTS.md`.\n2. Use the local Atlas project Skill for onboarding/navigation.\n3. Create durable work as an Issue when the outcome needs tracking.\n4. Verify real state before claiming completion.\n\n## Navigation\n\n- Skills: `https://github.com/{owner}/{skills}`\n- Research: `https://github.com/{owner}/{research}`\n- FolderDesk upstream: https://github.com/tbhrc/folderdesk\n- Learning course: https://github.com/tbhrc/gh-course\n"""


def generated_agents(owner: str, repo: dict[str, Any], navigation: dict[str, str]) -> str:
    skills = navigation.get("skills", "skills")
    research = navigation.get("research", "research")
    skills_base = f"https://github.com/{owner}/{skills}"
    workflow = f"{skills_base}/tree/main/github-agent-workflow"
    sniper = f"{skills_base}/blob/main/human-ai-operations-map/references/ai-sniper-entry-map.md"
    orchestrator = f"{skills_base}/tree/main/github-multi-agent-orchestrator"
    return f"""# AGENTS.md — Repository Router\n\nThis file is the repository **Router** and cold-start contract. Read it first. Follow only the Fast Link needed for the task; do not preload linked material.\n\n**Repository role:** {role_label(repo['role'])}\n\n**Core Fast Links:** [Skills]({skills_base}) · [Research](https://github.com/{owner}/{research}) · [Workflow]({workflow}) · [Sniper]({sniper}) · [Multi-Agent Orchestrator]({orchestrator})\n\n**Repository Fast Links:** [README](README.md) · [Atlas](.github/skills/atlas/SKILL.md) · [Issues](https://github.com/{owner}/{repo['name']}/issues) · [FolderDesk](https://github.com/tbhrc/folderdesk)\n\n## Route\n\n- **Known owner + bounded task** → use the most-specific repository Fast Link / Skill and execute.\n- **Owner or source unclear** → use [Sniper]({sniper}).\n- **Normal authorised durable GitHub work** → Level 0 Direct. Ordinary already-authorised bounded work executes directly; do not ask twice. Load [Workflow]({workflow}) only when Hybrid or Controlled may be needed.\n- **Multiple agents, specialist delegation or genuine parallel work** → use [Multi-Agent Orchestrator]({orchestrator}).\n- **Onboarding, adoption or recovery** → use [Atlas](.github/skills/atlas/SKILL.md); it is not the daily routing layer.\n\n## Rules\n\n- Fast Links are pointers, not preload instructions.\n- This repository owns only the facts/state declared by its role.\n- Reusable HOW belongs in `{owner}/{skills}`; external research/proving belongs in `{owner}/{research}`.\n- If a referenced Skill has not yet been adopted into `{owner}/{skills}`, use the local Atlas starter guidance and adopt/author the missing equivalent. Authorised TBHRC operators may temporarily consult `tbhrc/skills`; external deployments must not depend on that private fallback.\n- Preserve existing systems and owners unless a deliberate change is required.\n- Never place secrets, credentials or unnecessary private data in repository surfaces.\n- Verify the requested outcome in the correct owner before claiming completion.\n"""


def generated_atlas_pointer() -> str:
    return """---\nname: atlas\ndescription: \"FolderDesk front-door pointer. Use for FolderDesk onboarding, adoption, audit, health, upgrade, recovery, next-action guidance, deployment, diagnosis or `/atlas`. Load and follow the current upstream Atlas Skill from tbhrc/folderdesk; inspect/plan when useful and never mutate solely because credentials exist.\"\n---\n\n# Atlas Pointer\n\nCurrent canonical Atlas: https://github.com/tbhrc/folderdesk/blob/main/.github/skills/atlas/SKILL.md\n\nLoad the current upstream Skill and FolderDesk repository contract before acting. Inspect/plan when useful. The current instruction is sufficient authority for ordinary bounded work, and `--apply` is a deliberate mutation-mode selector. Fresh authority is required only at real destructive/root/private-data/spend/legal/client-commitment boundaries.\n"""


def generated_atlas_prompt() -> str:
    return """Use the local `atlas` project Skill and load the current FolderDesk upstream contract from https://github.com/tbhrc/folderdesk. Inspect/plan when useful. The current instruction is sufficient authority for ordinary bounded work, and `--apply` is a deliberate mutation-mode selector. Fresh authority is required only at real destructive/root/private-data/spend/legal/client-commitment boundaries. Atlas supports onboard, adopt, audit, health, upgrade, recover and next modes.\n"""


def put_content(full: str, path: str, content: str, *, sha: str | None = None) -> None:
    payload: dict[str, str] = {
        "message": f"Seed FolderDesk {path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    result = run(["gh", "api", f"repos/{full}/contents/{path}", "-X", "PUT", "--input", "-"], check=False, input_text=json.dumps(payload))
    if result.returncode != 0:
        raise ArcError(f"Failed to seed {full}/{path}: {result.stderr.strip() or result.stdout.strip()}")


def seed_new_repo(owner: str, repo: dict[str, Any], navigation: dict[str, str]) -> None:
    full = f"{owner}/{repo['name']}"
    current = run(["gh", "api", f"repos/{full}/contents/README.md", "--jq", ".sha"], check=False)
    if current.returncode != 0 or not current.stdout.strip():
        raise ArcError(f"Cannot resolve initial README for {full}")
    put_content(full, "README.md", generated_readme(owner, repo, navigation), sha=current.stdout.strip())
    put_content(full, "AGENTS.md", generated_agents(owner, repo, navigation))
    put_content(full, ".github/skills/atlas/SKILL.md", generated_atlas_pointer())
    put_content(full, ".github/prompts/atlas.prompt.md", generated_atlas_prompt())
    print(f"SEED {full} README + AGENTS + Atlas")


def create_repo(owner: str, owner_type: str, repo: dict[str, Any], navigation: dict[str, str]) -> bool:
    full = f"{owner}/{repo['name']}"
    if gh_repo_exists(full):
        print(f"REUSE {full} (existing repository left unchanged)")
        return False
    cmd = ["gh", "repo", "create", full, f"--{repo['visibility']}", "--description", repo["description"], "--add-readme"]
    result = run(cmd, check=False)
    if result.returncode != 0:
        raise ArcError(f"Failed to create {full}: {result.stderr.strip() or result.stdout.strip()}")
    print(f"CREATE {full}")
    seed_new_repo(owner, repo, navigation)
    return True


def command_bootstrap(data: dict[str, Any], apply: bool) -> int:
    if not apply:
        print("FolderDesk bootstrap preview: no mutation selected. Use --apply to create missing repositories.")
        return command_plan(data)
    if not gh_authenticated():
        raise ArcError("GitHub is FolderDesk's first requirement. Connect/authenticate GitHub before bootstrap --apply.")
    target = data["target"]
    navigation = navigation_from_config(data)
    repos = repos_from_config(data)
    total = len(repos)
    started = time.monotonic()
    print("FolderDesk bootstrap starting.")
    print(f"GitHub connection: confirmed. Target: {target['owner']}.")
    print(f"Work ahead: {total} configured repositories will be checked one by one.")
    print("Time estimate: remaining time will be calculated after the first repository check; progress will stream continuously.")
    for index, repo in enumerate(repos, start=1):
        full = f"{target['owner']}/{repo['name']}"
        print(f"[{index}/{total}] Checking {full}...")
        create_repo(target["owner"], target.get("owner_type", "org"), repo, navigation)
        elapsed = max(time.monotonic() - started, 0.0)
        average = elapsed / index
        remaining = max(average * (total - index), 0.0)
        print(f"[{index}/{total}] Complete | elapsed {elapsed:.1f}s | estimated remaining {remaining:.1f}s")
    elapsed = max(time.monotonic() - started, 0.0)
    print(f"FolderDesk bootstrap complete in {elapsed:.1f}s. External owner data and credential values were intentionally not modified.")
    return 0


def gh_path_exists(full: str, path: str) -> bool:
    return run(["gh", "api", f"repos/{full}/contents/{path}"], check=False).returncode == 0


def command_verify(data: dict[str, Any]) -> int:
    if not gh_authenticated():
        raise ArcError("GitHub CLI (gh) must be available and authenticated for target verification")
    owner = data["target"]["owner"]
    failed = False
    for repo in repos_from_config(data):
        full = f"{owner}/{repo['name']}"
        result = run(["gh", "repo", "view", full, "--json", "nameWithOwner,visibility,url"], check=False)
        if result.returncode != 0:
            if repo["required"]:
                failed = True
            print(f"MISSING {full}")
            continue
        missing_contract = [path for path in ("README.md", "AGENTS.md", ".github/skills/atlas/SKILL.md") if not gh_path_exists(full, path)]
        if missing_contract:
            if repo["required"]:
                failed = True
            print(f"INCOMPLETE {full}: missing {', '.join(missing_contract)}")
        else:
            print(f"OK {full}: repository + agent contract + Atlas")
    print("Target repository verification complete. Finish the human/agent gates in VERIFY.md.")
    return 1 if failed else 0


# ----------------------------- Safe harbour -----------------------------

def manifest_from_config(
    data: dict[str, Any], *, inspect_target: bool = False, exists_fn: Callable[[str], bool] | None = None
) -> dict[str, Any]:
    validate_config(data)
    state_by_name: dict[str, str] = {}
    observed = False
    if inspect_target:
        rows = inspect_repository_state(data, exists_fn=exists_fn)
        state_by_name = {row["name"]: row["action"] for row in rows}
        observed = any(row["action"] != "UNKNOWN" for row in rows)

    repositories = []
    for repo in repos_from_config(data):
        row = dict(repo)
        row["observed_action"] = state_by_name.get(repo["name"], "NOT_OBSERVED")
        repositories.append(row)

    target = data["target"]
    deployment_context = json.loads(json.dumps(data.get("deployment_context", {"scope": "shared"})))
    integrations = data.get("integrations", {})
    specialist_systems = list(integrations.get("specialist_systems", []))
    private_files = integrations.get("private_files", "not-declared")
    memory = integrations.get("memory", "optional")

    manual_prerequisites = [
        "reprovision required credentials through the approved external credential/identity owner",
        "restore or reconnect private files through the declared private-file owner",
        "restore or reconnect specialist-system data through each owning system",
        "restore trusted runtime machine/state separately when one is required",
        "run ARC verification after repository and external-owner restoration",
    ]

    manifest: dict[str, Any] = {
        "manifest_schema": MANIFEST_SCHEMA,
        "arc_version": read_arc_version(),
        "exported_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "target": {
            "business_name": target.get("business_name", ""),
            "owner": target["owner"],
            "owner_type": target.get("owner_type", "org"),
            "default_visibility": target.get("default_visibility", "private"),
        },
        "repositories": repositories,
        "deployment_context": deployment_context,
        "integrations": {
            "private_files": private_files,
            "specialist_systems": specialist_systems,
            "memory": memory,
        },
        "observation": {
            "repository_state_observed": observed,
            "meaning": "REUSE means observed present; CREATE means observed missing; UNKNOWN/NOT_OBSERVED is not evidence of absence.",
        },
        "compatibility": {
            "manifest_schema": MANIFEST_SCHEMA,
            "exported_by_arc": read_arc_version(),
            "minimum_reader": "0.3.0",
        },
        "recovery": {
            "repository_reconstruction": "ARC bootstrap may recreate missing configured GitHub repositories when --apply selects bounded mutation; existing repositories remain unchanged.",
            "excluded_material": [
                "credential values",
                "private-file contents",
                "CRM/ERP/ATS/accounting records",
                "database contents",
                "trusted-runtime machine state",
                "derived memory contents",
            ],
            "manual_prerequisites": manual_prerequisites,
        },
    }
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> None:
    if not isinstance(manifest, dict):
        raise ArcError("Estate manifest root must be a JSON object")
    assert_no_sensitive_material(manifest, "ARC estate manifest")
    if manifest.get("manifest_schema") != MANIFEST_SCHEMA:
        raise ArcError(f"Unsupported estate manifest schema: {manifest.get('manifest_schema')!r}; expected {MANIFEST_SCHEMA}")
    arc_version = manifest.get("arc_version")
    if not isinstance(arc_version, str) or arc_version.count(".") != 2:
        raise ArcError("Estate manifest arc_version must be semantic version X.Y.Z")
    target = manifest.get("target")
    if not isinstance(target, dict) or not isinstance(target.get("owner"), str) or not target["owner"].strip():
        raise ArcError("Estate manifest requires target.owner")
    if target.get("owner_type", "org") not in VALID_OWNER_TYPES:
        raise ArcError("Estate manifest target.owner_type is invalid")
    if target.get("default_visibility", "private") not in VALID_VISIBILITY:
        raise ArcError("Estate manifest default visibility is invalid")
    repos = manifest.get("repositories")
    if not isinstance(repos, list) or not repos:
        raise ArcError("Estate manifest requires repositories")
    seen: set[str] = set()
    for repo in repos:
        if not isinstance(repo, dict):
            raise ArcError("Estate manifest repository rows must be objects")
        name = repo.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ArcError("Estate manifest repository requires name")
        if name in seen:
            raise ArcError(f"Estate manifest duplicate repository: {name}")
        seen.add(name)
        if repo.get("visibility", target.get("default_visibility", "private")) not in VALID_VISIBILITY:
            raise ArcError(f"Estate manifest invalid visibility for {name}")
        if repo.get("observed_action", "NOT_OBSERVED") not in {"REUSE", "CREATE", "UNKNOWN", "NOT_OBSERVED"}:
            raise ArcError(f"Estate manifest invalid observed_action for {name}")
    integrations = manifest.get("integrations", {})
    if not isinstance(integrations, dict):
        raise ArcError("Estate manifest integrations must be an object")
    systems = integrations.get("specialist_systems", [])
    if not isinstance(systems, list) or not all(isinstance(item, str) for item in systems):
        raise ArcError("Estate manifest specialist_systems must be a string list")
    config_from_manifest(manifest, _validated=True)


def load_manifest(path: str) -> dict[str, Any]:
    manifest = _load_json(path, "Estate manifest")
    validate_manifest(manifest)
    return manifest


def write_manifest(manifest: dict[str, Any], path: str, *, overwrite: bool = False) -> Path:
    validate_manifest(manifest)
    target = Path(path)
    if target.exists() and not overwrite:
        raise ArcError(f"Refusing to overwrite existing estate manifest: {path}. Use --overwrite explicitly.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return target


def config_from_manifest(manifest: dict[str, Any], _validated: bool = False) -> dict[str, Any]:
    if not _validated:
        if manifest.get("manifest_schema") != MANIFEST_SCHEMA:
            raise ArcError(f"Unsupported estate manifest schema: {manifest.get('manifest_schema')!r}")
    target = manifest["target"]
    repositories: list[dict[str, Any]] = []
    domains: list[dict[str, Any]] = []
    for repo in manifest.get("repositories", []):
        base = {
            "name": repo["name"],
            "description": repo.get("description", "ARC recovered owner."),
            "visibility": repo.get("visibility", target.get("default_visibility", "private")),
        }
        if repo.get("role") == "business-domain":
            domains.append(base)
        else:
            repositories.append({
                **base,
                "role": repo.get("role", "component"),
                "required": bool(repo.get("required", True)),
            })
    config = {
        "arc_version": manifest.get("arc_version", read_arc_version()),
        "target": {
            "business_name": target.get("business_name", ""),
            "owner": target["owner"],
            "owner_type": target.get("owner_type", "org"),
            "default_visibility": target.get("default_visibility", "private"),
        },
        "repositories": repositories,
        "domains": domains,
        "deployment_context": json.loads(json.dumps(manifest.get("deployment_context", {"scope": "shared"}))),
        "integrations": {
            "private_files": manifest.get("integrations", {}).get("private_files", "not-declared"),
            "specialist_systems": list(manifest.get("integrations", {}).get("specialist_systems", [])),
            "memory": manifest.get("integrations", {}).get("memory", "optional"),
        },
    }
    validate_config(config)
    return config


def command_export(data: dict[str, Any], args: argparse.Namespace) -> int:
    manifest = manifest_from_config(data, inspect_target=args.inspect_target)
    path = write_manifest(manifest, args.output, overwrite=args.overwrite)
    print(f"ARC estate manifest written: {path}")
    print(f"Manifest schema: {MANIFEST_SCHEMA}; ARC version: {manifest['arc_version']}")
    print("No secret values or external owner contents were exported. No remote mutation performed.")
    return 0


def command_restore_plan(manifest: dict[str, Any], inspect_target: bool = False) -> int:
    print("ARC safe-harbour restore plan")
    print(f"Manifest schema: {manifest['manifest_schema']}")
    print(f"Exported by ARC: {manifest['arc_version']}")
    data = config_from_manifest(manifest)
    command_plan(data, inspect_target=inspect_target)
    print("External/manual recovery prerequisites:")
    for item in manifest.get("recovery", {}).get("manual_prerequisites", []):
        print(f"- {item}")
    print("No mutation performed. Use `restore --apply` to create missing configured repositories when mutation is authorised.")
    return 0


def command_restore(manifest: dict[str, Any], *, apply: bool, inspect_target: bool = False) -> int:
    data = config_from_manifest(manifest)
    if not apply:
        print("ARC recovery preview: no mutation selected. Use `restore --apply` to create missing configured repositories.")
        return command_restore_plan(manifest, inspect_target=inspect_target)
    print("ARC restore apply boundary: bounded GitHub repository reconstruction only; existing repositories remain unchanged.")
    result = command_bootstrap(data, True)
    print("External owners were NOT restored. Complete the manifest manual prerequisites, then run ARC verification.")
    return result


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
    modes = (ROOT / ".github/skills/atlas/references/modes.md").read_text(encoding="utf-8")
    for mode in ATLAS_MODES:
        if f"`{mode}`" not in modes:
            raise ArcError(f"Atlas mode missing from reference: {mode}")
    example = json.loads((ROOT / "profiles/generic-business/arc.example.json").read_text(encoding="utf-8"))
    clone = json.loads(json.dumps(example))
    if clone.get("target", {}).get("owner") == "YOUR-GITHUB-ORG":
        clone["target"]["owner"] = "example-org"
    validate_config(clone)
    sample_manifest = manifest_from_config(clone)
    validate_manifest(sample_manifest)
    restored = config_from_manifest(sample_manifest)
    validate_config(restored)
    print(f"ARC self-verification PASS (v{version}, estate manifest schema {MANIFEST_SCHEMA})")
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="FolderDesk deployment and recovery utility")
    sub = p.add_subparsers(dest="command", required=True)

    onboard = sub.add_parser("onboard", help="Create a valid ARC profile without remote mutation")
    onboard.add_argument("--output", default="arc.json")
    onboard.add_argument("--overwrite", action="store_true")
    onboard.add_argument("--non-interactive", action="store_true")
    onboard.add_argument("--business-name")
    onboard.add_argument("--owner")
    onboard.add_argument("--owner-type", choices=sorted(VALID_OWNER_TYPES), default="org")
    onboard.add_argument("--visibility", choices=sorted(VALID_VISIBILITY), default="private")
    onboard.add_argument("--domains")
    onboard.add_argument("--private-files", default="not-declared")
    onboard.add_argument("--specialist-systems")
    onboard.add_argument("--memory", default="optional")
    onboard.add_argument("--tenant-id", help="Canonical tenant identifier for a managed-client deployment")
    onboard.add_argument("--entity-ref", help="Optional canonical owner-system entity reference; requires --tenant-id")

    doctor = sub.add_parser("doctor")
    doctor.add_argument("--config", required=True)
    doctor.add_argument("--connectors", action="store_true", help="Show read-only connector/MCP/runtime readiness without inspecting secrets")

    plan = sub.add_parser("plan")
    plan.add_argument("--config", required=True)
    plan.add_argument("--inspect-target", action="store_true", help="Classify configured repositories as REUSE/CREATE without mutation")

    bootstrap = sub.add_parser("bootstrap")
    bootstrap.add_argument("--config", required=True)
    bootstrap.add_argument("--apply", action="store_true", help="Create missing configured repositories")

    verify = sub.add_parser("verify")
    verify.add_argument("--config", required=True)

    export = sub.add_parser("export", help="Export a non-secret ARC estate manifest")
    export.add_argument("--config", required=True)
    export.add_argument("--output", default="arc-estate.json")
    export.add_argument("--overwrite", action="store_true")
    export.add_argument("--inspect-target", action="store_true")

    restore_plan = sub.add_parser("restore-plan", help="Produce a non-mutating plan from an ARC estate manifest")
    restore_plan.add_argument("--manifest", required=True)
    restore_plan.add_argument("--inspect-target", action="store_true")

    restore = sub.add_parser("restore", help="Plan or apply bounded GitHub repository reconstruction")
    restore.add_argument("--manifest", required=True)
    restore.add_argument("--inspect-target", action="store_true")
    restore.add_argument("--apply", action="store_true")

    sub.add_parser("verify-self")
    return p


def main() -> int:
    args = parser().parse_args()
    try:
        if args.command == "verify-self":
            return command_verify_self()
        if args.command == "onboard":
            return command_onboard(args)
        if args.command in {"restore-plan", "restore"}:
            manifest = load_manifest(args.manifest)
            if args.command == "restore-plan":
                return command_restore_plan(manifest, inspect_target=args.inspect_target)
            return command_restore(manifest, apply=args.apply, inspect_target=args.inspect_target)

        data = load_config(args.config)
        if args.command == "doctor":
            return command_doctor(data, connectors=args.connectors)
        if args.command == "plan":
            return command_plan(data, args.inspect_target)
        if args.command == "bootstrap":
            return command_bootstrap(data, args.apply)
        if args.command == "verify":
            return command_verify(data)
        if args.command == "export":
            return command_export(data, args)
        raise ArcError(f"Unknown command: {args.command}")
    except ArcError as exc:
        print(f"ARC ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())