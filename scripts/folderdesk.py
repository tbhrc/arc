#!/usr/bin/env python3
"""FolderDesk onboarding, deployment, export and recovery CLI.

FolderDesk starts with one useful workspace repository. Additional repositories are an
explicit expansion choice, not a bootstrap requirement. The CLI stores only portable
architecture metadata: never credential values or copied external business data.
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
MANIFEST_SCHEMA = "2.0"
VALID_VISIBILITY = {"public", "private", "internal"}
VALID_OWNER_TYPES = {"org", "user"}
VALID_DEPLOYMENT_SCOPES = {"shared", "tenant"}
ATLAS_MODES = ("onboard", "adopt", "audit", "health", "upgrade", "recover", "next")
BASELINE_SKILLS = (
    "structure",
    "skill-builder",
    "lessons",
    "auditor",
    "document-intake",
    "client-experience",
)
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
    "profiles/generic-business/folderdesk.example.json",
    "scripts/package_atlas.py",
]
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


class FolderDeskError(RuntimeError):
    pass


def read_folderdesk_version() -> str:
    path = ROOT / "VERSION"
    if path.exists():
        value = path.read_text(encoding="utf-8").strip()
        if value:
            return value
    return "2.0.0"


def _load_json(path: str, label: str) -> dict[str, Any]:
    p = Path(path)
    if not p.exists():
        raise FolderDeskError(f"{label} not found: {path}")
    try:
        value = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise FolderDeskError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise FolderDeskError(f"{label} root must be a JSON object")
    return value


def _walk_secret_like_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            path = f"{prefix}.{key_text}" if prefix else key_text
            if any(fragment in key_text.lower() for fragment in SECRET_KEY_FRAGMENTS):
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
    elif isinstance(value, str) and any(pattern.search(value) for pattern in SENSITIVE_VALUE_PATTERNS):
        found.append(prefix or "<root>")
    return found


def assert_no_sensitive_material(value: Any, label: str) -> None:
    secret_keys = _walk_secret_like_keys(value)
    if secret_keys:
        raise FolderDeskError(f"{label} must never contain secret-like fields: " + ", ".join(secret_keys))
    sensitive_values = _walk_sensitive_values(value)
    if sensitive_values:
        raise FolderDeskError(f"{label} appears to contain credential values at: " + ", ".join(sensitive_values))


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise FolderDeskError(f"Cannot derive repository/folder name from: {value!r}")
    return slug


def parse_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_config(data: dict[str, Any]) -> None:
    if not isinstance(data, dict):
        raise FolderDeskError("Config root must be a JSON object")
    assert_no_sensitive_material(data, "FolderDesk configuration")

    version = data.get("folderdesk_version")
    if not isinstance(version, str) or version.count(".") != 2:
        raise FolderDeskError("folderdesk_version must be semantic version X.Y.Z")

    target = data.get("target")
    if not isinstance(target, dict):
        raise FolderDeskError("Config must contain target object")
    owner = target.get("owner")
    if not isinstance(owner, str) or not owner.strip() or owner == "YOUR-GITHUB-ORG":
        raise FolderDeskError("target.owner must be a real GitHub organisation/user")
    if target.get("owner_type", "org") not in VALID_OWNER_TYPES:
        raise FolderDeskError(f"target.owner_type must be one of {sorted(VALID_OWNER_TYPES)}")
    visibility = target.get("default_visibility", "private")
    if visibility not in VALID_VISIBILITY:
        raise FolderDeskError(f"target.default_visibility must be one of {sorted(VALID_VISIBILITY)}")

    deployment_context = data.get("deployment_context", {"scope": "shared"})
    if not isinstance(deployment_context, dict):
        raise FolderDeskError("deployment_context must be an object")
    scope = deployment_context.get("scope", "shared")
    if scope not in VALID_DEPLOYMENT_SCOPES:
        raise FolderDeskError(f"deployment_context.scope must be one of {sorted(VALID_DEPLOYMENT_SCOPES)}")
    tenant_id = deployment_context.get("tenant_id")
    entity_ref = deployment_context.get("entity_ref")
    if scope == "tenant":
        if not isinstance(tenant_id, str) or not tenant_id.strip():
            raise FolderDeskError("tenant-scoped deployment requires deployment_context.tenant_id")
        if entity_ref is not None and (not isinstance(entity_ref, str) or not entity_ref.strip()):
            raise FolderDeskError("deployment_context.entity_ref must be non-empty when provided")
    elif tenant_id not in (None, "") or entity_ref not in (None, ""):
        raise FolderDeskError("shared deployment_context must not declare tenant_id or entity_ref")

    repos = data.get("repositories")
    if not isinstance(repos, list) or not repos:
        raise FolderDeskError("repositories must contain at least the primary workspace repository")
    names: set[str] = set()
    workspace_count = 0
    for repo in repos:
        if not isinstance(repo, dict):
            raise FolderDeskError("each repositories item must be an object")
        name = repo.get("name")
        if not isinstance(name, str) or not name.strip():
            raise FolderDeskError("each repository requires a non-empty name")
        if name in names:
            raise FolderDeskError(f"duplicate repository name: {name}")
        names.add(name)
        if repo.get("visibility", visibility) not in VALID_VISIBILITY:
            raise FolderDeskError(f"invalid visibility for {name}")
        if repo.get("role", "workspace") == "workspace":
            workspace_count += 1
    if workspace_count != 1:
        raise FolderDeskError("exactly one primary workspace repository is required")

    domains = data.get("domains", [])
    if not isinstance(domains, list):
        raise FolderDeskError("domains must be a list")
    domain_names: set[str] = set()
    for domain in domains:
        if not isinstance(domain, dict) or not isinstance(domain.get("name"), str) or not domain["name"].strip():
            raise FolderDeskError("each domain requires a non-empty name")
        if domain["name"] in domain_names:
            raise FolderDeskError(f"duplicate domain: {domain['name']}")
        domain_names.add(domain["name"])


def build_onboarding_config(
    *,
    business_name: str,
    owner: str,
    repository: str | None = None,
    owner_type: str = "org",
    visibility: str = "private",
    domains: list[str] | None = None,
    private_files: str = "not-declared",
    specialist_systems: list[str] | None = None,
    memory: str = "optional",
    tenant_id: str | None = None,
    entity_ref: str | None = None,
) -> dict[str, Any]:
    workspace = slugify(repository or business_name)
    domain_rows = [
        {"name": slugify(domain), "label": domain.strip(), "description": f"{domain.strip()} domain/context inside the workspace."}
        for domain in (domains or [])
    ]
    deployment_context: dict[str, Any] = {"scope": "shared"}
    if tenant_id:
        deployment_context = {"scope": "tenant", "tenant_id": tenant_id.strip()}
        if entity_ref:
            deployment_context["entity_ref"] = entity_ref.strip()
    elif entity_ref:
        raise FolderDeskError("entity_ref requires tenant_id for tenant-scoped deployment")

    data: dict[str, Any] = {
        "folderdesk_version": read_folderdesk_version(),
        "target": {
            "business_name": business_name.strip(),
            "owner": owner.strip(),
            "owner_type": owner_type,
            "default_visibility": visibility,
        },
        "deployment_context": deployment_context,
        "repositories": [
            {
                "name": workspace,
                "description": f"{business_name.strip()} FolderDesk workspace.",
                "role": "workspace",
                "required": True,
            }
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
        raise FolderDeskError(f"Refusing to overwrite existing config: {path}. Use --overwrite explicitly.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return target


def load_config(path: str) -> dict[str, Any]:
    data = _load_json(path, "Config")
    validate_config(data)
    return data


def repos_from_config(data: dict[str, Any]) -> list[dict[str, Any]]:
    default_visibility = data["target"].get("default_visibility", "private")
    rows: list[dict[str, Any]] = []
    for repo in data.get("repositories", []):
        rows.append({
            "name": repo["name"],
            "description": repo.get("description", "FolderDesk repository."),
            "role": repo.get("role", "component"),
            "required": bool(repo.get("required", True)),
            "visibility": repo.get("visibility", default_visibility),
        })
    return rows


def primary_workspace(data: dict[str, Any]) -> dict[str, Any]:
    for repo in repos_from_config(data):
        if repo["role"] == "workspace":
            return repo
    raise FolderDeskError("No workspace repository configured")


def run(cmd: list[str], *, check: bool = True, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, input=input_text, capture_output=True, check=check)


def gh_available() -> bool:
    return shutil.which("gh") is not None


def gh_authenticated() -> bool:
    return gh_available() and run(["gh", "auth", "status"], check=False).returncode == 0


def gh_active_login() -> str | None:
    if not gh_authenticated():
        return None
    result = run(["gh", "api", "user", "--jq", ".login"], check=False)
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def gh_repo_identity(full_name: str) -> dict[str, str] | None:
    result = run(["gh", "repo", "view", full_name, "--json", "nameWithOwner,url"], check=False)
    if result.returncode != 0:
        return None
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise FolderDeskError(f"GitHub returned invalid repository metadata for {full_name}") from exc
    resolved = payload.get("nameWithOwner")
    if not isinstance(resolved, str) or not resolved.strip():
        raise FolderDeskError(f"GitHub did not return resolved repository ownership for {full_name}")
    return {"requested": full_name, "resolved": resolved, "url": str(payload.get("url", ""))}


def gh_repo_exists(full_name: str) -> bool:
    return gh_repo_identity(full_name) is not None


def gh_target_operability(data: dict[str, Any]) -> tuple[bool, str]:
    actor = gh_active_login()
    if not actor:
        return False, "active GitHub identity could not be resolved"
    target = data["target"]
    owner = target["owner"]
    owner_type = target.get("owner_type", "org")
    if owner_type == "user":
        ok = actor.lower() == owner.lower()
        return ok, f"active account {actor}; target user {owner}"
    query = "query($login:String!){organization(login:$login){viewerCanCreateRepositories}}"
    result = run(["gh", "api", "graphql", "-f", f"query={query}", "-F", f"login={owner}"], check=False)
    if result.returncode != 0:
        return False, f"active account {actor}; could not confirm repository-create access to organisation {owner}"
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        return False, f"active account {actor}; GitHub organisation access response was invalid"
    org = payload.get("data", {}).get("organization")
    allowed = bool(isinstance(org, dict) and org.get("viewerCanCreateRepositories"))
    return allowed, f"active account {actor}; target organisation {owner}; create access {'confirmed' if allowed else 'not confirmed'}"


def inspect_repository_state(
    data: dict[str, Any], exists_fn: Callable[[str], bool] | None = None
) -> list[dict[str, str]]:
    owner = data["target"]["owner"]
    repos = repos_from_config(data)
    if exists_fn is not None:
        rows: list[dict[str, str]] = []
        for repo in repos:
            requested = f"{owner}/{repo['name']}"
            exists = exists_fn(requested)
            rows.append({
                "name": repo["name"],
                "full_name": requested,
                "resolved_name": requested if exists else "",
                "action": "REUSE" if exists else "CREATE",
            })
        return rows
    if not gh_authenticated():
        return [
            {"name": repo["name"], "full_name": f"{owner}/{repo['name']}", "resolved_name": "", "action": "UNKNOWN"}
            for repo in repos
        ]
    rows = []
    for repo in repos:
        requested = f"{owner}/{repo['name']}"
        identity = gh_repo_identity(requested)
        if identity is None:
            rows.append({"name": repo["name"], "full_name": requested, "resolved_name": "", "action": "CREATE"})
            continue
        resolved = identity["resolved"]
        action = "REUSE" if resolved.lower() == requested.lower() else "OWNER_MISMATCH"
        rows.append({"name": repo["name"], "full_name": requested, "resolved_name": resolved, "action": action})
    return rows


def role_label(role: str) -> str:
    return {
        "workspace": "Primary FolderDesk workspace",
        "skills": "Optional separate reusable HOW / Skills owner",
        "research": "Optional separate research owner",
        "trusted-runtime": "Optional privileged runtime owner",
        "component": "Explicit expansion repository",
    }.get(role, role.replace("-", " ").title())


def generated_readme(data: dict[str, Any], repo: dict[str, Any]) -> str:
    business = data["target"].get("business_name") or repo["name"]
    domains = data.get("domains", [])
    domain_text = ", ".join(domain.get("label", domain["name"]) for domain in domains) if domains else "none declared yet"
    expansion_note = (
        "This is the primary workspace. Keep work here until a real ownership, scale, security, concurrency or lifecycle boundary earns another repository."
        if repo["role"] == "workspace"
        else "This repository exists because the deployment explicitly expanded beyond the primary workspace."
    )
    return f"""# {business}\n\n**FolderDesk role:** {role_label(repo['role'])}\n\n{repo['description']}\n\n{expansion_note}\n\n## Human surface\n\n- `work/` — active human/agent work\n- `knowledge/` — durable business/domain knowledge\n- `outputs/` — finished deliverables\n- `archive/` — inactive historical material\n- `.folderdesk/` — agent support, reusable Skills, configuration and machinery\n\nDeclared domains: {domain_text}. Domains are in-repository context/folder concerns by default, **not repositories**.\n\n## Start\n\n1. Read `AGENTS.md`.\n2. Do the real work in the smallest appropriate human folder.\n3. Use `.folderdesk/` only for reusable support/machinery.\n4. Expand to another repository only after a concrete boundary proves it useful.\n5. Verify the requested real-world result before claiming completion.\n\nFolderDesk upstream: https://github.com/tbhrc/folderdesk\n"""


def generated_agents(data: dict[str, Any], repo: dict[str, Any]) -> str:
    owner = data["target"]["owner"]
    full = f"{owner}/{repo['name']}"
    return f"""# AGENTS.md — FolderDesk Router\n\nStart with the work. FolderDesk supports the task; it is not the task.\n\n**Repository:** {full}  \n**Role:** {role_label(repo['role'])}\n\n- Assume a capable reasoning agent. Use clear instructions + existing tools first.\n- Human work lives in `work/`, `knowledge/`, `outputs/`, or `archive/`.\n- Agent support, reusable Skills, configuration and machinery live under `.folderdesk/`.\n- **Folder/naming/placement question** → use [Structure](.folderdesk/skills/structure/SKILL.md).\n- **Repeatable operating behaviour worth keeping** → use [Skill Builder](.folderdesk/skills/skill-builder/SKILL.md).\n- **Material failure/insight that should change future behaviour** → use [Lessons](.folderdesk/skills/lessons/SKILL.md).\n- **Suspected structural/semantic/behaviour/purpose drift** → use [Auditor](.folderdesk/skills/auditor/SKILL.md) once; it is not a recurring gate.\n- **User gives you a file/document** → use [Document Intake](.folderdesk/skills/document-intake/SKILL.md).\n- **Client-facing onboarding, communication or business artifact** → use [Client Experience](.folderdesk/skills/client-experience/SKILL.md).\n- Issues are optional continuity, not runtime permission.\n- Reuse before create. Prefer direct reasoning and native repository/platform capability before wrappers.\n- Route before loading. Keep cold-start context small and load depth only when needed.\n- One meaning, one canonical home. Do not create duplicate truth or status layers.\n- Domains are local context/folder concerns unless a real boundary earns separation.\n- Additional repositories are optional expansion. Add one only for a proven ownership, security, scale, concurrency, lifecycle or independent-review boundary.\n- Add deterministic code only for a repeated mechanical failure, exact machine contract, scale advantage or hard boundary.\n- Verify the requested outcome once in the correct owner, then stop.\n\n**Core Skills:** [Structure](.folderdesk/skills/structure/SKILL.md) · [Skill Builder](.folderdesk/skills/skill-builder/SKILL.md) · [Lessons](.folderdesk/skills/lessons/SKILL.md) · [Auditor](.folderdesk/skills/auditor/SKILL.md) · [Document Intake](.folderdesk/skills/document-intake/SKILL.md) · [Client Experience](.folderdesk/skills/client-experience/SKILL.md)\n\n**Fast links:** [README](README.md) · [FolderDesk support](.folderdesk/README.md) · [Atlas](.github/skills/atlas/SKILL.md) · [Issues](https://github.com/{full}/issues) · [Upstream](https://github.com/tbhrc/folderdesk)\n"""


def generated_folderdesk_support() -> str:
    return """# FolderDesk support\n\nThis directory contains agent support and reusable machinery for this workspace.\n\nDefault rule: **keep it small**. Start with files + native reasoning. Add a Skill, script, index, database, agent or service only after a real requirement proves the current surface insufficient.\n\n## Core local Skills\n\n- `skills/structure/` — canonical workspace vocabulary and placement\n- `skills/skill-builder/` — reusable capability creation/update\n- `skills/lessons/` — material learning that changes future behaviour\n- `skills/auditor/` — one-shot drift/necessity check; never a recurring gate\n- `skills/document-intake/` — preserve, ingest, route and retrieve documents\n- `skills/client-experience/` — business-first onboarding and client-facing output\n\nOther local homes:\n\n- `config/` — non-secret FolderDesk/workspace configuration\n- `evidence/` — bounded machine/operator evidence when native Git history is insufficient\n\nDo not move normal business work out of `work/`, `knowledge/`, `outputs/`, or `archive/` merely because an agent is doing it.\n"""


def generated_atlas_pointer() -> str:
    return """---\nname: atlas\ndescription: \"FolderDesk front-door pointer. Use for FolderDesk onboarding, adoption, audit, health, upgrade, recovery, next-action guidance, deployment or diagnosis.\"\n---\n\n# Atlas Pointer\n\nCurrent canonical Atlas: https://github.com/tbhrc/folderdesk/blob/main/.github/skills/atlas/SKILL.md\n\nStart single-repository-first. Expand only when a concrete boundary earns it. Inspect/plan when useful; ordinary authorised bounded work does not require a second approval ritual.\n"""


def generated_atlas_prompt() -> str:
    return """Use the local `atlas` project Skill and load the current FolderDesk upstream contract from https://github.com/tbhrc/folderdesk. Start single-repository-first and expand only from demonstrated need. Atlas supports onboard, adopt, audit, health, upgrade, recover and next modes.\n"""


def put_content(full: str, path: str, content: str, *, sha: str | None = None) -> None:
    payload: dict[str, str] = {
        "message": f"Seed FolderDesk {path}",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    result = run(["gh", "api", f"repos/{full}/contents/{path}", "-X", "PUT", "--input", "-"], check=False, input_text=json.dumps(payload))
    if result.returncode != 0:
        raise FolderDeskError(f"Failed to seed {full}/{path}: {result.stderr.strip() or result.stdout.strip()}")


def starter_skill_files() -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for skill in BASELINE_SKILLS:
        path = ROOT / "starter" / "skills" / skill / "SKILL.md"
        if not path.exists():
            raise FolderDeskError(f"Missing baseline Skill: {path.relative_to(ROOT)}")
        rows.append((f"{skill}/SKILL.md", path.read_text(encoding="utf-8")))
    return rows


def generated_managed_marker(repo: dict[str, Any]) -> str:
    return json.dumps({
        "managed_by": "FolderDesk",
        "folderdesk_version": read_folderdesk_version(),
        "role": repo["role"],
    }, indent=2) + "\n"


def seed_new_repo(data: dict[str, Any], repo: dict[str, Any]) -> None:
    owner = data["target"]["owner"]
    full = f"{owner}/{repo['name']}"
    current = run(["gh", "api", f"repos/{full}/contents/README.md", "--jq", ".sha"], check=False)
    if current.returncode != 0 or not current.stdout.strip():
        raise FolderDeskError(f"Cannot resolve initial README for {full}")
    put_content(full, "README.md", generated_readme(data, repo), sha=current.stdout.strip())
    put_content(full, "AGENTS.md", generated_agents(data, repo))
    put_content(full, ".github/skills/atlas/SKILL.md", generated_atlas_pointer())
    put_content(full, ".github/prompts/atlas.prompt.md", generated_atlas_prompt())
    put_content(full, ".folderdesk/README.md", generated_folderdesk_support())
    put_content(full, ".folderdesk/managed.json", generated_managed_marker(repo))
    sync_adapter = (ROOT / "scripts" / "sync_agent_skills.py").read_text(encoding="utf-8")
    put_content(full, ".folderdesk/scripts/sync_agent_skills.py", sync_adapter)
    put_content(full, ".folderdesk/skills/README.md", "# Workspace Skills\n\nFolderDesk's core local Skills are seeded here. Add another Skill only after repeatable real work earns it.\n")
    for skill_path, content in starter_skill_files():
        put_content(full, f".folderdesk/skills/{skill_path}", content)
    for seed_path in ("work/.gitkeep", "knowledge/.gitkeep", "outputs/.gitkeep", "archive/.gitkeep"):
        put_content(full, seed_path, "")
    print(f"SEED {full}: self-contained FolderDesk workspace")


def create_repo(data: dict[str, Any], repo: dict[str, Any]) -> bool:
    owner = data["target"]["owner"]
    full = f"{owner}/{repo['name']}"
    identity = gh_repo_identity(full)
    if identity is not None:
        if identity["resolved"].lower() != full.lower():
            raise FolderDeskError(f"Refusing repository owner/path mismatch: requested {full}, resolved {identity['resolved']}")
        print(f"REUSE {full} (existing repository left unchanged)")
        return False
    cmd = ["gh", "repo", "create", full, f"--{repo['visibility']}", "--description", repo["description"], "--add-readme"]
    result = run(cmd, check=False)
    if result.returncode != 0:
        raise FolderDeskError(f"Failed to create {full}: {result.stderr.strip() or result.stdout.strip()}")
    print(f"CREATE {full}")
    seed_new_repo(data, repo)
    return True


def command_onboard(args: argparse.Namespace) -> int:
    if args.non_interactive:
        if not args.business_name or not args.owner:
            raise FolderDeskError("--non-interactive requires --business-name and --owner")
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
        repository=args.repository,
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
    print(f"Primary workspace: {owner}/{primary_workspace(data)['name']}")
    print("Single-repository-first: add another repositories[] entry only when a real boundary earns it.")
    return 0


def command_connection_readiness(data: dict[str, Any]) -> int:
    print("Connection readiness (read-only; not a deployment gate)")
    print("Repositories:")
    for repo in repos_from_config(data):
        print(f"- {repo['name']} ({repo['role']})")
    if gh_available() and gh_authenticated():
        print("- GitHub: WIRED (gh authenticated)")
    elif gh_available():
        print("- GitHub: NOT WIRED (gh present but unauthenticated)")
    else:
        print("- GitHub: NOT WIRED (gh unavailable)")
    integrations = data.get("integrations", {})
    print(f"- Private files connector: DECLARED {integrations.get('private_files', 'not-declared')}; external wiring UNVERIFIED")
    for system in integrations.get("specialist_systems", []):
        print(f"- Specialist connector/MCP: DECLARED {system}; external wiring UNVERIFIED")
    print(f"- Memory: DECLARED {integrations.get('memory', 'optional')}; external wiring UNVERIFIED")
    return 0


def command_doctor(data: dict[str, Any], *, connectors: bool = False) -> int:
    print(f"FolderDesk doctor for {data['target']['owner']}/{primary_workspace(data)['name']}")
    ok = True
    print(f"PASS Python {sys.version_info.major}.{sys.version_info.minor}")
    if not gh_available():
        print("FAIL GitHub CLI (gh) not found")
        ok = False
    elif gh_authenticated():
        print("PASS GitHub CLI found and authenticated")
        actor = gh_active_login()
        print(f"PASS GitHub identity resolved: {actor}" if actor else "CHECK GitHub identity could not be resolved")
    else:
        print("FAIL GitHub CLI is not authenticated for the intended target")
        ok = False
    states = inspect_repository_state(data) if gh_authenticated() else []
    mismatches = [row for row in states if row["action"] == "OWNER_MISMATCH"]
    for row in mismatches:
        print(f"FAIL repository identity mismatch: requested {row['full_name']}, resolved {row['resolved_name']}")
    ok = ok and not mismatches
    print("PASS configuration schema")
    if connectors:
        command_connection_readiness(data)
    return 0 if ok else 1


def command_plan(data: dict[str, Any], inspect_target: bool = False) -> int:
    target = data["target"]
    print("FolderDesk deployment plan")
    print(f"Business: {target.get('business_name', '')}")
    print(f"Target: {target['owner']} ({target.get('owner_type', 'org')})")
    state_by_name: dict[str, str] = {}
    if inspect_target:
        state_by_name = {row["name"]: row["action"] for row in inspect_repository_state(data)}
    for repo in repos_from_config(data):
        action = state_by_name.get(repo["name"], "PLANNED")
        marker = "primary" if repo["role"] == "workspace" else "explicit expansion"
        print(f"- {repo['name']}: {repo['role']} | {repo['visibility']} | {marker} | {action}")
    domains = data.get("domains", [])
    print("Domains (in-repository by default): " + (", ".join(d.get("label", d["name"]) for d in domains) if domains else "none declared"))
    print("No mutation performed.")
    return 0


def command_bootstrap(data: dict[str, Any], apply: bool) -> int:
    if not apply:
        print("FolderDesk bootstrap preview: no mutation selected. Use --apply to create missing configured repositories.")
        return command_plan(data)
    if not gh_authenticated():
        raise FolderDeskError("GitHub must be connected/authenticated before bootstrap --apply")
    states = inspect_repository_state(data)
    mismatches = [row for row in states if row["action"] == "OWNER_MISMATCH"]
    if mismatches:
        row = mismatches[0]
        raise FolderDeskError(f"Refusing repository owner/path mismatch: requested {row['full_name']}, resolved {row['resolved_name']}")
    if any(row["action"] == "CREATE" for row in states):
        target_ok, detail = gh_target_operability(data)
        if not target_ok:
            raise FolderDeskError(f"Cannot create repositories in configured target: {detail}")
        print(f"GitHub target access: confirmed ({detail}).")
    repos = repos_from_config(data)
    total = len(repos)
    started = time.monotonic()
    print(f"FolderDesk bootstrap starting with {total} configured repository/repositories.")
    for index, repo in enumerate(repos, start=1):
        full = f"{data['target']['owner']}/{repo['name']}"
        print(f"[{index}/{total}] Checking {full}...")
        create_repo(data, repo)
        elapsed = max(time.monotonic() - started, 0.0)
        remaining = max((elapsed / index) * (total - index), 0.0)
        print(f"[{index}/{total}] Complete | elapsed {elapsed:.1f}s | estimated remaining {remaining:.1f}s")
    print("FolderDesk bootstrap complete. New workspaces include the self-contained baseline Skills; existing repositories remain unchanged for explicit adoption/repair.")
    return 0


def gh_path_exists(full: str, path: str) -> bool:
    return run(["gh", "api", f"repos/{full}/contents/{path}"], check=False).returncode == 0


def command_verify(data: dict[str, Any]) -> int:
    if not gh_authenticated():
        raise FolderDeskError("GitHub CLI (gh) must be available and authenticated for target verification")
    owner = data["target"]["owner"]
    failed = False
    for repo in repos_from_config(data):
        full = f"{owner}/{repo['name']}"
        identity = gh_repo_identity(full)
        if identity is None:
            failed = failed or repo["required"]
            print(f"MISSING {full}")
            continue
        if identity["resolved"].lower() != full.lower():
            failed = failed or repo["required"]
            print(f"OWNER_MISMATCH {full}: resolves to {identity['resolved']}")
            continue
        if not gh_path_exists(full, ".folderdesk/managed.json"):
            print(f"REUSED/UNMANAGED {full}: existing repository is not claimed as FolderDesk-managed; adopt/seed explicitly if desired")
            continue
        required_paths = [
            "README.md",
            "AGENTS.md",
            ".folderdesk/README.md",
            ".folderdesk/managed.json",
            ".folderdesk/scripts/sync_agent_skills.py",
            ".github/skills/atlas/SKILL.md",
        ]
        required_paths.extend(f".folderdesk/skills/{skill}/SKILL.md" for skill in BASELINE_SKILLS)
        missing = [required_path for required_path in required_paths if not gh_path_exists(full, required_path)]
        if missing:
            failed = failed or repo["required"]
            print(f"INCOMPLETE {full}: missing {', '.join(missing)}")
        else:
            print(f"OK {full}: FolderDesk-managed workspace and baseline Skills present")
    print("Structural verification complete. External connectors, runtimes and business systems are operational only when separately verified through their owning systems.")
    return 1 if failed else 0


def manifest_from_config(data: dict[str, Any], *, inspect_target: bool = False, exists_fn: Callable[[str], bool] | None = None) -> dict[str, Any]:
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

    integrations = data.get("integrations", {})
    manifest: dict[str, Any] = {
        "manifest_schema": MANIFEST_SCHEMA,
        "folderdesk_version": read_folderdesk_version(),
        "exported_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "target": json.loads(json.dumps(data["target"])),
        "repositories": repositories,
        "domains": json.loads(json.dumps(data.get("domains", []))),
        "deployment_context": json.loads(json.dumps(data.get("deployment_context", {"scope": "shared"}))),
        "integrations": {
            "private_files": integrations.get("private_files", "not-declared"),
            "specialist_systems": list(integrations.get("specialist_systems", [])),
            "memory": integrations.get("memory", "optional"),
        },
        "observation": {
            "repository_state_observed": observed,
            "meaning": "REUSE means exact configured owner/path observed; OWNER_MISMATCH means GitHub resolved elsewhere; CREATE means observed missing; UNKNOWN/NOT_OBSERVED is not evidence of absence.",
        },
        "compatibility": {
            "manifest_schema": MANIFEST_SCHEMA,
            "exported_by_folderdesk": read_folderdesk_version(),
            "minimum_reader": "2.0.0",
        },
        "recovery": {
            "repository_reconstruction": "FolderDesk may recreate missing configured GitHub repositories; existing repositories remain unchanged.",
            "excluded_material": [
                "credential values",
                "private-file contents",
                "CRM/ERP/ATS/accounting records",
                "database contents",
                "trusted-runtime machine state",
                "derived memory contents",
            ],
        },
    }
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> None:
    if not isinstance(manifest, dict):
        raise FolderDeskError("Estate manifest root must be a JSON object")
    assert_no_sensitive_material(manifest, "FolderDesk estate manifest")
    if manifest.get("manifest_schema") != MANIFEST_SCHEMA:
        raise FolderDeskError(f"Unsupported estate manifest schema: {manifest.get('manifest_schema')!r}; expected {MANIFEST_SCHEMA}")
    version = manifest.get("folderdesk_version")
    if not isinstance(version, str) or version.count(".") != 2:
        raise FolderDeskError("Estate manifest folderdesk_version must be semantic version X.Y.Z")
    repos = manifest.get("repositories")
    if not isinstance(repos, list) or not repos:
        raise FolderDeskError("Estate manifest requires repositories")
    config_from_manifest(manifest, _validated=True)


def config_from_manifest(manifest: dict[str, Any], _validated: bool = False) -> dict[str, Any]:
    if not _validated and manifest.get("manifest_schema") != MANIFEST_SCHEMA:
        raise FolderDeskError(f"Unsupported estate manifest schema: {manifest.get('manifest_schema')!r}")
    config = {
        "folderdesk_version": manifest.get("folderdesk_version", read_folderdesk_version()),
        "target": json.loads(json.dumps(manifest["target"])),
        "repositories": [
            {
                "name": repo["name"],
                "description": repo.get("description", "FolderDesk repository."),
                "role": repo.get("role", "component"),
                "required": bool(repo.get("required", True)),
                "visibility": repo.get("visibility", manifest["target"].get("default_visibility", "private")),
            }
            for repo in manifest.get("repositories", [])
        ],
        "domains": json.loads(json.dumps(manifest.get("domains", []))),
        "deployment_context": json.loads(json.dumps(manifest.get("deployment_context", {"scope": "shared"}))),
        "integrations": json.loads(json.dumps(manifest.get("integrations", {}))),
    }
    validate_config(config)
    return config


def load_manifest(path: str) -> dict[str, Any]:
    manifest = _load_json(path, "Estate manifest")
    validate_manifest(manifest)
    return manifest


def write_manifest(manifest: dict[str, Any], path: str, *, overwrite: bool = False) -> Path:
    validate_manifest(manifest)
    target = Path(path)
    if target.exists() and not overwrite:
        raise FolderDeskError(f"Refusing to overwrite existing estate manifest: {path}. Use --overwrite explicitly.")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return target


def command_export(data: dict[str, Any], args: argparse.Namespace) -> int:
    manifest = manifest_from_config(data, inspect_target=args.inspect_target)
    path = write_manifest(manifest, args.output, overwrite=args.overwrite)
    print(f"FolderDesk estate manifest written: {path}")
    print(f"Manifest schema: {MANIFEST_SCHEMA}; FolderDesk version: {manifest['folderdesk_version']}")
    return 0


def command_restore_plan(manifest: dict[str, Any], inspect_target: bool = False) -> int:
    print("FolderDesk safe-harbour restore plan")
    print(f"Manifest schema: {manifest['manifest_schema']}")
    print(f"Exported by FolderDesk: {manifest['folderdesk_version']}")
    return command_plan(config_from_manifest(manifest), inspect_target=inspect_target)


def command_restore(manifest: dict[str, Any], *, apply: bool, inspect_target: bool = False) -> int:
    data = config_from_manifest(manifest)
    if not apply:
        return command_restore_plan(manifest, inspect_target=inspect_target)
    print("FolderDesk restore boundary: recreate only missing configured repositories; leave existing repositories unchanged.")
    return command_bootstrap(data, True)


def command_verify_self() -> int:
    missing = [path for path in REQUIRED_SELF_FILES if not (ROOT / path).exists()]
    if missing:
        raise FolderDeskError("Missing required FolderDesk files: " + ", ".join(missing))
    version = read_folderdesk_version()
    if version.count(".") != 2:
        raise FolderDeskError("VERSION must contain semantic version X.Y.Z")
    atlas = (ROOT / ".github/skills/atlas/SKILL.md").read_text(encoding="utf-8")
    if not atlas.startswith("---\nname: atlas\n"):
        raise FolderDeskError("Atlas Skill frontmatter missing or malformed")
    modes = (ROOT / ".github/skills/atlas/references/modes.md").read_text(encoding="utf-8")
    for mode in ATLAS_MODES:
        if f"`{mode}`" not in modes:
            raise FolderDeskError(f"Atlas mode missing from reference: {mode}")
    for skill in BASELINE_SKILLS:
        skill_path = ROOT / "starter" / "skills" / skill / "SKILL.md"
        if not skill_path.exists():
            raise FolderDeskError(f"Missing baseline Skill: {skill_path.relative_to(ROOT)}")
    example = json.loads((ROOT / "profiles/generic-business/folderdesk.example.json").read_text(encoding="utf-8"))
    clone = json.loads(json.dumps(example))
    if clone.get("target", {}).get("owner") == "YOUR-GITHUB-ORG":
        clone["target"]["owner"] = "example-org"
    validate_config(clone)
    manifest = manifest_from_config(clone)
    validate_manifest(manifest)
    validate_config(config_from_manifest(manifest))
    print(f"FolderDesk self-verification PASS (v{version}, manifest schema {MANIFEST_SCHEMA})")
    return 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="FolderDesk single-repo-first deployment and recovery utility")
    sub = p.add_subparsers(dest="command", required=True)

    onboard = sub.add_parser("onboard", help="Create a FolderDesk profile without remote mutation")
    onboard.add_argument("--output", default="folderdesk.json")
    onboard.add_argument("--overwrite", action="store_true")
    onboard.add_argument("--non-interactive", action="store_true")
    onboard.add_argument("--business-name")
    onboard.add_argument("--owner")
    onboard.add_argument("--repository", help="Primary workspace repository; defaults to a slug of the business name")
    onboard.add_argument("--owner-type", choices=sorted(VALID_OWNER_TYPES), default="org")
    onboard.add_argument("--visibility", choices=sorted(VALID_VISIBILITY), default="private")
    onboard.add_argument("--domains", help="Logical domains inside the primary workspace, comma-separated")
    onboard.add_argument("--private-files", default="not-declared")
    onboard.add_argument("--specialist-systems")
    onboard.add_argument("--memory", default="optional")
    onboard.add_argument("--tenant-id")
    onboard.add_argument("--entity-ref")

    doctor = sub.add_parser("doctor")
    doctor.add_argument("--config", required=True)
    doctor.add_argument("--connectors", action="store_true")

    plan = sub.add_parser("plan")
    plan.add_argument("--config", required=True)
    plan.add_argument("--inspect-target", action="store_true")

    bootstrap = sub.add_parser("bootstrap")
    bootstrap.add_argument("--config", required=True)
    bootstrap.add_argument("--apply", action="store_true")

    verify = sub.add_parser("verify")
    verify.add_argument("--config", required=True)

    export = sub.add_parser("export", help="Export a non-secret FolderDesk estate manifest")
    export.add_argument("--config", required=True)
    export.add_argument("--output", default="folderdesk-estate.json")
    export.add_argument("--overwrite", action="store_true")
    export.add_argument("--inspect-target", action="store_true")

    restore_plan = sub.add_parser("restore-plan")
    restore_plan.add_argument("--manifest", required=True)
    restore_plan.add_argument("--inspect-target", action="store_true")

    restore = sub.add_parser("restore")
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
        raise FolderDeskError(f"Unknown command: {args.command}")
    except FolderDeskError as exc:
        print(f"FOLDERDESK ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
