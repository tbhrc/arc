# Private Files Component

ARC explicitly separates private files from the public/durable operating desk.

A business should declare an approved private-file owner for items such as:

- client deliverables;
- personnel/candidate records;
- contracts;
- sensitive assessments;
- confidential source material.

## Ownership contract

The private file platform owns the file bytes, permissions, versions and retention state. GitHub may own the Issue/decision/workflow that creates or references a file, but it does not become the file database.

Agents may use authorised file connectors when needed. Prefer exact file IDs/paths/version references over copying file contents into public GitHub surfaces.

## Safe integration

```text
business task
→ Skill
→ approved private-file owner
→ narrow authorised read/write
→ verify exact file/path/version
→ record safe durable reference where useful
```

Do not put confidential file content into Issues, PRs, logs, prompts or public examples merely because an agent needs temporary context.

## Access and recovery

- permissions remain governed by the file platform;
- public ARC never carries private-file credentials or content backups;
- the target business defines retention, backup and recovery in the file owner;
- estate manifests may name the provider/owner and recovery dependency only;
- a shared/public link is itself an access decision and must be created only when authorised.

See [Integration Classes](../../integrations/README.md) and [Security and Governance Baseline](../../contracts/governance.md).
