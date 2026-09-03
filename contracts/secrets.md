# Secrets and Credential Contract

ARC never stores credential or secret values.

For each required credential, document only:

```text
name / identifier
purpose
resource owner
consumer/runtime
minimum permissions
correct secret store
repository/environment scope
rotation/expiry owner
verification method
```

Preferred order:

```text
native runtime identity
-> short-lived/OIDC/GitHub App identity
-> purpose-scoped credential
-> root/break-glass only for explicitly approved bootstrap/admin work
```

Root credentials must not become routine agent identities.

## Configuration and safe-harbour rule

Neither `arc.json` nor an ARC estate manifest may contain credential values. ARC rejects common secret-like field names and known credential-value patterns as a defensive check, but that heuristic is not a substitute for correct secret-store discipline.

A safe-harbour manifest may state that credential reprovisioning is required and identify the responsible owner/store **by name or purpose only**. Recovery obtains fresh/current credentials through the approved external identity/secret-management process; it does not restore them from ARC.

If a credential value is exposed publicly, revoke/rotate it. History cleanup alone does not restore confidentiality.
