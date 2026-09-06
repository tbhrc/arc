# ARC Verification Contract

ARC is healthy when the intended operating capability works. Verification proves outcomes; it does not create permission gates.

## Repository baseline

Run the normal executable checks:

```bash
python3 scripts/arc.py verify-self
python3 -m unittest discover -s tests -p 'test_*.py'
```

Use `doctor`, `plan --inspect-target` and target `verify` when they materially help diagnose or prove the requested deployment. They are tools, not mandatory preconditions for ordinary authorised mutation.

## Deployment proof

For a new or adopted estate, prove only what is relevant:

- root `AGENTS.md` routes a known bounded task directly to the smallest relevant Skill/owner;
- owner lookup, Workflow and Multi-Agent Orchestrator remain unloaded unless genuinely needed;
- Fast Links are pointers rather than preload requirements;
- an already-authorised bounded mutation executes without a second approval ritual;
- `--apply` selects mutation mode;
- existing configured repositories are reused unchanged;
- missing configured repositories can be created through the authorised bootstrap path;
- one real workflow reaches real-state verification.

## Safe-harbour proof

A valid estate manifest must:

- use supported `manifest_schema: 1.0`;
- identify the ARC version that exported it;
- round-trip into valid ARC topology/configuration;
- contain architecture/owner references only;
- exclude credential values, private-file contents, specialist-system records, database contents, trusted-runtime machine state and derived memory contents;
- reject unsupported schemas and obvious credential material.

Useful commands:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current `restore --apply` is bounded reconstruction: existing repositories remain unchanged and only missing configured repositories are created. It is not a separate approval class.

If a future operation actually deletes, overwrites, force-updates, uses root/super-admin authority, moves private/confidential data, spends materially, creates a legal/compliance commitment or makes a material external/client commitment, protect that specific boundary only.

## Data and credential boundary

These controls remain because they protect concrete public-repository risks:

- no credential values in public ARC configuration or manifests;
- no private client/personnel/business records copied into public ARC;
- exposed credentials are revoked/rotated rather than treated as remediated by deleting text;
- external systems remain owners of their live records and backups;
- existing target repositories and Skills are not silently overwritten.

## Provider and runtime proof

One authorised capable route is enough when it can complete and verify the intended work.

- use the simplest existing authorised route that can do the job;
- do not require redundant providers, extra runtime hops or weaker execution merely for appearance of safety;
- use a trusted/local/self-hosted/VPS runtime only when its capability is actually needed;
- changing provider should not require redesigning ARC ownership.

## Continuity

Preserve continuity only when it materially helps future execution. An Issue, PR, repository file or owner-system record may be used; no specific object is mandatory merely because work is material.

Useful continuity is limited to:

- objective;
- current state;
- evidence;
- exact next action.

## Definition of green

ARC is green when a fresh human or capable agent can:

```text
request
→ Repository Router
→ smallest relevant Skill / owner truth
→ authorised execution
→ real-state verification
→ stop
```

with no unnecessary approval loop, mandatory planning ceremony, issue-first requirement, redundant provider/runtime requirement, duplicate control plane or hypothetical security restriction.
