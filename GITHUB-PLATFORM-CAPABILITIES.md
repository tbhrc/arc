# FolderDesk V5 — GitHub Platform Capability Inventory

**Status:** Canonical product/reference inventory — discussion-stage knowledge promoted under [#53](https://github.com/tbhrc/folderdesk/issues/53)  
**Product owner:** [`tbhrc/folderdesk`](https://github.com/tbhrc/folderdesk)  
**General FolderDesk catalogue:** [`FEATURES.md`](FEATURES.md)  
**As-of date:** 10 September 2026

## Why this document exists

FolderDesk changed category when it moved from a local hard-drive implementation onto GitHub as its durable operating substrate.

The earlier product could organise files and tasks locally. The GitHub-native architecture inherits a much larger platform surface: durable version history, indexed search, identity and access control, organisation/repository boundaries, Issues and Projects, review controls, automation, secrets handling, Apps/OAuth, APIs, webhooks, auditability, enterprise policy, security tooling, release management and extensibility.

Those capabilities are not merely engineering conveniences. They are part of the product leverage behind FolderDesk V5 and must be visible in product, sales and architecture discussions without falsely claiming that every optional GitHub feature is already enabled in every FolderDesk deployment.

## Product-era boundary

This document uses the founder-defined FolderDesk product eras:

- **V3 — local / hard-drive era.** FolderDesk operated primarily from the computer filesystem. Work items were treated as local tasks and the product did not inherit GitHub's organisation, access, search, API, automation, audit and enterprise platform surface.
- **V4 — failed build.** Historical references may remain for provenance, but V4 is not the current product baseline.
- **V5 — clean GitHub-native era.** GitHub is the durable backend/operating substrate and FolderDesk can use or connect the platform capabilities below.

**Important versioning boundary:** `V5` is currently a **product-era/generation identity**. The repository's formal software release line remains semantic versioning (`vMAJOR.MINOR.PATCH`; currently `1.3.0`) until [#53](https://github.com/tbhrc/folderdesk/issues/53) explicitly reconciles whether product-era V5 should also map to a software major version.

## Capability-state legend

- **ACTIVE** — currently evidenced in FolderDesk or the TBHRC/iMPLEMENTAi reference implementation.
- **NATIVE** — a GitHub platform capability that the GitHub-native architecture can inherit/use, but this document does not claim it is configured in every FolderDesk deployment.
- **CONDITIONAL** — depends materially on GitHub plan/licence, enterprise configuration, repository settings, permissions, Copilot, Apps/OAuth, Actions/runners or another explicit activation.

A capability can be strategically important even when classified NATIVE or CONDITIONAL. Sales claims must not convert those labels into an assertion that a particular client has already enabled the feature.

## The search breakthrough — a critical V5 distinction

FolderDesk V5 does **not** depend on primitive recursive file reads as its only discovery mechanism.

GitHub Code Search is an indexed, code-aware search system with exact-string search, Boolean expressions, regular expressions, repository/organisation/enterprise scoping, path/language/content qualifiers and symbol search. GitHub also provides code navigation to definitions and references. Private repositories are searchable by authorised users when indexed.

Separately, GitHub Copilot can use a **semantic code search index** and repository context to answer natural-language questions about a codebase. That is a Copilot-dependent capability and must not be confused with standard GitHub Code Search. FolderDesk may additionally combine GitHub search with its own authorised semantic-memory/retrieval layers such as Hindsight where appropriate.

This distinction matters commercially: the breakthrough is not "grep got faster". The operating environment gained **indexed, structured, permission-aware and optionally semantic retrieval over durable organisational context**.

---

# Capability inventory

## A. Repository and version-control substrate

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| A01 | Durable Git repositories as persistent workspaces | ACTIVE | Canonical operating surfaces survive chat/runtime loss. |
| A02 | Distributed cloning of repository history | NATIVE | Durable context can be copied/recovered without one machine being the only source. |
| A03 | Commit-based immutable change history | ACTIVE | Material changes are attributable and recoverable. |
| A04 | Branches for isolated change streams | ACTIVE | Agents/humans can separate work without overwriting `main`. |
| A05 | Tags for named historical anchors | ACTIVE | Known-good versions can be referenced deterministically. |
| A06 | Commit and branch diff/compare views | ACTIVE | Agents can inspect exactly what changed. |
| A07 | Per-line blame/history | NATIVE | Provenance can be traced to the change that introduced a line. |
| A08 | Configurable default branch | ACTIVE | One canonical current branch can be declared. |
| A09 | Branch rename support | NATIVE | Repository conventions can evolve while preserving history. |
| A10 | Public/private repository visibility | NATIVE | Business context can be separated by appropriate visibility. |
| A11 | Internal repository visibility inside enterprises | CONDITIONAL | Enterprise-only shared surfaces can exist without public exposure. |
| A12 | Repository archiving/read-only preservation | NATIVE | Historical owners can be frozen without deleting provenance. |
| A13 | Fork networks | NATIVE | Controlled derivatives/experiments can retain upstream ancestry. |
| A14 | Template repositories | NATIVE | Repeatable structures can be instantiated without hand-copying every file. |
| A15 | Branch protection and repository rulesets | NATIVE | Important branches/tags can enforce required change conditions. |

## B. Search, indexing and discovery

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| B01 | Integrated GitHub search across platform resources | ACTIVE | Agents can find durable work without knowing the exact path first. |
| B02 | Repository-scoped search | ACTIVE | Retrieval can be bounded to the known owner. |
| B03 | Organisation-scoped code search | ACTIVE | Agents can search across the organisation instead of repo-by-repo file scans. |
| B04 | Enterprise-scoped code search | CONDITIONAL | Large estates can search organisation-owned repositories under one enterprise scope. |
| B05 | Indexed private-repository code search for authorised users | NATIVE | Permission-aware retrieval extends to private canon. |
| B06 | Exact-string code search | NATIVE | Precise identifiers/phrases can be located reliably. |
| B07 | Boolean `AND` / `OR` / `NOT` code queries | NATIVE | Complex discovery can be expressed directly. |
| B08 | Parenthesised/nested Boolean expressions | NATIVE | Search can encode richer logic than sequential grepping. |
| B09 | Regular-expression code search | NATIVE | Patterns can be found across repositories and paths. |
| B10 | `path:` search with path/glob targeting | NATIVE | Agents can search structural regions without reading entire trees. |
| B11 | `language:` search qualification | NATIVE | Results can be restricted to relevant code/content languages. |
| B12 | `content:` qualification distinct from filename/path matches | NATIVE | Search can target actual file content rather than ambiguous path hits. |
| B13 | Symbol-definition search | NATIVE | Functions/classes/symbols can be found structurally. |
| B14 | Code navigation to definitions and references | NATIVE | Agents can move through code relationships without manual text scanning. |
| B15 | Semantic repository/code indexing for GitHub Copilot | CONDITIONAL | Natural-language codebase discovery can use semantic retrieval when Copilot/indexing is enabled. |

## C. Issues and durable work management

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| C01 | GitHub Issues as durable work identities | ACTIVE | Work survives sessions and can be resumed by another authorised agent. |
| C02 | Issue assignees | NATIVE | Explicit human/agent responsibility can be represented. |
| C03 | Labels | ACTIVE | Lifecycle, priority and operational classification are searchable metadata. |
| C04 | Milestones | NATIVE | Related Issues/PRs can be grouped toward a delivery target. |
| C05 | Organisation issue types | NATIVE | Work can be typed beyond ad-hoc title prefixes. |
| C06 | Issue templates and Issue Forms | NATIVE | Structured intake can be standardised. |
| C07 | Organisation issue fields | NATIVE | Typed metadata such as priority, effort or dates can live on work items. |
| C08 | Sub-issues | NATIVE | Large work can be decomposed while retaining parent context. |
| C09 | Parent/sub-issue progress tracking | NATIVE | Completion state can roll up to larger work. |
| C10 | Issue ↔ pull-request linking | ACTIVE | Implementation evidence can point directly to the work controller. |
| C11 | Closing keywords from pull requests/commits | NATIVE | Completion can reconcile automatically when changes merge. |
| C12 | Durable Issue comments and timeline | ACTIVE | Material discussion/decision chronology is externally recoverable. |
| C13 | Reactions, @mentions and team mentions | NATIVE | Lightweight signalling and targeted attention are built in. |
| C14 | Native close reasons such as completed / not planned / reopened | ACTIVE | Final state can preserve semantic meaning. |
| C15 | Advanced Issue/PR filtering and cross-repository dashboards | ACTIVE | "What is pending?" can be answered from structured durable state rather than memory alone. |

## D. Projects, planning and portfolio views

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| D01 | User and organisation Projects | NATIVE | Work across repositories can be aggregated into a planning surface. |
| D02 | High-density table views | NATIVE | Structured work can be managed like a live spreadsheet. |
| D03 | Kanban/board views | NATIVE | Work state can be visualised without building a custom task UI. |
| D04 | Roadmap/timeline views | NATIVE | Delivery horizons can be viewed over time. |
| D05 | Multiple saved project views | NATIVE | Different teams/agents can see the same truth through different lenses. |
| D06 | Project filters | NATIVE | Large portfolios can be reduced to the relevant slice. |
| D07 | Sort/group/slice controls | NATIVE | Work can be reorganised by owner, state, priority, iteration or other fields. |
| D08 | Custom text fields | NATIVE | Free-text operational metadata can be attached without a new database. |
| D09 | Custom number fields | NATIVE | Estimates/scores/capacity metrics can be structured. |
| D10 | Custom date fields | NATIVE | Target dates can be tracked and visualised. |
| D11 | Custom single-select fields | NATIVE | Consistent controlled classifications can be added. |
| D12 | Iteration fields with repeating time blocks and breaks | NATIVE | Sprint/cycle planning is available without external PM software. |
| D13 | Parent issue, sub-issue progress and PR fields in Projects | NATIVE | Hierarchy and implementation state can be surfaced in portfolio views. |
| D14 | Configurable charts/insights | NATIVE | Work trends and distributions can be visualised from current project data. |
| D15 | Built-in, API and Actions-based Project automation | NATIVE | Project maintenance can be automated instead of manually copied between systems. |

## E. Pull requests, review and governed change

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| E01 | Pull requests as explicit change proposals | ACTIVE | Material repository mutations can be reviewed before merge. |
| E02 | Draft pull requests | NATIVE | Work-in-progress can be visible without signalling readiness. |
| E03 | Individual review requests | NATIVE | Specific reviewers can be routed into consequential changes. |
| E04 | Team review requests | NATIVE | Review responsibility can follow organisational teams. |
| E05 | Inline review comments and threaded conversations | NATIVE | Evidence and challenge attach to the exact changed lines. |
| E06 | Suggested changes in review | NATIVE | Reviewers can propose directly applicable patches. |
| E07 | `CODEOWNERS` ownership mapping | NATIVE | Files/paths can have declared responsible people/teams. |
| E08 | Required Code Owner review | NATIVE | Sensitive paths can require owner approval. |
| E09 | Required approval counts | NATIVE | Merge can depend on a defined review threshold. |
| E10 | Dismiss stale approvals after new changes | NATIVE | Approval can be invalidated when reviewed content materially changes. |
| E11 | Require approval of the most recent reviewable push | NATIVE | Last-minute changes cannot silently inherit old approval. |
| E12 | Required status checks | ACTIVE | Tests/validation can become deterministic merge conditions. |
| E13 | Required conversation resolution | NATIVE | Unresolved review threads can block merge. |
| E14 | Auto-merge after requirements are satisfied | NATIVE | Approved low-friction changes can complete without manual babysitting. |
| E15 | Merge queue | CONDITIONAL | High-change repositories can serialise validated merges safely at scale. |

## F. Identity, access and multi-tenant boundary primitives

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| F01 | GitHub Organisations as separate administrative namespaces | ACTIVE | Businesses/clients can have explicit owner boundaries rather than one local folder tree. |
| F02 | Enterprise accounts spanning multiple organisations | CONDITIONAL | Larger clients can govern multiple organisations centrally. |
| F03 | Teams for group access management | NATIVE | Repository access can follow business structure. |
| F04 | Nested teams | NATIVE | Organisational hierarchy can be represented without duplicating permissions manually. |
| F05 | Visible and secret team visibility | NATIVE | Team discoverability can match collaboration/privacy needs. |
| F06 | Repository roles: Read, Triage, Write, Maintain, Admin | NATIVE | Access can be differentiated by job rather than all-or-nothing file-system access. |
| F07 | Organisation base repository permissions | NATIVE | Default member access can be governed centrally. |
| F08 | Outside collaborators | NATIVE | Clients/consultants can receive bounded repository access without full organisation membership. |
| F09 | Predefined organisation roles | NATIVE | Administration can be delegated by function. |
| F10 | Custom organisation roles | CONDITIONAL | Enterprise clients can build more granular admin roles. |
| F11 | Custom repository roles | CONDITIONAL | Enterprise clients can create repository access profiles beyond the default five roles. |
| F12 | Security Manager, CI/CD Admin and App Manager delegation | NATIVE | Security, automation and app administration can be separated from full ownership. |
| F13 | Organisation/enterprise two-factor-authentication enforcement | NATIVE | Stronger user authentication can be required centrally. |
| F14 | SAML SSO, SCIM provisioning and identity-provider team synchronisation | CONDITIONAL | Corporate identity lifecycle can control GitHub access and team membership. |
| F15 | Enterprise Managed Users with SAML/OIDC and conditional-access integration | CONDITIONAL | Enterprise identity can be centrally provisioned and governed by the client's IdP. |

### FolderDesk-specific multi-tenant note

GitHub's organisations, enterprises, repositories, teams and roles are **segmentation/control primitives**, not by themselves a complete application-level multi-tenant data model. FolderDesk's current reference implementation separately carries explicit tenant deployment context (`tenant_id` / optional canonical entity reference) through deployment and recovery under [FolderDesk #49](https://github.com/tbhrc/folderdesk/issues/49). The two layers complement each other and should not be conflated.

## G. Secrets, security and software-supply-chain controls

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| G01 | GitHub Actions secrets at organisation, repository and environment scope | NATIVE | Workflow credentials need not be stored in repository files. |
| G02 | Client-side encryption of Actions secrets before reaching GitHub | NATIVE | Secret values are protected in transit into GitHub's storage path. |
| G03 | Automatic redaction of recognised secrets from Actions logs | NATIVE | Accidental log exposure risk is reduced. |
| G04 | Secret scope precedence | NATIVE | Environment/repository/organisation boundaries can override more general values. |
| G05 | Environment secrets loaded when the referencing job starts | NATIVE | Sensitive deployment values can remain unavailable until the protected environment is entered. |
| G06 | Configuration variables separate from encrypted secrets | NATIVE | Non-secret configuration does not need to be mixed with credentials. |
| G07 | Configurable `GITHUB_TOKEN` permissions | NATIVE | Workflow authority can be purpose-fit rather than implicitly broad. |
| G08 | OpenID Connect federation from Actions to cloud providers | NATIVE | Cloud automation can use short-lived identity instead of long-lived cloud secrets. |
| G09 | Secret scanning | CONDITIONAL | Exposed credentials can be detected across repository history. |
| G10 | Push protection for secrets | CONDITIONAL | Supported secrets can be blocked before they are committed. |
| G11 | Custom secret-scanning patterns | CONDITIONAL | Organisations can detect credential formats specific to their estate. |
| G12 | Code scanning | CONDITIONAL | Vulnerabilities and coding errors can be detected inside the repository workflow. |
| G13 | CodeQL analysis with default or advanced setup | CONDITIONAL | GitHub-native static analysis can be standardised across repositories. |
| G14 | SARIF ingestion from third-party scanners | CONDITIONAL | External security tools can report into one GitHub alert surface. |
| G15 | Dependency graph | NATIVE | Repository dependency relationships can be inventoried automatically. |
| G16 | Dependabot vulnerability alerts | NATIVE | Known vulnerable dependencies can raise actionable alerts. |
| G17 | Dependabot security updates | NATIVE | Security-fix pull requests can be generated automatically. |
| G18 | Dependabot version updates | NATIVE | Dependency currency can be automated on a controlled schedule. |
| G19 | Repository security advisories | NATIVE | Vulnerabilities can be discussed/fixed privately before disclosure. |
| G20 | Private vulnerability reporting | NATIVE | External researchers can report supported public-repository vulnerabilities privately. |
| G21 | Copilot Autofix / AI-assisted code-scanning remediation | CONDITIONAL | Security alerts can receive generated fix proposals subject to review. |

## H. GitHub Apps, OAuth, APIs, webhooks and integration surface

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| H01 | GitHub Apps | NATIVE | Purpose-built integrations can operate natively inside the GitHub permission model. |
| H02 | Fine-grained GitHub App permissions | NATIVE | Apps can request specific resource permissions rather than blanket account access. |
| H03 | Per-installation repository selection for GitHub Apps | NATIVE | An app can be restricted to selected repositories. |
| H04 | Short-lived GitHub App installation tokens | NATIVE | Automations do not need permanent user tokens for routine operation. |
| H05 | GitHub Apps acting independently of a human user | NATIVE | Durable automation can survive staff turnover where correctly installed. |
| H06 | GitHub App user access tokens for actions on behalf of users | NATIVE | Integrations can combine app identity with explicit user authority. |
| H07 | Centralised webhook subscriptions for GitHub Apps | NATIVE | Apps can react to events across authorised repositories/organisations. |
| H08 | OAuth Apps | NATIVE | User-authorised integrations remain supported where OAuth is the right model. |
| H09 | OAuth 2.0 web/device flows, scopes and refresh patterns | NATIVE | External applications can establish explicit user consent and token lifecycle. |
| H10 | Repository webhooks | NATIVE | External systems can receive repository events without polling. |
| H11 | Organisation webhooks | NATIVE | Organisation-level events can feed external automation/integration. |
| H12 | Versioned REST API | ACTIVE | Agents/connectors can read and mutate GitHub through stable machine interfaces. |
| H13 | GraphQL API | NATIVE | Complex connected GitHub data can be queried with selective fields. |
| H14 | Fine-grained personal access tokens | NATIVE | Human/token automation can be scoped more narrowly than classic PATs. |
| H15 | Deploy keys | NATIVE | Repository-specific SSH automation is available where appropriate. |
| H16 | GitHub CLI | ACTIVE | Agents/runtimes can perform GitHub operations through a mature command interface. |
| H17 | Git over SSH and HTTPS | ACTIVE | Repositories can integrate with standard Git tooling/runtimes. |
| H18 | Checks/status APIs | ACTIVE | External and GitHub-native validators can publish machine-readable pass/fail evidence. |

## I. GitHub Actions, automation, runners and deployment controls

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| I01 | Event-driven Actions workflows | ACTIVE | Repository events can trigger deterministic automation. |
| I02 | Scheduled workflows | ACTIVE | Recurring verification/reconciliation can run without a persistent custom daemon. |
| I03 | Manual workflow dispatch | NATIVE | Operators can invoke controlled automation on demand. |
| I04 | Multi-job workflows | NATIVE | Complex processes can be decomposed into explicit execution stages. |
| I05 | Script and GitHub CLI execution in workflows | ACTIVE | Existing deterministic tooling can run inside the GitHub control plane. |
| I06 | Matrix jobs | NATIVE | The same validation can run across multiple versions/platforms/configurations. |
| I07 | Conditional job/step execution | NATIVE | Workflows can skip irrelevant branches of work. |
| I08 | Job dependency graphs (`needs`) | NATIVE | Ordered execution and gating can be expressed declaratively. |
| I09 | Outputs passed between jobs | NATIVE | Deterministic results can flow to downstream stages. |
| I10 | Reusable workflows | ACTIVE | Proven automation can be called instead of copied. |
| I11 | Workflow templates and composite actions | NATIVE | Common operational patterns can be packaged and reused. |
| I12 | Workflow/environment/configuration variables | NATIVE | Reusable automation can be parameterised without hard-coding values. |
| I13 | GitHub-hosted runners | NATIVE | Automation can execute without the client operating runner infrastructure. |
| I14 | Self-hosted runners | ACTIVE | Work can execute on controlled Mac/Linux/VPS/on-prem/cloud hardware. |
| I15 | Runner groups and scoped runner access | CONDITIONAL | Runner availability can be governed across repositories/organisations. |
| I16 | Actions Runner Controller (ARC) Kubernetes autoscaling | ACTIVE | GitHub's reference scale-set architecture can elastically operate self-hosted runners. |
| I17 | Ephemeral autoscaled self-hosted runners | NATIVE | Clean one-job runner patterns can reduce cross-job state leakage. |
| I18 | Workflow/job concurrency groups and cancel-in-progress | NATIVE | Duplicate/conflicting automation can be serialised or superseded. |
| I19 | Deployment environments and protection rules | NATIVE | Sensitive deployment stages can have explicit environment boundaries. |
| I20 | Workflow artifacts | NATIVE | Build/test/output evidence can persist after a run. |
| I21 | Actions caches | NATIVE | Repeated workflows can reuse expensive dependencies/build state. |
| I22 | Workflow-level and job-level permission controls | NATIVE | Automation authority can be bounded at the execution point. |
| I23 | Enterprise/organisation Actions policy controls | CONDITIONAL | Clients can govern which Actions/runners/workflows are permitted at scale. |

## J. Enterprise governance, auditability, collaboration and distribution

| ID | Capability | State | FolderDesk leverage |
|---|---|---|---|
| J01 | Organisation audit log | NATIVE | Administrative/security activity can be reviewed after the fact. |
| J02 | Enterprise-wide aggregated audit log | CONDITIONAL | Activity across multiple organisations can be reviewed centrally. |
| J03 | Searchable audit events | CONDITIONAL | Specific actions/settings/access changes can be investigated efficiently. |
| J04 | Identification of audit events performed by access tokens | CONDITIONAL | Machine actions can be traced to token identities. |
| J05 | Audit-log export | CONDITIONAL | Audit evidence can be retained/analyzed outside GitHub. |
| J06 | Audit-log streaming | CONDITIONAL | Events can feed SIEM/data systems such as S3, Azure, Datadog, GCS or Splunk. |
| J07 | Enterprise/global webhooks | CONDITIONAL | Enterprise events can drive external monitoring/integration. |
| J08 | Enterprise IP allow lists | CONDITIONAL | Access to protected resources can be bounded by network source where required. |
| J09 | Enterprise policies for repositories, Actions, security and PATs | CONDITIONAL | Large clients can enforce platform-wide operating standards. |
| J10 | Repository policies for creation, deletion, transfer, visibility and naming | CONDITIONAL | Repository lifecycle and naming can be governed centrally. |
| J11 | Enterprise/organisation rulesets across multiple repositories | CONDITIONAL | Change controls can be managed consistently at scale. |
| J12 | Custom repository properties | CONDITIONAL | Repositories can carry structured enterprise metadata for governance/targeting. |
| J13 | GitHub Releases | ACTIVE | Known-good FolderDesk packages can be published from exact Git history. |
| J14 | Release notes and downloadable release assets | NATIVE | Versioned distribution can include human/machine consumption artifacts. |
| J15 | GitHub Packages | NATIVE | Packages/containers can be distributed alongside source where relevant. |
| J16 | GitHub Discussions | NATIVE | Longer-form community/product conversations can live beside the repository. |
| J17 | Repository wikis | NATIVE | Supplemental knowledge spaces are available when they add value. |
| J18 | GitHub Pages | NATIVE | Repository-backed public documentation/sites can be published without a separate CMS. |
| J19 | Notifications and repository/release subscriptions | NATIVE | Humans can follow the changes that matter without polling everything. |
| J20 | User/team mentions and review notifications | NATIVE | Attention routing is part of the platform rather than an external manual process. |
| J21 | GitHub Flavoured Markdown, task lists and rich linking | ACTIVE | Human-readable operational docs remain structured, linkable and agent-readable. |
| J22 | Repository Insights / contributors / activity views | NATIVE | Repository activity and participation can be inspected without building custom analytics first. |

---

# What this means for FolderDesk V5

The platform inheritance changes the commercial description of FolderDesk.

FolderDesk V5 is not simply "the same local folder organiser, now stored online". The GitHub move introduces a durable enterprise operating substrate around the FolderDesk method:

1. **Durability:** work, context, decisions and changes have external identities and history.
2. **Findability:** indexed/structured search replaces blind filesystem traversal as the primary discovery layer; semantic repository retrieval is additionally available through Copilot where enabled.
3. **Governance:** organisations, teams, roles, rulesets, review requirements and enterprise policies create real control surfaces.
4. **Security:** scoped secrets, token permissions, OIDC, scanning and supply-chain controls can be used instead of placing credentials/configuration directly into local files.
5. **Integration:** GitHub Apps, OAuth, APIs, webhooks and CLI make the operating desk programmable and connectable.
6. **Automation:** Actions and runner infrastructure convert repeatable agent/human operations into deterministic workflows when that is the right lever.
7. **Enterprise readiness:** SSO/SCIM/managed users, audit streams, IP controls, central policies and multi-organisation governance are available for clients whose plan and requirements justify them.
8. **Portability:** Git repositories, releases and standard interfaces reduce dependence on one machine, one AI provider or one session.

This is the pivotal difference between the V3 local era and the V5 GitHub-native era.

## Current FolderDesk evidence already proving part of this layer

- [`FEATURES.md`](FEATURES.md) — GitHub is already defined as the canonical operating desk and work-continuity surface.
- [FolderDesk #49](https://github.com/tbhrc/folderdesk/issues/49) — implemented multi-tenant deployment/recovery context with explicit tenant identity boundaries.
- [FolderDesk #48](https://github.com/tbhrc/folderdesk/issues/48) — GitHub Actions/self-hosted runner reconciliation and deterministic parity automation.
- [FolderDesk #50](https://github.com/tbhrc/folderdesk/issues/50) — verified GitHub-first deployment/recovery and connector/runtime readiness.
- [FolderDesk #51](https://github.com/tbhrc/folderdesk/issues/51) — client deployment feedback and the current GitHub-backed capture/recall product direction.
- [`RELEASES.md`](RELEASES.md) — versioned FolderDesk release and Safe Harbour contract.

## Sales/marketing rule

Treat this document as a **platform capability inventory**, not a blanket promise that every GitHub Enterprise, Advanced Security or Copilot capability is included/configured in every FolderDesk engagement.

For a client claim, distinguish:

```text
FolderDesk capability we implement/use now
+ GitHub-native capability available in the client's plan
+ configuration/integration required to activate it
= truthful client-specific capability statement
```

Do not market standard GitHub Code Search as semantic search. Standard Code Search is indexed/code-aware search; GitHub Copilot semantic indexing is a separate conditional capability.

## Primary current GitHub evidence

Official GitHub documentation used to verify the platform surface represented here:

- [About GitHub Code Search](https://docs.github.com/en/search-github/github-code-search/about-github-code-search)
- [GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)
- [Filtering and searching Issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/filtering-and-searching-issues-and-pull-requests)
- [GitHub Issues documentation](https://docs.github.com/en/issues)
- [Planning and tracking with Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [About CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Managing protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Repository roles for an organisation](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization)
- [Organisation teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)
- [GitHub Apps vs OAuth Apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps)
- [Creating GitHub Apps](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)
- [GitHub Actions workflow capabilities](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do)
- [GitHub Actions secrets](https://docs.github.com/en/actions/concepts/security/secrets)
- [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners)
- [Code security documentation](https://docs.github.com/en/code-security)
- [Secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
- [Code scanning](https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning)
- [Enterprise IAM with SAML/SCIM](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam)
- [Enterprise Managed User authentication](https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/configuring-authentication-for-enterprise-managed-users)
- [Enterprise audit-log streaming](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise)
- [Enterprise policies](https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- [GitHub Copilot repository/codebase context](https://docs.github.com/en/copilot/tutorials/explore-a-codebase)
- [GitHub Copilot context concepts](https://docs.github.com/en/copilot/concepts/context)

Feature availability and GitHub plan packaging can change. Re-verify plan-specific claims against current GitHub documentation before contractual/client use.

## Research boundary

The FolderDesk Independent Advisor evidence corpus was consulted for the architectural framing: it supports durable external state, Git history, one canonical owner and selective retrieval while warning that file organisation alone does not guarantee retrieval quality and that long context/instruction bloat can reduce performance. This inventory therefore treats GitHub's indexed/search/automation/governance layers as leverage **around** the file-native substrate rather than claiming files alone solve enterprise operation.

Research remains **BASELINE / EXPANDING**, not comprehensive. See the canonical FolderDesk Independent Advisor research owner in `tbhrc/research` for the current evidence boundary.
