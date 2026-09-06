---
name: github-workflow
description: Thin bootstrap pointer for GitHub execution. Use when a newly deployed ARC estate needs a Workflow entrypoint before its own canonical Skills repository has adopted or authored the current execution Skill.
---

# GitHub Workflow Pointer

Root `AGENTS.md` is the repository Router.

This starter exists only to make a blank ARC estate usable. It is **not** a second editable operating canon.

For the TBHRC reference implementation, use the current canonical Workflow:

https://github.com/tbhrc/skills/tree/main/github-agent-workflow

For another organisation, adopt or author the equivalent Workflow in that organisation's canonical Skills repository, then treat that Skills-owned version as current truth.

Minimum invariant while bootstrapping:

```text
authorised objective
→ simplest sufficient execution route
→ execute
→ verify once
→ preserve continuity only when useful
→ stop
```

Do not add local approval, Issue, review, provider, security or orchestration doctrine here. Those rules belong in their actual canonical owner.
