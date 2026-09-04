# ARC

**Reproduce a proven human + AI operating ecosystem on a blank environment.**

**Fast links:** [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Reconnections](RECONNECTIONS.md) · [Starter Skills](starter/skills/README.md) · [Root Contract](AGENTS.md) · [Proof](https://github.com/tbhrc/arc/issues/11) · [Issues](https://github.com/tbhrc/arc/issues)

## Primary objective

**ARC is the simplest reliable way to reproduce the current proven TBHRC ecosystem onto a blank environment for ourselves or another organisation/client, reconnect the required external owners, and prove the redeployed ecosystem works.**

ARC is a portable **architecture backup / deployment / recovery package**. It is not a second business operating system and it does not copy live business data.

```text
blank environment
→ deploy the required GitHub operating structure
→ install Skills + agent/routing contracts
→ establish the organisation North Star
→ establish durable Issue / Anti-Drift control
→ reconnect required external owners
→ run one real workflow
→ export non-secret architecture state
→ recover/reproduce the estate again
```

## What ARC reproduces

- repository roles/topology needed to operate;
- Skills-first operating method;
- machine-first routing and useful Fast Links;
- organisation-level North-Star mechanism;
- durable Issue / `Anti-Drift — Original Objective` pattern;
- provider/runtime guidance where needed;
- non-secret deployment configuration;
- external-system ownership/reconnection references;
- bootstrap, verification and recovery instructions.

## What ARC does not copy

- CRM / ATS / ERP / accounting / mailbox live records;
- private client/personnel files;
- secret values or credentials;
- machine-local runtime state unless explicitly required as a reference;
- derived memory contents.

Those remain with their real owners and are reconnected after deployment.

## Start with Atlas

Tell a capable agent:

```text
Use the Atlas skill in this repository.
Understand my business and current ARC state.
Start in plan mode.
Do not mutate anything until the target ownership map is explicit and apply authority is given.
```

Atlas is ARC's deployment/onboarding/lifecycle front door. The deployed estate's day-to-day machine router is separate and should route directly to its North Star, Skills, owners, workflow and Issues.

## Deploy

Prerequisites: Git, Python 3.10+, GitHub CLI (`gh`) and authority over the intended target.

```bash
git clone https://github.com/tbhrc/arc.git
cd arc

python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target

# Explicit mutation gates:
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply

python3 scripts/arc.py verify --config arc.json
```

Existing repositories are reused rather than overwritten. Credentials being available never imply apply authority.

Read [BOOTSTRAP.md](BOOTSTRAP.md) for the complete deployment path.

## Reconnect external owners

ARC keeps this deliberately simple. For each external system actually required by a workflow, record only the smallest useful non-secret handoff:

```text
System / provider
Live owner
Connection / identity reference
Required authority / scope
Verification
```

Add recovery/revocation ownership only when materially useful. See [RECONNECTIONS.md](RECONNECTIONS.md).

## Run one real workflow

A deployment is not accepted because folders exist. Prove:

```text
organisation North Star
→ request / Anti-Drift objective
→ Skill
→ current owner truth
→ authorised execution
→ real-state verification
→ durable evidence
```

## Safe harbour / recovery

Export the architecture map, not the private data:

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target

python3 scripts/arc.py restore-plan \
  --manifest arc-estate.json \
  --inspect-target
```

Only after the recovery plan is accepted:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

The estate manifest records topology, owner references and recovery boundaries. External systems restore their own live data through their own approved processes.

## Independent v1 proof

ARC v1 passed an independent non-TBHRC clean-room proof on **4 September 2026**.

The proof used a near-blank personal GitHub estate and demonstrated:

- target-specific North Star;
- machine-first routing;
- independent Skills owner;
- durable Issue / Anti-Drift workflow;
- successful external-system reconnection using the minimal Gmail handoff without copying mailbox content;
- one real source-backed research workflow from Issue → execution → verified durable artifact;
- non-secret estate snapshot;
- destructive recovery: the deployed `AGENTS.md` was deleted and reconstructed from durable ARC/estate sources.

Evidence: [ARC Core Proof #11](https://github.com/tbhrc/arc/issues/11).

The proof did **not** justify a new health subsystem, Gate-E schema, Fast-Links validator, policy engine or continuous deployment service.

## Architecture in one view

```text
ORGANISATION NORTH STAR
        ↓
HUMANS + AI AGENTS
        ↓
SKILLS FIRST
        ↓
CURRENT OWNER TRUTH
        ↓
LOWEST SUFFICIENT AUTHORISED EXECUTION
        ↓
VERIFY REAL STATE
        ↓
DURABLE EVIDENCE
```

GitHub is the durable operating desk, not the database for everything. Specialist systems remain authoritative for their live records. Trusted runtimes are exceptional, not the default path. Memory is derived context, not current canon.

## Core files

- [ATLAS.md](ATLAS.md) — deployment/onboarding front door
- [ARCHITECTURE.md](ARCHITECTURE.md) — system model and ownership boundaries
- [BOOTSTRAP.md](BOOTSTRAP.md) — blank-slate deployment and recovery path
- [VERIFY.md](VERIFY.md) — acceptance checks
- [RECONNECTIONS.md](RECONNECTIONS.md) — minimal external-system handoff
- [starter/skills/](starter/skills/) — first-day Skills foundation
- [profiles/generic-business/](profiles/generic-business/) — generic deployment profile
- [profiles/tbhrc-reference/](profiles/tbhrc-reference/) — reference wiring only, not copied live data

## KISSS rule

**The operating system must not become the work.**

When ARC scope grows, ask:

> Does this materially help blank-slate redeployment, reconnection, proof or recovery?

If not: **delete or defer**.

Licensed under the [MIT License](LICENSE).

## Status

**ARC v1.0.0 — blank-slate reproduction, real-workflow and recovery proof complete.**
