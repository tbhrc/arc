# ARC Foundational Skills

A newly deployed ARC estate should not begin with an empty Skills repository or an undefined operating direction.

ARC seeds a **small generic foundation**, not a copy of TBHRC's live Skill Bank. The target organisation owns its own canonical **North Star** — mission, vision and/or directives — and its own editable Skills canon.

**Fast links:** [Atlas](../../ATLAS.md) · [Architecture](../../ARCHITECTURE.md) · [Bootstrap](../../BOOTSTRAP.md) · [Verify](../../VERIFY.md) · [ARC Issues](https://github.com/tbhrc/arc/issues)

## Foundation

| Skill | Purpose |
|---|---|
| `owner-router` | conditional owner/source lookup only when the repository Router cannot resolve ownership |
| `github-workflow` | preserve Anti-Drift and choose the lowest sufficient durable GitHub execution level |
| `skill-authoring` | turn repeatable operating method into a reusable Skill |
| `research-escalation` | turn recurring friction into problem-to-platform research |

Atlas remains ARC's architecture/onboarding/lifecycle front door and is already seeded by ARC repository bootstrap. It is separate from the deployed estate's day-to-day Repository Router at root `AGENTS.md`.

## First-day operating model

```text
repository root AGENTS.md Router
-> one relevant Fast Link
-> smallest relevant Skill / owner
-> execute
-> verify real state
-> durable Issue evidence when work needs continuity
```

If the Router cannot resolve the correct owner/source, use `owner-router` as the conditional fallback, then return to the resolved repository/Skill and execute.

For substantive durable GitHub work, the controlling Issue should distinguish:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

North Star is organisation-level direction. Anti-Drift is the original requested outcome of the specific work item. Do not use the two labels interchangeably.

## Doctrine

These are **starter capabilities**. After deployment, the target organisation's Skills repository becomes the editable canon for its own reusable HOW.

Do not hard-code TBHRC's Top Five into a generic deployment. ARC reproduces the North-Star mechanism; the target organisation owns the actual wording.

Do not continuously sync these templates over target edits. ARC upgrades may propose improvements, but target Skill changes require normal review and explicit adoption.
