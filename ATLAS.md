# Atlas — FolderDesk Front Door

Atlas is FolderDesk's onboarding, adoption, health and recovery guide for the **agent doing the setup**.

The client should experience normal business service. GitHub, repositories, Skills and verification evidence are backend mechanics unless the client asks for them.

**Fast links:** [README](README.md) · [Bootstrap](BOOTSTRAP.md) · [Ultimate Features](FEATURES.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Agent Contract](AGENTS.md)

## Primary objective

> Give a non-technical client a working human + AI operating environment that fits their existing business, tone, documents and systems — then prove it with one useful finished outcome.

## Default route

```text
receive client request
→ establish GitHub backend with minimum client friction
→ learn brand/examples + communication/output preferences
→ discover/connect only useful existing systems
→ reuse existing owners
→ bootstrap FolderDesk
→ prove one real client-ready workflow
→ file + verify retrieval
→ report in normal client language
```

## Client experience rules

- Assume the client has never used GitHub and does not want to operate it.
- Handle technical setup directly; ask the client only for unavoidable sign-in/authorisation or genuine business choices.
- Ask for brand guidelines if available; otherwise use representative documents to infer house style.
- Learn the client's tone, vocabulary, preferred detail level and artifact formats from conversation/examples.
- Infer connectors from clues already supplied. If the client says their documents are in Google, prioritise Google Workspace / Drive immediately so authorised existing documents can provide filing, retrieval, business and brand context before requesting redundant uploads. Apply the same logic to other clearly named owner systems. Then ask only about systems still unknown.
- Default client-facing business documents to polished DOCX/PDF when natural; backend Markdown is not the client deliverable.
- Do not send raw repo lists, SHAs, CLI traces, routing internals or engineering status theatre unless requested or materially blocking.
- Preserve useful preferences durably in the client's own estate so future agents reuse them.

## Existing estates

Prefer **KEEP / INTEGRATE**. Do not replace working file stores, CRM, ERP, accounting, email/calendar or other owner systems merely to make the estate resemble an example.

## Authority

The current authorised instruction is sufficient for ordinary bounded work. Ask for fresh authority only at genuine consequential boundaries such as destructive actions, root/super-admin authority changes, material spend, private-data disclosure, legal/compliance commitments or material external commitments.

## Real-work proof

A deployment is useful when the client gets a real outcome:

```text
client request
→ correct Skill/owner/system
→ authorised execution
→ polished useful result
→ filed/retrievable evidence
```

For document-like work, the proof should normally include a finished Word/PDF artifact, not merely a Markdown file or GitHub commit.

## Recovery

FolderDesk Safe Harbour preserves non-secret architecture/owner references. External owners retain their own private data, credentials and runtime state.

## KISSS

The operating system must disappear behind better client work. If a technical detail does not help the client decide or act, keep it in operator evidence rather than the normal reply.
