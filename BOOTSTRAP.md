# Bootstrap ARC

ARC bootstrap is deliberately **inspectable before mutation**, but inspection is not a mandatory second approval ceremony. The goal is reproducibility without surprise mutation or operational drag.

**Fast links:** [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Manifest](MANIFEST.md) · [Verify](VERIFY.md) · [Starter Skills](starter/skills/README.md) · [Repository Router](AGENTS.md) · [ARC Issues](https://github.com/tbhrc/arc/issues)

## 1. Create a business profile through Atlas

For a normal new organisation/client, do not start by hand-editing the example JSON. Use Atlas or the deterministic onboarding command:

```bash
python3 scripts/arc.py onboard --output arc.json
```

The command asks only for business-specific facts needed to create a valid profile. A capable agent that already knows those facts can use `onboard --non-interactive`.

The generic example remains available at `profiles/generic-business/arc.example.json` for inspection and automation. The TBHRC profile is reference wiring only; do not clone TBHRC names blindly into another business.

`onboard` writes local configuration only. It does not mutate GitHub or any specialist system.

## 2. Resolve the ownership configuration and North Star

Establish at minimum:

- the target organisation's canonical **North Star** location — its mission, vision and/or directives owner;
- `target.business_name` and `target.owner`;
- `target.owner_type` — `org` or `user`;
- repository visibility defaults;
- domain repositories required by the business;
- selected optional business modules;
- provider routes and runtimes available to agents;
- private-file owner;
- specialist systems already owning structured state;
- whether a trusted runtime repository is genuinely required.

ARC reproduces the **North-Star mechanism**, not TBHRC's editable mission wording. A generic deployment must point to the target organisation's own canonical direction rather than copying TBHRC's Top Five.

Do not put secret values or secret-like fields in `arc.json`. ARC rejects common secret-field names and known credential-value patterns by design.

If `arc.json` already exists, onboarding refuses to overwrite it unless `--overwrite` is deliberately supplied because overwrite is a genuine destructive boundary.

Read [modules](modules/README.md), [providers](providers/README.md) and [runtimes](runtimes/README.md) only when adding optional capability selections. ARC modules are ownership patterns, not mandatory software bundles.

## 3. Doctor

```bash
python3 scripts/arc.py doctor --config arc.json
```

Doctor checks local prerequisites and authentication. It does not create repositories.

## 4. Inspect and plan when useful

```bash
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Where authenticated GitHub CLI access is available, the plan classifies each configured repository as:

```text
REUSE  — repository already exists; leave it unchanged during bootstrap
CREATE — repository is missing and will be created when mutating mode is selected
```

If GitHub CLI is unavailable or unauthenticated, ARC reports `UNKNOWN` rather than guessing that a repository is missing.

The plan is a visibility tool. It is useful for checking ownership, repository roles/visibility, modules, existing repositories, external owners and manual integrations. It is **not** a required human approval checkpoint when the current instruction already authorises ordinary bounded deployment.

For an established business, Atlas should classify existing owners as **KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE** before structural change when that classification is materially useful.

## 5. Apply ordinary authorised deployment directly

If the current instruction already authorises ordinary bounded deployment, execute without asking the human again:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

`--apply` deliberately selects mutating mode. It does not create a second approval requirement.

The bootstrap remains conservative:

- existing repositories are reused, not overwritten;
- missing configured repositories are created;
- no credentials are created or copied;
- no production specialist system is modified;
- no private business data is migrated;
- the script does not grant broad organisation permissions.

Stop for fresh authority only when the next action actually crosses a consequential boundary: destructive overwrite/delete/force, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

## 6. Confirm repository seeding and navigation

For each **new** repository, bootstrap seeds a role-aware README, root `AGENTS.md`, Atlas Skill pointer and `/atlas` prompt-file entrypoint. Existing repositories are deliberately left unchanged.

Root `AGENTS.md` is the first-hop Repository Router. It should make these destinations directly reachable through progressive Fast Links without broad rediscovery:

```text
North Star
Skills
workflow / durable work method
owner / system map
Issues when useful
```

Known bounded work should follow only the needed Fast Link to the smallest relevant Skill/owner. Owner/source lookup is conditional when the Router cannot resolve the route. Workflow and Multi-Agent Orchestrator are loaded only when their execution/delegation responsibilities are genuinely needed.

Important active front doors should use compact **Fast Links**. Fast Links are pointers, not preload instructions. Do not manufacture decorative links or add Fast Links to raw evidence/generated/archive material unless a canonical return/replacement link materially helps.

When an Issue materially improves continuity, a concise structure is useful:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

North Star is organisation-level direction. **Anti-Drift** is the founder/user's original requested outcome for the specific work item. The route may change; the destination must not silently change.

Atlas should then guide the operator/agent to establish or reconcile only what is needed:

- declared owner/boundary;
- continuity/evidence method when useful;
- initial Skills canon;
- Research front door;
- private-file and specialist-system ownership map.

If `verify` reports an existing repository as `INCOMPLETE`, integrate the missing ARC navigation deliberately rather than overwriting the repository.

Use the [GitHub Course](https://github.com/tbhrc/gh-course) when a human needs to learn why these objects matter.

## 7. Seed the first-day Skills foundation

A newly created ARC Skills repository should be usable immediately rather than empty.

Inspection is available when useful:

```bash
python3 scripts/seed_foundation.py --config arc.json
```

It resolves the configured repository with role `skills` and lists the generic starter Skills that are missing. When ordinary bounded seeding is already authorised, execute directly:

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

Do not ask for a second approval merely because mutating mode is selected.

ARC creates only missing files for:

- `owner-router`;
- `github-workflow`;
- `skill-authoring`;
- `research-escalation`.

`owner-router` is a conditional fallback for unresolved owner/source questions after root `AGENTS.md` cannot already route the task. `github-workflow` preserves Anti-Drift and chooses the lowest sufficient durable GitHub execution lane.

Existing target Skills are never overwritten. After this first seed, the target organisation's Skills repository owns its editable reusable HOW. ARC does not continuously overwrite those Skills from upstream templates.

## 8. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Then complete only the relevant non-automatable acceptance in [VERIFY.md](VERIFY.md).

## 9. Run one real workflow

The first meaningful proof is not an empty architecture. Select one real business workflow and prove:

```text
organisation North Star
-> request / Anti-Drift objective
-> Repository Router
-> relevant Skill / owner truth
-> authorised provider/runtime
-> agent execution
-> verification
-> durable evidence when useful
```

Capture what failed. Promote reusable corrections into the correct owner rather than patching only a chat session.

## 10. Export the safe-harbour architecture snapshot

Once the estate is healthy, create a non-secret estate manifest:

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

Keep the estate manifest with the organisation's approved recovery documentation together with a reference to the formal ARC release/tag used by the estate. The manifest contains architecture metadata and owner references only. It is **not** a backup of private files, specialist-system data, credentials, runtime machine state or memory contents.

Read [contracts/safe-harbour.md](contracts/safe-harbour.md) and ensure each external owner has its own appropriate backup/recovery method.

## 11. Recovery / redeployment

To inspect recovery without mutation when useful:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

For ordinary authorised bounded reconstruction:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

`restore --apply` reuses existing configured repositories unchanged and creates only missing configured GitHub repositories through the same conservative bootstrap contract. It does not restore external owner contents. Reconnect/restore those owners separately, then rerun the complete ARC verification contract before declaring recovery complete.

If a future recovery operation actually deletes, overwrites or force-updates material state, protect that specific action as the real destructive boundary.

## 12. Preserve continuation state when useful

When continuity materially helps future work, preserve only what is needed to resume: objective, current state, evidence and exact next action. An Issue is one available surface, not a mandatory runtime prerequisite.
