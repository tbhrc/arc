# FolderDesk Verification Contract

FolderDesk is healthy when useful work can begin from one workspace and expansion remains possible without being mandatory. Verification proves outcomes; it does not create permission gates.

## Repository baseline

```bash
python3 scripts/folderdesk.py verify-self
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Default deployment proof

For a fresh deployment, prove that:

- onboarding creates a profile with exactly one `workspace` repository;
- declared domains remain in-repository context and do not create repositories;
- bootstrap creates/reuses only the explicitly configured repository list;
- the workspace has `README.md`, `AGENTS.md`, `.folderdesk/` and the Atlas pointer;
- human work has clear `work/`, `knowledge/`, `outputs/`, `archive/` homes;
- starter Skills can be seeded under `.folderdesk/skills/`;
- a real requested workflow reaches a useful real-world result.

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
- contains no credential values, private-file contents, specialist-system records, database contents or derived memory contents;
- round-trips into a valid FolderDesk config.

Restore leaves existing repositories unchanged and creates only missing configured repositories.

## Data and credential boundary

- No credential values in public FolderDesk configuration or manifests.
- No private client/personnel/business records copied into public FolderDesk.
- External systems remain owners of their live records and backups.
- A file-first operating surface is not a transactional database.

## Definition of green

```text
request
→ one workspace
→ smallest relevant local context / Skill / connected owner
→ authorised execution
→ useful result
→ verify once
→ stop
```

with no forced multi-repository topology, unnecessary approval loop, duplicate control plane or speculative machinery.
