# Bootstrap FolderDesk

FolderDesk bootstrap is **agent-led for a non-technical business client**. The client should not need to know or operate GitHub. The default deployment is one private workspace repository with normal human work in `work/`, `knowledge/`, `outputs/` and `archive/`, and agent support under `.folderdesk/`.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [README](README.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Agent Router](AGENTS.md)

## 0. Client handoff

The normal handoff is exactly the two-line prompt in [README](README.md#start-here--give-this-to-your-ai-agent): repository URL, then `fork this repository and run BOOTSTRAP.md`.

Use the existing authorised GitHub identity to fork FolderDesk into the client's/target operator's authorised organisation or account, then continue this bootstrap from that fork. The FolderDesk fork is the deployment/reference copy; normal client business data still belongs in the private workspace repository created or reused by the steps below. Do not put client business data into a public FolderDesk fork.

If the current GitHub account is not connected, ask only for the normal sign-in/authorisation action. If GitHub or organisation policy prevents the fork, report that exact blocker instead of silently inventing a different deployment path. Do not begin by teaching the client GitHub architecture or pasting this whole bootstrap into chat.

## 1. Establish the exact GitHub backend

Reuse an existing authorised GitHub connection where possible. Otherwise ask only for the unavoidable sign-in/authorisation action, then resume setup immediately.

```bash
gh auth status
```

Before mutation, resolve the active GitHub identity and exact configured owner/path. A GitHub rename/transfer redirect is **not** permission to silently deploy somewhere else. FolderDesk refuses an owner/path mismatch. If a repository must be created, confirm the active identity can create repositories in the configured target owner.

## 2. Learn the client experience

Ask only what is not already evident.

### Brand and visual style

- Ask for formal brand guidelines if they exist.
- Otherwise use representative documents such as proposals, reports, invoices, presentations or letterhead to infer a practical house style.
- Ask for logos/assets only when the expected output needs them.

### Communication and output preferences

Infer first, then ask only what remains unclear: tone, vocabulary, concise vs detailed, technical vs business language, approval style and preferred artifact formats.

## 3. Infer, then connect, wherever the client's data already lives

Do not start with a generic app questionnaire when the client already supplied a clue. Treat the named location as a routing signal and connect the existing owner system before asking the client to manually reproduce that context.

Examples:

```text
"our documents are in Google"
→ Google Workspace / Google Drive

"everything is in Microsoft / SharePoint / OneDrive"
→ Microsoft 365 / SharePoint / OneDrive

"sales is in HubSpot / Salesforce"
→ the matching CRM connector

"finance is in Zoho Books / Xero / QuickBooks"
→ the matching accounting connector
```

Prefer the smallest useful connector set for real work now. Keep each external system authoritative for its own live records.

## 4. Create the FolderDesk profile

The default is **one repository**. Domains such as Sales, Delivery or Finance are in-repository context/folder concerns, not separate repositories.

```bash
python3 scripts/folderdesk.py onboard --output folderdesk.json
```

Non-interactive example:

```bash
python3 scripts/folderdesk.py onboard \
  --non-interactive \
  --business-name "Example Business" \
  --owner example-org \
  --domains "sales,delivery" \
  --output folderdesk.json
```

The primary repository name defaults to a slug of the business name. Use `--repository` only when a different name is useful.

### Expansion rule

Do **not** create separate Skills, Research, Operations or domain repositories during normal bootstrap. Add another `repositories[]` entry only when a concrete ownership, security, scale, concurrency, lifecycle or independent-review boundary earns separation.

## 5. Inspect readiness when useful

```bash
python3 scripts/folderdesk.py doctor --config folderdesk.json --connectors
python3 scripts/folderdesk.py plan --config folderdesk.json --inspect-target
```

These are operator tools, not approval rituals. `plan --inspect-target` distinguishes exact-path `REUSE`, missing `CREATE`, and an unsafe `OWNER_MISMATCH`.

## 6. Bootstrap the self-contained workspace

```bash
python3 scripts/folderdesk.py bootstrap --config folderdesk.json --apply
```

A **new** workspace receives in the same bootstrap:

- `README.md` and a compact root `AGENTS.md` Router;
- `work/`, `knowledge/`, `outputs/`, `archive/`;
- `.folderdesk/README.md` plus a FolderDesk-managed marker;
- a local Atlas pointer;
- six local foundational Skills under `.folderdesk/skills/`:
  - `structure` — canonical workspace vocabulary and placement;
  - `skill-builder` — create/update the smallest earned reusable capability;
  - `lessons` — convert material real-work learning into behaviour change;
  - `auditor` — one-shot drift/necessity check without audit ceremony;
  - `document-intake` — preserve, ingest, route and retrieve documents;
  - `client-experience` — business-first onboarding and client-facing output.

The CLI leaves an existing configured repository unchanged. It does not claim an existing repository as FolderDesk-managed merely because the name exists.

### Add or import another Skill

For a deployed FolderDesk workspace, `.folderdesk/skills/` is the editable local Skill source. To add a Skill, place the complete Skill directory there, then refresh every supported local agent discovery surface from that one source:

```bash
# example
cp -R /path/to/uae-corporate-tax .folderdesk/skills/uae-corporate-tax
python3 scripts/sync_agent_skills.py
```

The adapter symlinks Skills into `.claude/skills/` and `.codex/skills/`, and writes `.agents/skills.json` for Antigravity. These are derived adapters, not editable Skill canon. Re-run the adapter after adding, renaming or removing a Skill.

## 7. Adopt or repair an existing workspace when needed

For a reused existing repository, inspect it first. Seed the six foundational Skills only when the client wants that repository adopted into FolderDesk and the mutation is authorised:

```bash
python3 scripts/seed_foundation.py --config folderdesk.json --apply
```

The seeder creates only missing Skill files and never overwrites existing target Skill files. Adoption of other FolderDesk router/support files should likewise be explicit and bounded rather than silently rewriting an existing repository.

## 8. Prove value with a real outcome

Do not use “a Markdown file exists in GitHub” as the client proof when the natural output is a business artifact. Deliver the useful result. For proposal/report/quote-style work, default to a **polished DOCX and/or PDF** using the client's brand/style when available.

Use the local Skills progressively:

```text
placement/naming → Structure
repeatable HOW → Skill Builder
material lesson → Lessons
suspected drift or unnecessary machinery → Auditor once
file/document → Document Intake
client-facing work → Client Experience
```

The Auditor is not a deployment gate, recurring job, Issue requirement or approval state. Use it after a material structural change or when actual drift/over-engineering is suspected.

## 9. File and remember the result

For document workflows:

```text
file source/output
→ ingest useful content
→ route durable facts/tasks
→ preserve provenance
→ verify retrieval
```

The client should be able to ask for the document or its meaning later in normal language.

## 10. Client-facing completion

Normal completion answers only:

1. What is ready?
2. What useful systems are connected?
3. What finished result was produced?
4. Is there anything the client must do now?
5. What can FolderDesk do next?

Keep backend GitHub evidence behind the scenes unless requested.

## 11. Verify / Safe Harbour

```bash
python3 scripts/folderdesk.py verify --config folderdesk.json
python3 scripts/folderdesk.py export --config folderdesk.json --output folderdesk-estate.json --inspect-target
```

FolderDesk verification proves the **FolderDesk structural contract**. External connectors, runtimes and specialist business systems are operational only when separately verified through their actual owners.

Use [VERIFY.md](VERIFY.md) for acceptance and [MANIFEST.md](MANIFEST.md) for recovery.

## KISSS

Start with one useful workspace. Expand only from demonstrated need. The operating system must not become the work.
