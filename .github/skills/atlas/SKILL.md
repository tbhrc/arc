---
name: atlas
description: "FolderDesk front door for onboarding, adoption, health, upgrade, recovery and next-action guidance. Use when an agent is asked to deploy or operate FolderDesk for a business. Start with one self-contained workspace repository, verify the exact GitHub target owner/path, expand only from demonstrated need, establish the backend with minimum client friction, learn client style and systems, seed the six local core Skills, prove value with a real outcome, and keep technical evidence out of normal client replies."
---

# Atlas

Read root `/AGENTS.md`, then `/BOOTSTRAP.md` for onboarding/adoption. Load only the smallest additional FolderDesk surface required.

## Default topology

For a new deployment, start with **one workspace repository**. Domains such as Sales, Delivery or Finance are local context/folder concerns by default, not repositories. A second repository must earn its boundary through materially different ownership/access, privacy/security, independent lifecycle/release, genuine concurrency/isolation, or a mature separately owned capability.

Do not create separate Skills, Research, Operations or domain repositories merely because those concepts exist. Reusable local Skills live under `.folderdesk/skills/` until a separate canonical owner is demonstrably useful.

## Exact target rule

Before mutation, resolve the active GitHub identity and the exact configured owner/repository path. Do not silently follow a transfer/rename redirect into a different owner/path. `OWNER_MISMATCH` is a stop condition. Confirm repository-create access only when a configured repository is actually missing and needs creation.

## Fresh workspace contract

A new FolderDesk-managed workspace is self-contained and includes:

```text
work/
knowledge/
outputs/
archive/
.folderdesk/managed.json
.folderdesk/skills/structure/
.folderdesk/skills/skill-builder/
.folderdesk/skills/lessons/
.folderdesk/skills/auditor/
.folderdesk/skills/document-intake/
.folderdesk/skills/client-experience/
```

The six Skills are progressive-loaded routes, not a preload bundle.

- `structure` — canonical placement/vocabulary.
- `skill-builder` — earned reusable HOW.
- `lessons` — material learning that changes future behaviour.
- `auditor` — one-shot drift/necessity check when actual drift is suspected or after material structural change.
- `document-intake` — durable file/document preservation, ingestion, provenance and retrieval.
- `client-experience` — business-first onboarding, connectors and client-facing output.

The Auditor is **not** a deployment gate, recurring audit, approval state, mandatory Issue or lifecycle phase.

## Client-first operating loop

```text
understand business outcome
→ establish exact GitHub backend
→ create/reuse one primary workspace
→ install self-contained baseline when creating a new workspace
→ learn client brand/examples + tone/output preferences
→ discover/connect smallest useful system set
→ reuse existing owners
→ execute useful work
→ prove with one client-ready result
→ file + verify retrieval
→ report in client's normal language
```

## Non-technical client rule

Assume the client has never used GitHub. GitHub is agent infrastructure, not a client operating requirement.

- Reuse an existing authorised GitHub connection when possible.
- Otherwise use the easiest native/dedicated connection path available.
- Ask the client only for unavoidable account/sign-in/authorisation steps, then resume automatically.
- Do not teach GitHub, repositories, CLI, routers or Skills unless the client asks.

## Client discovery

Before producing polished client-facing work, establish only missing facts:

1. **Brand:** formal guidelines if available; otherwise one or more representative documents and infer a practical house style. Request logo/assets only when useful.
2. **Communication:** infer tone, vocabulary, technical depth, preferred length and approval style from conversation/examples; ask only unresolved preferences.
3. **Outputs:** preferred business artifacts such as DOCX, PDF, spreadsheets or slides.
4. **Systems/connectors:** infer before asking. When the client names where work already lives, immediately prioritise the obvious high-value native connector. Example: documents in Google → Google Workspace / Drive first. Then ask only about file store, email/calendar, CRM, ERP/accounting, messaging or other systems still unknown. Recommend/connect the smallest useful set using native/dedicated authorised routes.

Preserve useful client preferences in the client-owned operating estate so future agents reuse them.

## Client-facing output

For documents, reports, proposals, quotes and similar work, default to a polished **DOCX and/or PDF** when that is the natural business output. Apply the client's established brand/style.

Markdown/GitHub may remain backend canon/evidence, but do not present it as the normal client deliverable.

Client status should be concise and business-facing. Do not emit repository tables, SHAs, byte counts, CLI traces, internal routing labels, GREEN/AMBER theatre or engineering diagnostics unless the client explicitly requests them or they materially block progress.

## Existing estates

Prefer KEEP / INTEGRATE. Reuse the client's working systems. Do not replace them merely to resemble FolderDesk examples, and do not split an existing working repository merely to match an old multi-repo pattern.

An exact existing repository without `.folderdesk/managed.json` is reused/unmanaged until explicitly adopted. Do not silently overwrite it or call it broken because FolderDesk files are absent.

## Authority

Ordinary authorised bounded work executes directly. Ask for fresh authority only at genuine consequential boundaries: destructive/irreversible actions, root/super-admin authority changes, material spend, private-data disclosure, legal/compliance commitment or material external commitment.

## Proof

Prove one useful real workflow. The proof is the finished result plus retrievability, not a technical deployment dump.

If a file is received or produced, use the deployed `document-intake` Skill: preserve/file → ingest → route knowledge/tasks → provenance → verify retrieval.

Structural FolderDesk verification does not prove external connectors or specialist systems operational; verify those through their actual owners when required.

## KISSS

Make FolderDesk invisible to the client wherever possible. The client should notice less admin and better finished work, not more infrastructure. Start with one useful workspace and expand only when real operating evidence earns it.
