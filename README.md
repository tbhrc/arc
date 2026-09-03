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
                 +-----------------+-----------------+
                 |                                   |
                 v                                   v
        NORMAL AUTHORISED AGENT                RESEARCH ESCALATION
      GitHub · API · MCP · browser          recurring capability gap?
                 |                                   |
                 |                         symptom -> workflow
                 |                         -> capability -> platform
                 |                                   |
                 +-----------------+-----------------+
                                   |
                    can normal capability execute?
                         /                     \
                       YES                     NO
                        |                       |
                        v                       v
                 DIRECT EXECUTION          TRUSTED RUNTIME
                                           privileged bridge
                        \                       /
                         +----------+----------+
                                    |
                                    v
                              VERIFY REALITY
                                    |
                                    v
                          DURABLE OWNER TRUTH
                                    |
                    reusable learning or capability?
                         /                     \
                       YES                     NO
                        |                       |
                        v                       v
                  IMPROVE SKILL              FINISH
```

The architecture is intentionally modular. GitHub is the operating desk, not the database for everything. Skills own reusable method. Business/domain systems own their facts. Research finds better tools. Privileged runtimes exist only for capabilities that normal agents cannot safely reach. Memory supports context; it does not replace current canon.

## Start with Atlas

**Atlas is ARC's front door.**

If your AI environment supports repository Agent Skills, tell your agent:

```text
Use the Atlas skill in this repository. Onboard me to ARC for my business.
Start in plan mode. Do not mutate anything until the deployment plan is explicit.
```

On IDE surfaces that support GitHub prompt files, use:

```text
/atlas
```

Atlas will orient the agent, select the correct profile, identify what already exists, ask only for missing business-specific inputs, produce a deployment plan, and guide the bootstrap and verification sequence.

- Human front door: [ATLAS.md](ATLAS.md)
- Project Agent Skill: [.github/skills/atlas/SKILL.md](.github/skills/atlas/SKILL.md)
- Prompt-file entrypoint: [.github/prompts/atlas.prompt.md](.github/prompts/atlas.prompt.md)
- Learn the operating method: [GitHub Course](https://github.com/tbhrc/gh-course)

## Deploy ARC

Prerequisites: Git, Python 3.10+, GitHub CLI (`gh`), and permission to create or configure repositories in the target GitHub account or organisation.

```bash
git clone https://github.com/tbhrc/arc.git
cd arc
cp profiles/generic-business/arc.example.json arc.json

python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

`plan` and `doctor` are non-mutating. `bootstrap` is also non-mutating unless `--apply` is present. ARC never asks you to place secret values in its configuration file.

Read [BOOTSTRAP.md](BOOTSTRAP.md) before the first deployment.

## What ARC installs

The generic profile can create a small operating estate rather than one giant repository:

| Component | Default repository | Purpose |
|---|---|---|
| Reusable method | `skills` | Canonical Skills and agent HOW |
| Discovery | `research` | External research, technology/tool discovery and proving |
| Operations | `ops` | Business-wide operating architecture, decisions and cross-domain control |
| Trusted runtime | `ai-engine` | Optional privileged execution bridge for VPS/local/self-hosted capability gaps |
| Domain owners | configurable | Business units, products, services or workflows that own their facts |

ARC does **not** automatically configure production secrets, grant broad credentials, move client data, or connect third-party systems. Those are explicit deployment decisions documented in the contracts.

Every **newly created** repository is immediately seeded with:

- a role-aware `README.md`;
- a root `AGENTS.md`;
- a thin Atlas Agent Skill pointer;
- an `/atlas` prompt-file entrypoint for supported IDE surfaces.

Existing repositories are detected and reused **without overwrite**; Atlas then proposes how to integrate them safely.

## Why ARC exists

ARC grew out of a real operating migration. The [GitHub Course](https://github.com/tbhrc/gh-course) began as an attempt to learn GitHub properly. Each useful capability was immediately applied to real business operations. Issues became durable work objects. Pull Requests became controlled integration boundaries. Skills replaced scattered reusable SOP logic. Research became the discovery layer for missing capability. Self-hosted and VPS runtimes became bounded execution bridges rather than general control planes.

The system was not invented on a whiteboard. It was learned, tested, corrected and operated.

ARC packages the resulting architecture so another business does not need to repeat the entire discovery journey.

## What makes ARC different

### 1. Skills first
A capable agent should not need a giant hard-coded application for every workflow. Give the agent current truth, the right tools and a concise reusable Skill.

### 2. One owner for each kind of truth
Repository documentation, CRM state, accounting records, private files and research evidence are different classes of truth. ARC makes those boundaries explicit.

### 3. AI agents are operators, not ornaments
Agents get durable instructions, bounded tools, Issues to execute, verification expectations and clear authority limits.

### 4. Research is an operating reflex
Repeated friction can trigger problem-to-platform research before a team builds another custom workaround.

### 5. Privileged infrastructure is exceptional
Use normal APIs, MCP, connectors and GitHub capabilities first. Reach for trusted runners/VPS/local profiles only when a real runtime or privilege gap exists.

### 6. Deployment is not complete until verified
Green automation is not proof unless it tested the required outcome. ARC ships with an explicit verification contract.

## Repository map

```text
ARC
├── ATLAS.md                         human + agent front door
├── ARCHITECTURE.md                  system model and boundaries
├── MANIFEST.md                      deployable component inventory
├── BOOTSTRAP.md                     deployment path
├── VERIFY.md                        acceptance and health checks
├── profiles/                        deployment profiles
├── components/                      component-specific design guidance
├── contracts/                       ownership, config, secrets, portability
├── scripts/arc.py                   plan/bootstrap/verify CLI
└── .github/
    ├── skills/atlas/SKILL.md        Atlas project Agent Skill
    ├── prompts/atlas.prompt.md      /atlas-compatible prompt file
    └── workflows/validate-arc.yml   repository self-validation
```

## The two profiles

- [Generic Business](profiles/generic-business/README.md) — start here for a new business or client.
- [TBHRC Reference](profiles/tbhrc-reference/README.md) — shows how the architecture maps onto the live environment that produced ARC. It is reference wiring, not copied live business data.

## Architecture contracts

Before adapting ARC, understand these four contracts:

- [Configuration](contracts/configuration.md)
- [Secrets and credentials](contracts/secrets.md)
- [Ownership and source of truth](contracts/ownership.md)
- [Portability](contracts/portability.md)

## Public by design

ARC is open because the value is not in hiding a folder structure. The value is in understanding a business, implementing the architecture correctly, selecting and integrating the right tools, governing authority, and continuously improving the operating system.

Licensed under the [MIT License](LICENSE).

## Status

**ARC v0.1.0 — Public Foundation**

The repository is usable today for a guided GitHub-first deployment. More provider adapters, portable Skill distributions and end-to-end deployment benchmarks will be added through normal Issues and Pull Requests rather than hidden setup knowledge.
