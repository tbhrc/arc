# Atlas — ARC Front Door

Atlas is the onboarding, adoption, audit and recovery front door for ARC.

Use Atlas when a founder, operator or capable AI agent needs to **understand a target environment and reproduce the ARC operating model there without first learning the entire repository**.

**Fast links:** [README](README.md) · [Architecture](ARCHITECTURE.md) · [Ecosystem Evidence](ECOSYSTEM-EVIDENCE.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Reconnections](RECONNECTIONS.md) · [Agent Contract](AGENTS.md) · [ARC Issues](https://github.com/tbhrc/arc/issues)

---

## What Atlas is trying to achieve

ARC's Primary Objective is:

> **Reproduce the proven human + AI operating ecosystem on a blank environment for ourselves or another organisation/client, reconnect the required external owners, prove the redeployed ecosystem works, and preserve enough non-secret architecture state to reproduce it again.**

Atlas exists to make the first part of that journey understandable and safe.

It should help a user move from:

```text
I have a business / new environment / existing estate
```

into:

```text
I know what ARC should create,
what should stay where it already is,
what must be connected,
what authority is already present,
and what real workflow will prove the deployment.
```

Atlas is **not** the deployed estate's permanent day-to-day router. After deployment, normal work starts at root `AGENTS.md` as the Repository Router, then follows only the relevant Fast Link to the smallest Skill/owner needed.

---

## What ecosystem Atlas is reproducing

Atlas should understand that ARC is reproducing this operating model:

```text
organisation North Star
→ humans + AI agents
→ GitHub durable operating desk
→ Skills-first reusable HOW
→ current owner truth
→ lowest-sufficient authorised execution
→ real-state verification
→ durable evidence
→ reusable learning
```

With separate owners for:

```text
private files
specialist systems
credentials
trusted runtime state
memory
```

The measured TBHRC/iMPLEMENTAi reference estate reached 29 repositories, 57 canonical Skills and seven named AI execution lanes during the first 7.57-day GitHub operating-era snapshot. Those are **reference-evidence figures**, not requirements for a target deployment. See [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md).

---

## Say this to your agent

```text
Use the Atlas skill in this repository.
Understand my business and current environment.
Identify where my organisation should own its North Star.
Work out which existing systems and repositories should be kept rather than replaced.
Ask only for facts or authority you cannot resolve.
If my current instruction already authorises ordinary bounded mutation, execute it without asking me again.
Stop only when a real destructive, root/credential, private-data, spend, legal/compliance, production-destructive or material external/client-commitment boundary is crossed.
Tell me what first real workflow will prove the deployment.
```

On supported IDE prompt-file surfaces:

```text
/atlas
```

The editable Skill canon is:

```text
.github/skills/atlas/SKILL.md
```

---

## Atlas modes

Atlas can route the user's intent into these practical modes:

| Mode | Purpose |
|---|---|
| `onboard` | Create the first valid ARC profile for a new estate. |
| `adopt` | Bring an existing organisation into ARC without unnecessary replacement. |
| `audit` | Inspect architecture, owners, routes and gaps without mutation. |
| `health` | Assess current ARC state using present verification/owner truth; no special health subsystem is required. |
| `upgrade` | Plan movement toward a newer ARC release through ordinary migration reasoning and verification. |
| `recover` | Export/inspect a non-secret estate map, plan recovery and perform bounded reconstruction. |
| `next` | Return the single smallest safe next action from durable state. |

Detailed mode behaviour lives in `.github/skills/atlas/references/modes.md`.

---

## The first questions Atlas must answer

Atlas needs enough information to resolve:

1. **North Star** — where will the organisation own its canonical mission/vision/directives?
2. **Purpose** — what business/environment is ARC supporting?
3. **GitHub home** — which account/organisation owns durable work?
4. **Domains** — which business areas/products/services require their own truth owners?
5. **Existing estate** — what repositories, processes and systems already exist?
6. **Skills** — where will reusable HOW live?
7. **Private files** — where must confidential evidence remain?
8. **Specialist systems** — what owns CRM, finance, HR, ATS, service delivery or other structured live state?
9. **Execution** — can normal connected tools perform the required work, or is trusted runtime actually needed?
10. **Authority** — what does the current instruction already authorise, and is any real risk boundary crossed?
11. **Proof workflow** — what real work will demonstrate that the deployed estate actually operates?

If the user already supplied an answer or a connected owner proves it, do not ask again.

---

## New organisation / blank environment

A normal new deployment can start with:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

These are non-mutating inspection tools. They are useful for clarity, not mandatory human approval ceremonies.

For capable agents with the required facts already available, non-interactive onboarding may be used where supported rather than forcing a questionnaire.

Minimum useful inputs are usually:

```text
organisation/business name
North Star owner/location if already known
GitHub organisation/login
visibility defaults
first domains
private-file owner
known specialist systems
```

Everything else should be derived or postponed until needed.

---

## Existing organisation / adoption path

Do **not** rebuild working systems merely to make them resemble an ARC example.

Inventory:

```text
North Star owner
GitHub repositories
Skills / SOP / knowledge owners
existing automations
CRM / ERP / ATS / accounting
private file stores
agent providers / connected tools
trusted runtime if any
identity/credential boundaries
```

Classify relevant existing owners:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

For configured repositories, surface:

```text
REUSE
CREATE
```

where observable before apply.

The default is **reuse/integrate**, not replacement.

---

## Atlas deployment view

Before making changes, understand enough of the target to avoid accidental replacement or scope drift. A compact deployment view may contain:

```text
Target
Purpose
North Star owner/location
Atlas mode
Core repositories
Domain owners
Existing owners: KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE
Configured repositories: REUSE / CREATE where observable
Skills strategy
Repository Router / first-hop operational front door
Useful Fast Links
Durable Issue / Anti-Drift strategy
Private-file owner
Specialist-system owners
Research owner/path
Agent/provider strategy
Normal execution capabilities
Trusted-runtime need, if genuine
Credential/manual input names and purposes only — never values
Bootstrap/recovery route
Verification plan
First real workflow to prove
```

Clearly distinguish required core, optional components, existing owners to keep/integrate and future improvements. Do not build future improvements before the core deployment needs them.

If the current instruction already authorises ordinary bounded mutation, continue directly after resolving the necessary facts. Do not manufacture a second review/approval round-trip.

---

## North Star and Anti-Drift

Keep these separate:

```text
North Star = organisation-level mission / vision / directives
Anti-Drift — Original Objective = original requested outcome of one durable work item
```

ARC reproduces the North-Star **ownership mechanism**, not TBHRC's editable wording.

For substantive durable work use:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

The implementation route may evolve. The original objective must not silently change.

---

## Authority rule — no ceremonial second approval

ARC separates **authority** from **mutation mode**.

```text
current instruction authorises ordinary bounded work
→ select the required mutating command deliberately (`--apply` where applicable)
→ execute
→ verify
```

`--apply` means the tool is intentionally entering mutation mode. It does **not** mean the agent must return to the human for another approval when the current instruction already grants authority.

Stop for fresh authority only when the next step crosses a real boundary such as destructive overwrite/delete/force/recovery, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

Credentials or connected capabilities alone still do not create authority.

`bootstrap` and `restore` remain non-mutating without `--apply`; destructive recovery remains separately gated because its risk is materially different from ordinary bounded creation.

---

## Apply route

When ordinary bounded mutation is already authorised by the current instruction:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

Do not ask for another confirmation merely because these commands mutate state.

Existing repositories should be reused rather than overwritten.

After bootstrap:

1. establish the target North Star route;
2. establish the Skills owner;
3. establish root `AGENTS.md` as the Repository Router / first-hop front door;
4. establish durable Issue/Anti-Drift control;
5. reconnect only the external systems required for actual work;
6. run one real workflow;
7. verify real state;
8. capture durable evidence.

---

## External-system reconnection

Keep it minimal.

For each system genuinely required by the proof workflow, record:

```text
System / provider
Live owner
Connection / identity reference
Required authority / scope
Verification
```

Do not copy private/live records into ARC.

See [RECONNECTIONS.md](RECONNECTIONS.md).

---

## Real-work proof

A successful deployment is not:

```text
repositories created
folders exist
README looks correct
```

It is:

```text
organisation North Star
→ request / Anti-Drift objective
→ Skill
→ owner truth
→ authorised execution
→ real-state verification
→ durable evidence
```

Choose a proof workflow that is real but proportionate.

ARC v1 itself passed this model in an independent non-TBHRC clean-room test. See [Core Proof #11](https://github.com/tbhrc/arc/issues/11).

---

## Safe-harbour export

After the estate is working, preserve the non-secret architecture map:

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The manifest may record:

- ARC version/schema;
- topology;
- repository roles;
- external owner names/references;
- non-secret observations useful for recovery.

It must not contain:

- private files;
- CRM/ATS/ERP/accounting records;
- credential values;
- machine-local runtime state;
- memory contents.

---

## Recovery

Plan without mutation:

```bash
python3 scripts/arc.py restore-plan \
  --manifest arc-estate.json \
  --inspect-target
```

Recovery may overwrite/reconstruct missing operating surfaces and is a genuine destructive-risk boundary. After that boundary is explicitly authorised:

```bash
python3 scripts/arc.py restore \
  --manifest arc-estate.json \
  --apply
```

Then reconnect external owners through their own approved identity/backup processes and rerun verification.

ARC v1 destructive proof deliberately removed a deployed `AGENTS.md` and successfully reconstructed it from durable ARC/estate sources.

---

## Health and upgrade honesty

ARC v1 intentionally avoids speculative lifecycle machinery.

- **health** = use current `VERIFY.md`, CLI checks and owner-state inspection;
- **upgrade** = compare release/contracts, make the smallest justified migration and verify it;
- **recover** = use export → restore-plan → bounded restore + external-owner reconnection.

Do not invent a dedicated health/upgrade service unless real deployment evidence proves the simpler methods insufficient.

---

## KISSS rule

> **The operating system must not become the work.**

Atlas should always ask:

> What is the smallest deployment path that gets this organisation to a verified working estate?

Do not add:

- validators;
- policy engines;
- daemons;
- services;
- schemas;
- mandatory repositories;
- integrations;
- agent routes;
- precautionary approval loops;

unless the target actually needs them.

The measured TBHRC/iMPLEMENTAi ecosystem is a **reference implementation and proof source**, not a requirement to clone all 29 repositories or all historical infrastructure into every deployment.

---

## Default deployment route

```text
read ARC README
→ Atlas selects mode
→ identify organisation North Star owner
→ inspect current target only as much as needed
→ reconcile existing owners
→ generate/reconcile arc.json
→ doctor / plan when useful for validation
→ current instruction already authorises ordinary bounded mutation? execute directly
→ bootstrap --apply
→ seed foundation --apply
→ verify base estate
→ establish root AGENTS.md Repository Router and progressive Fast Links
→ establish Skills owner
→ reconnect required external systems
→ run one real workflow with Anti-Drift
→ verify real outcome
→ export safe-harbour manifest
→ capture reusable learning
```

If a real risk boundary is crossed, stop at that boundary only. Do not turn ordinary mutation into a security ritual.

---

## Durable continuity

For material ARC programme/change work, the controlling GitHub Issue—not the current chat—must preserve:

- North Star;
- Anti-Drift objective;
- active branch/PR;
- implementation state;
- evidence;
- material failures/abandoned paths;
- exact next action.

A cold capable agent should be able to continue from GitHub alone.

---

## Learning path

If the user wants to understand how this architecture emerged rather than only deploy it:

- read [README.md](README.md) for the public story;
- read [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md) for measured provenance;
- read the [Founder Story / Mission / Vision](https://github.com/tbhrc/skills/tree/main/founder-story-mission-vision) for founder direction;
- use the [GitHub Course](https://github.com/tbhrc/gh-course) for the operating method and learning journey.

**Course = learn the method. ARC = reproduce the operating architecture.**
