# Security Policy

FolderDesk is public. Never report credential values, private client/personnel data or exploit details in a public Issue or Pull Request.

## Principles

- Secrets belong in the target platform's approved secret store, never repository files.
- Configuration examples contain names/placeholders only.
- Runtime identities must have **purpose-fit authority sufficient for their intended function**. Do not narrow an organisation-wide or cross-repository capability below the scope it actually needs merely to satisfy generic “least privilege” doctrine.
- Root/break-glass credentials are reserved for genuine root/bootstrap/incident-control boundaries rather than routine work when a normal authorised identity can perform the same function.
- Treat genuinely untrusted repository Issues, PR text and external content as untrusted input when executing commands.
- Use the least restrictive effective guardrail; every added restriction must protect a concrete current boundary.

If a security issue requires sensitive details, use GitHub's private security reporting/advisory surface when it is available for this repository rather than a public Issue. If a credential has been exposed, revoke or rotate it first; deleting text is not sufficient remediation.
