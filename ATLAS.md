# Atlas — ARC Front Door

Atlas is the single onboarding and navigation entrypoint for ARC.

It exists so a founder, operator or AI agent does not need to understand the whole repository before beginning.

## Say this to your agent

```text
Use the Atlas skill in this repository.
I want to deploy ARC for my business.
Start in plan mode and tell me what you can infer from the current environment.
Ask only for information you genuinely cannot resolve.
Do not mutate anything until the plan and target ownership map are explicit.
```

On supported IDE prompt-file surfaces, invoke:

```text
/atlas
```

## What Atlas should establish

Atlas needs enough information to answer six questions:

1. **Purpose** — what business/environment is ARC supporting?
2. **GitHub home** — user account or organisation, and desired repository visibility defaults.
3. **Domains** — what business units, products or workflows need their own truth owners?
4. **Private files** — where confidential documents should live.
5. **Specialist systems** — which systems already own CRM, finance, HR, ATS, service delivery or other structured state?
6. **Execution** — can normal APIs/connectors/tools perform the work, or is a trusted runtime genuinely required?

If the user already supplied an answer, do not ask again.

## Atlas output

Before mutation, return a compact deployment plan containing:

```text
Target
Core repositories
Domain repositories
Truth-owner map
Skills strategy
Research strategy
Agent entrypoints
Private-file owner
Specialist-system owners
Runtime requirement
Credential/manual-input list
Bootstrap command
Verification plan
```

The plan should distinguish:

- **required core**;
- **optional module**;
- **existing system to integrate**;
- **future improvement**.

## Default deployment route

```text
read ARC
-> select profile
-> inspect target GitHub state
-> create/adjust arc.json
-> doctor
-> plan
-> founder/operator reviews plan
-> bootstrap --apply
-> verify
-> onboard agents
-> connect specialist systems deliberately
-> run one real business workflow
-> capture reusable learning
```

## Minimum information path

For a brand-new GitHub organisation with no existing operating architecture, Atlas can start with:

```text
business name
GitHub organisation/login
private vs public default
first 1-3 business domains
private-file store
known specialist systems
```

Everything else should be derived or postponed until needed.

## Existing-business path

For an established business, do **not** force replacement.

Inventory first:

```text
existing GitHub repos
existing SOP/knowledge stores
existing automations
existing CRM/ERP/ATS/accounting
private file stores
agent providers/tools
credentials and identity boundaries
```

Then classify each item:

```text
KEEP
INTEGRATE
MIGRATE
RESEARCH
RETIRE
```

## Learning path

If the user wants to understand why ARC is designed this way rather than only deploy it, route them to the [GitHub Course](https://github.com/tbhrc/gh-course).

The Course teaches the journey. ARC packages the deployable architecture.
