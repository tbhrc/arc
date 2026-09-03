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
provisioning owner/method
rotation/expiry trigger
revocation path
verification method
```

## Preferred identity order

```text
native connected/runtime identity
→ short-lived OIDC / GitHub App / OAuth identity
→ purpose-scoped service credential
→ trusted-runtime credential only when the capability genuinely lives there
→ root / break-glass only for explicitly approved current bootstrap/admin work
```

Root credentials must not become routine agent identities.

## Lifecycle

```text
NEED
→ prove native identity is insufficient
→ PROVISION minimum scope in the correct external store
→ CONNECT by reference/name, never copy value into ARC
→ VERIFY bounded capability
→ OPERATE
→ ROTATE when policy/risk/expiry requires
→ REVOKE when no longer needed
→ VERIFY dependent routes no longer rely on stale privilege
```

Temporary privilege or a secret-transfer bridge is incomplete until teardown/revocation is verified.

## Secret naming and configuration

Stable non-sensitive values such as host names, repository names, ports, paths and service identifiers should be normal versioned configuration when safe. Do not turn ordinary configuration into secrets merely because a workflow needs it.

Secret names should communicate purpose without exposing the value, for example:

```text
CRM_SERVICE_TOKEN
ACCOUNTING_API_TOKEN
DEPLOYMENT_SIGNING_KEY
```

Examples in public ARC must use placeholders only. Never place a real-looking token/private-key body in example configuration.

## Configuration and safe-harbour rule

Neither `arc.json` nor an ARC estate manifest may contain credential values. ARC rejects common secret-like field names and known credential-value patterns as a defensive check, but that heuristic is not a substitute for correct secret-store discipline.

A safe-harbour manifest may state that credential reprovisioning is required and identify the responsible owner/store **by name or purpose only**. Recovery obtains fresh/current credentials through the approved external identity/secret-management process; it does not restore them from ARC.

## Exposure response

If a credential value reaches a public repository, Issue, PR, log, artifact, prompt or other exposed surface:

1. treat it as compromised;
2. revoke/rotate it through the owning provider;
3. verify dependent systems use the replacement;
4. clean exposed repository/history/log surfaces where appropriate;
5. record the incident/lesson in the correct private/security owner.

Deleting the visible text or rewriting history alone does **not** restore confidentiality.

See [Security and Governance Baseline](governance.md) for repository, Actions, runner and break-glass boundaries.
