---
name: skill-authoring
description: Turn a repeatable ARC operating method into a concise reusable Skill. Use when a workflow, convention, integration method or learned pattern is likely to recur across agents or sessions and should become reusable HOW rather than remain in chat, an Issue comment or duplicated SOP text.
---

# Skill Authoring

Create or update Skills only for reusable method.

```text
repeatable problem
→ collect concrete use examples
→ identify inputs / outputs / tools
→ keep SKILL.md concise
→ add scripts/references only where they improve reliability
→ validate on a real use case
→ publish into the target organisation's canonical Skills home
```

Rules:

- one editable canon per Skill;
- frontmatter description must make triggering clear;
- do not copy live business facts into Skills;
- use deterministic scripts for fragile repeatable operations;
- route detailed reference material out of the core Skill when large;
- improve the Skill after real failures or repeated friction, not speculative complexity.
