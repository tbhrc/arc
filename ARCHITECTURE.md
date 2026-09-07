# ARC Architecture

ARC reproduces the minimum portable architecture needed for a human + AI operating ecosystem without turning process into the work.

**Fast links:** [README](README.md) · [Atlas](ATLAS.md) · [Router](AGENTS.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Manifest](MANIFEST.md)

## Core operating graph

```text
organisation direction
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
- root `AGENTS.md` Repository Router with progressive Fast Links;
- one canonical Skills home for reusable HOW;
- source-of-truth boundaries;
- provider/runtime-neutral execution;
- private-file and specialist-system ownership references;
- inspectable bootstrap and bounded recovery;
- real-state verification;
- non-secret estate manifest/reconnection model.

## What ARC does not reproduce

ARC does not copy or become the owner of:

- editable mission/vision wording;
- business/product/client facts;
- private client/candidate files;
- CRM/ATS/ERP/accounting records;
- credentials;
- runtime machine state;
- derived memory contents;
- the target organisation's evolving Skills canon after deployment.

## Skills-first ownership

Reusable HOW belongs in one canonical Skills repository.

ARC may seed thin starter pointers so a blank environment is usable on day one. Those starters are bootstrap assets only. They must not become a competing editable copy of the live operating system.

For the TBHRC reference implementation, current operating doctrine lives in `tbhrc/skills`, including:

- Repository Router / Agent OS conventions;
- GitHub Agent Workflow;
- Multi-Agent Orchestrator;
- anti-friction / real-boundary security policy.

ARC should point to those current owners where appropriate rather than restating their full rules.

## Durable context without Issue ceremony

Issues, PRs, plans and evidence are not part of the minimum execution path and are never runtime permission for ordinary authorised work. ARC does not require a named `Anti-Drift` section, controlling Issue, checklist or evidence object merely to execute.

When substantive work changes a material objective, scope, acceptance condition, architecture/decision, blocker or continuation state, preserve that change once in the appropriate durable owner record before handoff, closure or the end of the meaningful work unit. Do not interrupt authorised execution for pre-mutation documentation ceremony.

## One owner / one truth

| State | Owner |
|---|---|
| reusable HOW | Skills canon |
| business/product facts | business/domain owner |
| external research/proving | Research |
| private documents | private file owner |
| CRM/ATS/ERP/accounting state | specialist system |
| privileged runtime state | trusted-runtime owner |
| derived context | memory layer |
| ARC portable architecture | ARC |

Do not copy mutable state into GitHub merely because GitHub is convenient for an agent.

## Execution and authority

ARC starts with the simplest existing authorised route that can complete the work.

`--apply` or an equivalent mutating mode is an execution selector, not a second approval request.

Additional human authority is reserved for genuine consequential boundaries such as root/super-admin changes, destructive or irreversible mutation, material spend, legal/compliance commitment, private-data disclosure or material external/client commitment.

Security controls must protect a concrete current boundary and earn their friction. Generic hardening, read-only defaults, approval rituals, fail-closed machinery, provider hierarchies and duplicate validation are not architecture by default.

## Recovery

ARC Safe Harbour is architecture recovery, not data backup.

```text
known-good ARC release
+ non-secret estate manifest
+ external owners' own recovery methods
→ recreate missing ARC-owned repository surfaces
→ reconnect external owners
→ verify
```

Current `restore --apply` reuses existing configured repositories unchanged and creates only missing configured repositories. If a future recovery action actually deletes, overwrites or force-updates material state, protect that specific destructive action then.

## Acceptance

ARC is healthy when a fresh capable human or agent can:

1. enter through root `AGENTS.md`;
2. reach the correct Skill/owner without broad preload;
3. execute ordinary authorised work directly;
4. use extra routing/coordination only when genuinely needed;
5. verify the requested real-world result once;
6. preserve material durable context when needed without turning it into execution permission.

## KISSS

> **The operating system must not become the work.**

Before adding architecture, ask whether a direct edit, pointer, existing Skill, existing system or ordinary agent judgement already solves the need.
