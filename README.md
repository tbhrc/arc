# ARC — Reproduce a Proven Human + AI Operating Ecosystem

ARC is a public, non-secret architecture package for reproducing a proven human + AI operating ecosystem on a blank environment without pretending that one repository should own every piece of live business state.

ARC is the **reproducible DNA of the organisation**: direction, operating method, routing, ownership boundaries, deployment, verification and recovery contracts that can be recreated while private files, credentials and specialist-system data remain with their proper owners.

**Fast links:** [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Manifest](MANIFEST.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Reconnections](RECONNECTIONS.md) · [Repository Router](AGENTS.md) · [Ecosystem Evidence](ECOSYSTEM-EVIDENCE.md) · [Releases](RELEASES.md)

## The outcome

ARC should let a capable founder, operator or AI agent take a blank or existing environment and reach a working estate where:

- the organisation has a canonical North Star owner;
- root `AGENTS.md` is the first-hop Repository Router;
- reusable HOW lives in Skills;
- current facts stay with their real owners;
- GitHub carries durable work, decisions and architecture evidence;
- Fast Links are progressive pointers rather than preload instructions;
- owner/source lookup is conditional only when the Router cannot resolve the route;
- normal authorised work executes directly at the lowest sufficient level;
- specialist agents/runtime are used only when genuinely needed;
- private files, credentials and structured live systems remain external owners;
- deployment is inspectable before mutation without requiring ceremonial second approval;
- destructive recovery remains explicitly gated;
- real work is verified and leaves durable evidence.

## Why ARC exists

The reference TBHRC/iMPLEMENTAi operating estate evolved rapidly once GitHub became the durable operating desk for both humans and AI agents. The useful pattern was not the number of repositories or agents. It was the separation of concerns:

1. **North Star ownership** — the organisation keeps one canonical direction source.
2. **GitHub durable work** — Issues, PRs, decisions and architecture survive individual chats.
3. **Skills-first architecture** — reusable HOW becomes versioned, discoverable operating intelligence rather than repeated prompting.
4. **Repository Router** — root `AGENTS.md` gives a small cold-start surface and routes known bounded work directly to the smallest relevant Skill/owner.
5. **Progressive Fast Links** — agents load only what the current task needs.
6. **One owner / one truth** — current state stays in the correct system rather than being copied everywhere.
7. **Lowest-sufficient execution** — direct connected capability beats unnecessary infrastructure.
8. **Provider neutrality** — agent/provider choice is an implementation detail, not the architecture itself.
9. **Verification** — work is accepted only after real-state evidence.
10. **Safe Harbour recovery** — non-secret topology and owner references can reproduce ARC-owned operating surfaces without pretending to back up private external systems.

## Core operating route

For ordinary deployed-repository work:

```text
request
  ↓
root AGENTS.md = Repository Router
  ↓
known bounded task → one relevant Fast Link → smallest relevant Skill / owner → execute
  ↓ only when owner/source is unclear
owner lookup / Sniper
  ↓ only when execution-level choice is genuinely needed
Workflow
  ↓ only when delegation/specialist/parallel work is genuinely required
Multi-Agent Orchestrator
  ↓
verify real state once
  ↓
update controlling Issue / durable evidence
  ↓
stop
```

The Router is deliberately small. Fast Links are pointers, not mandatory reads. There is no separate routing service, daemon, queue or provider hierarchy.

## Authority without friction

For ordinary bounded work, the current authorised instruction is the authority. ARC must not manufacture a second human confirmation merely because a command changes state.

`--apply` is a deliberate CLI mutation-mode selector. It does not mean “ask the human again.”

Fresh authority is required only when the next step crosses a real boundary such as destructive overwrite/delete/force/recovery, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

## What ARC reproduces

ARC reproduces portable architecture and contracts such as:

- North-Star ownership mechanism;
- repository/domain topology pattern;
- root `AGENTS.md` Repository Router;
- Skills-first method;
- progressive Fast Links;
- durable Issue / Anti-Drift control;
- source-of-truth boundaries;
- provider/runtime-neutral execution rules;
- inspectable bootstrap and bounded recovery;
- verification contracts;
- non-secret estate manifests and external-owner references.

ARC does **not** copy the target organisation's editable live truth.

## What remains external

The target organisation continues to own its own:

- mission/vision/directive wording;
- client and candidate files;
- CRM, ATS, ERP and accounting records;
- credentials and identity material;
- machine-local runtime state;
- memory contents;
- business/product facts that belong in domain systems.

ARC records only the minimum non-secret references required to reconstruct the operating architecture and reconnect those owners through their own approved recovery processes.

## Blank-environment route

A new deployment can inspect first:

```bash
python3 scripts/arc.py onboard --output arc.json
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

When the current instruction already authorises ordinary bounded deployment, execute directly:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

No second approval round-trip is required.

Bootstrap is conservative:

- existing repositories are classified REUSE and left unchanged;
- only missing configured repositories are CREATE candidates;
- no credentials are copied;
- no private business data is migrated;
- no production specialist system is rewritten merely to resemble ARC.

Read [BOOTSTRAP.md](BOOTSTRAP.md) for the full deployment contract.

## Existing-estate adoption

ARC is reuse-first.

Before structural change, classify existing systems and owners as appropriate:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

For configured GitHub repositories, ARC surfaces:

```text
REUSE
CREATE
```

where the target state can be observed.

Existing working systems should normally be integrated rather than replaced.

## Starter Skills

A new ARC Skills repository can seed a minimal generic foundation:

- `owner-router` — conditional owner/source lookup when root `AGENTS.md` cannot resolve the route;
- `github-workflow` — durable execution-level method;
- `skill-authoring` — how to create reusable Skills;
- `research-escalation` — when recurring friction merits structured research.

These are starter assets only. After deployment, the target organisation owns and evolves its own Skills canon.

## Real acceptance

ARC is not accepted because folders or repositories exist.

A real proof should demonstrate:

```text
organisation North Star
→ request / Anti-Drift objective
→ Repository Router
→ relevant Skill / owner truth
→ authorised execution
→ real-state verification
→ durable evidence
```

That proof should use actual work but remain proportionate and bounded.

## Safe Harbour

After the estate works, export a non-secret architecture snapshot:

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The resulting estate manifest is a **map, not a data dump**. It may contain topology, repository roles and non-secret owner references. It must not contain private files, live CRM/ATS/ERP data, credentials, machine state or memory contents.

Plan recovery without mutation:

```bash
python3 scripts/arc.py restore-plan \
  --manifest arc-estate.json \
  --inspect-target
```

Destructive recovery is a real risk boundary. After that boundary is explicitly authorised:

```bash
python3 scripts/arc.py restore \
  --manifest arc-estate.json \
  --apply
```

External owners are then restored or reconnected through their own approved backup and identity mechanisms.

## Measured reference evidence

ARC was extracted from a measured TBHRC/iMPLEMENTAi operating transformation. Historical metrics are reference evidence rather than deployment requirements.

The 27 Aug–4 Sep 2026 snapshot recorded, among other measures:

| Measure | Reference evidence |
|---|---:|
| GitHub repositories | 29 |
| Canonical Skills | 57 |
| Named AI execution lanes | 7 |
| Governed GitHub work objects | ~1,000 |
| GitHub notification emails | 1,358 |
| Targeted router turnaround | 92 sec → 18 sec |
| Tool calls in targeted router benchmark | 20 → 5 |
| Tool-call reduction | 75% |
| Relative router speed | 5.1× |

These figures describe the reference ecosystem during that measurement window. ARC does not require another organisation to reproduce its size, provider mix or historical infrastructure.

Read [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md) for provenance before repeating historical statistics.

## KISSS guardrail

> **The operating system must not become the work.**

Before adding architecture, ask whether the requirement materially improves deployment, routing, reconnection, real-work proof or recovery.

Prefer:

```text
direct edit
pointer
Fast Link
existing Skill
existing system
ordinary agent judgement
```

before creating:

```text
validator
daemon
scheduler
queue
policy engine
provider hierarchy
new control plane
precautionary approval loop
```

## Start here

- Deploy/adopt/recover: [Atlas](ATLAS.md)
- Understand the model: [Architecture](ARCHITECTURE.md)
- Work inside this repository: [Repository Router](AGENTS.md)
- Bootstrap: [Bootstrap](BOOTSTRAP.md)
- Verify: [Verify](VERIFY.md)
- Recovery boundaries: [Manifest](MANIFEST.md) and [Reconnections](RECONNECTIONS.md)
- Historical proof: [Ecosystem Evidence](ECOSYSTEM-EVIDENCE.md)

**Issue keeps continuity. `main` keeps progress. KISSS keeps speed.**
