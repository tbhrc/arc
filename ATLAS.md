# Atlas — ARC Front Door

Atlas is the onboarding, adoption, audit and recovery front door for ARC.

Use Atlas to understand a target environment and reproduce a useful human + AI operating model **without turning the operating system into the work**.

**Fast links:** [README](README.md) · [Architecture](ARCHITECTURE.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Agent Contract](AGENTS.md)

## Primary objective

> Reproduce a working human + AI operating ecosystem on a blank or existing environment, reconnect the required external owners, prove one real workflow works, and preserve enough non-secret architecture state to reproduce it again.

## Default route

```text
understand the target
→ keep/reuse working owners and systems
→ identify North Star + Skills owner
→ choose the simplest existing authorised execution route
→ bootstrap ordinary authorised changes directly
→ reconnect only systems required for real work
→ run one real workflow
→ verify once
→ preserve useful non-secret continuity
→ stop
```

## Operating principles

- Root `AGENTS.md` is the deployed estate's first-hop Router.
- Skills own reusable HOW.
- Existing CRM/ERP/ATS/file stores remain owner truth where appropriate.
- **Issues are optional continuity/evidence records, never runtime permission.**
- Do not require an Issue, branch, PR, approval label, proof workflow or plan merely to perform already-authorised bounded work.
- Use **purpose-fit authority sufficient for the intended function**. Organisation-wide capability may legitimately require organisation-wide access.
- Do not narrow access merely because “least privilege”, isolation or hardening sounds safer.
- Reuse an existing authorised connection/credential/runtime before creating another one.
- If one provider/route is unavailable, use another already-authorised route before building infrastructure.
- Human approval is reserved for genuine consequential boundaries: root/super-admin changes, destructive/irreversible mutation, material spend, private-data disclosure, legal/compliance commitment or material external/client commitment.

## Modes

| Mode | Purpose |
|---|---|
| `onboard` | Create the first valid ARC profile for a new estate. |
| `adopt` | Integrate an existing organisation without unnecessary replacement. |
| `audit` | Inspect owners/routes/gaps without mutation. |
| `health` | Check current real state. |
| `upgrade` | Apply the smallest justified migration and verify it. |
| `recover` | Reconstruct from durable non-secret state when actually needed. |
| `next` | Return the smallest useful next action. |

## What Atlas must resolve

Only resolve facts needed for the requested outcome:

1. organisation/business purpose and North Star owner;
2. GitHub owner/home;
3. current repositories/domain owners;
4. Skills owner;
5. private-file and specialist-system owners;
6. available authorised execution routes;
7. any **real** consequential boundary crossed by the requested action;
8. one real workflow that will prove usefulness.

If the user or authoritative system already supplied a fact, do not ask again.

## Existing estate

Default to **KEEP / INTEGRATE**, not replacement.

Use `MIGRATE`, `RESEARCH` or `RETIRE` only when the current objective provides a concrete reason.

Do not rebuild working systems merely to resemble an ARC example.

## Mutation and `--apply`

`--apply` selects mutating mode. It is not a second human approval ritual.

When the current instruction already authorises ordinary bounded mutation:

```text
select mutating mode
→ execute
→ verify
```

Ask for fresh authority only when the next action crosses a genuine protected boundary.

Inspection commands such as `doctor` or `plan --inspect-target` are optional aids. Do not force them before every authorised mutation.

## Bootstrap

Typical authorised path:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

After bootstrap:

1. establish the North Star owner;
2. establish the Skills owner;
3. establish root `AGENTS.md` as the Router;
4. reconnect only external systems needed for actual work;
5. run one real workflow;
6. verify the real result;
7. record continuity only if it materially helps future recovery/coordination.

Do **not** establish mandatory Issue/Anti-Drift machinery as a prerequisite for execution.

## External reconnection

For each system genuinely needed by the real workflow, record only what helps operation:

```text
system/provider
live owner
connection/identity reference
purpose-fit authority needed
verification
```

Never copy secret values or private live records into ARC.

## Real-work proof

A deployment is useful when real work succeeds:

```text
request
→ Skill / owner truth
→ authorised execution
→ real-state verification
```

A proof Issue or elaborate acceptance programme is not required when one decisive real workflow already proves the capability.

## Recovery

Current ARC recovery is bounded reconstruction: existing repositories are reused unchanged and missing configured repositories may be created when `--apply` selects mutation.

Use restore planning only when useful. If a future recovery operation actually deletes, overwrites, force-updates or crosses another genuine consequential boundary, protect that specific action only.

## KISSS test

Before adding anything, ask:

> What material failure does this prevent, and can the estate still do the authorised job without extra friction?

Do not add validators, policy engines, services, schemas, mandatory repositories, approval loops, isolation, credentials, bridges or agent routes unless real deployment evidence shows they are needed.

## Continuity

When durable continuity is useful, preserve enough to resume:

- objective;
- current state;
- evidence;
- exact next action.

That continuity may live in an Issue, PR, repository file or appropriate owner record. **No specific object is mandatory merely because the work is substantive.**

## Learning

- [README](README.md) — public ARC story
- [Architecture](ARCHITECTURE.md) — ownership model
- [GitHub Course](https://github.com/tbhrc/gh-course) — learn the operating method

**Course = learn the method. ARC = reproduce useful capability. KISSS = keep it working.**