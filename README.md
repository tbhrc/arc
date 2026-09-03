# ARC

**An open, Skills-first operating architecture for businesses where humans and AI agents work from the same durable map.**

ARC is not an AI chatbot, an automation bundle, or another project-management framework. It is a reproducible operating architecture for combining **GitHub, reusable Skills, AI agents, research, trusted runtimes, private files, specialist systems and durable verification** without turning any one tool into the whole business.

> Build once. Make the operating logic explicit. Give every capable agent the same map. Improve the system through evidence. Preserve enough non-secret architecture evidence to rebuild it.

## The ARC model

```text
HUMAN / BUSINESS NEED
        |
        v
PURPOSE / PRIORITY
        |
        v
SKILLS FIRST
what reusable HOW applies?
        |
        v
FIND THE OWNER
where do facts and state belong?
        |
        +-----------------------+
        |                       |
        v                       v
NORMAL AUTHORISED AGENT   RESEARCH ESCALATION
API / MCP / browser / CLI recurring capability gap?
        |                       |
        +-----------+-----------+
                    |
        can normal capability execute?
              /             \
            YES             NO
             |               |
             v               v
      DIRECT EXECUTION   TRUSTED RUNTIME
                         privileged bridge
              \             /
               +-----+-----+
                     |
                     v
               VERIFY REALITY
                     |
                     v
             DURABLE OWNER TRUTH
                     |
        reusable learning/capability?
              /             \
            YES             NO
             |               |
             v               v
        IMPROVE SKILL      FINISH
```

GitHub is the operating desk, not the database for everything. Skills own reusable method. Business/domain systems own their facts. Research finds better tools. Privileged runtimes exist only for capabilities normal agents cannot safely reach. Memory supports context; it does not replace current canon.

## Start with Atlas

**Atlas is ARC's universal human + agent front door.**

Tell a capable agent:

```text
Use the Atlas skill in this repository.
Understand my business and current ARC state.
Choose the correct Atlas mode.
Start in plan mode. Do not mutate anything until the plan is explicit and apply authority is given.
```

On IDE surfaces supporting GitHub prompt files:

```text
/atlas
```

Atlas supports seven intents:

```text
onboard | adopt | audit | health | upgrade | recover | next
```

For an established business, Atlas inventories first and classifies existing owners as:

```text
KEEP | INTEGRATE | MIGRATE | RESEARCH | RETIRE
```

For configured GitHub repositories, `plan --inspect-target` can show **REUSE / CREATE** before apply.

- Human front door: [ATLAS.md](ATLAS.md)
- Project Agent Skill: [.github/skills/atlas/SKILL.md](.github/skills/atlas/SKILL.md)
- Mode reference: [.github/skills/atlas/references/modes.md](.github/skills/atlas/references/modes.md)
- Prompt-file entrypoint: [.github/prompts/atlas.prompt.md](.github/prompts/atlas.prompt.md)
- Learn the operating method: [GitHub Course](https://github.com/tbhrc/gh-course)

## Deploy ARC

Prerequisites: Git, Python 3.10+, GitHub CLI (`gh`), and permission to create/configure repositories in the intended target.

```bash
git clone https://github.com/tbhrc/arc.git
cd arc

python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
# Review ownership, modules, provider/runtime routes, REUSE/CREATE and integrations.
python3 scripts/arc.py bootstrap --config arc.json --apply

# Review first-day Skills before applying them.
python3 scripts/seed_foundation.py --config arc.json
python3 scripts/seed_foundation.py --config arc.json --apply

python3 scripts/arc.py verify --config arc.json
```

`onboard`, `doctor`, `plan` and the Skills-foundation plan are non-mutating. `bootstrap` and Skills seeding mutate only when explicit `--apply` authority is present. A credential being available is never treated as apply authority.

ARC rejects common secret-like configuration fields and known credential-value patterns. Credential values belong in the correct external identity/secret store, never `arc.json`.

Read [BOOTSTRAP.md](BOOTSTRAP.md) before the first deployment.

## Modular by design

ARC does not impose one universal business stack.

The generic profile can declare optional **business modules**, **capable-agent/provider routes** and **runtime routes**:

```json
"modules": ["sales", "research", "website"],
"providers": ["capable-agent"],
"runtimes": ["github-hosted-actions"]
```

- [Business modules](modules/README.md) are ownership patterns, not mandatory SaaS bundles.
- [Provider routes](providers/README.md) are interchangeable capable-agent paths; no vendor is architectural canon.
- [Runtime routes](runtimes/README.md) follow least privilege: normal connected capability first, trusted runtime only for a genuine gap.
- [Integration classes](integrations/README.md) define how live specialist systems remain authoritative while agents operate through narrow identities and verifiable actions.
- [Security and governance](contracts/governance.md) defines repository visibility, merge protection, Actions permissions, agent authority, runner trust and break-glass boundaries.

A newly created Skills repository can also receive ARC's small generic first-day foundation: owner routing, proportionate GitHub work control, Skill authoring and Research escalation. Existing target Skill files are never overwritten automatically; after seeding, the target organisation owns its Skills canon.

## Safe harbour: export the architecture, not the private data

After a healthy deployment, export a non-secret ARC estate manifest and retain it alongside the formal ARC release/tag used by the estate:

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The estate manifest records:

- manifest schema version;
- ARC version/release reference;
- target GitHub/business ownership metadata;
- repository/domain names, roles, visibility and required/optional state;
- declared private-file and specialist-system owners **by name only**;
- optional observed GitHub repository state;
- compatibility and recovery-boundary metadata.

It explicitly does **not** contain:

- credential values;
- private-file contents;
- CRM / ERP / ATS / accounting records;
- database contents;
- trusted-runtime machine state;
- derived memory contents.

Plan recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Only after repository reconstruction is explicitly authorised:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

The apply boundary is deliberately narrow: ARC may recreate missing configured GitHub repositories through the same conservative bootstrap contract. External owners must be restored/reconnected through their own approved backup and identity processes, then the full ARC verification contract must pass.

Read [Safe-Harbour Contract](contracts/safe-harbour.md).

## What ARC installs

The generic profile describes a small operating estate rather than one giant repository:

| Component | Default repository | Purpose |
|---|---|---|
| Reusable method | `skills` | Canonical Skills and agent HOW |
| Discovery | `research` | External research, technology/tool discovery and proving |
| Operations | `ops` | Business-wide architecture, decisions and cross-domain control |
| Trusted runtime | `ai-engine` | Optional privileged execution bridge for genuine runtime gaps |
| Domain owners | configurable | Business units, products, services or workflows owning their facts |

ARC does **not** automatically configure production credentials, grant broad privileges, move client data, or restore third-party system records. Those remain explicit owner-specific decisions.

Every **newly created** repository is seeded with:

- a role-aware `README.md`;
- root `AGENTS.md`;
- a thin Atlas Agent Skill pointer;
- an `/atlas` prompt-file entrypoint for supported IDE surfaces.

Existing repositories are detected and reused **without overwrite**. Atlas then proposes how to integrate them safely.

## Portable Atlas Skill

Atlas has one editable canon: `.github/skills/atlas/`.

```bash
python3 scripts/package_atlas.py
```

This creates `dist/skill.zip` from that same directory. The package includes the canonical `SKILL.md`, ChatGPT metadata and Atlas mode reference; ARC does not maintain a second editable portable copy.

## Why ARC exists

ARC grew out of a real operating migration. The [GitHub Course](https://github.com/tbhrc/gh-course) began as an attempt to learn GitHub properly. Each useful capability was immediately applied to real operations. Issues became durable work objects. Pull Requests became controlled integration boundaries. Skills replaced scattered reusable SOP logic. Research became the discovery layer for missing capability. Self-hosted and VPS runtimes became bounded execution bridges rather than general control planes.

The system was learned, tested, corrected and operated—not invented only on a whiteboard. ARC packages the resulting architecture so another business does not need to repeat the entire discovery journey.

## Core design principles

1. **Skills first.** Reusable operating intelligence belongs in a canonical Skill layer.
2. **One owner for each kind of truth.** CRM state, accounting records, private files, research and GitHub canon are different owners.
3. **AI agents are operators.** They receive durable instructions, bounded tools, authority limits and verification expectations.
4. **Research recurring friction.** Repeated workarounds can trigger problem-to-platform discovery before custom infrastructure is invented.
5. **Privileged infrastructure is exceptional.** Use normal APIs/connectors first; trusted runtimes exist only for real execution gaps.
6. **Plan is not authority.** Inspection/planning stays separate from mutation.
7. **Existing businesses are adopted, not flattened.** Keep/integrate correct owners instead of replacing them to match a template.
8. **Deployment and recovery are incomplete until verified.** Green automation matters only when it proves the required outcome.
9. **Safe harbour references owners instead of stealing their data.** ARC preserves reconstructable architecture while private/live data remains with its real backup owner.
10. **Provider and runtime are separate choices.** A business can change capable-agent providers without redesigning ownership or forcing privileged execution.
11. **Chat is temporary context.** Material programme/Stage state belongs in GitHub Issues so a cold agent can continue without hidden conversation history.
12. **Specialist systems stay authoritative.** ARC coordinates their use; it does not clone live mailboxes, CRM, ATS, finance, private-file or database state into GitHub for agent convenience.
13. **Authority is action-specific.** Repository access never silently grants production, specialist-system, runner, secret-admin or root authority.

## Repository map

```text
ARC
├── ATLAS.md                         human + agent front door
├── ARCHITECTURE.md                  system model and boundaries
├── MANIFEST.md                      deployable component inventory
├── BOOTSTRAP.md                     deployment + safe-harbour path
├── VERIFY.md                        acceptance, recovery and health checks
├── profiles/                        deployment profiles
├── modules/                         optional business capability patterns
├── providers/                       provider-neutral agent contract
├── runtimes/                        least-privilege runtime contract
├── integrations/                    specialist-system integration classes
├── starter/skills/                  generic first-day Skills foundation
├── components/                      component-specific guidance
├── contracts/
│   ├── configuration.md             non-secret configuration contract
│   ├── ownership.md                 source-of-truth boundaries
│   ├── portability.md               what is portable vs externally owned
│   ├── safe-harbour.md              release/export/recovery contract
│   ├── governance.md                security and governance baseline
│   └── secrets.md                   credential boundary
├── scripts/arc.py                   onboard/plan/bootstrap/export/restore/verify CLI
├── scripts/package_atlas.py         portable Atlas packager
├── scripts/seed_foundation.py       first-day Skills seeder
└── .github/
    ├── skills/atlas/                 canonical Atlas Skill
    ├── prompts/atlas.prompt.md      /atlas-compatible prompt file
    └── workflows/validate-arc.yml   repository self-validation
```

## Profiles

- [Generic Business](profiles/generic-business/README.md) — start here for a new business/client; normally generate `arc.json` through Atlas/onboard rather than editing the example manually.
- [TBHRC Reference](profiles/tbhrc-reference/README.md) — shows how ARC maps onto the live environment that produced it. It is reference wiring, not copied live business data.

## Architecture contracts

Before adapting or recovering ARC, understand:

- [Configuration](contracts/configuration.md)
- [Secrets and credentials](contracts/secrets.md)
- [Ownership and source of truth](contracts/ownership.md)
- [Portability](contracts/portability.md)
- [Safe harbour](contracts/safe-harbour.md)
- [Integration classes](integrations/README.md)
- [Security and governance](contracts/governance.md)

## Lifecycle boundary

ARC 0.5 adds portable specialist-system integration contracts and a security/governance baseline on top of ARC 0.4's business-neutral modules, first-day Skills foundation and provider/runtime portability. Richer estate drift/health reporting and automated release-to-estate upgrade lifecycle remain owned by ARC.7.

## Public by design

ARC is open because the value is not hiding a folder structure. The value is understanding a business, implementing the architecture correctly, selecting/integrating the right tools, governing authority, and continuously improving the operating system.

Licensed under the [MIT License](LICENSE).

## Status

**ARC v0.5.0 — Integrations and Governance**

ARC now supports guided onboarding/adoption, safe-harbour recovery, optional business capability modules, a generic first-day Skills foundation, provider-neutral capable-agent routes, least-privilege runtime selection, specialist-system integration ownership and a portable security/governance baseline. The Level 3 ARC v1 programme continues with estate health/upgrades, independent clean-room proof and the final public reference monument.
