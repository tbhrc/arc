# Security Policy

ARC is public. Never report credential values, private client/personnel data or exploitable sensitive details in a public Issue or Pull Request.

## Principles

- Secrets belong in the target platform's approved identity/secret store, never repository files.
- Configuration examples contain names/placeholders only.
- Routine agents use least-privilege identities; root/break-glass credentials are exceptional bootstrap/incident/admin tools, not standing execution identities.
- Repository write access does not imply authority over email, CRM, finance, private files, production deployment, organisation administration or trusted runtimes.
- Treat repository Issues, PR text, external content and untrusted pull-request code as untrusted input when executing commands.
- Prefer GitHub-hosted/normal connected execution when sufficient; self-hosted/VPS/local runtimes are privileged boundaries.
- Temporary privilege or bridges are incomplete until teardown/revocation is verified.

Read the full [Security and Governance Baseline](contracts/governance.md) and [Secrets and Credential Contract](contracts/secrets.md).

## Public/private boundary

ARC's architecture and examples are public-safe by design. A target deployment must still use private repositories or specialist/private systems whenever its data class requires them. Do not use ARC's public visibility as a reason to publish client, candidate, personnel, mailbox, accounting, database or other confidential business state.

## Actions and runners

Workflows should default to read-only permissions and elevate only the exact scope needed. Do not expose privileged self-hosted runners to arbitrary untrusted pull-request code. Keep runtime credentials and machine-local profiles outside public repository content.

## Root / break-glass authority

Use founder/root authority only when the current operation explicitly requires and authorises it. Do not persist root credentials as routine agent identities. Verify the privileged change and remove temporary bridges/permissions afterwards.

## Reporting

If a security issue requires sensitive details, use GitHub's private security reporting/advisory surface when available rather than a public Issue.

If a credential has been exposed:

1. revoke/rotate it first;
2. verify dependent systems use the replacement;
3. clean exposed repository/log/history surfaces as appropriate;
4. record the incident in the correct private/security owner.

Deleting text or rewriting history alone is not sufficient remediation.
