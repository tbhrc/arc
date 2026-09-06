# ARC Repository Router cold-start proof — 2026-09-06

Controlling Issue: #41  
Master: #36  
Upstream canon: `tbhrc/skills#394`

## Result

**PASS.** Current ARC cold-start routing is progressive and remains comfortably inside the TBHRC Agent Operating System hard budget of **<=200 physical Markdown instruction lines**.

## Measured current surfaces

| Surface | Physical lines | Load rule |
|---|---:|---|
| `tbhrc/arc/AGENTS.md` | 31 | Always: repository Router / first hop |
| Sniper owner index | 22 | Only when owner/source is unclear |
| GitHub Workflow `SKILL.md` | 10 | Only when Hybrid/Controlled selection is needed |
| Multi-Agent Orchestrator `SKILL.md` | 23 | Only when delegation/specialist/genuine parallel work is needed |

Counts are from current `main` and include headings, blanks and frontmatter where present.

## Representative cold starts

| Case | Mandatory instruction surfaces before task evidence | Lines | Result |
|---|---|---:|---|
| Known bounded ARC task | Router only | 31 | PASS |
| Owner/source unclear | Router + Sniper | 53 | PASS |
| Execution-level decision needed | Router + Workflow | 41 | PASS |
| Delegation genuinely needed | Router + Orchestrator | 54 | PASS |

A normal known-owner task therefore does **not** preload Sniper, Workflow, Orchestrator, broad indexes, governance sets or provider status.

## Budget headroom

The current policy allocation allows up to 60 lines for the task-specific Skill core and up to 25 lines for one genuinely required conditional policy/guardrail. Even the largest representative control path above (54 lines) plus both allowances is **139 lines**, leaving 61 lines of headroom below the 200-line hard limit.

This is not permission to preload those surfaces. Progressive loading remains mandatory.

## Routing observations

- Root `AGENTS.md` explicitly says Fast Links are pointers, not preload instructions.
- Known owner + bounded task routes directly to the most-specific repository Fast Link / Skill.
- Sniper is explicitly fallback-only.
- Workflow is explicitly conditional for Hybrid/Controlled decisions; Level 0 Direct is the default.
- Multi-Agent Orchestrator is explicitly conditional for delegation/specialist/genuine parallel work.
- No second Router layer is required for any representative path.

## Unnecessary-read check

**PASS.** No mandatory chain requires README, INDEX, System Map, Governance collection, Workflow, Sniper or Orchestrator after the owner and needed task surface are already resolved.

## Blockers / follow-on

None found in the current cold-start contract itself.

Issue #37 still owns generated-Router implementation/tests and Issue #38 owns public architecture wording. If either lands with broader mandatory reads or duplicated routing logic, rerun this same measurement against merged `main` before final ARC release.

## Acceptance

`request -> root AGENTS.md Router -> only needed Fast Link/Skill -> execute`

**PASS — concise, progressive, Direct-first, and within budget.**
