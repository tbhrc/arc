# Bootstrap ARC

ARC bootstrap is deliberately **plan-first**. The goal is reproducibility without surprise mutation.

## 1. Create a business profile through Atlas

For a normal new organisation/client, do not start by hand-editing the example JSON. Use Atlas or the deterministic onboarding command:

```bash
python3 scripts/arc.py onboard --output arc.json
```

The command asks only for business-specific facts needed to create a valid profile. A capable agent that already knows those facts can use `onboard --non-interactive`.

The generic example remains available at `profiles/generic-business/arc.example.json` for inspection and automation. The TBHRC profile is reference wiring only; do not clone TBHRC names blindly into another business.

`onboard` writes local configuration only. It does not mutate GitHub or any specialist system.

## 2. Review the generated ownership configuration

Confirm at minimum:

- `target.business_name` and `target.owner`;
- `target.owner_type` — `org` or `user`;
- repository visibility defaults;
- domain repositories required by the business;
- selected optional business modules;
- provider routes and runtimes available to agents;
- private-file owner;
- specialist systems already owning structured state;
- whether a trusted runtime repository is genuinely required.

Do not put secret values or secret-like fields in `arc.json`. ARC rejects common secret-field names and known credential-value patterns by design.

If `arc.json` already exists, onboarding refuses to overwrite it unless `--overwrite` is explicitly supplied.

Read [modules](modules/README.md), [providers](providers/README.md) and [runtimes](runtimes/README.md) before adding optional capability selections. ARC modules are ownership patterns, not mandatory software bundles.

## 3. Doctor

```bash
python3 scripts/arc.py doctor --config arc.json
```

Doctor checks local prerequisites and authentication. It does not create repositories.

## 4. Inspect and plan

```bash
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Where authenticated GitHub CLI access is available, the plan classifies each configured repository as:

```text
REUSE  — repository already exists; leave it unchanged during bootstrap
CREATE — repository is missing and would be created only after apply authority
```

If GitHub CLI is unavailable or unauthenticated, ARC reports `UNKNOWN` rather than guessing that a repository is missing.

Review:

- target owner;
- repository roles and visibility;
- required vs optional components;
- domain owners;
- modules selected by the business;
- authorised provider/runtime routes;
- existing repositories to reuse;
- private files and specialist systems that remain external owners;
- manual integrations that remain outside repository bootstrap.

For an established business, Atlas should additionally classify existing owners as **KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE** before recommending structural change.

## 5. Apply

A plan is not permission to mutate. Only after the target plan is accepted:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

The bootstrap is intentionally conservative:

- existing repositories are reused, not overwritten;
- missing configured repositories are created;
- no credentials are created or copied;
- no production specialist system is modified;
- no private business data is migrated;
- the script does not grant broad organisation permissions.

## 6. Confirm repository seeding and ownership

For each **new** repository, bootstrap seeds a role-aware README, root `AGENTS.md`, Atlas Skill pointer and `/atlas` prompt-file entrypoint. Existing repositories are deliberately left unchanged.

Atlas should then guide the operator/agent to establish or reconcile:

- declared owner/boundary;
- Issue/PR workflow;
- initial Skills canon;
- Research front door;
- private-file and specialist-system ownership map.

If `verify` reports an existing repository as `INCOMPLETE`, integrate the missing ARC navigation deliberately rather than overwriting the repository.

Use the [GitHub Course](https://github.com/tbhrc/gh-course) when a human needs to learn why these objects matter.

## 7. Seed the first-day Skills foundation

A newly created ARC Skills repository should be usable immediately rather than empty.

First inspect the non-mutating plan:

```bash
python3 scripts/seed_foundation.py --config arc.json
```

The plan resolves the configured repository with role `skills` and lists the generic starter Skills that are missing. After explicit approval:

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

ARC creates only missing files for:

- `owner-router`;
- `github-workflow`;
- `skill-authoring`;
- `research-escalation`.

Existing target Skills are never overwritten. After this first seed, the target organisation's Skills repository owns its editable reusable HOW. ARC does not continuously overwrite those Skills from upstream templates.

## 8. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Then complete the non-automatable acceptance in [VERIFY.md](VERIFY.md).

## 9. Run one real workflow

The first meaningful proof is not an empty architecture. Select one real business workflow and prove:

```text
request
-> Skill
-> owner truth
-> authorised provider/runtime
-> agent execution
-> verification
-> durable evidence
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

To understand recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Only after the recovery plan is understood and GitHub repository reconstruction is explicitly authorised:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

`restore --apply` recreates missing configured GitHub repositories through the same conservative bootstrap contract. It does not restore external owner contents. Reconnect/restore those owners separately, then rerun the complete ARC verification contract before declaring recovery complete.

## 12. Preserve durable continuation state

For material ARC Stage/programme work, update the controlling GitHub Issue before stopping. It must contain current branch/state, verification evidence, blockers and the exact next action so a cold agent can resume without chat history.
