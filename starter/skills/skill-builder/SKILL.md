---
name: skill-builder
description: "Build or update a reusable FolderDesk capability when real work exposes a repeatable instruction, tool or decision pattern worth keeping. Use before creating loose repeatable operating guidance or when an existing local Skill should absorb a learned behaviour."
---

# Skill Builder

**Rule:** build the smallest complete reusable capability for a capable reasoning agent, not machinery for a hypothetical weak executor.

## Build loop

`real outcome → reuse → concise instructions → representative test → observe failure → smallest fix`

1. Freeze the outcome, source of truth and non-obvious invariants.
2. Reuse an existing Skill, native platform capability, approved example or direct reasoning before creating a new Skill.
3. Create a distinct Skill only when the job has its own repeatable trigger + behaviour/output and no existing owner can absorb it cleanly.
4. Keep `SKILL.md` as the smallest complete decision map: trigger, key decisions, invariants, proof and stop condition.
5. Put conditional depth behind direct semantic links instead of bloating cold-start instructions.
6. Use model reasoning for semantic judgement. Add deterministic code only for a repeated mechanical failure, exact machine contract, meaningful scale advantage or hard boundary.
7. Test one natural representative case. Test the user-facing behaviour/output, not only file validity or prose quality.
8. Keep one editable canon per capability. Do not create mirrored SOPs, policy chains, ledgers or lifecycle machinery around it.
9. Route new terminology/structure through the local `structure` Skill.

**Acceptance:** another capable agent can discover and perform the repeatable job from concise local canon without knowing the implementation history.