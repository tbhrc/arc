# FolderDesk Deployment Manifest

FolderDesk v2 starts with the **smallest complete deployment**: one useful workspace repository. Extra repositories are supported, but they are expansion—not bootstrap requirements.

| Component | Default | Owns | Expansion rule |
|---|---|---|---|
| Primary workspace | One GitHub repository | durable work, local knowledge, outputs, archive, agent support | always present |
| Human surface | `work/`, `knowledge/`, `outputs/`, `archive/` | normal business work and artifacts | add folders only from real use |
| FolderDesk support | `.folderdesk/` | reusable Skills, config and agent machinery | keep small |
| Root Router | `AGENTS.md` | cold-start routing | keep minimal |
| Atlas | local project Skill/prompt | onboarding, health, recovery, next action | upstream remains canonical |
| Starter Skills | `.folderdesk/skills/` | reusable local HOW | may move to a separate Skills repo only when earned |
| External systems | connectors/APIs/native apps | live CRM/ERP/files/calendar/etc. | remain authoritative |
| Additional GitHub repositories | none by default | explicit separated ownership or execution boundaries | add only when justified |

## Profile

The generated non-secret profile is `folderdesk.json` and uses `folderdesk_version`.

```bash
python3 scripts/folderdesk.py onboard --output folderdesk.json
```

The default profile contains exactly one `workspace` repository. `domains[]` describes in-repository context such as Sales or Delivery; it does **not** create domain repositories.

To expand later, explicitly add another `repositories[]` entry. Valid reasons include:

- materially different ownership or access boundary;
- independent lifecycle/release boundary;
- genuine concurrency or isolated execution need;
- security/privacy separation;
- a large mature capability that is demonstrably easier to operate separately.

“Because we have several departments” is not enough by itself.

## Safe Harbour

Export a non-secret architecture manifest:

```bash
python3 scripts/folderdesk.py export \
  --config folderdesk.json \
  --output folderdesk-estate.json \
  --inspect-target
```

Inspect or restore it:

```bash
python3 scripts/folderdesk.py restore-plan --manifest folderdesk-estate.json --inspect-target
python3 scripts/folderdesk.py restore --manifest folderdesk-estate.json --apply
```

The v2 manifest uses:

- `manifest_schema: "2.0"`;
- `folderdesk_version`;
- `repositories` for the primary workspace plus any explicit expansion repos;
- `domains` for logical in-repository domains;
- `integrations` for named external owners only;
- no credential values or copied external-system records.

Restore creates only missing configured repositories and leaves existing ones unchanged.

## Boundary

FolderDesk is an operating/context substrate, not a replacement for transactional databases, CRMs, accounting systems or private file stores. Keep those systems authoritative and connect them when useful.

## Acceptance

A valid default deployment can start from one repository, perform useful work immediately, preserve reusable context, and expand without redesign when a real boundary later appears.
