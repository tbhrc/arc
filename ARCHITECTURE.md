# FolderDesk Architecture

FolderDesk is a small file-native operating surface for capable human + AI work. **Start with one self-contained workspace repository. Expand only when demonstrated need earns another boundary.** The preserved ChatGPT FolderDesk connector is one ingress into multiple authorised execution nodes; node-specific transports stay behind that connector rather than multiplying ChatGPT apps per machine.

The design intentionally combines the strongest proven ideas from FolderDesk Tiny—small canonical structure, smart-agent-first execution, earned Skills, learning and lightweight drift checking—with the fuller FolderDesk business capabilities needed for real client deployment: document intake, client experience, integration/recovery boundaries and optional expansion.

**Fast links:** [README](README.md) · [Atlas](ATLAS.md) · [Router](AGENTS.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Manifest](MANIFEST.md)

## Core operating graph

```text
request
→ one workspace
→ root AGENTS.md Router
→ smallest relevant local context / Skill / connected owner
→ optional execution through the preserved connector to the required authorised node
→ act with native reasoning or an existing tool
→ write useful result
→ verify once
→ learn only when a material lesson exists
→ stop
```

The current live mesh proof routes FD0 to the VPS and Mac through existing transports. A home-server node is reserved in the same contract but remains unavailable until its real authorised transport is identified. This is a routing concern behind the connector, not a reason to create another ChatGPT connector, queue or control plane.

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
    ├── managed.json
    └── skills/
        ├── structure/
        ├── skill-builder/
        ├── lessons/
        ├── auditor/
        ├── document-intake/
        └── client-experience/
```

- `work/` — active work.
- `knowledge/` — durable business/domain knowledge.
- `outputs/` — finished deliverables.
- `archive/` — inactive history.
- `.folderdesk/` — reusable agent support, Skills, non-secret config and earned machinery.

Domains such as Sales, Delivery, Finance or Marketing are **local context/folder concerns by default**. They do not automatically become repositories or a pre-created departmental tree.

## Six foundational local Skills

A fresh FolderDesk-managed workspace is usable without depending on TBHRC's internal Skill Bank:

| Skill | Owns |
|---|---|
| `structure` | canonical workspace vocabulary and placement |
| `skill-builder` | creation/update of earned reusable local HOW |
| `lessons` | material real-work learning that changes future behaviour |
| `auditor` | one-shot semantic/structural/behaviour/purpose drift and necessity checking |
| `document-intake` | durable file/document preservation, ingestion, provenance and retrieval |
| `client-experience` | business-first onboarding, communication, connectors and polished outputs |

These are progressive-loaded. Their presence does not mean every task loads every Skill.

The Auditor is deliberately not the organisation's old mandatory lifecycle. It does not require an Issue, approval state, recurring run, ledger or audit-before-execution ritual. It is used when actual drift/over-engineering is suspected or after a material structural change.

## Expansion is optional

A second repository must earn its boundary. Good reasons include:

- materially different access/security/privacy requirements;
- independently owned or released product/capability;
- genuine concurrent or isolated execution needs;
- an external/public distribution boundary;
- a mature capability whose separate lifecycle is demonstrably simpler.

Bad reason: “there are several departments.”

When expansion is earned, add it explicitly to `repositories[]`; FolderDesk supports multiple configured repositories without requiring them at bootstrap.

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

Do not pre-build queues, databases, agents, services, status layers, control planes or approval machinery for hypothetical future needs. Add deterministic code when an exact machine contract, repeated mechanical failure, scale advantage or hard boundary proves it valuable.

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

## Managed vs adopted repositories

FolderDesk-created repositories carry `.folderdesk/managed.json`. That marker means the repository claims the FolderDesk-managed structural contract.

An existing exact-path repository without that marker is **reused/unmanaged** until explicitly adopted. FolderDesk must not call it broken merely because it lacks FolderDesk scaffolding, and bootstrap must not silently overwrite it.

GitHub redirects/transfers are resolved before mutation. An exact configured owner/path is required; `OWNER_MISMATCH` is a stop condition rather than an implicit redirect-following deployment.

## Context discipline

- Keep root routing small.
- Route before loading.
- Put conditional depth one semantic hop away.
- Human-readable files do not replace deterministic validation where correctness needs it.
- File organisation can decay; prune, promote or reset when structure starts becoming the work.
- Research/programme machinery belongs outside the first-day client baseline unless a real deployment need earns it.

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

FolderDesk is healthy when a fresh capable person or agent can enter one repository, discover the six core routes without preloading them, produce useful work, preserve files/learning with provenance, detect real drift without governance ceremony, and expand topology only after a real boundary appears.

## KISSS

> **The operating system must not become the work.**

Before adding structure or machinery: `DELETE → COLLAPSE → REUSE → DIRECT → SKILL → only then ADD`.