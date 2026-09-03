---
name: github-workflow
description: Govern durable GitHub work proportionately. Use when an ARC agent must create or change repository state and decide between a small direct Issue change, a standard Issue/branch/PR workflow, or a large multi-stage Master programme with independently verifiable Stage Issues.
---

# GitHub Workflow

Choose the lowest sufficient level.

```text
Level 1 — small, reversible, low-risk
Issue → bounded change → verify → close

Level 2 — multi-file/code/automation/reviewable
Issue → branch → implement → test → PR → review → merge → verify

Level 3 — genuinely multi-stage programme
Master Issue → linked Stage Issues → each Stage follows Level 2 → end-to-end acceptance
```

Rules:

- keep founder/business intent in the controlling Issue;
- a cold agent must be able to continue from GitHub without chat history;
- check latest owner truth before writing;
- assume another agent may be working concurrently;
- close only after acceptance, not merely after a PR merge;
- record reusable learning in the smallest correct owner.
