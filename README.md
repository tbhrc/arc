# ARC

**An open, Skills-first operating architecture for businesses where humans and AI agents work from the same durable map.**

ARC is not an AI chatbot, an automation bundle, or another project-management framework. It is a reproducible operating architecture for combining **GitHub, reusable Skills, AI agents, research, trusted runtimes, private files, specialist systems and durable verification** without turning any one tool into the whole business.

> Build once. Make the operating logic explicit. Give every capable agent the same map. Improve the system through evidence.

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

Atlas supports seven intents without restarting onboarding:

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
# Review ownership, REUSE/CREATE and integrations before authorising apply.
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

`onboard`, `doctor` and `plan` are non-mutating. `bootstrap` is also non-mutating unless `--apply` is present. A credential being available is never treated as apply authority.

ARC rejects common secret-like configuration fields. Secret values belong in the correct external secret store, never `arc.json`.

Read [BOOTSTRAP.md](BOOTSTRAP.md) before the first deployment.

## What ARC installs

The generic profile describes a small operating estate rather than one giant repository:

| Component | Default repository | Purpose |
|---|---|---|
| Reusable method | `skills` | Canonical Skills and agent HOW |
| Discovery | `research` | External research, technology/tool discovery and proving |
| Operations | `ops` | Business-wide architecture, decisions and cross-domain control |
| Trusted runtime | `ai-engine` | Optional privileged execution bridge for genuine runtime gaps |
| Domain owners | configurable | Business units, products, services or workflows owning their facts |

ARC does **not** automatically configure production secrets, grant broad credentials, move client data, or connect third-party systems. Those are explicit deployment decisions documented in the contracts.

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
8. **Deployment is incomplete until verified.** Green automation matters only when it proves the required outcome.
9. **Chat is temporary context.** Material programme/Stage state belongs in GitHub Issues so a cold agent can continue without hidden conversation history.

## Repository map

```text
ARC
├── ATLAS.md                         human + agent front door
├── ARCHITECTURE.md                  system model and boundaries
├── MANIFEST.md                      deployable component inventory
├── BOOTSTRAP.md                     deployment path
├── VERIFY.md                        acceptance and health checks
├── profiles/                        deployment profiles
├── components/                      component-specific guidance
├── contracts/                       ownership, config, secrets, portability
├── scripts/arc.py                   onboard/plan/bootstrap/verify CLI
├── scripts/package_atlas.py         portable Atlas packager
└── .github/
    ├── skills/atlas/
    │   ├── SKILL.md                 Atlas canonical Agent Skill
    │   ├── agents/openai.yaml       ChatGPT metadata
    │   └── references/modes.md      Atlas mode contract
    ├── prompts/atlas.prompt.md      /atlas-compatible prompt file
    └── workflows/validate-arc.yml   repository self-validation
```

## Profiles

- [Generic Business](profiles/generic-business/README.md) — start here for a new business/client; normally generate `arc.json` through Atlas/onboard rather than editing the example manually.
- [TBHRC Reference](profiles/tbhrc-reference/README.md) — shows how ARC maps onto the live environment that produced it. It is reference wiring, not copied live business data.

## Architecture contracts

Before adapting ARC, understand:

- [Configuration](contracts/configuration.md)
- [Secrets and credentials](contracts/secrets.md)
- [Ownership and source of truth](contracts/ownership.md)
- [Portability](contracts/portability.md)

## Lifecycle boundary

ARC 0.2 provides the universal Atlas front door and current verification routes. Atlas does not invent capabilities that are still under development:

- richer safe-harbour export/restore/redeploy is owned by ARC.4;
- richer estate health and upgrade lifecycle is owned by ARC.7.

Until those stages are implemented and verified, Atlas uses the current release/contracts and produces an honest plan rather than claiming unsupported automation.

## Public by design

ARC is open because the value is not hiding a folder structure. The value is understanding a business, implementing the architecture correctly, selecting/integrating the right tools, governing authority, and continuously improving the operating system.

Licensed under the [MIT License](LICENSE).

## Status

**ARC v0.2.0 — Atlas Universal Front Door**

ARC is usable for guided GitHub-first onboarding, adoption, planning, bootstrap and verification. The Level 3 ARC v1 programme tracks release/recovery, modules/provider portability, integrations/security, health/upgrades, independent clean-room proof and the final public reference monument through linked GitHub Stage Issues.
