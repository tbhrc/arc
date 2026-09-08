# FolderDesk Capability Catalogue

**Status:** Current product/reference capability map  
**Product owner:** [`tbhrc/folderdesk`](https://github.com/tbhrc/folderdesk)  
**Marketing controller:** [`tbhrc/marketing#1`](https://github.com/tbhrc/marketing/issues/1)  
**Hermes comparison research:** [`tbhrc/research#41`](https://github.com/tbhrc/research/issues/41)

## Purpose

This file is the canonical product-facing catalogue of capabilities FolderDesk can reproduce or connect in the TBHRC/iMPLEMENTAi reference implementation. It prevents Marketing, Sales and comparison assets from inventing a separate feature truth.

FolderDesk is not one monolithic agent runtime. It is the portable architecture for reproducing a human + AI operating ecosystem while live mutable truth remains with the correct owner.

### Scope labels

- **Core** — directly implemented by the portable FolderDesk package.
- **Reference** — proven in the TBHRC/iMPLEMENTAi reference ecosystem and reproducible by connecting the relevant owner/capability.
- **Connected** — provided by an authorised external/runtime/provider surface that FolderDesk routes to rather than reimplementing.

## Capability map

| Category | Capability | Scope | Primary owner / mechanism |
|---|---|---|---|
| Core harness | General-purpose human + AI operating harness | Core | FolderDesk Router + owners |
| Work management | Durable task/work identity across agents and sessions | Core/Reference | GitHub Issues + owner state |
| Work management | Extract actions, decisions and follow-ups from received documents | Reference | Document Intake + domain/task owner |
| Documents | Default client file/document intake | Core | `document-intake` starter Skill + Router |
| Documents | File/preserve original source in declared private-file owner | Core/Connected | Private-file owner (for example OneDrive/SharePoint) |
| Documents | Selective content ingestion instead of read-once chat use | Reference | Document Intake / LOOP3 pattern |
| Documents | Provenance from durable knowledge/tasks back to source | Core/Reference | Source locator + canonical owner |
| Documents | Retrieve source documents and derived organisational knowledge later | Core/Reference | File owner + GitHub/owner search |
| Documents | Admin-chaos reduction through filing + task + knowledge continuity | Core/Reference | FolderDesk operating model |
| Core harness | Persistent operating environment | Core | GitHub + durable owners |
| Core harness | Autonomous authorised execution | Reference | Agent runtimes + Workflow |
| Core harness | Tool-using agents | Reference | Native tools / plugins / MCP / gateways |
| Core harness | Long-running agent work | Reference | ChatGPT/Codex/Claude/Jules + GitHub continuity |
| Core harness | Provider/runtime-neutral execution | Core | Router + provider/operator Skills |
| Core harness | Web-agent-native operation without one mandatory local agent runtime | Core | GitHub-first Router/Skills + capable web agents/connectors |
| Core harness | Distributed specialist-owner architecture | Core | Repository/domain ownership model |
| Routing | Root request router | Core | Root `AGENTS.md` |
| Routing | Domain-owner routing | Core | Repository Router + Sniper/LIB1 when needed |
| Routing | One owner / one truth | Core | Source-of-truth architecture |
| Routing | Progressive Fast Links | Core | Router / Skill design |
| Routing | Cross-repository operation | Reference | Integrated TBHRC GitHub network |
| Skills | Canonical reusable Skills system | Reference | `tbhrc/skills` |
| Skills | Progressive Skill loading | Reference | Skill Router / Fast Links |
| Skills | Shared Skills across runtimes | Reference | Canonical GitHub Skills + pointers/adapters |
| Skills | Skill versioning | Reference | Skill `VERSION.md` lifecycle |
| Skills | Durable Skill lessons | Reference | Skill `LESSONS.md` |
| Skills | Skill packaging / distribution | Reference | Skill Builder + platform adapters |
| Self-evolution | Failure/correction → reusable learning | Reference | Skill Builder / Lessons |
| Self-evolution | Idea → audit → GREEN → implementation | Reference | LOOP1 |
| Self-evolution | Autonomous implementation when GREEN | Reference | LOOP1 authority model |
| Self-evolution | Over-engineering reduction | Reference | KISSS Auditor / PL2 |
| Self-evolution | Continuous OSS capability discovery | Reference | Open-Source Operations Radar |
| Self-evolution | Context/cold-start reduction | Reference | LOOP2 / context strategy |
| Multi-agent | Controller + bounded workers | Reference | MAO1 |
| Multi-agent | Parallel specialist workers | Reference | MAO1 + provider operators |
| Multi-agent | Independent AI review | Reference | MAO1 / reviewer routes |
| Multi-agent | Provider substitution | Reference | MAO1 + runtime/operator routes |
| Multi-agent | Durable worker handoff | Reference | GitHub Issue / owner state |
| Multi-agent | Evidence-backed worker acceptance | Reference | MAO1 verification model |
| Memory | Cross-session memory | Reference | Hindsight |
| Memory | Cross-agent shared memory | Reference | Hindsight |
| Memory | Canonical truth separated from memory | Core | GitHub owner truth + Hindsight derived memory |
| Memory | Memory correction / invalidation | Reference | Hindsight operator |
| Memory | Current-fact re-verification | Reference | Hindsight → owner truth |
| Automation | Scheduled tasks | Connected | ChatGPT Automations / workflow owners |
| Automation | Recurring tasks | Connected | Automations / GitHub Actions where appropriate |
| Automation | Conditional monitoring | Connected | Condition watches / owner automations |
| Automation | Silent no-change runs | Reference | Deterministic preflight / delta-first loops |
| Automation | Persistent scheduled-run continuity | Reference | Durable owner state / GitHub / checkpoints |
| Automation | Automated audits | Reference | KISSS Auditor and domain audits |
| Automation | Automated research runs | Reference | Research radar / automations |
| Ingestion | File/folder crawling | Reference | LOOP3 |
| Ingestion | OneDrive/SharePoint ingestion | Reference | LOOP3 provider routes |
| Ingestion | Repository-tree ingestion | Reference | LOOP3 / GitHub |
| Ingestion | Deterministic inventory | Reference | LOOP3 manifest |
| Ingestion | Delta detection | Reference | LOOP3 checkpoint diff |
| Ingestion | Changed-material-only AI processing | Reference | LOOP3 |
| Ingestion | Exact source provenance | Reference | LOOP3 + owner records |
| Ingestion | Checkpointing | Reference | LOOP3 manifests |
| Ingestion | Tiny metadata run logging | Reference | Ingestion Run Logger |
| Ingestion | Completeness gates | Reference | LOOP3 |
| Tools | MCP support | Connected | MCP-capable runtimes / connectors |
| Tools | Native app connectors | Connected | ChatGPT plugins/connectors |
| Tools | Composio app connectivity | Connected | Composio |
| Tools | Specialist API/tool gateway | Connected | Monid / Tool API Gateway |
| Tools | Terminal execution | Connected | Runtime operators |
| Tools | VPS execution | Connected | AI Engine / VPS operators |
| Tools | Local Mac execution | Connected | Mac runner/operator |
| Tools | Docker execution | Connected | Runtime owner |
| Tools | Web search / research | Connected | Agent web tools |
| Tools | Browser automation / extraction | Reference | Native browser routes / Scrapling / Playwright / agent-browser when justified |
| Tools | Image generation | Connected | Model/runtime image tooling |
| Tools | Speech / transcription | Reference | PLAUD / transcription Skills |
| GitHub | GitHub as canonical operating desk | Core | GitHub repositories / Issues / PRs |
| GitHub | Durable Issues as work identity / task tracker | Reference | GitHub Issues |
| GitHub | Cross-agent work recovery from objective, state, evidence and exact next action | Reference | GitHub Issues + canonical owner truth |
| GitHub | Fresh authorised web agent can continue work without the original runtime/session | Reference | GitHub-canonical work identity + Router/Skills |
| GitHub | PR-based engineering | Reference | GitHub workflow |
| GitHub | Persistent architecture history | Core | Git history |
| GitHub | Durable decisions / rationale | Reference | Owner docs / Issues / Hindsight derivative |
| Data | Universal person/organisation DB | Reference | `tbhrc/db` |
| Data | Neutral identity model | Reference | Universal DB |
| Data | Person-360 | Reference | Universal DB operator |
| Data | CRM/commercial projection | Reference | DB commercial view + adapters |
| Data | ATS/recruitment projection | Reference | DB + Recruitment/OpenCATS |
| Data | Employee/HR projection | Reference | DB + Employees |
| Data | Multi-tenant business context | Core/Reference | PL8 + department owners |
| Data | Provenance-aware shared data | Reference | DB + ingestion/domain owners |
| Governance | Real-boundary security | Reference | PL3 / owner controls |
| Governance | Founder approval only at consequential boundaries | Reference | Authority policies |
| Governance | KISSS / anti-overengineering | Core/Reference | FolderDesk principle + KISSS Auditor |
| Governance | Wolf detection / friction hunting | Reference | Auditor / Wolf ledger mechanisms |
| Governance | Incident ledger + learning | Reference | Incident owners + Skills lessons |
| Governance | Evidence-backed GREEN / AMBER / RED | Reference | Workflow convention |
| Governance | Proof-before-adopt research loop | Reference | Research → Test → Benchmark → Decide |
| Deployment | Bootstrap blank organisation | Core | `arc.py onboard/bootstrap` |
| Deployment | Adopt an existing organisation | Core | Atlas adopt mode / reuse owners |
| Deployment | Estate manifest | Core | FolderDesk manifest/export |
| Deployment | Architecture export | Core | Safe Harbour export |
| Deployment | Recovery plan | Core | Restore plan |
| Deployment | Bounded reconstruction | Core | Safe Harbour restore |
| Deployment | External-owner reconnection model | Core | Manifest / Atlas |
| Deployment | Client-specific deployment profiles | Core | FolderDesk profiles/config |
| Deployment | Reuse across organisations | Core | Portable architecture contract |
| Verification | Health / doctor inspection | Core | `arc.py doctor` |
| Verification | Deployment verification | Core | `arc.py verify` |
| Verification | Self-verification | Core | FolderDesk tests / verify-self |
| Product evidence | Measured reference implementation | Core | `ECOSYSTEM-EVIDENCE.md` |

## Flagship differentiators

### External GitHub-canonical work continuity

FolderDesk's reference operating model can anchor substantive work in GitHub Issues as an external durable work identity. The Issue is not runtime permission; it is the recoverable task/work record. A fresh authorised agent can recover the objective, current state, evidence and exact next action and continue without depending on the original chat session or agent runtime.

This is different from an agent runtime shipping its own internal task board. Current Hermes has a Kanban task system; the differentiator is **cross-agent, GitHub-canonical continuity outside the runtime**, not the existence of task cards alone.

### Web-agent-native adoption

FolderDesk does not require one mandatory installed local agent runtime. A capable web agent with the required GitHub/connectors/tools can operate the same canonical Router, Skills, Issues and owner truth. In suitable deployments this can materially reduce onboarding friction and avoid duplicating local runtime/API infrastructure; actual financial savings depend on the customer's chosen model subscriptions, connectors and execution mix and must be measured rather than assumed.

## Known capability gaps / deliberate non-features

These are not silently represented as available features:

| Capability | Current state |
|---|---|
| Live provider-neutral steer of a running worker | **Gap / research candidate** — Hermes pattern identified in `research#41`. |
| Stop one worker while preserving partial output across providers | **Gap / research candidate**. |
| Unified cross-provider Connection Doctor | **Partial / fragmented** — FolderDesk has health/reconnection architecture; unified doctor is a candidate. |
| Global emergency stop across all controlled execution | **Gap / deeper integration candidate**. |
| Unified exact raw session search across ChatGPT/Claude/Codex | **Gap / watch** — Hindsight is semantic memory, not a raw cross-provider transcript ledger. |
| Full web administration/control dashboard | **Deliberate non-feature for v1** unless real client friction proves it necessary. |
| Monolithic all-in-one agent runtime | **Deliberately rejected** — FolderDesk coordinates specialised owners/runtimes instead. |
| Duplicate canonical memory layer | **Deliberately rejected** — GitHub remains canon; Hindsight is derived memory. |
| Automatic local Skill self-editing outside GitHub canon | **Deliberately rejected** — Skill Builder owns reusable HOW lifecycle. |

## Marketing usage rule

Marketing and Sales may transform this catalogue into comparison pages, sales decks and positioning material, but claims must link back here or to the owning evidence. When a capability changes materially, update the product/owner truth first, then refresh downstream assets.
