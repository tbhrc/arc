from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# 1) Human front door: client starts with their agent, not GitHub.
(ROOT / "README.md").write_text(r'''# FolderDesk by iMPLEMENTAi — Your Business AI Operating System

FolderDesk is a **task-management, filing and organisational-memory system for humans and AI agents**. It helps your AI keep work organised, file what you give it, remember what matters, retrieve it later, and produce finished business work instead of leaving you with disconnected chats and admin chaos.

**You do not need GitHub experience to use FolderDesk.** GitHub is the durable backend your agent uses to keep the operating system organised.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [Get Started](BOOTSTRAP.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Releases](RELEASES.md) · [Agent Router](AGENTS.md)

## Start here — give this to your agent

Copy this into the AI agent you want to use:

```text
Set up FolderDesk for my business from https://github.com/tbhrc/folderdesk.

Assume I have never used GitHub and do not want to operate it myself. Establish the required GitHub backend using the lowest-friction supported route. Handle the technical work yourself and ask me only when I must sign in, create/confirm an account, approve access, or make a real business decision. Do not teach me GitHub unless I ask.

Before producing client-facing work, learn how my business should look and sound. Ask me for brand guidelines if I have them; otherwise ask for one or more representative documents and infer a practical house style. Ask for a logo/assets only when useful.

Ask which systems I already use for files, email/calendar, CRM, ERP/accounting, messaging and other important work. Recommend the smallest useful connector set and connect what I approve using the easiest native/dedicated route available.

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

## What FolderDesk gives you

- a durable task-management layer so work survives chats, sessions and agents;
- default document intake: file the source, ingest useful content, preserve provenance and retrieve it later;
- organisational memory tied back to real source documents and owner systems;
- reusable Skills so your agent learns repeatable ways of working;
- brand/style learning from formal guidelines **or your existing documents**;
- client-tone adaptation from your real communication and examples;
- connector-aware operation across the systems you already use;
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
''', encoding='utf-8')

# 2) Bootstrap contract: agent owns backend setup; client discovery comes before proving work.
(ROOT / "BOOTSTRAP.md").write_text(r'''# Bootstrap FolderDesk

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

## 3. Discover and connect the systems the client already uses

Ask what currently owns:

- files/documents;
- email and calendar;
- CRM/sales;
- ERP/accounting;
- messaging/collaboration;
- other business-critical systems.

Recommend the **smallest useful connector set for real work now**. Prefer native/dedicated authorised connectors. Reuse existing systems rather than replacing them.

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
''', encoding='utf-8')

# 3) Atlas public narrative and skill: client experience is part of successful onboarding.
(ROOT / "ATLAS.md").write_text(r'''# Atlas — FolderDesk Front Door

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
- Discover the systems they already use and connect the smallest useful set through native/dedicated routes where possible.
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
''', encoding='utf-8')

(ROOT / ".github/skills/atlas/SKILL.md").write_text(r'''---
name: atlas
description: "FolderDesk front door for onboarding, adoption, health, upgrade, recovery and next-action guidance. Use when an agent is asked to deploy or operate FolderDesk for a business. Assume the client is non-technical: establish GitHub backend with minimum client friction, learn brand/examples and communication/output preferences, discover useful connectors, reuse existing systems, prove value with a polished real outcome, and keep technical evidence out of normal client replies."
---

# Atlas

Read root `/AGENTS.md`, then `/BOOTSTRAP.md` for onboarding/adoption. Load only the smallest additional FolderDesk surface required.

## Client-first operating loop

```text
understand business outcome
→ establish GitHub backend with lowest-friction route
→ learn client brand/examples + tone/output preferences
→ discover/connect smallest useful system set
→ reuse existing owners
→ execute bounded setup
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
4. **Systems/connectors:** file store, email/calendar, CRM, ERP/accounting, messaging and other important systems. Recommend/connect the smallest useful set using native/dedicated authorised routes.

Preserve useful client preferences in the client-owned operating estate so future agents reuse them.

## Client-facing output

For documents, reports, proposals, quotes and similar work, default to a polished **DOCX and/or PDF** when that is the natural business output. Apply the client's established brand/style.

Markdown/GitHub may remain backend canon/evidence, but do not present it as the normal client deliverable.

Client status should be concise and business-facing. Do not emit repository tables, SHAs, byte counts, CLI traces, internal routing labels, GREEN/AMBER theatre or engineering diagnostics unless the client explicitly requests them or they materially block progress.

## Existing estates

Prefer KEEP / INTEGRATE. Reuse the client's working systems. Do not replace them merely to resemble FolderDesk examples.

## Authority

Ordinary authorised bounded work executes directly. Ask for fresh authority only at genuine consequential boundaries: destructive/irreversible actions, root/super-admin authority changes, material spend, private-data disclosure, legal/compliance commitment or material external commitment.

## Proof

Prove one useful real workflow. The proof is the finished result plus retrievability, not a technical deployment dump.

If a file is received or produced, use the deployed `document-intake` Skill: preserve/file → ingest → route knowledge/tasks → provenance → verify retrieval.

## KISSS

Make FolderDesk invisible to the client wherever possible. The client should notice less admin and better finished work, not more infrastructure.
''', encoding='utf-8')

# 4) New public-safe starter Skill for every deployment.
skill_dir = ROOT / "starter" / "skills" / "client-experience"
skill_dir.mkdir(parents=True, exist_ok=True)
(skill_dir / "SKILL.md").write_text(r'''---
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
5. **Discover connectors.** Ask which systems own files, email/calendar, CRM, ERP/accounting, messaging and important business data. Recommend the smallest useful connector set. Prefer native/dedicated authorised connectors; do not ask for raw credential values.
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
''', encoding='utf-8')

# 5) Seed the new Skill.
seed = ROOT / "scripts" / "seed_foundation.py"
s = seed.read_text(encoding="utf-8")
if '"client-experience"' not in s:
    s = s.replace('    "document-intake",\n)', '    "document-intake",\n    "client-experience",\n)', 1)
seed.write_text(s, encoding="utf-8")

# 6) Generated client Router inherits client-facing behaviour.
arc = ROOT / "scripts" / "arc.py"
a = arc.read_text(encoding="utf-8")
a = a.replace(
    '    document_intake = f"{skills_base}/tree/main/document-intake"\n',
    '    document_intake = f"{skills_base}/tree/main/document-intake"\n    client_experience = f"{skills_base}/tree/main/client-experience"\n',
    1,
)
a = a.replace(
    '**Core Fast Links:** [Skills]({skills_base}) · [Document Intake]({document_intake}) · [Research]',
    '**Core Fast Links:** [Skills]({skills_base}) · [Client Experience]({client_experience}) · [Document Intake]({document_intake}) · [Research]',
    1,
)
a = a.replace(
    '## Route\\n\\n- **User gives you a file/document**',
    '## Route\\n\\n- **Client-facing onboarding, status or business artifact** → use [Client Experience]({client_experience}) by default: assume zero GitHub knowledge, learn/adapt to the client\'s tone and output expectations, ask for brand guidelines or representative documents, discover the smallest useful connector set, keep technical evidence behind the scenes, and deliver polished DOCX/PDF when that is the natural business output.\\n- **User gives you a file/document**',
    1,
)
# Human-facing generated README note.
a = a.replace(
    'This repository was bootstrapped from [FolderDesk](https://github.com/tbhrc/folderdesk). Its live facts and decisions belong here only where this repository is the declared owner.',
    'This repository was bootstrapped from [FolderDesk](https://github.com/tbhrc/folderdesk). Human clients do not need to operate this GitHub repository; their agent uses it as durable backend state. Its live facts and decisions belong here only where this repository is the declared owner.',
    1,
)
arc.write_text(a, encoding="utf-8")

# 7) Root Router gets client-experience route.
agents = ROOT / "AGENTS.md"
g = agents.read_text(encoding="utf-8")
g = g.replace(
    '**Core Fast Links:** [Workflow](https://github.com/tbhrc/skills/tree/main/github-agent-workflow) · [LOOP3 File Ingestion]',
    '**Core Fast Links:** [Workflow](https://github.com/tbhrc/skills/tree/main/github-agent-workflow) · [Client Experience](starter/skills/client-experience/SKILL.md) · [LOOP3 File Ingestion]',
    1,
)
route_anchor = '- **User gives you a file/document** → default to [LOOP3]'
client_route = '- **Client-facing onboarding, status or business artifact** → use [Client Experience](starter/skills/client-experience/SKILL.md): treat GitHub as backend infrastructure, learn/adapt tone + output expectations, request brand guidelines or representative documents, discover useful connectors, and default natural business-document outputs to polished DOCX/PDF. Keep technical evidence out of normal client replies.\n'
if client_route not in g:
    idx = g.find(route_anchor)
    if idx == -1:
        raise SystemExit('root AGENTS insertion point not found')
    g = g[:idx] + client_route + g[idx:]
agents.write_text(g, encoding="utf-8")

# 8) Ultimate Features additions.
features = ROOT / "FEATURES.md"
f = features.read_text(encoding="utf-8")
anchor = '| Work management | Durable task/work identity across agents and sessions | Core/Reference | GitHub Issues + owner state |\n'
rows = '''| Client experience | Non-technical client onboarding with GitHub hidden as agent backend | Core | Atlas + Client Experience Skill |\n| Client experience | Lowest-friction GitHub establishment handled by agent | Core/Connected | Agent + authorised GitHub route |\n| Client experience | Brand learning from formal guidelines or representative documents | Core/Reference | Client Experience Skill + client-owned brand sources |\n| Client experience | Communication tone/terminology/detail adaptation | Core/Reference | Client Experience Skill + durable client profile |\n| Client experience | Preferred artifact-format learning and reuse | Core/Reference | Client Experience Skill + client-owned profile |\n| Client experience | Existing-system/connector discovery and smallest-useful-set activation | Core/Connected | Native/dedicated connectors + owner systems |\n| Client experience | Polished DOCX/PDF default for natural business-document outputs | Reference/Connected | Document tools + client brand/style |\n| Client experience | Backend technical evidence separated from normal client communication | Core | Router + Client Experience Skill |\n'''
if rows not in f:
    if anchor not in f:
        raise SystemExit('FEATURES insertion point not found')
    f = f.replace(anchor, anchor + rows, 1)
features.write_text(f, encoding="utf-8")

# 9) Update old test assumption: client no longer starts by connecting GitHub.
test51 = ROOT / "tests" / "test_issue_51_client_ux.py"
t = test51.read_text(encoding="utf-8")
t = t.replace('self.assertIn("Step 1 — Connect GitHub", readme)', 'self.assertIn("You do not need GitHub experience", readme)')
test51.write_text(t, encoding="utf-8")

# Foundation count is now six starter Skills.
test_foundation = ROOT / "tests" / "test_foundation.py"
tf = test_foundation.read_text(encoding="utf-8")
tf = tf.replace('self.assertEqual(len(rows), 5)', 'self.assertEqual(len(rows), 6)')
if 'self.assertIn("client-experience/SKILL.md", paths)' not in tf:
    tf = tf.replace('self.assertIn("document-intake/SKILL.md", paths)', 'self.assertIn("document-intake/SKILL.md", paths)\n        self.assertIn("client-experience/SKILL.md", paths)')
test_foundation.write_text(tf, encoding="utf-8")

# 10) Regression coverage for issue #52.
(ROOT / "tests" / "test_issue_52_client_experience.py").write_text(r'''import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue52", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class Issue52ClientExperienceTests(unittest.TestCase):
    def test_readme_starts_from_agent_not_client_github_operation(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Start here — give this to your agent", text)
        self.assertIn("You do not need GitHub experience", text)
        self.assertIn("Assume I have never used GitHub", text)
        self.assertIn("Do not teach me GitHub unless I ask", text)
        self.assertNotIn("## Step 1 — Connect GitHub", text)

    def test_bootstrap_discovers_brand_connectors_tone_and_output(self):
        text = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
        self.assertIn("representative documents", text)
        self.assertIn("Communication and output preferences", text)
        self.assertIn("Discover and connect the systems", text)
        self.assertIn("smallest useful connector set", text)
        self.assertIn("polished DOCX and/or PDF", text)

    def test_client_experience_starter_skill_is_seeded(self):
        skill = (ROOT / "starter/skills/client-experience/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Assume zero GitHub knowledge", skill)
        self.assertIn("representative documents", skill)
        self.assertIn("polished DOCX", skill)
        self.assertIn("Avoid status theatre", skill)
        seed_spec = importlib.util.spec_from_file_location("folderdesk_seed52", ROOT / "scripts" / "seed_foundation.py")
        seed = importlib.util.module_from_spec(seed_spec)
        assert seed_spec.loader is not None
        seed_spec.loader.exec_module(seed)
        self.assertIn("client-experience", seed.STARTER_SKILLS)

    def test_generated_router_inherits_client_experience(self):
        repo = {"name": "sales", "role": "business-domain", "description": "Sales", "required": True, "visibility": "private"}
        agents = arc.generated_agents("acme", repo, {"skills": "skills", "research": "research"})
        self.assertIn("[Client Experience](https://github.com/acme/skills/tree/main/client-experience)", agents)
        self.assertIn("Client-facing onboarding, status or business artifact", agents)
        self.assertIn("polished DOCX/PDF", agents)
        self.assertIn("keep technical evidence behind the scenes", agents)

    def test_features_capture_product_behaviour(self):
        text = (ROOT / "FEATURES.md").read_text(encoding="utf-8")
        self.assertIn("Non-technical client onboarding with GitHub hidden as agent backend", text)
        self.assertIn("Brand learning from formal guidelines or representative documents", text)
        self.assertIn("Communication tone/terminology/detail adaptation", text)
        self.assertIn("Existing-system/connector discovery", text)
        self.assertIn("Polished DOCX/PDF default", text)
        self.assertIn("Backend technical evidence separated", text)


if __name__ == "__main__":
    unittest.main()
''', encoding='utf-8')
