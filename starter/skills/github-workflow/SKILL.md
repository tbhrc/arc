---
name: github-workflow
description: Govern durable GitHub work proportionately. Use when an ARC agent must create or change repository state and decide between a small direct Issue change, a standard Issue/branch/PR workflow, or a large multi-stage Master programme with independently verifiable Stage Issues.
---

# GitHub Workflow

Choose the lowest sufficient governed level.

```text
Level 1 — small, reversible, low-risk
Issue → bounded change → verify → close

Level 2 — multi-file/code/automation/reviewable
Issue → branch → implement → test → PR → review → merge → verify

Level 3 — genuinely multi-stage programme
Master Issue → linked Stage Issues → each Stage follows Level 2 → end-to-end acceptance
```

Every substantive durable Issue should preserve the same lightweight structure:

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

- `North Star` points to the organisation-level canonical mission / vision / directives; do not silently duplicate editable North-Star wording into every Issue;
- `Anti-Drift — Original Objective` preserves the founder/user's original requested outcome and must not be rewritten as local implementation evolves;
- use `Local Objective` only when the active bounded implementation is materially different from the Anti-Drift objective;
- use the lowest sufficient path and do not add workflow machinery merely because it is available;
- a cold agent must be able to continue from GitHub without chat history;
- check latest owner truth before writing;
- assume another agent may be working concurrently and keep one writer per mutation scope;
- close only after acceptance, not merely after a PR merge;
- verify the material result once unless evidence is stale or ambiguous;
- keep compact Fast Links on important active routers/front doors when they reduce rediscovery;
- record reusable learning in the smallest correct owner.
