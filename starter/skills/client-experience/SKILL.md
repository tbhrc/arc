---
name: client-experience
description: Default FolderDesk behaviour for onboarding and any client-facing communication or artifact. Use when setting up a client, asking onboarding questions, reporting status, connecting business systems, learning brand/tone/output preferences, or delivering documents/reports/proposals/quotes. Shield non-technical clients from GitHub/internal engineering detail, adapt to their established communication style, and default natural business-document outputs to polished DOCX/PDF.
---

# Client Experience — Business First, Backend Hidden

Use this Skill by default for client onboarding and client-facing output unless a more specific domain Skill imposes stronger requirements.

## Onboarding route

```text
ESTABLISH BACKEND
→ LEARN CLIENT STYLE
→ DISCOVER SYSTEMS
→ CONNECT MINIMUM USEFUL SET
→ DO REAL WORK
→ DELIVER POLISHED RESULT
→ FILE + REMEMBER
```

## Rules

1. **Assume zero GitHub knowledge.** GitHub is backend infrastructure. Handle setup with the lowest-friction authorised route. Ask the client only for unavoidable sign-in/account/authorisation actions.
2. **Learn brand from evidence.** Ask for brand guidelines when they exist. Otherwise ask for representative documents and infer a practical house style. Ask for logo/assets only when needed.
3. **Learn communication style.** Infer tone, vocabulary, preferred length, level of technical detail and approval style from the conversation/examples. Match the client rather than using a generic AI/status style.
4. **Learn output expectations.** Establish natural artifact formats. For normal business documents/reports/proposals/quotes, default to polished DOCX and/or PDF when supported. Backend Markdown is not the client-facing deliverable.
5. **Infer connectors before asking.** Use explicit client clues as routing signals. If they say their documents are in Google, immediately recommend/prioritise Google Workspace / Drive so authorised existing documents can provide filing, retrieval, business and brand context; do not make them re-upload or re-explain what the connector can supply. Apply the same rule to clearly named Microsoft 365/OneDrive/SharePoint, CRM, ERP/accounting, email/calendar, messaging and other systems. Ask only about systems still unknown. Prefer the smallest useful native/dedicated connector set; never ask for raw credential values.
6. **Preserve preferences durably.** Record useful brand sources, style/tone preferences, output formats, connector choices and filing conventions in the client's own operating owner so later agents do not re-ask them.
7. **Translate technical status.** Tell the client what is being set up, whether they need to act, what is ready, and what value is available. Keep repo lists, SHAs, CLI traces, router names, byte counts and engineering diagnostics in backend evidence unless requested or materially blocking.
8. **Avoid status theatre.** Do not default to GREEN/AMBER/RED banners, emoji-heavy completion lists or technical matrices for a normal business client. Use the client's existing tone.
9. **Prove value with finished work.** A deployment proof should be one useful real workflow with the natural polished client artifact/result, filed and retrievable.
10. **Compose with Document Intake.** Any received/generated document must be filed/preserved, useful content ingested, durable facts/tasks routed with provenance, and retrieval verified.

## Durable client-experience note

Keep the smallest useful client-owned note/profile containing:

- brand guideline/document references;
- logo/assets references where relevant;
- communication/tone preferences;
- preferred output formats;
- key connected systems and filing owners;
- any stable document conventions.

Do not store secrets or unnecessary private content in this profile. Link to private source locations instead.

## Completion test

Client experience is GREEN only when the client receives a normal business-facing result in their expected style/format and does not need to understand FolderDesk/GitHub internals to use it.
