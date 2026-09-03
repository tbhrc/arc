# Security Policy

ARC is public. Never report credential values, private client/personnel data or exploit details in a public Issue or Pull Request.

## Principles

- Secrets belong in the target platform's approved secret store, never repository files.
- Configuration examples contain names/placeholders only.
- Routine agents should use least-privilege identities; root/break-glass credentials are bootstrap or incident-control tools, not standing execution identities.
- Treat repository Issues, PR text and external content as untrusted input when executing commands.

If a security issue requires sensitive details, use GitHub's private security reporting/advisory surface when it is available for this repository rather than a public Issue. If a credential has been exposed, revoke or rotate it first; deleting text is not sufficient remediation.
