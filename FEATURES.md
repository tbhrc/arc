# FolderDesk Capability Catalogue

**Status:** Current FolderDesk v2 product/reference capability map  
**Product owner:** [`tbhrc/folderdesk`](https://github.com/tbhrc/folderdesk)

## Product baseline

FolderDesk v2 is a **single-repository-first, file-native human + AI operating workspace**. A new deployment starts with one useful workspace repository, normal human folders (`work/`, `knowledge/`, `outputs/`, `archive/`) and agent support under `.folderdesk/`. Domains are local context/folder concerns by default. Additional repositories are optional expansion and must earn their boundary.

Live mutable truth stays with the correct owner. FolderDesk connects CRM, accounting, file stores, databases, calendars, memory and specialist runtimes rather than copying them into a competing source of truth.

### Scope labels

- **Core** — directly implemented by FolderDesk v2.
- **Reference** — proven in the TBHRC/iMPLEMENTAi ecosystem and reusable when the relevant owner/capability is connected.
- **Connected** — supplied by an authorised external platform, connector, runtime or specialist system.

## Core capability map

| Category | Capability | Scope | Primary mechanism |
|---|---|---|---|
| Workspace | One useful workspace repository by default | Core | `scripts/folderdesk.py` + workspace Router |
| Workspace | `work/`, `knowledge/`, `outputs/`, `archive/` human surface | Core | FolderDesk workspace seed |
| Workspace | `.folderdesk/` agent-support surface | Core | Local Skills/config/machinery |
| Workspace | Domains as in-repository context rather than forced repositories | Core | `domains[]` profile metadata |
| Workspace | Optional repository expansion after demonstrated need | Core | Explicit `repositories[]` entries |
| Routing | Compact root request router | Core | `AGENTS.md` |
| Routing | Route before loading / progressive context | Core | Router + Skills |
| Routing | One owner / one truth | Core | Owner/source discipline |
| Skills | Reusable local Skills without a mandatory separate Skills repo | Core | `.folderdesk/skills/` |
| Skills | Optional promotion to a separate Skills owner later | Core/Reference | Explicit `role: skills` repository |
| Client experience | Non-technical client onboarding with GitHub hidden as agent backend | Core | Atlas + Client Experience Skill |
| Client experience | Brand learning from formal guidelines or representative documents | Core/Reference | Client Experience Skill + client sources |
| Client experience | Communication tone/terminology/detail adaptation | Core/Reference | Client Experience Skill + durable client context |
| Client experience | Proactive connector inference from client clues | Core/Connected | Atlas + native/dedicated connectors |
| Client experience | Google Workspace / Drive priority when client says documents are in Google | Core/Connected | Google Workspace / Drive connector + document intake |
| Client experience | Existing-system/connector discovery and smallest-useful-set activation | Core/Connected | Native/dedicated connectors + owner systems |
| Client experience | Polished DOCX/PDF default for natural business-document outputs | Reference/Connected | Document tools + client brand/style |
| Client experience | Backend technical evidence separated from normal client communication | Core | Router + Client Experience Skill |
| Documents | Default client file/document intake | Core | `document-intake` starter Skill |
| Documents | Selective content ingestion instead of read-once chat use | Reference | Document Intake / LOOP3 pattern |
| Documents | Provenance from durable knowledge/tasks back to source | Core/Reference | Source locator + canonical owner |
| Documents | Retrieve source documents and derived organisational knowledge later | Core/Reference | File owner + owner search |
| Documents | Admin-chaos reduction through filing + task + knowledge continuity | Core/Reference | FolderDesk operating model |
| Recovery | Non-secret portable deployment profile | Core | `folderdesk.json` |
| Recovery | Estate manifest | Core | `folderdesk-estate.json`, schema 2.0 |
| Recovery | Conservative reconstruction of missing configured repositories | Core | FolderDesk restore |
| Recovery | External-owner reconnection model | Core | Manifest + reconnection contract |
| Verification | Health / doctor inspection | Core | `scripts/folderdesk.py doctor` |
| Verification | Deployment verification | Core | `scripts/folderdesk.py verify` |
| Verification | Self-verification | Core | `scripts/folderdesk.py verify-self` + tests |
| Portability | Provider/runtime-neutral execution | Core | Native tools/connectors + optional specialist runtimes |
| Portability | Existing-estate adoption without forced restructuring | Core | Atlas KEEP / INTEGRATE default |
| Portability | Multi-tenant deployment context without cloning topology | Core | `deployment_context` |

## Expansion capabilities

These are available when real operating evidence warrants them; they are **not default bootstrap requirements**.

| Capability | Scope | When to use it |
|---|---|---|
| Separate Skills repository | Reference | Reusable HOW has a real independent owner/lifecycle |
| Separate Research repository | Reference | Research volume/ownership has matured beyond local workspace needs |
| Separate product/runtime repository | Reference | Independent release, access, execution or operational lifecycle |
| Multi-agent orchestration | Reference | Genuine parallel specialist work materially improves the outcome |
| Cross-repository routing | Reference | The organisation already has or has earned a multi-repo estate |
| Universal database / transactional stores | Connected/Reference | Identity, transactions, joins, concurrency or query guarantees exceed file semantics |
| Scheduled/conditional automation | Connected | Recurring or event-driven work requires persistent execution |
| File/folder ingestion loops | Reference | Large estates need deterministic inventory, delta detection and provenance |
| Hindsight/shared memory | Reference | Cross-session derived recall adds value without replacing canonical owner truth |
| VPS/local/self-hosted runtime | Connected | A capability genuinely requires privileged/local execution |

## Expansion test

A second repository should normally have at least one concrete reason:

- materially different ownership or access boundary;
- privacy/security separation;
- independent release/lifecycle;
- genuine concurrency or isolated execution need;
- public distribution separate from private work;
- mature reusable capability whose separate ownership is demonstrably simpler.

Several departments alone is **not** a reason to create several repositories.

## Current deployment commands

```bash
python3 scripts/folderdesk.py onboard --output folderdesk.json
python3 scripts/folderdesk.py doctor --config folderdesk.json --connectors
python3 scripts/folderdesk.py plan --config folderdesk.json --inspect-target
python3 scripts/folderdesk.py bootstrap --config folderdesk.json --apply
python3 scripts/folderdesk.py verify --config folderdesk.json
python3 scripts/folderdesk.py export --config folderdesk.json --output folderdesk-estate.json --inspect-target
```

## Deliberate non-features

- Forced repository-per-domain topology.
- Mandatory separate Skills, Research or Operations repositories for a new client.
- Monolithic all-in-one agent runtime.
- Duplicate canonical memory layer.
- Replacing specialist systems merely to make the estate look uniform.
- Databases, queues, vector stores or services before a demonstrated requirement earns them.

## Product principle

> **Start with one useful workspace. Expand only from demonstrated need. The operating system must not become the work.**
