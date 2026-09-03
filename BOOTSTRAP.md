# Bootstrap ARC

ARC bootstrap is deliberately **plan-first**. The goal is reproducibility without surprise mutation.

## 1. Choose a deployment context

Use the generic profile for a new organisation/client:

```bash
cp profiles/generic-business/arc.example.json arc.json
```

Use the TBHRC profile only as a reference for how a mature deployment can be structured. Do not clone TBHRC names blindly into another business.

## 2. Edit only business-specific configuration

At minimum set:

- `target.owner` — GitHub user or organisation;
- `target.owner_type` — `org` or `user`;
- repository visibility defaults;
- domain repositories required by the business;
- whether a trusted runtime repository is required.

Do not put secret values in `arc.json`.

## 3. Doctor

```bash
python3 scripts/arc.py doctor --config arc.json
```

Doctor checks local prerequisites and authentication. It does not create repositories.

## 4. Plan

```bash
python3 scripts/arc.py plan --config arc.json
```

Review:

- target owner;
- repositories to be created or reused;
- visibility;
- required vs optional components;
- domain owners;
- manual integrations that remain outside repository bootstrap.

## 5. Apply

Only after the target plan is accepted:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

The bootstrap is intentionally conservative:

- existing repositories are reused, not overwritten;
- missing configured repositories are created;
- no secrets are created or copied;
- no production system is modified;
- no private business data is migrated;
- the script does not grant broad organisation permissions.

## 6. Seed each repository

Repository creation is only the shell. Atlas should then guide the operator/agent to establish:

- root README;
- `AGENTS.md`;
- declared owner/boundary;
- Issue/PR workflow;
- initial Skills canon;
- Research front door;
- private-file and specialist-system ownership map.

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

Capture what failed. Promote reusable corrections into the correct owner rather than patching only the chat session.
