---
name: auditor
description: "Lightweight FolderDesk drift check. Use when semantic/structural/behaviour drift, duplicate ownership, unnecessary machinery or controls, misleading agent instructions, loose reusable operating docs, or loss of the work-first purpose is suspected, and after a deliberate material structural change."
---

# Auditor

**Purpose:** protect the useful work surface without becoming governance.

## Check

1. **Outcome** — current behaviour still serves the authorised real-world job.
2. **Shape** — the workspace still follows the local `structure` Skill; synonyms have not become competing folders.
3. **Ownership** — no duplicate canonical file, Skill, status layer or owner exists for substantially the same job.
4. **Skills first** — repeatable HOW lives in an existing/new Skill rather than an orphan operating manual.
5. **Boundary** — machinery lives under `.folderdesk/`; ordinary human work is not forced through machinery.
6. **Necessity** — every added structure, control, workflow, agent, service or repository can name the real need/failure that earned it.
7. **Native/smart-agent test** — before keeping a wrapper, schema, validator, agent layer or workflow, ask whether a capable agent or the host platform already performs the requirement directly.
8. **Control test** — a restriction/gate/log exists only if it protects a concrete boundary and actually intercepts the relevant execution path.
9. **Continuity** — Issues are optional. If an Issue is used, it should preserve only material objective/decision/blocker/next-action state and must not become execution permission or per-step narration. Absence of an Issue is not itself drift.
10. **Induced behaviour** — audit what the Router/Skills actually cause an agent to load, duplicate, skip, require or fail to discover; prose elegance is not the test.
11. **Completeness** — simplification has not removed unique useful capability, source-of-truth handling, retrievability, acceptance truth or a deliberate user-facing interface.
12. **Proof** — when inspection cannot prove behaviour, run the smallest natural representative scenario without giving the agent the expected path or answer.

## Verdict

- `GREEN` — smallest complete path, direct discoverability, no unnecessary machinery, enough current evidence.
- `AMBER` — ambiguous ownership/meaning, questionable machinery/control, weak discoverability or unproven behaviour.
- `RED` — duplicate canon, reusable HOW stranded outside Skills, machinery/control becomes the work, a false protection exists, or material capability/purpose is lost.

## Repair

`DELETE → COLLAPSE → REUSE → DIRECT → SKILL → only then ADD`

Fix obvious safe in-scope drift in the same pass. Do not create an audit backlog for trivial repairs. If broad drift makes repair larger than the useful system, recommend reset/reseed rather than preserving accumulated process.

## Output

```text
Status: GREEN | AMBER | RED
Drift: <none or exact path/behaviour>
Outcome at risk: <none or short outcome>
Canonical route: <existing owner / structure / Skill / native path>
Proof: <inspection or representative scenario>
Action: <none | delete | collapse | reuse | direct | skill | route | reset>
```

**Stop:** audit once at a meaningful change or suspected drift. No recurring audit, ledger, metrics, approval state or persistent audit log.