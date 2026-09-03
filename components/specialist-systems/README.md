# Specialist Systems Component

Specialist systems remain authoritative for the live structured fields they are selected to own. ARC coordinates work around them without cloning their databases into GitHub.

## Common integration contract

Every specialist-system integration must answer:

1. **Owner** — which system is authoritative for the live field/state?
2. **Purpose** — what bounded business capability does the integration provide?
3. **Method** — which reusable Skill/instruction governs agent behaviour?
4. **Identity** — which narrow authorised connector/API/account performs the action?
5. **Authority** — read, create, update, delete, admin or break-glass; do not infer more than granted.
6. **Evidence** — what real system state proves success?
7. **Durable work** — which GitHub owner records the decision/Issue/PR when durable coordination is required?
8. **Recovery** — who backs up/reprovisions the specialist system, identity and data outside ARC?

```text
business need
→ reusable Skill
→ specialist-system owner
→ least-privilege identity
→ bounded read/write
→ verify actual system state
→ durable GitHub evidence where needed
→ specialist system remains source of truth
```

## Supported integration classes

| Class | Typical live owner | GitHub/ARC owns | Must not be mirrored as GitHub canon |
|---|---|---|---|
| Email / calendar / identity | Microsoft 365, Google Workspace | durable workflow, architecture, integration decisions | mailboxes, calendars, directory state |
| Private files | SharePoint, OneDrive, Google Drive or declared file store | file ownership map, durable work references | private/client/personnel file contents |
| CRM / sales | HubSpot, HighLevel, Salesforce or declared CRM | sales process HOW, durable implementation work | contacts, deals, activities, pipeline state |
| ATS / HRIS | declared ATS/HRIS | recruitment/HR workflow HOW, integration work | candidates, applications, personnel records |
| Finance / accounting / ERP | Zoho Books, Xero, QuickBooks, ERP | finance operating method and integration work | invoices, ledgers, payments, accounting records |
| Website / CMS / DNS | website repo + CMS/hosting/DNS provider | site code/config decisions, deployment work | provider control-plane state unless explicitly versioned/non-secret |
| Database / warehouse / BI | declared database/warehouse/BI tool | schemas/contracts where intentionally canonical, analytics work | production rows and credentials |
| Support / service | helpdesk, CRM/service platform | service workflow HOW, durable changes | tickets/conversations unless GitHub is explicitly the service owner |
| Memory / knowledge | declared knowledge store + derived memory layer | knowledge architecture and reusable method | memory as substitute for current business canon |
| Trusted runtime | runtime owner / AI Engine equivalent | runtime contract and implementation evidence | root credentials, machine secrets, mutable machine state |

## Read/write discipline

- Read only the fields required to answer or execute the current task.
- Write only when the user/owner has authorised the relevant action.
- Prefer typed/native connector actions over scraping or copying whole datasets.
- Verify writes from the specialist system after mutation.
- Agents must **never mirror the specialist system** into GitHub or ARC merely for convenience; the live owner remains authoritative.
- Do not convert a temporary export into a new source of truth.
- If the integration exposes a recurring tooling limitation, route the capability gap through Research rather than repeatedly adding local workarounds.

## Identity and credential boundary

Prefer, in order:

```text
native connected identity / OAuth / GitHub token scoped to job
→ service identity with minimum required scope
→ explicitly provisioned API credential
→ trusted-runtime credential only when the capability truly lives there
→ founder/root break-glass only under explicit current approval
```

Secret **names/purposes** may be documented. Secret **values** must never enter ARC files, Issues, PRs, prompts, logs, artifacts, examples or estate manifests.

## Integration lifecycle

```text
DECLARE owner + scope
→ CONNECT narrow identity
→ TEST bounded read
→ TEST bounded write only if required/authorised
→ VERIFY owner state
→ OPERATE through Skill
→ ROTATE/REVOKE credentials per owner policy
→ REMOVE temporary privilege/bridges
```

Temporary privilege is not complete until teardown is verified.

## Return path

When an agent arrives here from a domain workflow, return to:

- the target organisation's Skills canon for reusable HOW;
- its Research owner for capability discovery/proving;
- the domain/operations Issue that owns the durable business outcome;
- the specialist system itself for current live state.

ARC defines the portable integration contract. It does not become the owner of client data.
