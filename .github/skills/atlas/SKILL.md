---
name: atlas
description: "ARC's universal front-door onboarding, adoption, audit, health, upgrade, recovery, deployment and navigation Skill. Use when a founder, operator or AI agent asks to install, bootstrap, deploy, reproduce, onboard to, adopt, understand, diagnose, audit, check health, upgrade, export a safe-harbour estate manifest, recover/redeploy, decide the next ARC action, migrate toward or operate the ARC architecture; when the user invokes or refers to `/atlas` or Atlas; or when an existing business must be assessed against ARC. Atlas reads current ARC truth, selects the right mode, reuses existing owners where appropriate, asks only for irreducible missing business inputs, executes ordinary already-authorised bounded work directly, and never treats credentials as authority to mutate."
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

Read [`references/modes.md`](references/modes.md) before choosing an operating mode. For recovery, also read `/contracts/safe-harbour.md`. Read other `/contracts/`, `/components/` and `/VERIFY.md` only as the current decision requires.

## Select the mode

Choose one dominant mode automatically:

- `onboard` — create a first ARC profile for a new estate;
- `adopt` — map an existing business into ARC without forced replacement;
- `audit` — inspect architecture and ownership without mutation;
- `health` — diagnose current verified state;
- `upgrade` — plan movement toward a newer ARC release;
- `recover` — export/recover/redeploy from known-good ARC evidence;
- `next` — determine the smallest safe next action from current durable state.

Do not make the user choose a mode unless ambiguity materially changes the action.

## Default operating loop

```text
understand target and current intent
-> inspect only what is needed
-> choose Atlas mode
-> map truth owners
-> identify required core vs optional components
-> classify existing owners when useful
-> ask only unresolved inputs
-> current instruction authorises ordinary bounded mutation? execute directly
-> stop only at a real destructive/root/private-data/spend/legal/client-commitment boundary
-> verify real state
-> run/prove one real workflow where deployment is involved
-> promote reusable learning
```

Do not turn onboarding into a long questionnaire or approval ceremony. Infer from connected systems and durable repository truth when safe. If the user already supplied an answer or authority, do not ask again.

## New-estate onboarding

Prefer the deterministic first-run path where useful:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

`onboard`, `doctor` and `plan` do not mutate the target. They are inspection/validation tools, not mandatory human approval checkpoints.

For agent-driven/non-interactive onboarding, use the current `arc.py onboard --non-interactive` arguments rather than asking a human to hand-edit JSON when the facts are already known.

## Existing-business adoption

Inventory only what matters:

```text
GitHub repositories
SOP / knowledge owners
existing automations
CRM / ERP / ATS / accounting
private file stores
AI/provider/runtime routes
identity / permission boundaries
```

Classify each relevant owner when useful:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

Prefer **KEEP** or **INTEGRATE** when the existing owner is already correct. Do not destroy or overwrite working systems merely to resemble an ARC example.

Use `python3 scripts/arc.py plan --config arc.json --inspect-target` when it materially helps classify configured repositories as **REUSE / CREATE**. Do not force it as a ceremonial gate before ordinary authorised work.

## Skills-first operating model

For substantive work, use the relevant reusable HOW before inventing process. A deployed ARC environment should have one canonical Skills home and should not maintain competing editable copies of the same workflow.

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

Never infer production or root authority from repository write access or the presence of credentials.

## Authority rule

For ordinary bounded work, the current authorised instruction is sufficient authority. Do not ask for a second approval merely because the operation mutates state.

- `doctor`, `onboard`, `plan`, `export` and `restore-plan` are non-mutating inspection tools.
- `bootstrap` is non-mutating without `--apply`; when ordinary bounded bootstrap is already authorised, select `--apply` directly.
- `seed_foundation.py` is non-mutating without `--apply`; when ordinary bounded seeding is already authorised, select `--apply` directly.
- `--apply` is a deliberate mutation-mode selector, not a request for another human confirmation.
- Existing repositories are reused and not overwritten by bootstrap.
- Never add secret values to `arc.json` or an estate manifest.
- Never mutate solely because credentials exist.

Fresh authority is required only at a real boundary: destructive overwrite/delete/force/recovery, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

Founder approval is exceptional, not precautionary. Do not request founder approval simply because an action changes something.

## Deployment view

Before mutation, understand enough to avoid accidental replacement or scope drift. When useful, a compact deployment view can contain:

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
Bootstrap command / recovery command
Verification gates
First real workflow to prove
```

Distinguish **required core**, **optional component**, **existing owner to keep/integrate**, and **future improvement**. If the current instruction already authorises the ordinary bounded mutation, proceed after resolving necessary facts; do not pause for ritual review.

## Safe-harbour recovery

A healthy estate can export a non-secret architecture snapshot:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

The manifest contains ARC topology/ownership metadata and external owner **names/references only**. It does not contain private-file contents, CRM/ERP/ATS/accounting records, database contents, credential values, trusted-runtime machine state or derived memory contents.

To plan recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Destructive recovery is a real risk boundary. After GitHub repository reconstruction is explicitly authorised:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

`restore --apply` is deliberately bounded to ARC's existing conservative GitHub repository bootstrap. External owners must be restored/reconnected through their own approved backup/identity processes, then the full ARC verification contract must pass.

## Health and upgrade honesty

Use the capabilities actually present in the current ARC release.

- `health` uses current `/VERIFY.md`, CLI verification and observable target evidence.
- `upgrade` identifies the current formal ARC release and manifest schema, then makes the smallest justified migration and verifies it.
- `recover` uses the implemented safe-harbour export/restore-plan/bounded-restore path plus the external-owner backup responsibilities in `/contracts/safe-harbour.md`.

If a requested capability is not implemented, identify the current safe route rather than pretending success or inventing machinery.

## Portable distribution

The editable Atlas canon is this directory: `.github/skills/atlas/`.

Use `scripts/package_atlas.py` to package that same directory as `dist/skill.zip`. Do not maintain a second editable Atlas Skill body for portable distribution. Generated target repositories receive a thin pointer back to current ARC Atlas rather than a copied mutable canon.

## Learning route

If the user wants to learn the method rather than only deploy it, route them to:

https://github.com/tbhrc/gh-course

Course = learning and operator capability. ARC = deployable/recovery architecture.

## Completion

Do not call deployment or recovery complete until the relevant `/VERIFY.md` gates pass and one real workflow proves:

```text
request -> Skill -> owner truth -> execution -> verification -> durable evidence
```

For ongoing Stage/programme work, do not leave execution state only in chat. Update the controlling Issue with evidence and exact next action so a cold agent can continue from GitHub alone.
