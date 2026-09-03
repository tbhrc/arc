---
name: atlas
description: "ARC's universal front-door onboarding, adoption, audit, health, upgrade, recovery, deployment and navigation Skill. Use when a founder, operator or AI agent asks to install, bootstrap, deploy, reproduce, onboard to, adopt, understand, diagnose, audit, check health, upgrade, recover/redeploy, decide the next ARC action, migrate toward or operate the ARC architecture; when the user invokes or refers to `/atlas` or Atlas; or when an existing business must be assessed against ARC. Atlas reads current ARC truth, selects the right mode, starts plan-first, reuses existing owners where appropriate, asks only for irreducible missing business inputs, and never treats credentials as authority to mutate."
---

# Atlas

Atlas is ARC's single front door. Use current repository truth; never rely on a remembered or chat-only copy of ARC.

## Start

Always read:

1. `/AGENTS.md`
2. `/ATLAS.md`
3. `/ARCHITECTURE.md`
4. `/MANIFEST.md`
5. `/BOOTSTRAP.md`
6. the selected deployment profile.

Read [`references/modes.md`](references/modes.md) before choosing an operating mode. Read `/contracts/`, `/components/` and `/VERIFY.md` only as the current decision requires.

## Select the mode

Choose one dominant mode automatically:

- `onboard` — create a first ARC profile for a new estate;
- `adopt` — map an existing business into ARC without forced replacement;
- `audit` — inspect architecture and ownership without mutation;
- `health` — diagnose current verified state;
- `upgrade` — plan movement toward a newer ARC release;
- `recover` — plan restore/redeployment from known-good evidence;
- `next` — determine the smallest safe next action from current durable state.

Do not make the user choose a mode unless ambiguity materially changes the action.

## Default operating loop

```text
understand target and current intent
-> inspect what already exists
-> choose Atlas mode
-> map truth owners
-> identify required core vs optional components
-> classify existing owners
-> produce plan
-> ask only unresolved inputs
-> wait for explicit apply authority before mutation
-> execute through the correct owner
-> verify real state
-> run/prove one real workflow where deployment is involved
-> promote reusable learning
```

Do not turn onboarding into a long questionnaire. Infer from connected systems and durable repository truth when safe. If the user already supplied an answer, do not ask again.

## New-estate onboarding

Prefer the deterministic first-run path where available:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

`onboard`, `doctor` and `plan` do not mutate the target. Generated ARC configuration must contain ownership/configuration metadata only, never secret values.

For agent-driven/non-interactive onboarding, use the current `arc.py onboard --non-interactive` arguments rather than asking a human to hand-edit JSON when the facts are already known.

## Existing-business adoption

Inventory first:

```text
GitHub repositories
SOP / knowledge owners
existing automations
CRM / ERP / ATS / accounting
private file stores
AI/provider/runtime routes
identity / permission boundaries
```

Classify each relevant owner:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

Prefer **KEEP** or **INTEGRATE** when the existing owner is already correct. Do not destroy or overwrite working systems merely to resemble an ARC example.

Use `python3 scripts/arc.py plan --config arc.json --inspect-target` when GitHub CLI access is available to classify configured repositories as **REUSE / CREATE** before any apply step.

## Skills-first operating model

For substantive work, ask which reusable HOW applies before inventing process. A deployed ARC environment should have one canonical Skills home and should not maintain competing editable copies of the same workflow.

## One owner, one truth

Declare the correct owner:

- reusable HOW -> Skills canon;
- external research -> Research;
- business/product facts -> domain owner;
- private documents -> private file store;
- CRM/ERP/ATS/accounting state -> declared specialist system;
- privileged runtime -> trusted-runtime owner;
- memory -> derived context only;
- ARC portable deployment/recovery contract -> this repository.

Do not move a fact into GitHub merely because an agent can read GitHub more easily.

## Research reflex

If a repeated failure/workaround suggests a broader tooling gap:

```text
contain immediate safe issue if needed
-> symptom
-> workflow
-> capability
-> platform/system
-> compare native / existing / open-source / paid
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

Never infer production, root or apply authority from repository write access or the presence of credentials.

## Deployment plan format

Before mutation, return a compact plan containing:

```text
Target
Purpose
Atlas mode
Core repositories
Domain owners
Existing owners: KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE
Configured repositories: REUSE / CREATE where observable
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

Distinguish **required core**, **optional component**, **existing owner to keep/integrate**, and **future improvement**.

## Apply gate

`plan` is not permission to mutate.

- `doctor`, `onboard` and `plan` are non-mutating.
- `bootstrap` is non-mutating without `--apply`.
- Existing repositories are reused and not overwritten by bootstrap.
- Never add secret values to `arc.json`.
- Never mutate solely because credentials exist.

## Health, upgrade and recovery honesty

Use the capabilities actually present in the current ARC release. Do not invent future lifecycle tooling.

- `health` uses current `/VERIFY.md`, CLI verification and observable target evidence; richer lifecycle health belongs to ARC.7.
- `upgrade` produces a plan from known current/release contracts until deterministic release-to-estate upgrade support is implemented.
- `recover` uses only known releases/manifests/backups and declared owners; safe-harbour export/restore is owned by ARC.4.

If the requested capability is not yet implemented, identify the owning Stage/contract and give the current safe route rather than pretending success.

## Portable distribution

The editable Atlas canon is this directory: `.github/skills/atlas/`.

Use `scripts/package_atlas.py` to package that same directory as `dist/skill.zip`. Do not maintain a second editable Atlas Skill body for portable distribution. Generated target repositories receive a thin pointer back to current ARC Atlas rather than a copied mutable canon.

## Learning route

If the user wants to learn the method rather than only deploy it, route them to:

https://github.com/tbhrc/gh-course

Course = learning and operator capability. ARC = deployable/recovery architecture.

## Completion

Do not call deployment complete until the relevant `/VERIFY.md` gates pass and one real workflow proves:

```text
request -> Skill -> owner truth -> execution -> verification -> durable evidence
```

For ongoing Stage/programme work, do not leave execution state only in chat. Update the controlling Issue with evidence and exact next action so a cold agent can continue from GitHub alone.
