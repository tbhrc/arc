# FolderDesk Architecture

FolderDesk is a small file-native operating surface for capable human + AI work. **Start with one workspace repository. Expand only when demonstrated need earns another boundary.**

**Fast links:** [README](README.md) · [Atlas](ATLAS.md) · [Router](AGENTS.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Manifest](MANIFEST.md)

## Core operating graph

```text
request
→ one workspace
→ root AGENTS.md Router
→ smallest relevant local context / Skill / connected owner
→ act with native reasoning or an existing tool
→ write useful result
→ verify once
→ stop
```

## Default workspace

```text
workspace repository/
├── AGENTS.md
├── README.md
├── work/
├── knowledge/
├── outputs/
├── archive/
└── .folderdesk/
    ├── README.md
    └── skills/
```

- `work/` — active work.
- `knowledge/` — durable business/domain knowledge.
- `outputs/` — finished deliverables.
- `archive/` — inactive history.
- `.folderdesk/` — reusable agent support, Skills, non-secret config and earned machinery.

Domains such as Sales, Delivery, Finance or Marketing are **local context/folder concerns by default**. They do not automatically become repositories.

## Expansion is optional

A second repository must earn its boundary. Good reasons include:

- materially different access/security/privacy requirements;
- independently owned or released product/capability;
- genuine concurrent or isolated execution needs;
- an external/public distribution boundary;
- a mature capability whose separate lifecycle is demonstrably simpler.

Bad reason: “there are several departments.”

When expansion is earned, add it explicitly to `repositories[]`; FolderDesk already supports multiple configured repositories without requiring them at bootstrap.

## Files first, machinery second

Use:

```text
clear instruction
+ source evidence
+ native reasoning/tools
→ useful result
→ observe real failure
→ smallest proven fix
```

Do not pre-build queues, databases, agents, services, status layers or approval machinery for hypothetical future needs. Add deterministic code when an exact machine contract, repeated mechanical failure, scale advantage or hard boundary proves it valuable.

## One owner / one truth

Keep live truth in its real owner:

| State | Default owner |
|---|---|
| active business work | workspace `work/` |
| durable business/domain knowledge | workspace `knowledge/` or connected owner system |
| finished deliverables | workspace `outputs/` / declared file owner |
| reusable local HOW | `.folderdesk/skills/` |
| CRM/ERP/accounting records | specialist system |
| transactional/identity data | database/system designed for it |
| private documents | approved private-file owner |
| credentials | approved secret/identity store |

A mature organisation may later promote reusable Skills, Research or product/runtime code into separate repositories. Promotion changes the owner; it is not a default deployment requirement.

## Context discipline

- Keep root routing small.
- Route before loading.
- Put conditional depth one semantic hop away.
- Human-readable files do not replace deterministic validation where correctness needs it.
- File organisation can decay; prune, promote or reset when structure starts becoming the work.

## Recovery

FolderDesk Safe Harbour is architecture/context recovery, not a substitute for every external owner's backup.

```text
known-good FolderDesk release
+ folderdesk-estate.json
+ external owners' recovery methods
→ recreate missing configured repositories
→ reconnect external owners
→ verify
```

Existing repositories are left unchanged by current restore/bootstrap behavior.

## Acceptance

FolderDesk is healthy when a fresh capable person or agent can enter one repository, find the relevant context, produce useful work, preserve reusable learning without ceremony, and expand the topology only after a real boundary appears.

## KISSS

> **The operating system must not become the work.**

Before adding structure or machinery: `DELETE → COLLAPSE → REUSE → DIRECT → only then ADD`.
