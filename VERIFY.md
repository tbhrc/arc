# FolderDesk Verification Contract

FolderDesk is healthy when useful work can begin from one self-contained workspace and expansion remains possible without being mandatory. Verification proves outcomes; it does not create permission gates.

## Repository baseline

```bash
python3 scripts/folderdesk.py verify-self
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Default fresh-deployment proof

For a fresh FolderDesk-managed deployment, prove that:

- onboarding creates a profile with exactly one `workspace` repository;
- declared domains remain in-repository context and do not create repositories;
- the exact configured GitHub owner/path is resolved, with transfer/redirect mismatches refused;
- create permission is confirmed only when creation is actually needed;
- bootstrap creates/reuses only the explicitly configured repository list;
- a new workspace has `README.md`, `AGENTS.md`, `.folderdesk/`, the managed marker and Atlas pointer;
- human work has clear `work/`, `knowledge/`, `outputs/`, `archive/` homes;
- all six foundational local Skills are present under `.folderdesk/skills/`: `structure`, `skill-builder`, `lessons`, `auditor`, `document-intake`, `client-experience`;
- a real requested workflow reaches a useful real-world result.

## Existing-repository / adoption proof

Existence alone does not make a repository FolderDesk-managed.

If the exact configured repository already exists and has no `.folderdesk/managed.json`, verification reports it as **REUSED/UNMANAGED** rather than falsely declaring the repository broken. Adoption is a separate explicit bounded action: inspect the current repository, preserve its real owners, seed only useful missing FolderDesk capability, and do not overwrite established files by default.

A repository that carries `.folderdesk/managed.json` is claiming the FolderDesk-managed contract and must satisfy the managed baseline above.

## Auditor proof

The local `auditor` is intentionally lightweight and event-driven. It is healthy when a capable agent can use it to detect concrete semantic/structural/behaviour/purpose drift, duplicate ownership, unnecessary machinery or false controls and then route the smallest repair.

Do **not** require:

- a controlling Issue for every task;
- recurring audit jobs;
- audit ledgers or scorecards;
- lifecycle labels or approval states;
- an audit before ordinary authorised execution.

The absence of those mechanisms is not a defect.

## Expansion proof

When another repository is added, prove the boundary that earned it. The reason should be observable—for example access isolation, independent release/lifecycle, concurrency, security/privacy, or a mature separately owned capability.

The deployment must continue to work when no optional expansion repositories exist.

## Safe-harbour proof

```bash
python3 scripts/folderdesk.py export --config folderdesk.json --output folderdesk-estate.json --inspect-target
python3 scripts/folderdesk.py restore-plan --manifest folderdesk-estate.json --inspect-target
python3 scripts/folderdesk.py restore --manifest folderdesk-estate.json --apply
```

A valid manifest:

- uses `manifest_schema: 2.0`;
- identifies `folderdesk_version`;
- preserves the workspace plus explicit expansion repositories;
- preserves logical domains separately from repositories;
- records observed exact-path `REUSE`, missing `CREATE`, or `OWNER_MISMATCH` without treating unknown state as absence;
- contains no credential values, private-file contents, specialist-system records, database contents or derived memory contents;
- round-trips into a valid FolderDesk config.

Restore leaves existing repositories unchanged and creates only missing configured repositories.

## Structural vs operational readiness

`folderdesk.py verify` proves the FolderDesk/GitHub structural contract. It does **not** prove that an external CRM, file store, accounting system, runtime, memory provider or other connector is operational merely because that system is declared in configuration.

External capability is ready only after the owning system/connector is separately verified through a representative read/write or other appropriate proof.

## Data and credential boundary

- No credential values in public FolderDesk configuration or manifests.
- No private client/personnel/business records copied into public FolderDesk.
- External systems remain owners of their live records and backups.
- A file-first operating surface is not a transactional database.

## Definition of green

```text
request
→ one self-contained workspace
→ smallest relevant local context / Skill / connected owner
→ authorised direct execution
→ useful result
→ verify once
→ learn only when a material lesson exists
→ stop
```

with no forced multi-repository topology, unnecessary approval loop, duplicate control plane, hidden owner redirect or speculative machinery.
