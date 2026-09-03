# ARC Business Modules

ARC modules are **optional ownership patterns**, not software bundles and not mandatory stacks.

A module answers four questions:

1. What business capability exists?
2. Which system/repository owns its durable truth?
3. Which reusable Skills should agents use?
4. Which specialist systems or runtimes are optional integrations rather than canon?

## Module catalogue

| Module | Typical owner | Examples of specialist systems |
|---|---|---|
| CRM / Sales | `sales` or CRM system | HubSpot, HighLevel, Salesforce |
| Recruitment / HR | `people` / `recruitment` + ATS/HRIS | ATS, HRIS, Microsoft 365 |
| Finance | finance system + bounded repo | Xero, Zoho Books, QuickBooks, ERP |
| Marketing | `marketing` | CMS, ad platforms, social platforms |
| Customer Service | `service` | Helpdesk, CRM, inbox/chat systems |
| Product / Software | product/software repo | GitHub, issue tracker, CI/CD |
| Research | `research` | web, OSS, vendor/source evidence |
| Knowledge / Memory | declared knowledge owner | docs/wiki + derived memory layer |
| Website | website/product repo | CMS, hosting, DNS/provider |
| Reporting / BI | analytics/reporting owner | BI tool, warehouse, spreadsheets |

## Rules

- Select only modules with a real business need.
- Do not create a GitHub repository merely because a module exists.
- Reuse an existing specialist system when it is already the correct owner.
- GitHub coordinates durable work; it does not become CRM, accounting, ATS or file storage by default.
- Each module must have a clear return path to Skills, Research and the owning live system.
- A recurring capability gap may route through Research before ARC introduces another tool.

## Profile contract

Deployment profiles may declare:

```json
"modules": ["sales", "research", "website"]
```

Unknown modules must be treated as configuration errors by tooling once module validation is enabled. Until then, Atlas must validate against this catalogue before apply.
