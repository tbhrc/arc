# FolderDesk by iMPLEMENTAi — Your Business AI Operating System

FolderDesk gives your business a **GitHub-first task-management, filing and organisational-memory system for humans and AI agents**. It turns capable AI tools into an organised operating environment that can track work, file what you give it, preserve useful knowledge and find it again later — reducing the admin chaos of disconnected chats, loose documents and forgotten follow-ups.

You keep your own business data, accounts and credentials with their proper owners. FolderDesk supplies the portable operating structure that connects the work.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [Get Started](BOOTSTRAP.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Releases](RELEASES.md) · [Agent Router](AGENTS.md)

## What you get

- a persistent GitHub operating desk and task-management layer for human + AI work;
- a default document-intake route that files source documents, ingests useful content and makes both the source and derived knowledge retrievable later;
- reusable Skills instead of repeatedly explaining the same process;
- clear owners for business truth, work and decisions;
- agent routing across repositories, tools and specialist systems;
- a clean way to add connectors, MCP, runtimes, memory and automations;
- deployment, verification and recovery without copying your private business data into FolderDesk;
- an architecture that can grow toward the full **[Ultimate Features](FEATURES.md)** catalogue as you connect the capabilities you need.

## Give FolderDesk a file

When you give your agent a document, the default is **not** "read it once and forget it." FolderDesk treats that as an intake event:

```text
receive file
→ file/preserve original in your declared private-file owner
→ identify + ingest useful content
→ route facts, decisions and tasks to the correct durable owner
→ preserve provenance back to the source
→ verify the document and useful knowledge can be found again
```

This is how FolderDesk becomes a filing machine and organisational memory rather than another chat window. It remembers **where the source lives and what durable work/knowledge came from it**. Inventory/checkpoint metadata alone does not count as ingestion.

## Step 1 — Connect GitHub

**GitHub is the first requirement.** FolderDesk uses GitHub as the durable operating desk where repositories, Skills, Issues, decisions and agent handoffs live.

Before bootstrap, make sure the human or AI agent doing the deployment can access the target GitHub organisation/account and is authenticated for the repository actions you want FolderDesk to perform.

With the CLI, the quick check is:

```bash
gh auth status
```

Then continue with [Get Started / Bootstrap](BOOTSTRAP.md).

## Give this to your agent

Copy and paste this into the AI agent you want to use for deployment:

```text
Open https://github.com/tbhrc/folderdesk and help me deploy FolderDesk into my GitHub organisation.
Read the root AGENTS.md first, then use the smallest relevant FolderDesk guidance.
First confirm that you can access and operate on my target GitHub organisation/account.
Then onboard and bootstrap FolderDesk, keeping me informed as each repository is checked, reused or created and showing the remaining-time estimate during bootstrap.
Do not copy TBHRC private business data or secrets. Use FolderDesk as the portable structure and create/adapt my organisation's own owners and Skills.
If I give you a file or document, treat it as a FolderDesk intake event: preserve/file the source, ingest useful content, route durable knowledge/tasks with provenance, and verify I can retrieve it later.
After deployment, show me verification status, connection readiness and the next useful capability to activate.
```

That is the intended front door. You do not need to understand the implementation files before asking a capable agent to operate FolderDesk for you.

## How deployment works

At a high level:

```text
connect GitHub
→ describe your organisation
→ FolderDesk plans the repository/owner structure
→ bootstrap streams progress as repositories are reused or created
→ seed the starter Skills
→ verify
→ connect the external tools/runtimes you want
→ start real work
```

FolderDesk reuses existing configured repositories unchanged and creates only missing configured repositories. It does not copy credentials, private files or specialist-system records into the public package.

### CLI path

Create your local deployment profile:

```bash
python3 scripts/arc.py onboard --output arc.json
```

Check GitHub and optional connector readiness:

```bash
python3 scripts/arc.py doctor --config arc.json --connectors
```

Inspect the target when useful:

```bash
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Bootstrap:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

During `bootstrap --apply`, FolderDesk reports the current repository, completed/total count, elapsed time and an estimated remaining time after the first repository check. It should not appear to go silent while GitHub work is happening.

## For agents and operators

FolderDesk also contains a compact machine-facing operating contract:

```text
request
→ root AGENTS.md Repository Router
→ smallest relevant Skill / owner
→ simplest authorised execution route
→ verify real state once
→ preserve material durable context when needed
→ stop
```

Fast Links are pointers, not preload instructions. Reusable HOW belongs in the organisation's canonical Skills repository; live mutable business truth remains with its real owner.

## Safe Harbour

FolderDesk can export a non-secret architecture map for recovery:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

When authorised, missing configured repositories can be reconstructed with:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

External owners recover their own files, records, credentials and runtime state through their own systems.

## What FolderDesk does not do

FolderDesk does **not** copy your editable live business truth, private files, specialist-system records, credentials, runtime machine state or memory contents into this public repository.

It also does not require a daemon, queue, control plane or approval ritual just to perform ordinary authorised work.

## KISSS

> **The operating system must not become the work.**

Prefer the direct route, existing Skill, existing owner or existing tool before adding more machinery.

**`main` keeps progress. KISSS keeps speed. Security protects real boundaries, not paperwork.**
