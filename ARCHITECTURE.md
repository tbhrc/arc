# ARC Architecture

ARC is the portable architecture for reproducing a proven human + AI operating ecosystem on a blank environment.

It separates **direction, method, truth, execution, verification and memory** so no single tool, model or repository becomes an accidental operating system.

**Fast links:** [README](README.md) · [Atlas](ATLAS.md) · [Agent Contract](AGENTS.md) · [Ecosystem Evidence](ECOSYSTEM-EVIDENCE.md) · [Bootstrap](BOOTSTRAP.md) · [Verify](VERIFY.md) · [Reconnections](RECONNECTIONS.md)

---

## 1. The operating graph

```text
                         ORGANISATION NORTH STAR
                    mission / vision / directives
                                   |
                                   v
                            PEOPLE + AI AGENTS
                                   |
                                   v
+-----------------------------------------------------------------------+
| GITHUB — DURABLE OPERATING DESK                                      |
| Issues · PRs · work control · architecture · automation · evidence   |
+-----------------------------------------------------------------------+
        |                            |                           |
        v                            v                           v
+------------------+      +--------------------+      +------------------+
| SKILLS CANON     |      | DOMAIN OWNERS      |      | RESEARCH         |
| reusable HOW     |      | current truth      |      | discover / prove |
+------------------+      +--------------------+      +------------------+
         \                            |                           /
          +---------------------------+--------------------------+
                                      |
                                      v
                              AUTHORISED AGENT
                                      |
                     normal connected capability enough?
                              /                   \
                            YES                   NO
                             |                     |
                             v                     v
                    DIRECT EXECUTION       TRUSTED RUNTIME
                  API/MCP/browser/CLI      Mac/VPS/runner
                             \                     /
                              +---------+---------+
                                        |
                                        v
                                VERIFY REAL STATE
                                        |
                                        v
                                 DURABLE EVIDENCE
                                        |
                                        v
                              PROMOTE REUSABLE LEARNING

+----------------------------+       +------------------------------+
| PRIVATE FILE OWNER         |       | SPECIALIST SYSTEMS           |
| confidential documents     |       | CRM · ATS · ERP · accounting |
+----------------------------+       +------------------------------+
               \                               /
                +--------------+---------------+
                               |
                               v
                        +---------------+
                        | MEMORY        |
                        | derived only  |
                        +---------------+
```

This graph is the core thing ARC reproduces.

## 2. What is portable vs organisation-specific

ARC packages the **mechanism** and operating contracts. The target organisation owns its own current business truth.

### Portable through ARC

- North-Star ownership mechanism;
- repository/domain topology pattern;
- Skills-first method;
- machine-first routing;
- durable Issue / Anti-Drift structure;
- source-of-truth boundaries;
- provider/runtime-neutral execution rules;
- external-system reconnection pattern;
- bootstrap/verification/recovery contracts;
- non-secret estate map.

### Owned by the target organisation

- mission/vision/directive wording;
- business/product/client facts;
- actual Skills canon after deployment;
- CRM/ATS/ERP/accounting records;
- private files;
- credentials;
- machine-local runtime state;
- memory contents.

A generic ARC deployment must therefore **reproduce the architecture without copying TBHRC's editable business state**.

---

## 3. North Star and Anti-Drift

These are different layers.

**North Star** = organisation-level mission / vision / directives that guide prioritisation and judgement.

**Anti-Drift — Original Objective** = the original requested outcome of one durable work item.

The North Star tells the system **why and toward what** the organisation operates.

Anti-Drift prevents a specific task from silently changing destination while implementation evolves.

A durable Issue uses:

```text
North Star
Anti-Drift — Original Objective
Local Objective
Checklist
Acceptance Criteria
Current Status
Exact Next Action
```

The North Star section normally points to the canonical organisation source instead of duplicating editable mission text.

---

## 4. Skills-first

Skills own reusable HOW.

A Skill should:

- describe a reusable method rather than mutable business facts;
- route to current owner truth;
- be understandable by a capable agent;
- include deterministic helpers only when judgement alone is unreliable or a machine interface requires them;
- remain one canonical editable copy rather than fragmented duplicates.

The Skills layer is the ecosystem's reusable operating intelligence / central nervous system.

ARC seeds a foundation; the target organisation owns its current canon.

---

## 5. Durable GitHub operating desk

GitHub owns durable work control and architecture evidence, not every piece of business data.

Appropriate GitHub-owned material includes:

- Issues / work objects;
- PRs / reviewable change;
- architecture and ownership maps;
- Skills repositories;
- domain repositories where Git is the real business owner;
- automation/configuration;
- durable evidence and decisions.

A machine-first operational front door should make these destinations directly reachable:

```text
North Star
Skills
workflow / change-control method
owner / system map
Issues / work queue
```

Use compact Fast Links where they reduce rediscovery. Fast Links are guidance, not a numeric quota.

---

## 6. One owner / one truth

Every current fact/state class should have one authoritative owner.

Examples:

| State | Owner |
|---|---|
| reusable HOW | Skills canon |
| business/product facts | business/domain owner |
| external technology evidence | Research |
| private client/candidate files | approved private file store |
| sales pipeline | CRM |
| candidate/application state | ATS |
| finance/accounting | accounting system |
| privileged machine/runtime state | trusted-runtime owner |
| derived context | memory layer |
| ARC portable architecture | ARC |

Do not copy state into GitHub simply because GitHub is easier for an agent to access.

---

## 7. Multi-agent and provider-neutral execution

The proven ecosystem evolved beyond dependence on one model/provider.

ARC therefore treats AI execution as routable capability rather than a permanent workhorse.

Eligible routes should be filtered/ranked by:

- authorisation;
- capability/task fit;
- required tools/runtime;
- sensitivity;
- collision risk;
- independent-review need;
- current capacity;
- execution overhead.

The measured reference ecosystem used named routes across ChatGPT, Copilot, Jules, Codex and Claude, with Gemini as a conditional route. These are **reference evidence**, not mandatory ARC dependencies. See [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md).

---

## 8. Lowest-sufficient execution

Do not route every action through infrastructure.

Preferred order:

```text
native connected capability
→ API / MCP / browser / CLI
→ owning system
→ deterministic GitHub Action when materially useful
→ trusted runtime only when a genuine privilege/runtime/profile gap remains
```

Trusted runtime is exceptional leverage, not the default hop.

A direct edit, pointer, template or existing tool should beat a new daemon/service/validator when it solves the need safely.

---

## 9. Research as capability discovery

When recurring friction suggests a real reusable capability gap:

```text
contain immediate problem if required
→ identify symptom
→ identify workflow
→ define reusable capability
→ inspect current/native options
→ compare open-source / paid / external routes
→ Research / Watch / Test / Reject
→ bounded proof
→ benchmark where useful
→ adopt only when proven and authorised
```

Research owns the evidence. Implementation returns to the correct domain/Skill/tool owner.

Do not turn one-off inconvenience into architecture by default.

---

## 10. Private files and specialist systems

Confidential and structured live systems are first-class owners.

Examples:

- client documents → approved private store;
- candidate files → approved private store / ATS as appropriate;
- accounting → accounting system;
- sales pipeline → CRM;
- recruitment applications → ATS;
- operational work/decision → GitHub Issue/domain owner.

ARC reconnects these systems through minimal non-secret references. It does not mirror their live contents.

---

## 11. Memory

Memory is derived context.

It may preserve:

- rationale;
- decisions;
- recurring patterns;
- lessons;
- useful historical context.

But current claims must be checked against current canon before action.

Memory must never outrank the system that owns the live fact.

---

## 12. Portability contract

A portable ARC estate consists of:

```text
North-Star ownership contract
+ architecture contract
+ repository topology
+ Skills strategy
+ machine-first agent entrypoints
+ durable Issue template
+ useful Fast-Link navigation
+ non-secret configuration
+ credential metadata/reference only
+ external-system owner map
+ bootstrap procedure
+ verification procedure
+ recovery procedure
```

It is **not** a raw copy of one company's filesystem or databases.

---

## 13. Safe harbour and recovery

ARC adds a recovery layer around live owners without replacing them.

```text
known-good ARC release
        |
        +----------------------+
        |                      |
        v                      v
portable ARC state       non-secret estate manifest
architecture/contracts   topology + owner references
        \                      /
         +----------+---------+
                    |
                    v
               restore-plan
                    |
           explicit apply authority
                    |
                    v
       bounded GitHub reconstruction
                    |
          reconnect external owners
                    |
                    v
                  verify
```

The manifest is intentionally a **map, not a data dump**.

Recovery ownership remains distributed:

| Recovery material | Owner |
|---|---|
| ARC portable architecture | formal ARC release/tag |
| target topology/role metadata | non-secret ARC estate manifest |
| target North Star wording | target organisation's North-Star owner |
| repository history/content | GitHub/source owner |
| private files | private-file/backup owner |
| CRM/ERP/ATS/accounting data | owning specialist system |
| credentials | approved identity/credential owner |
| VPS/Mac/runtime machine state | trusted-runtime owner |
| memory contents | memory owner |

---

## 14. Real deployment acceptance

ARC is not accepted because repositories were created.

A deployment should prove:

```text
organisation North Star
→ request / Anti-Drift objective
→ Skill
→ current owner truth
→ authorised execution
→ verify real state
→ durable evidence
```

ARC v1 passed this model in an independent non-TBHRC clean-room proof and then passed destructive recovery of an ARC-owned operating surface. See [Core Proof #11](https://github.com/tbhrc/arc/issues/11).

---

## 15. Reference ecosystem provenance

ARC was extracted from a measured operating transformation across TBHRC/iMPLEMENTAi.

The 27 Aug–4 Sep 2026 snapshot recorded, among other metrics:

- 29 repositories;
- 57 canonical Skills;
- seven named AI lanes;
- ~1,000 governed GitHub work objects;
- 1,358 GitHub notifications;
- targeted router improvement from 92 sec / 20 calls to 18 sec / 5 calls;
- real recruitment, sourcing, research and commercial outcomes.

Those figures show the scale of the **reference ecosystem**, not mandatory target size and not ARC-repository-only activity.

Read [ECOSYSTEM-EVIDENCE.md](ECOSYSTEM-EVIDENCE.md) before repeating historical statistics.

---

## 16. KISSS architecture guardrail

> **The operating system must not become the work.**

Before adding architecture, ask:

> Does this materially improve blank-slate reproduction, reconnection, real-work proof or recovery?

If not: delete or defer.

Before adding an Action, validator, daemon, policy engine, schema or subsystem, ask whether a pointer, template, direct edit or ordinary agent judgement is sufficient.

ARC v1 intentionally removed several speculative enforcement/lifecycle layers before release. Simplicity is part of the architecture, not an omission to be automatically filled.
