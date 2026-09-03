# Secrets and Credential Contract

ARC never stores secret values.

For each required credential, document only:

```text
name
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

If a secret value is exposed publicly, revoke/rotate it. History cleanup alone does not restore confidentiality.
