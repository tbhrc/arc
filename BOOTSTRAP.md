# Bootstrap FolderDesk

FolderDesk bootstrap is **agent-led for a non-technical business client**. The client should not need to know or operate GitHub. GitHub is required backend infrastructure; the agent establishes it with the lowest-friction supported route and exposes only unavoidable sign-in/authorisation steps to the client.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [README](README.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Agent Router](AGENTS.md)

## 0. Client handoff

The normal client starts by giving the FolderDesk link to a capable agent. Use the copy/paste instruction in [README](README.md#start-here--give-this-to-your-agent).

Do not begin by teaching the client GitHub, repository architecture or CLI commands.

## 1. Agent establishes GitHub backend

FolderDesk needs a GitHub owner/home, but **this is the agent's setup responsibility**.

Lowest-friction order:

1. reuse an existing authorised GitHub connection/session if available;
2. if GitHub is not connected, use the current platform's native/dedicated GitHub connection path where available;
3. otherwise guide the client through only the unavoidable account/sign-in/authorisation step;
4. immediately resume setup after connection.

Do not ask the client to learn repositories, branches, `gh`, `AGENTS.md` or GitHub administration unless they explicitly want to.

Operator/CLI check when relevant:

```bash
gh auth status
```

## 2. Learn the client experience before producing work

Ask only what is not already evident.

### Brand and visual style

- Ask for formal brand guidelines **if they exist**.
- If they do not, ask for one or more representative documents (proposal, quote, report, letterhead, brochure, invoice, presentation, etc.) and infer a practical house style from them.
- Ask for logo/assets only when needed for the expected output.
- Preserve the source/reference so future agents can apply the same style.

### Communication and output preferences

Infer from the conversation and examples first, then ask only what remains unclear:

- tone and vocabulary;
- concise vs detailed;
- technical vs business language;
- normal approval/review style;
- preferred artifact formats (DOCX, PDF, spreadsheet, slides, etc.).

Record the useful preferences durably in the client-owned operating estate so they are reused instead of repeatedly re-asked.

## 3. Infer, then connect, the systems the client already uses

**Do not start with a generic app questionnaire when the client has already supplied a clue.** Convert explicit business context into the obvious connector recommendation immediately.

Canonical example:

```text
client: "our documents are in Google"
→ infer Google Workspace / Google Drive
→ explain that connecting it lets FolderDesk inspect authorised existing documents, learn business/brand context, file and retrieve work, and avoid redundant manual uploads
→ connect/authorise it using the lowest-friction native/dedicated route available
→ inventory/ingest only the relevant authorised scope
→ ask only about remaining systems that are still unknown
```

Apply the same principle to Microsoft 365/OneDrive/SharePoint, email/calendar, CRM, ERP/accounting, messaging and other named systems.

Only after using existing clues, ask what still owns:

- files/documents;
- email and calendar;
- CRM/sales;
- ERP/accounting;
- messaging/collaboration;
- other business-critical systems.

Recommend the **smallest useful connector set for real work now**, prioritising connectors that unlock the most existing context with the least client effort. Prefer native/dedicated authorised connectors. Reuse existing systems rather than replacing them. If a named source can supply documents/context directly once authorised, connect it before asking the client to manually reproduce that context.

Do not ask for credential values in chat or store them in FolderDesk. Ask only for necessary sign-in/authorisation actions.

## 4. Create the deployment profile

Use Atlas or:

```bash
python3 scripts/arc.py onboard --output arc.json
```

A capable agent that already knows the required facts can use `onboard --non-interactive`.

Only resolve deployment facts actually needed: GitHub owner, repository visibility, domain owners, Skills home, private-file owner, specialist-system owners and runtime route where relevant.

## 5. Inspect readiness when useful

```bash
python3 scripts/arc.py doctor --config arc.json --connectors
python3 scripts/arc.py plan --config arc.json --inspect-target
```

These are operator tools. Do not dump their raw output into normal client replies. Translate material results into plain language.

## 6. Bootstrap with streamed operator progress

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

The CLI reports configured repository progress, elapsed time and estimated remaining time. The agent should convert this into compact client updates such as:

```text
I’m setting up the workspace now. No action needed from you.
Core workspace is ready. I’m connecting your file/email systems next.
```

Do not send repository matrices, SHAs, CLI traces or router diagnostics unless requested or materially blocking.

## 7. Seed starter Skills

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

A blank deployment receives public-safe starter Skills including:

- owner routing;
- GitHub workflow;
- Skill authoring;
- research escalation;
- document intake;
- **client experience** — tone, brand/examples, connectors, polished artifacts and client-safe communication.

Existing target Skill files are never overwritten automatically.

## 8. Prove value with a real client-ready outcome

Do not use “a Markdown file exists in GitHub” as the normal client proof when the natural output is a business document.

Choose one useful real workflow and return its finished client-facing artifact. For document/report/proposal/quote style work, default to a **polished DOCX and/or PDF**, using the client's brand/style when available.

Backend GitHub/Markdown evidence may be preserved for agents/operators, but it is not the default client deliverable.

## 9. File and remember the result

If the workflow consumes or produces documents:

```text
file source/output
→ ingest useful content
→ route durable facts/tasks
→ preserve provenance
→ verify retrieval
```

The client should be able to ask for the document or its meaning later in normal language.

## 10. Client-facing completion

Normal completion should answer only:

1. What is ready?
2. What useful systems are connected?
3. What finished artifact/result did I produce?
4. Is there anything the client must do now?
5. What can FolderDesk do next?

Keep technical evidence behind the scenes unless requested.

## 11. Verify / Safe Harbour

```bash
python3 scripts/arc.py verify --config arc.json
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

Use [VERIFY.md](VERIFY.md) for operator acceptance and recovery evidence.

## KISSS

Do not add infrastructure merely to make onboarding look sophisticated. The product should remove admin and technical friction from the client, not expose it.
