---
name: owner-router
description: Thin bootstrap pointer for unresolved owner/source questions. Use only when root `AGENTS.md` cannot already route the task and before the deployed organisation has established its own canonical owner/source lookup Skill.
---

# Owner Lookup Pointer

Root `AGENTS.md` is the repository Router. Use this starter only when the owner/source remains unclear.

This file is a bootstrap pointer, not a second editable operating canon.

For the TBHRC reference implementation, use the current canonical owner/source lookup:

https://github.com/tbhrc/skills/blob/main/human-ai-operations-map/references/ai-sniper-entry-map.md

For another organisation, keep the owner/source map in that organisation's canonical Skills/operations owner and point here only until that owner exists.

Minimum invariant:

```text
unclear owner/source
→ identify the real owner
→ use current owner truth
→ execute in the correct owner
→ verify
```

Do not add task-control, Issue, approval, security or continuity doctrine here. Those rules belong in their actual canonical owner.
