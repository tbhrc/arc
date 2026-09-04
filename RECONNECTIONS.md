# External-System Reconnections

ARC does not copy live external-system data. A redeployed estate needs only enough durable information to reconnect each required owner safely.

For each external system needed by a real workflow, record the smallest useful handoff:

```text
System / provider:
Live owner:
Connection / identity reference:   # name or reference only; never a secret value
Required authority / scope:
Verification:
```

Add `Recovery / revocation owner:` only when it is materially useful.

## Example

```text
System / provider: Example CRM
Live owner: Sales Operations
Connection / identity reference: organisation CRM connector
Required authority / scope: read and update deals used by the workflow
Verification: read one known deal and confirm one authorised test update
```

## Rules

- Never store passwords, tokens, keys or private data here.
- The external system remains authoritative for its live records.
- Legacy name-only system lists are acceptable; enrich only the systems actually needed for deployment or recovery.
- Do not create a schema migration merely to satisfy ARC.
- A capable operator/agent should be able to use this handoff plus the external owner's approved identity/recovery process to reconnect the system.

For a deployed estate, keep the organisation-specific copy of this handoff in its operating owner repository so normal repository backup/history preserves the non-secret reconnection references.
