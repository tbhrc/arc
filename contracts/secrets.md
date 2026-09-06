# Secrets and Credential Contract

ARC never stores credential or secret values.

For each credential that is actually required, record only what helps operate or recover it:

```text
name / identifier
purpose
resource owner
consumer/runtime
purpose-fit authority required
correct secret store
scope required by the function
rotation/expiry owner when relevant
verification method
```

Use the existing authorised identity that can perform the intended function. Do not introduce a weaker credential, extra identity hop, artificial repository scope or credential hierarchy merely because it appears more restrictive.

Root/break-glass credentials remain exceptional because they cross a genuine high-authority boundary; use them only when the requested operation actually requires root/bootstrap/admin capability.

## Configuration and safe-harbour rule

Neither `arc.json` nor an ARC estate manifest may contain credential values. ARC rejects common secret-like field names and known credential-value patterns because public credential disclosure is a concrete risk.

A safe-harbour manifest may state that credential reprovisioning is required and identify the responsible owner/store **by name or purpose only**. Recovery obtains current credentials through the owning external identity/secret-management process; ARC does not restore them.

If a credential value is exposed publicly, revoke/rotate it. History cleanup alone does not restore confidentiality.
