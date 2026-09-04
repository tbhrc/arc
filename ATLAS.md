# Atlas — ARC Front Door

Atlas is the single onboarding, adoption and lifecycle entrypoint for ARC.

**Fast links:** [Architecture](ARCHITECTURE.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Starter Skills](starter/skills/README.md) · [Root Contract](AGENTS.md) · [ARC Issues](https://github.com/tbhrc/arc/issues)

It exists so a founder, operator or AI agent does not need to understand the whole repository before beginning, and so ARC operation does not depend on one person's memory or a hidden chat transcript.

Atlas is **not** the deployed estate's day-to-day machine router. Atlas owns ARC onboarding/adoption/audit/health/upgrade/recovery. A deployed estate should expose its own compact operational machine-first route to the organisation North Star, Skills, workflow, owner/system map and Issues.

## Say this to your agent

```text
Use the Atlas skill in this repository.
Understand my business and current ARC state.
Identify my organisation's canonical North Star location.
Choose the correct Atlas mode.
Start in plan mode and tell me what you can infer from the current environment.
Ask only for information you genuinely cannot resolve.
Do not mutate anything until the plan and target ownership map are explicit and apply authority is given.
```

On supported IDE prompt-file surfaces, invoke:

```text
/atlas
```

## Seven Atlas modes

Atlas chooses the mode from the user's intent and current state:

| Mode | Purpose |
|---|---|
| `onboard` | Create a valid first ARC profile for a new estate. |
| `adopt` | Bring an existing business into ARC without forced replacement. |
| `audit` | Inspect architecture, owners and gaps without mutation. |
| `health` | Diagnose current verified ARC state using capabilities that exist now. |
| `upgrade` | Plan movement toward a newer formal ARC release/contract. |
| `recover` | Export a safe-harbour manifest, plan recovery and perform bounded repository reconstruction. |
| `next` | Return the single smallest safe next action from current durable state. |

The detailed mode contract lives in `.github/skills/atlas/references/modes.md`.

## What Atlas should establish

Atlas needs enough information to answer:

1. **North Star** — where does the target organisation own its canonical mission, vision and/or directives?
2. **Purpose** — what business/environment is ARC supporting?
3. **GitHub home** — user account or organisation and repository visibility defaults.
4. **Domains** — what business units, products or workflows need their own truth owners?
5. **Existing estate** — which repositories, processes and systems already exist and should be kept or integrated?
6. **Private files** — where confidential documents should live.
7. **Specialist systems** — which systems own CRM, finance, HR, ATS, service delivery or other structured state?
8. **Execution** — can normal APIs/connectors/tools perform the work, or is a trusted runtime genuinely required?
9. **Authority** — what may be inspected, planned and applied?

If the user already supplied an answer or a connected owner proves it, do not ask again.

ARC reproduces the **North-Star mechanism**, not TBHRC's editable mission wording. A generic deployment must point to the target organisation's own canonical direction.

## New-business first run

A normal new deployment should not require hand-editing JSON:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

For capable agents with the required facts already available, `onboard --non-interactive` can generate the same validated profile without a questionnaire.

`onboard`, `doctor` and `plan` do not mutate the target.

## Existing-business path

Do **not** force replacement.

Inventory:

```text
organisation North Star owner
existing GitHub repositories
existing SOP / knowledge owners
existing automations
existing CRM / ERP / ATS / accounting
private file stores
agent providers / tools
credentials and identity boundaries
```

Classify each relevant owner:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

For repositories already declared in `arc.json`, use `plan --inspect-target` to surface **REUSE / CREATE** before apply where GitHub CLI access is available.

## Atlas output before mutation

Return a compact deployment/operation plan containing:

```text
Target
Organisation North Star owner/location
Purpose
Atlas mode
Core repositories
Domain repositories / owners
Existing owners: KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE
Configured repositories: REUSE / CREATE where observable
Truth-owner map
Skills strategy
Operational machine-router/front-door strategy
Fast Links strategy for important active front doors
Durable Issue / Anti-Drift strategy
Research strategy
Agent entrypoints
Private-file owner
Specialist-system owners
Runtime requirement
Credential/manual-input list (names/purpose only, never values)
Bootstrap / recovery command
Verification plan
First real workflow to prove when deploying
```

The plan should distinguish:

- **required core**;
- **optional component**;
- **existing owner to keep/integrate**;
- **future improvement**.

## North Star and Anti-Drift

Keep these concepts separate:

```text
North Star = organisation-level mission / vision / directives
Anti-Drift — Original Objective = the original requested outcome of one durable work item
```

Issues should normally point to the canonical North Star rather than duplicate editable mission text.

For substantive durable GitHub work, use the canonical structure:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

The route may change during implementation. The Anti-Drift destination must not silently change.

## Authority gate

```text
understand / inspect
-> plan
-> explicit apply authority
-> bounded mutation
-> verify
```

Credentials being available never imply apply authority. `bootstrap` and `restore` remain non-mutating unless `--apply` is supplied.

## Safe-harbour recovery

ARC can preserve the **architecture needed to rebuild an estate** without copying the estate's private/live data.

After the estate is healthy, export a non-secret manifest:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

The estate manifest records ARC version/schema, target topology, repository roles, declared external owners and optional repository observations. It does not contain private files, specialist-system records, database contents, credential values, trusted-runtime machine state or memory contents.

Plan recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Only after the repository reconstruction plan is accepted:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

That apply step is deliberately limited to conservative GitHub repository reconstruction. Restore/reconnect external owners through their own approved backup/identity processes, then run the complete ARC verification contract.

Read [contracts/safe-harbour.md](contracts/safe-harbour.md) before treating the manifest as a disaster-recovery artifact.

## Current lifecycle honesty

Atlas routes to what the current ARC release can actually prove:

- **health** uses current `VERIFY.md`, CLI checks and observable owner state; richer drift/health reporting belongs to ARC.7;
- **upgrade** identifies the formal ARC release + manifest schema and produces a migration plan; automated release-to-estate upgrade belongs to ARC.7;
- **recover** uses the implemented safe-harbour export → restore-plan → bounded restore path plus the external-owner backup boundaries.

Atlas must identify a missing capability or its owning Stage rather than pretend it already exists.

## Portable Atlas Skill

The editable Atlas canon is `.github/skills/atlas/`.

```bash
python3 scripts/package_atlas.py
```

This packages that same directory as `dist/skill.zip`. There is no second editable portable copy. ARC-generated repositories receive a thin pointer to the current upstream Atlas canon.

## Default deployment route

```text
read ARC
-> Atlas selects mode
-> identify organisation North Star owner
-> inspect current target
-> generate/reconcile arc.json
-> doctor
-> plan --inspect-target
-> operator reviews plan
-> explicit apply authority
-> bootstrap --apply
-> verify
-> establish machine-first operational routing + Fast Links
-> seed/onboard Skills and agents
-> connect specialist systems deliberately
-> run one real business workflow with Anti-Drift
-> export safe-harbour manifest
-> capture reusable learning
```

## Minimum information path

For a brand-new GitHub organisation, Atlas can start with:

```text
business name
North Star owner/location if already known
GitHub organisation/login
private vs public default
first business domains
private-file store
known specialist systems
```

Everything else should be derived or postponed until needed.

## Durable continuity

For material ARC programme/Stage work, the controlling GitHub Issue—not the current chat—must contain the Anti-Drift objective, branch, evidence, blockers and exact next action. A fresh agent should be able to continue from GitHub alone.

## Learning path

If the user wants to understand why ARC is designed this way rather than only operate or deploy it, route them to the [GitHub Course](https://github.com/tbhrc/gh-course).

The Course teaches the journey. ARC packages the deployable architecture.
