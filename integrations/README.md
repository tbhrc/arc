# ARC Integration Classes

ARC integrates with specialist systems through a common rule: **the system that owns the live state remains authoritative**.

Use this catalogue to decide what is being connected, what identity is needed and what must remain outside GitHub.

| Class | Live owner examples | Typical ARC interaction | Verification | Recovery owner |
|---|---|---|---|---|
| Email / calendar / identity | Microsoft 365, Google Workspace | search/read/send, calendar/event operations, directory resolution | re-read message/event/directory state | workspace/identity administrator |
| Private files | SharePoint, OneDrive, Google Drive | search/read/create approved files, reference paths/IDs | fetch exact file/version/path | file-platform administrator/business owner |
| CRM / sales | HubSpot, HighLevel, Salesforce | contacts, companies, deals, notes, pipeline actions | re-read exact record/state | CRM administrator |
| ATS / HRIS | ATS/HRIS provider | candidate/application/employee workflow actions | re-read exact record/stage | HR/ATS administrator |
| Finance / accounting / ERP | Zoho Books, Xero, QuickBooks, ERP | approved transactions/records/reporting | re-read transaction/ledger record | finance/system administrator |
| Website / CMS / DNS | GitHub + CMS/hosting/DNS provider | publish/deploy/configure bounded site state | fetch live route/config/deployment | website/platform administrator |
| Database / warehouse / BI | PostgreSQL, warehouse, BI tool | scoped queries, schema/report changes | query current schema/data/result | data/platform administrator |
| Support / service | helpdesk, CRM/service system | tickets/conversations/service workflow | re-read live ticket/service state | service-system administrator |
| Memory / knowledge | docs/wiki + derived memory | read current knowledge; write derived context after canon | verify against current canonical owner | knowledge/memory owner |
| Trusted runtime | self-hosted runner, VPS, local profile | machine-bound or privileged execution | inspect actual service/machine/job state | runtime administrator |

## Per-integration declaration

Before enabling automation, record this information in the target business's owner/configuration surface:

```text
integration class
system/provider name
live state it owns
business/domain owner
agent actions allowed
identity / connector name (not value)
minimum scope
read/write/admin boundary
verification method
recovery / revocation owner
private-data classification
```

## Handoff rules

### Microsoft 365 / Google Workspace

Mail, calendars and directory entries stay in the workspace. GitHub may own a recruitment/sales/operations Issue that causes an authorised email/calendar action, but it does not mirror the mailbox or calendar.

### Private files

Keep confidential client/personnel documents in the declared private file store. GitHub should retain only the durable work decision and safe file reference/path/ID when needed.

### CRM / ATS / finance

The structured system owns its records. Skills define HOW to operate it; GitHub owns durable implementation/process work; agents verify mutations by re-reading the actual record.

### Website / DNS / hosting

Version safe code/config in GitHub when appropriate. Provider control-plane state remains with the provider unless deliberately exported as non-secret reproducible configuration. DNS credentials never belong in repository files.

### Databases

Do not make data dumps the default agent context. Query only what is necessary. Schema definitions may be versioned when intentionally canonical; production rows and credentials remain external.

### Memory

Memory is derived context. When current truth matters, return to the live owner before acting.

### Trusted runtimes

A runtime is an execution bridge, not the owner of business truth. Persistent machine state and credentials require a separate runtime owner, security boundary and recovery path.

## What ARC automates

ARC may automate a specialist system when all are true:

1. the target owner is explicit;
2. a capable connected action exists;
3. the identity scope is sufficient and no broader than required;
4. the user/business has authorised that class of mutation;
5. the result can be verified from the live system;
6. the operation does not require moving private/live state into ARC.

Otherwise Atlas should keep the step manual, route to the specialist owner, or trigger Research for a missing capability.
