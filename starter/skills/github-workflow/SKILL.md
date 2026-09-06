---
name: github-workflow
description: Govern durable GitHub execution proportionately after repository routing is known. Use when an ARC agent must choose the execution method for a durable task: Level 0 Direct, Level 1 Hybrid, or Level 2 Controlled.
---

# GitHub Workflow

Root `AGENTS.md` is the repository Router. This Skill owns only HOW durable GitHub work executes.

Use the lowest sufficient level:

```text
Level 0 Direct — one authorised execution stream
Level 1 Hybrid — genuinely independent workstreams
Level 2 Controlled — material execution risk requiring stronger controls
```

Start at Level 0. Escalate only for a concrete reason.

Every substantive durable Issue should preserve:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

Rules:

- `North Star` points to the organisation-level canonical mission / vision / directives;
- `Anti-Drift — Original Objective` preserves the founder/user's requested outcome while implementation evolves;
- ordinary already-authorised bounded work executes directly; do not ask for a second confirmation merely because state will change;
- `--apply` or equivalent mutating mode is an execution selector, not a ceremonial human approval step;
- founder approval is exceptional, not precautionary;
- keep one active writer per unresolved mutation scope;
- check current owner truth before writing;
- verify the material result once unless evidence is stale or ambiguous;
- update/close the controlling Issue after acceptance, then stop;
- fresh authority is reserved for real boundaries: root/security, destructive/irreversible or production-destructive mutation, material spend, private-data disclosure/movement, legal/compliance commitment, or material external/client commitment.
