# ARC Architecture

## 1. The operating graph

ARC separates **method, truth, execution and memory** so no single tool becomes an accidental operating system.

```text
                         PEOPLE + AI AGENTS
                                |
                                v
+------------------------------------------------------------------+
| GITHUB — DURABLE OPERATING DESK                                 |
| Issues · PRs · architecture · Skills · automation · evidence    |
+------------------------------------------------------------------+
        |                         |                         |
        v                         v                         v
+----------------+      +------------------+      +------------------+
| SKILLS CANON   |      | DOMAIN OWNERS    |      | RESEARCH         |
| reusable HOW   |      | business truth   |      | discover/prove   |
+----------------+      +------------------+      +------------------+
        \                         |                         /
         +------------------------+------------------------+
                                  |
                                  v
                         AUTHORISED AI AGENT
                                  |
                    normal capability sufficient?
                         /                     \
                       YES                     NO
                        |                       |
                        v                       v
                 DIRECT EXECUTION       TRUSTED RUNTIME
                 API/MCP/browser        VPS/local/runner
                        \                       /
                         +----------+----------+
                                    |
                                    v
                             VERIFY REAL STATE
                                    |
                                    v
                              OWNER EVIDENCE

+---------------------------+     +-------------------------------+
| PRIVATE FILE STORE        |     | SPECIALIST SYSTEMS            |
| confidential documents    |     | CRM · ERP · ATS · accounting  |
+---------------------------+     +-------------------------------+
              \                          /
               +-----------+------------+
                           |
                           v
                    +---------------+
                    | MEMORY        |
                    | derived only  |
                    +---------------+
```

## 2. The four architectural questions

Every material workflow should answer:

1. **Which reusable method applies?** — Skills.
2. **Who owns the current fact/state?** — domain repo or specialist system.
3. **What is the smallest safe execution route?** — normal tool first; trusted runtime only when needed.
4. **How will we prove the result?** — real-state verification and durable evidence.

## 3. Skills-first

A Skill is the reusable HOW. It should be concise enough for a capable agent, use current owner truth, and include deterministic helpers only where reasoning alone is unreliable or a machine interface requires one.

ARC deploys the concept of a Skills canon; each organisation owns its own current Skills.

## 4. Domain ownership

Do not store all business state in one architecture repository.

A domain repository may represent:

- a business unit;
- a product;
- a service;
- a revenue engine;
- a regulated workflow;
- a platform/runtime.

Specialist systems remain authoritative for fields they are designed to own. A CRM should not be copied into Markdown merely to make an agent feel informed.

## 5. Research as capability discovery

When a local failure or repeated manual workaround suggests a missing reusable capability:

```text
contain immediate problem if needed
-> symptom
-> workflow
-> reusable capability
-> platform/system
-> compare native / open-source / paid options
-> Research / Watch / Test / Reject
-> bounded test
-> benchmark
-> adopt only when proven and authorised
```

Research owns the evidence. The eventual implementation returns to the correct owner.

## 6. Direct execution first

Do not route every action through an infrastructure layer.

Preferred order:

```text
native connected capability
-> API / MCP / browser / CLI available to agent
-> owning system
-> trusted runtime only when a real runtime/privilege gap exists
```

## 7. Trusted runtime

The optional `ai-engine` role is narrow: it gives authorised agents access to trusted execution surfaces they cannot otherwise safely reach, such as a VPS, isolated local runner or machine-local CLI profile.

It is not:

- a second Skills Bank;
- a second business database;
- the default hop for every action;
- a place for secret values in source control.

## 8. Private files and specialist systems

ARC treats confidential files and live structured applications as first-class owners rather than inconveniences to copy into GitHub.

Examples:

- client documents -> approved private file store;
- accounting -> accounting system;
- candidate/application state -> ATS;
- sales pipeline -> CRM;
- operational work/decision -> GitHub Issue/domain owner.

## 9. Memory

Memory is derived context. It can preserve decisions, rationale and lessons, but important claims must be checked against current canon before action.

## 10. Portability

A portable ARC deployment therefore consists of:

```text
architecture contract
+ repository topology
+ Skills strategy
+ agent entrypoints
+ configuration schema
+ secret metadata (never values)
+ external-system owner map
+ bootstrap procedure
+ verification procedure
```

Not a raw copy of one company's entire filesystem.
