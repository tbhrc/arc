# ARC — Reproduce a Proven Human + AI Operating Ecosystem

ARC is the public, non-secret architecture package for reproducing a working human + AI operating ecosystem without copying private business state or turning governance into the work.

ARC is the **reproducible DNA of the organisation**: routing, ownership, execution, verification, deployment and recovery patterns that can be recreated while live business truth stays with its real owners.

**Fast links:** [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Router](AGENTS.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Manifest](MANIFEST.md) · [Evidence](ECOSYSTEM-EVIDENCE.md) · [Releases](RELEASES.md)

## Core route

```text
request
→ root AGENTS.md Repository Router
→ smallest relevant Skill / owner
→ simplest authorised execution route
→ verify real state once
→ preserve material durable context when needed
→ stop
```

Conditional only when genuinely needed:

- owner/source unclear → owner lookup;
- execution method genuinely needs escalation → Workflow;
- specialist delegation or genuine parallelism → Multi-Agent Orchestrator;
- consequential boundary → smallest proven control protecting that boundary.

## What ARC reproduces

- organisation direction ownership mechanism;
- repository/domain ownership topology;
- root `AGENTS.md` Repository Router and progressive Fast Links;
- one canonical Skills home for reusable HOW;
- source-of-truth boundaries;
- provider/runtime-neutral execution;
- private-file and specialist-system owner references;
- inspectable bootstrap and bounded recovery;
- real-state verification;
- non-secret estate manifest/reconnection model.

ARC does **not** copy the target organisation's editable live truth, private files, specialist-system records, credentials, runtime machine state or memory contents.

## Skills-first, without duplicate canon

ARC seeds only the minimum starter surface needed to make a blank estate usable.

Starter `owner-router` and `github-workflow` assets are thin bootstrap pointers. They must not become competing copies of the organisation's live operating doctrine.

For the TBHRC reference implementation, current reusable operating rules live in [`tbhrc/skills`](https://github.com/tbhrc/skills). Other organisations should establish the equivalent current canon in their own Skills repository.

## Authority without friction

Ordinary authorised bounded work executes directly.

`--apply` selects mutating mode. It does not create a second approval requirement.

Additional human authority is reserved for genuine consequential boundaries such as root/super-admin changes, destructive or irreversible mutation, material spend, legal/compliance commitment, private-data disclosure or material external/client commitment.

Security, governance and continuity mechanisms must protect a concrete current boundary and earn their friction.

## Durable context without Issue ceremony

Issues, PRs, plans and durable evidence are not runtime permission for ordinary authorised work, and ARC does not require a named Anti-Drift field, controlling Issue, checklist or evidence object merely to execute.

When substantive work changes a material objective, scope, acceptance condition, architecture/decision, blocker or continuation state, preserve that change once in the appropriate durable owner record before handoff, closure or the end of the meaningful work unit. Do not interrupt authorised execution for pre-mutation documentation ceremony.

## Deploy

Inspect when useful:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Execute ordinary authorised deployment directly:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

Bootstrap reuses existing configured repositories unchanged and creates only missing configured repositories.

## Safe Harbour

Export a non-secret architecture map:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

Inspect recovery when useful:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Reconstruct missing configured repositories:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current restore reuses existing configured repositories unchanged and creates only missing configured repositories. External owners recover their own data and credentials through their own systems.

## Acceptance

ARC is healthy when a fresh capable human or agent can:

1. enter through root `AGENTS.md`;
2. reach the correct Skill/owner without broad preload;
3. execute ordinary authorised work directly;
4. use extra routing/coordination only when genuinely needed;
5. verify the requested real-world result once;
6. preserve material durable context when needed without turning it into execution permission.

## Evidence

ARC was extracted from the measured TBHRC/iMPLEMENTAi operating transformation. Historical scale and performance evidence is preserved in [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md); it is reference evidence, not a deployment requirement.

## KISSS

> **The operating system must not become the work.**

Prefer a direct edit, pointer, existing Skill, existing system or ordinary agent judgement before adding a validator, daemon, scheduler, queue, policy engine, provider hierarchy, approval loop or new control plane.

**`main` keeps progress. KISSS keeps speed. Security protects real boundaries, not paperwork.**
