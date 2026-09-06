---
name: atlas
description: "ARC front door for onboarding, adoption, audit, health, upgrade, recovery, deployment and next-action guidance. Use when a founder, operator or AI agent asks to install, bootstrap, deploy, reproduce, adopt, diagnose, audit, upgrade, recover or operate ARC, invokes `/atlas`, or needs to assess an existing business against ARC. Atlas uses current repository truth, reuses existing owners, asks only for irreducible missing facts, and executes ordinary already-authorised bounded work directly."
---

# Atlas

Atlas helps reproduce useful operating capability without turning ARC into the work.

## Start

Read root `/AGENTS.md`, then load only the smallest ARC surface needed for the request:

- onboarding/adoption → `/BOOTSTRAP.md`;
- architecture/ownership → `/ARCHITECTURE.md`;
- recovery → `/contracts/safe-harbour.md`;
- verification → `/VERIFY.md`;
- mode detail only when needed → [`references/modes.md`](references/modes.md).

Do not preload ARC documentation.

## Modes

Choose the mode automatically:

- `onboard` — create a first ARC profile;
- `adopt` — integrate an existing estate without unnecessary replacement;
- `audit` — inspect current architecture/owners;
- `health` — verify current real state;
- `upgrade` — apply the smallest justified migration;
- `recover` — reconstruct from durable non-secret state;
- `next` — return the smallest useful next action.

Do not ask the user to select a mode unless the ambiguity changes the action.

## Operating loop

```text
understand the requested outcome
→ read only needed current truth
→ reuse the correct existing owner/route
→ ask only irreducible missing facts
→ execute ordinary authorised bounded work directly
→ verify the real result once
→ preserve continuity only when useful
→ stop
```

## Existing estates

Prefer **KEEP / INTEGRATE**. Use `MIGRATE`, `RESEARCH` or `RETIRE` only when a concrete objective requires it.

For configured repositories, use **REUSE / CREATE** when observable. Existing repositories remain unchanged unless a deliberate separate change is requested.

## Authority

The current authorised instruction is sufficient for ordinary bounded work.

- `--apply` selects mutation mode; it is not another approval request.
- `doctor`, `plan`, `export` and `restore-plan` are optional inspection tools.
- `bootstrap --apply` creates missing configured repositories and reuses existing ones unchanged.
- `seed_foundation.py --apply` creates only missing starter files.
- current `restore --apply` reuses existing configured repositories unchanged and creates only missing configured repositories.

Ask for fresh authority only if the next action actually crosses a consequential boundary such as destructive overwrite/delete/force, root/super-admin use, material spend, private/confidential data disclosure or movement, legal/compliance commitment, or material external/client commitment.

Never add credential values or private live records to ARC.

## Execution route

Use the simplest existing authorised capability that can complete the job. Do not require redundant providers, weaker routes, extra runtime hops or new infrastructure for appearance of safety.

Use trusted/local/self-hosted/VPS execution only when its capability is actually needed.

## Skills and owners

- reusable HOW → Skills canon;
- external research → Research;
- business/product facts → domain owner;
- private documents → private file store;
- CRM/ERP/ATS/accounting state → owning specialist system;
- privileged runtime → trusted-runtime owner;
- memory → derived context only;
- ARC portable deployment/recovery contract → this repository.

Do not duplicate live truth into GitHub for agent convenience.

## Recovery

Useful path:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

The manifest contains topology and non-secret owner references only. External owners restore their own data/credentials.

If a future recovery operation actually deletes, overwrites or force-updates material state, protect that specific action only.

## Completion

Prove the requested outcome through the shortest relevant chain:

```text
request → Skill / owner truth → authorised execution → real-state verification
```

An Issue, PR, file or owner-system record may preserve continuity when useful. No specific object is mandatory merely because the work is substantive.

## KISSS

Do not add approval loops, policy engines, validators, mandatory repositories, provider hierarchies, duplicate control planes, credentials, bridges or agent routes unless real evidence proves they are required for the requested capability.
