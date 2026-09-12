---
name: structure
description: "Canonical FolderDesk workspace structure and vocabulary. Use before creating, renaming or moving a semantic folder/file, when deciding where something belongs, or when similar terminology could create duplicate structure."
---

# Structure

**Rule:** one meaning, one canonical term, one canonical route. Similar words route to the existing home; they do not create peer structures.

## Default workspace

```text
repo/
├── README.md
├── AGENTS.md
├── work/
├── knowledge/
├── outputs/
├── archive/
└── .folderdesk/
    └── skills/
```

Native runtime paths such as `.git/`, `.github/`, `.claude/`, package manifests or application source folders may exist when a real platform/tool requires them. They are not precedent for new business taxonomy.

## Codebook

| Canonical term | Similar words | Route | Meaning |
|---|---|---|---|
| `work` | active work, delivery, execution, projects, tasks, jobs, initiatives, cases | `/work/` | Work being done or actively managed. |
| `knowledge` | research, references, guidance, notes, learning, documentation, information | `/knowledge/` | Reusable information that helps work get done. |
| `outputs` | deliverables, reports, submissions, exports, artefacts, final files | `/outputs/` | Finished or externally usable results. |
| `archive` | old, historical, retired, superseded, inactive, closed material | `/archive/` | Retained history that is no longer active. |
| `folderdesk` | runtime, machinery, agents, automation, configuration, internal plumbing | `/.folderdesk/` | Hidden operating support and reusable machinery. |

Domains such as Sales, Finance or Delivery may be shallow subfolders where they improve retrieval, for example `work/sales/` or `knowledge/finance/`. Do not create empty departmental trees merely because the organisation has departments.

## Route

1. Match the intended meaning to the codebook.
2. Reuse the existing canonical home when the meaning already fits.
3. If no route fits, state **STRUCTURAL CHANGE REQUIRED** before inventing a new semantic root.
4. Add the smallest new term only after a recurring real-work need proves the gap.

**Acceptance:** a zero-context agent can answer “where does this belong?” without creating a competing folder system.