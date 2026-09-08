from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 1) Seed a public-safe, generic document-intake Skill into every new FolderDesk Skills estate.
skill_dir = ROOT / 'starter' / 'skills' / 'document-intake'
skill_dir.mkdir(parents=True, exist_ok=True)
(skill_dir / 'SKILL.md').write_text(r'''---
name: document-intake
description: Default FolderDesk intake for any file or document a user gives an agent. Preserve/file the source, ingest only useful material, route durable meaning/tasks to the correct owner, preserve provenance, and verify later retrieval.
---

# Document Intake — File It, Learn It, Find It Again

Use this Skill **by default whenever a user gives the agent a file/document** unless a more specific domain Skill owns the intake.

FolderDesk is not complete when an agent merely reads a file in the current chat. The source and its useful organisational meaning must survive the session.

## Default route

```text
RECEIVE
→ FILE SOURCE
→ INVENTORY / IDENTIFY
→ EXTRACT USEFUL CONTENT
→ CLASSIFY
→ ROUTE KNOWLEDGE + TASKS
→ PRESERVE PROVENANCE
→ VERIFY RETRIEVAL
→ STOP
```

## Rules

1. **File the source** — preserve the original document in the organisation's declared private-file owner/project folder when an authorised write route exists. Do not bulk-copy private binaries into public GitHub. If the source is already durably stored, reuse it and preserve its stable locator instead of duplicating it.
2. **Identify it deterministically** — record enough metadata to distinguish the document: source/provider, stable id or path/locator where available, filename/title, type and useful modified/version marker. This is inventory, not ingestion.
3. **Ingest useful material** — extract/read the material needed for the user's work. Do not report a file as ingested merely because it was listed or inventoried.
4. **Classify and route** — place durable business meaning with the correct canonical owner. Reusable operating HOW belongs in the organisation's Skills owner. Neutral identity belongs with the organisation's identity/data owner where applicable. Domain facts stay with the domain owner.
5. **Create/attach tasks when the document implies work** — actions, deadlines, decisions or follow-ups should become durable task/work state in the organisation's normal task owner rather than remaining trapped in chat.
6. **Preserve provenance** — retained facts/summaries/actions must point back to the source locator/id/path so another agent can verify them.
7. **Verify retrieval** — before calling intake complete, prove that a future agent can find both (a) the source document or durable source locator and (b) the useful canonical knowledge/task state derived from it using a reasonable filename/topic/person/project query.
8. **No duplicate corpus** — do not create a new global vector database, document lake, daemon or duplicate knowledge store merely for intake. Use the organisation's existing file owner, canonical owners and search/retrieval surfaces.

## Completion test

A file intake is GREEN only when all are true:

- original source is durably filed or already durably stored with a preserved locator;
- useful content was actually extracted when needed;
- durable meaning/tasks were routed to the correct owner;
- provenance is preserved;
- retrieval was tested successfully.

If any one is missing, report the exact incomplete stage rather than saying the file is "saved" or "remembered".

## Reference implementation

The TBHRC/iMPLEMENTAi reference implementation uses LOOP3 for bounded ingestion and LIB1 for canonical placement. Other organisations should keep equivalent behaviour in their own canonical Skills system without depending on TBHRC-private business data.
''', encoding='utf-8')

# 2) Ensure the foundation seeder installs the intake Skill and uses current product branding.
seed = ROOT / 'scripts' / 'seed_foundation.py'
text = seed.read_text(encoding='utf-8')
text = text.replace('''    "research-escalation",\n)''', '''    "research-escalation",\n    "document-intake",\n)''', 1)
text = text.replace("Seed ARC foundational Skill", "Seed FolderDesk foundational Skill")
text = text.replace("ARC Skills foundation preview", "FolderDesk Skills foundation preview")
text = text.replace("ARC foundational Skills seeding complete", "FolderDesk foundational Skills seeding complete")
text = text.replace('description="ARC foundational Skills seeder"', 'description="FolderDesk foundational Skills seeder"')
text = text.replace("ARC FOUNDATION ERROR", "FOLDERDESK FOUNDATION ERROR")
seed.write_text(text, encoding='utf-8')

# 3) Make the generated client Router carry the default file-intake route.
arc = ROOT / 'scripts' / 'arc.py'
text = arc.read_text(encoding='utf-8')
old = '''    orchestrator = f"{skills_base}/tree/main/github-multi-agent-orchestrator"\n    return f"""# AGENTS.md — Repository Router\\n\\nThis file is the repository **Router** and cold-start contract. Read it first. Follow only the Fast Link needed for the task; do not preload linked material.\\n\\n**Repository role:** {role_label(repo['role'])}\\n\\n**Core Fast Links:** [Skills]({skills_base}) · [Research](https://github.com/{owner}/{research}) · [Workflow]({workflow}) · [Sniper]({sniper}) · [Multi-Agent Orchestrator]({orchestrator})\\n\\n**Repository Fast Links:** [README](README.md) · [Atlas](.github/skills/atlas/SKILL.md) · [Issues](https://github.com/{owner}/{repo['name']}/issues) · [FolderDesk](https://github.com/tbhrc/folderdesk)\\n\\n## Route\\n\\n- **Known owner + bounded task** → use the most-specific repository Fast Link / Skill and execute.\\n'''
new = '''    orchestrator = f"{skills_base}/tree/main/github-multi-agent-orchestrator"\n    document_intake = f"{skills_base}/tree/main/document-intake"\n    return f"""# AGENTS.md — Repository Router\\n\\nThis file is the repository **Router** and cold-start contract. Read it first. Follow only the Fast Link needed for the task; do not preload linked material.\\n\\n**Repository role:** {role_label(repo['role'])}\\n\\n**Core Fast Links:** [Skills]({skills_base}) · [Document Intake]({document_intake}) · [Research](https://github.com/{owner}/{research}) · [Workflow]({workflow}) · [Sniper]({sniper}) · [Multi-Agent Orchestrator]({orchestrator})\\n\\n**Repository Fast Links:** [README](README.md) · [Atlas](.github/skills/atlas/SKILL.md) · [Issues](https://github.com/{owner}/{repo['name']}/issues) · [FolderDesk](https://github.com/tbhrc/folderdesk)\\n\\n## Route\\n\\n- **User gives you a file/document** → use [Document Intake]({document_intake}) by default: preserve/file the source in the declared private-file owner, ingest useful material, route durable knowledge/tasks to the correct owner with provenance, then verify the source and derived knowledge can be retrieved later. Inventory alone is not ingestion.\\n- **Known owner + bounded task** → use the most-specific repository Fast Link / Skill and execute.\\n'''
if old not in text:
    raise SystemExit('generated_agents insertion point not found')
text = text.replace(old, new, 1)
arc.write_text(text, encoding='utf-8')

# 4) Root Router: make file intake a first-hop default in the FolderDesk repo itself.
agents = ROOT / 'AGENTS.md'
a = agents.read_text(encoding='utf-8')
a = a.replace(
    '**Core Fast Links:** [Workflow](https://github.com/tbhrc/skills/tree/main/github-agent-workflow) · [LIB1 Librarian](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian)',
    '**Core Fast Links:** [Workflow](https://github.com/tbhrc/skills/tree/main/github-agent-workflow) · [LOOP3 File Ingestion](https://github.com/tbhrc/skills/tree/main/loop-data-source-ingestion) · [LIB1 Librarian](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian)',
    1,
)
needle = '- **Known owner + bounded task** → execute with the most-specific Skill/tool.\n'
insert = '- **User gives you a file/document** → default to [LOOP3](https://github.com/tbhrc/skills/tree/main/loop-data-source-ingestion) + [LIB1](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian): preserve/file the source in its declared private-file owner, ingest useful material, route durable meaning/tasks to the correct owner with provenance, and verify later retrieval. Inventory alone is not ingestion; do not leave the only useful copy/meaning trapped in chat.\n'
if insert not in a:
    if needle not in a:
        raise SystemExit('root AGENTS route insertion point not found')
    a = a.replace(needle, insert + needle, 1)
agents.write_text(a, encoding='utf-8')

# 5) Human-facing product description and default file flow.
readme = ROOT / 'README.md'
r = readme.read_text(encoding='utf-8')
r = r.replace(
    'FolderDesk gives your business a **GitHub-first operating desk for humans and AI agents**. It provides the reusable structure, routing, Skills model, deployment and recovery patterns needed to turn capable AI tools into an organised operating environment rather than a collection of disconnected chats.',
    'FolderDesk gives your business a **GitHub-first task-management, filing and organisational-memory system for humans and AI agents**. It turns capable AI tools into an organised operating environment that can track work, file what you give it, preserve useful knowledge and find it again later — reducing the admin chaos of disconnected chats, loose documents and forgotten follow-ups.',
    1,
)
r = r.replace(
    '- a persistent GitHub operating desk for human + AI work;\n',
    '- a persistent GitHub operating desk and task-management layer for human + AI work;\n- a default document-intake route that files source documents, ingests useful content and makes both the source and derived knowledge retrievable later;\n',
    1,
)
marker = '## Step 1 — Connect GitHub\n'
section = '''## Give FolderDesk a file\n\nWhen you give your agent a document, the default is **not** "read it once and forget it." FolderDesk treats that as an intake event:\n\n```text\nreceive file\n→ file/preserve original in your declared private-file owner\n→ identify + ingest useful content\n→ route facts, decisions and tasks to the correct durable owner\n→ preserve provenance back to the source\n→ verify the document and useful knowledge can be found again\n```\n\nThis is how FolderDesk becomes a filing machine and organisational memory rather than another chat window. It remembers **where the source lives and what durable work/knowledge came from it**. Inventory/checkpoint metadata alone does not count as ingestion.\n\n'''
if section not in r:
    if marker not in r:
        raise SystemExit('README insertion point not found')
    r = r.replace(marker, section + marker, 1)
r = r.replace(
    'After deployment, show me verification status, connection readiness and the next useful capability to activate.\n',
    'If I give you a file or document, treat it as a FolderDesk intake event: preserve/file the source, ingest useful content, route durable knowledge/tasks with provenance, and verify I can retrieve it later.\nAfter deployment, show me verification status, connection readiness and the next useful capability to activate.\n',
    1,
)
readme.write_text(r, encoding='utf-8')

# 6) Bootstrap surfaces the seeded intake Skill and intended default behaviour.
bootstrap = ROOT / 'BOOTSTRAP.md'
b = bootstrap.read_text(encoding='utf-8')
b = b.replace(
    'Starter Skills exist only to make a blank environment usable. They remain thin bootstrap pointers; the deployed organisation should establish and evolve its own canonical Skills repository.\n',
    'Starter Skills exist only to make a blank environment usable. FolderDesk also seeds a generic `document-intake` Skill so a client-supplied file is filed, ingested, routed with provenance and retrieval-tested by default from day one. The deployed organisation should evolve its own canonical Skills repository without duplicating business truth.\n',
    1,
)
bootstrap.write_text(b, encoding='utf-8')

# 7) Ultimate Features: add the product promise as canonical capability truth.
features = ROOT / 'FEATURES.md'
f = features.read_text(encoding='utf-8')
anchor = '| Core harness | General-purpose human + AI operating harness | Core | FolderDesk Router + owners |\n'
rows = '''| Work management | Durable task/work identity across agents and sessions | Core/Reference | GitHub Issues + owner state |\n| Work management | Extract actions, decisions and follow-ups from received documents | Reference | Document Intake + domain/task owner |\n| Documents | Default client file/document intake | Core | `document-intake` starter Skill + Router |\n| Documents | File/preserve original source in declared private-file owner | Core/Connected | Private-file owner (for example OneDrive/SharePoint) |\n| Documents | Selective content ingestion instead of read-once chat use | Reference | Document Intake / LOOP3 pattern |\n| Documents | Provenance from durable knowledge/tasks back to source | Core/Reference | Source locator + canonical owner |\n| Documents | Retrieve source documents and derived organisational knowledge later | Core/Reference | File owner + GitHub/owner search |\n| Documents | Admin-chaos reduction through filing + task + knowledge continuity | Core/Reference | FolderDesk operating model |\n'''
if rows not in f:
    if anchor not in f:
        raise SystemExit('FEATURES insertion point not found')
    f = f.replace(anchor, anchor + rows, 1)
features.write_text(f, encoding='utf-8')

# 8) Regression coverage.
test_path = ROOT / 'tests' / 'test_issue_51_document_intake.py'
test_path.write_text(r'''import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_doc_intake", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class DocumentIntakeDefaultTests(unittest.TestCase):
    def test_starter_document_intake_skill_exists_and_requires_retrieval(self):
        text = (ROOT / "starter/skills/document-intake/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("by default whenever a user gives the agent a file/document", text)
        self.assertIn("FILE SOURCE", text)
        self.assertIn("VERIFY RETRIEVAL", text)
        self.assertIn("inventory, not ingestion", text.lower())
        self.assertIn("provenance", text.lower())

    def test_foundation_seeds_document_intake(self):
        spec2 = importlib.util.spec_from_file_location("folderdesk_seed", ROOT / "scripts" / "seed_foundation.py")
        seed = importlib.util.module_from_spec(spec2)
        assert spec2.loader is not None
        spec2.loader.exec_module(seed)
        self.assertIn("document-intake", seed.STARTER_SKILLS)
        paths = [path for path, _ in seed.starter_files()]
        self.assertIn("document-intake/SKILL.md", paths)

    def test_generated_agent_router_has_default_file_route(self):
        repo = {"name": "ops", "role": "operations", "description": "Ops", "required": True, "visibility": "private"}
        agents = arc.generated_agents("acme", repo, {"skills": "skills", "research": "research"})
        self.assertIn("[Document Intake](https://github.com/acme/skills/tree/main/document-intake)", agents)
        self.assertIn("User gives you a file/document", agents)
        self.assertIn("verify the source and derived knowledge can be retrieved later", agents)
        self.assertIn("Inventory alone is not ingestion", agents)

    def test_public_product_surfaces_file_task_memory_positioning(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        features = (ROOT / "FEATURES.md").read_text(encoding="utf-8")
        self.assertIn("task-management, filing and organisational-memory system", readme)
        self.assertIn("Give FolderDesk a file", readme)
        self.assertIn("find it again later", readme)
        self.assertIn("Default client file/document intake", features)
        self.assertIn("Retrieve source documents and derived organisational knowledge later", features)
        self.assertIn("Admin-chaos reduction", features)


if __name__ == "__main__":
    unittest.main()
''', encoding='utf-8')
