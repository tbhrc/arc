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
- private-file owner;
- specialist systems already owning structured state;
- whether a trusted runtime repository is genuinely required.

Do not put secret values or secret-like fields in `arc.json`. ARC rejects common secret-field names by design.

If `arc.json` already exists, onboarding refuses to overwrite it unless `--overwrite` is explicitly supplied.

## 3. Doctor

```bash
python3 scripts/arc.py doctor --config arc.json
```

Doctor checks local prerequisites and authentication. It does not create repositories.

## 4. Inspect and plan

```bash
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Where GitHub CLI access is available, the plan classifies each configured repository as:

```text
REUSE  — repository already exists; leave it unchanged during bootstrap
CREATE — repository is missing and would be created only after apply authority
```

Review:

- target owner;
- repository roles and visibility;
- required vs optional components;
- domain owners;
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
- no secrets are created or copied;
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

## 7. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Then complete the non-automatable acceptance in [VERIFY.md](VERIFY.md).

## 8. Run one real workflow

The first meaningful proof is not an empty architecture. Select one real business workflow and prove:

```text
request
-> Skill
-> owner truth
-> agent execution
-> verification
-> durable evidence
```

Capture what failed. Promote reusable corrections into the correct owner rather than patching only a chat session.

## 9. Preserve durable continuation state

For material ARC Stage/programme work, update the controlling GitHub Issue before stopping. It must contain current branch/state, verification evidence, blockers and the exact next action so a cold agent can resume without chat history.
