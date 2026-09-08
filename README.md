# FolderDesk by iMPLEMENTAi — Your Business AI Operating System

FolderDesk is a **task-management, filing and organisational-memory system for humans and AI agents**. It helps your AI keep work organised, file what you give it, remember what matters, find it again later, and produce finished business work instead of leaving you with disconnected chats and admin chaos.

**You do not need GitHub experience to use FolderDesk.** GitHub is the durable backend your agent uses to keep the operating system organised.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [Get Started](BOOTSTRAP.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Releases](RELEASES.md) · [Agent Router](AGENTS.md)

## Start here — Give this to your agent

Copy this into the AI agent you want to use:

```text
Set up FolderDesk for my business from https://github.com/tbhrc/folderdesk.

Assume I have never used GitHub and do not want to operate it myself. Establish the required GitHub backend using the lowest-friction supported route. Handle the technical work yourself and ask me only when I must sign in, create/confirm an account, approve access, or make a real business decision. Do not teach me GitHub unless I ask.

Before producing client-facing work, learn how my business should look and sound. Ask me for brand guidelines if I have them; otherwise ask for one or more representative documents and infer a practical house style. Ask for a logo/assets only when useful.

Use clues I already give you before asking broad connector questions. If I say where my files, email, CRM, ERP/accounting or other work lives, immediately infer the obvious high-value native connector and recommend connecting it. For example, if I say my documents are in Google, prioritise Google Workspace / Google Drive so you can use my authorised existing documents for filing, retrieval, brand/style learning and business context instead of asking me to upload or explain everything manually. Then ask only for the remaining systems you cannot infer. Recommend the smallest useful connector set and connect what I approve using the easiest native/dedicated route available.

Learn my normal communication style and output expectations from our conversation and examples. Adapt your tone, level of detail, terminology and preferred formats to me. Keep these preferences durable so I do not have to repeat them.

For normal business documents, reports, proposals, quotes and similar deliverables, give me a polished Word document and/or PDF when that is the natural output. Apply my brand/style when available. Markdown and GitHub may be used behind the scenes but are not my default deliverables.

Keep setup updates short and human. Tell me what you are setting up, whether you need anything from me, what is ready, and what I can do next. Do not dump repository lists, CLI commands, SHAs, router names or engineering diagnostics into normal replies unless I ask or they materially block me.

If I give you a file, file/preserve the source, ingest useful content, route durable knowledge/tasks with provenance, and verify it can be found again later.

Prove the setup with one useful real business workflow and return the finished client-ready artifact, not just backend evidence.
```

That is the normal FolderDesk front door.

## What FolderDesk should feel like

You should be able to work with your agent in normal business language:

- “Prepare this proposal in our normal style.”
- “File this supplier agreement and remind me what I committed to.”
- “Find the quote we sent last month and update it.”
- “Turn these notes into a polished client report.”
- “What am I still waiting on?”

The agent handles the filing, task continuity, retrieval and backend structure.

## What you get

- a durable task-management layer so work survives chats, sessions and agents;
- default document intake: file the source, ingest useful content, preserve provenance and retrieve it later;
- organisational memory tied back to real source documents and owner systems;
- reusable Skills so your agent learns repeatable ways of working;
- brand/style learning from formal guidelines **or your existing documents**;
- client-tone adaptation from your real communication and examples;
- proactive connector inference from what you already tell the agent — e.g. documents in Google → prioritise Google Workspace / Drive instead of making you spoon-feed context;
- polished client-facing Word/PDF outputs when documents are the natural deliverable;
- a technical backend that stays available to agents/operators without becoming client-facing noise;
- an architecture that can grow toward the full **[Ultimate Features](FEATURES.md)** catalogue.

## Give FolderDesk a file

When you give your agent a document, the default is not “read it once and forget it”:

```text
receive file
→ file/preserve original in the correct private-file owner
→ identify + ingest useful content
→ route facts, decisions and tasks to the correct durable owner
→ preserve provenance back to the source
→ verify the document and useful knowledge can be found again
```

Inventory/checkpoint metadata alone does not count as ingestion.

## For agents and operators

The client does not need to operate GitHub, but FolderDesk uses it as the durable backend for repositories, Skills, work identity, decisions and agent handoffs.

If GitHub is not available yet, the agent should establish it immediately using the lowest-friction supported route. Prefer an existing authenticated GitHub connection. Otherwise guide only the unavoidable sign-in/account/authorisation step, then resume setup without turning GitHub into a training exercise.

Technical CLI path, when useful:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json --connectors
python3 scripts/arc.py plan --config arc.json --inspect-target
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

During bootstrap FolderDesk reports repository progress, elapsed time and estimated remaining time so the **agent/operator** is not left with a silent run. Normal client updates should translate that evidence into concise business language.

## Client experience profile

During onboarding, the agent should learn and durably preserve the minimum useful client experience profile in the client-owned operating estate:

- brand source: formal guidelines or representative example documents;
- logo/assets where relevant;
- preferred output types (for example DOCX, PDF, spreadsheet, slides);
- tone, terminology, level of detail and communication preferences;
- important existing systems and the connections chosen for FolderDesk;
- filing location/owner conventions.

Reuse this profile. Do not repeatedly ask the client for facts already established.

## Safe Harbour

FolderDesk can export a non-secret architecture map for recovery. Private files, specialist-system records, credentials, runtime state and memory contents remain with their proper owners.

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

## KISSS

> **The operating system must not become the work.**

The client should experience better work, better filing, better recall and less admin — not more infrastructure.
