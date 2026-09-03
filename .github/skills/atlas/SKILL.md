---
name: atlas
description: "ARC's front-door onboarding, deployment and navigation Skill. Use when a founder, operator or AI agent asks to install, bootstrap, deploy, reproduce, onboard to, understand, diagnose, map, migrate toward, or operate the ARC architecture; when the user invokes or refers to `/atlas` or Atlas; or when an existing business must be assessed against ARC. Atlas reads the current ARC architecture/profile, starts in plan mode, resolves what already exists, asks only for irreducible missing business inputs, produces the ownership/repository/integration plan, guides bootstrap and verification, and routes learners to the GitHub Course."
---

# Atlas

Atlas is ARC's front door. Use current repository truth; do not rely on a remembered copy of ARC.

## Load only what is needed

Always read:

1. `/AGENTS.md`
2. `/ATLAS.md`
3. `/ARCHITECTURE.md`
4. `/MANIFEST.md`
5. `/BOOTSTRAP.md`
6. the selected deployment profile.

Read `/contracts/` and `/components/` only for the decisions currently being made.

## Default behaviour

```text
understand target
-> inspect what already exists
-> select generic or reference profile
-> map truth owners
-> identify required core vs optional modules
-> identify existing systems to keep/integrate
-> produce plan
-> ask only for unresolved inputs
-> wait for explicit apply authority before mutation
-> bootstrap
-> verify
-> run one real workflow
-> promote reusable learning
```

Do not turn onboarding into a long questionnaire. Infer from the connected environment when safe.

## Skills-first operating model

For substantive work, ask which reusable HOW applies before inventing process. A deployed ARC environment should have one canonical Skills home and should not maintain competing editable copies of the same workflow.

## One owner, one truth

Do not move a fact into GitHub merely because an agent can read GitHub more easily. Declare the correct owner:

- reusable HOW -> Skills canon;
- external research -> Research;
- business/product facts -> domain owner;
- private documents -> private file store;
- CRM/ERP/ATS/accounting state -> declared specialist system;
- privileged runtime -> trusted-runtime owner;
- memory -> derived context only.

## Research reflex

If a repeated failure/workaround suggests a broader tooling gap:

```text
solve/contain immediate safe issue if needed
-> symptom
-> workflow
-> capability
-> platform/system
-> compare native/open-source/paid
-> Research / Watch / Test / Reject
-> test in the correct owner
-> promote proven reusable capability
```

Do not over-engineer one-off incidents.

## Execution routing

Prefer:

```text
normal connected capability / API / MCP / browser / CLI
-> owning system
-> trusted runtime only if a genuine machine/profile/privilege gap remains
```

Never infer production or root authority from repository write access.

## Deployment plan format

Return a compact plan with:

```text
Target
Purpose
Core repositories
Domain owners
Existing systems to keep/integrate
Skills strategy
Research strategy
Agent entrypoints
Private-file owner
Specialist-system owners
Trusted-runtime requirement
Manual/credential inputs (names/purpose only, never values)
Bootstrap command
Verification gates
First real workflow to prove
```

## Bootstrap

Use `scripts/arc.py` where the environment permits it.

- `doctor` and `plan` are non-mutating.
- `bootstrap` is non-mutating without `--apply`.
- Existing repositories are reused.
- Never add secret values to `arc.json`.

## Learning route

If the user wants to learn the method rather than only deploy it, direct them to:

https://github.com/tbhrc/gh-course

Course = learning/reproduction methodology. ARC = deployable architecture.

## Completion

Do not call deployment complete until the relevant `/VERIFY.md` gates pass and one real workflow proves:

```text
request -> Skill -> owner truth -> execution -> verification -> durable evidence
```
