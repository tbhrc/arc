# ARC Security and Governance Baseline

ARC defaults to **least privilege, explicit ownership, reviewable mutation and recoverable authority**.

## Repository visibility

Choose visibility from the information class, not convenience.

### Public is appropriate when

- the content is reusable architecture, code, Skills, documentation or non-sensitive examples;
- no client/personnel/private operational evidence is embedded;
- exposure would not disclose credentials, internal identifiers or confidential commercial state.

### Private is appropriate when

- the repository contains client/candidate/personnel evidence;
- internal business records or sensitive commercial material are durable there;
- operational metadata itself is confidential;
- a contractual/legal/security boundary requires restricted access.

Do not make private data public merely because ARC itself is public.

## Branch and merge baseline

For repositories where changes can materially affect production, security, automation or shared operating method:

- protect the default branch or use an equivalent ruleset;
- require PR-based integration for material multi-file/code/automation changes;
- require status checks that test the real affected contract;
- prevent accidental force-push/deletion of the primary branch unless a deliberate recovery policy needs it;
- use CODEOWNERS or repository ownership rules where meaningful review ownership exists;
- avoid adding ceremony to low-risk repositories where it does not reduce risk.

## Actions permissions

Default workflow permissions to read-only and elevate per job/workflow only when required.

```yaml
permissions:
  contents: read
```

A workflow that needs write access should declare only the needed scope. Do not grant repository/org administration to ordinary CI.

Treat third-party Actions and external workflow input as supply-chain/untrusted-input surfaces. Pin or govern dependencies proportionately to risk.

## Agent authority

Repository write access does not imply:

- organisation administration;
- secret administration;
- root/VPS authority;
- permission to send email or modify CRM/accounting state;
- permission to delete or publish private files;
- permission to deploy production resources.

Agents must resolve the specific action authority in the owning system.

## Runner trust boundary

GitHub-hosted runners are preferred for deterministic work when sufficient.

Self-hosted runners and VPS/local runtimes may carry persistent credentials, network access or machine-local profiles. Treat them as privileged infrastructure:

- scope repository access and labels deliberately;
- do not expose a privileged runner to arbitrary untrusted pull-request code;
- isolate credentials and workloads by risk/domain where practical;
- verify service/runner identity before dispatch;
- remove retired runners and revoke stale credentials;
- record the runtime owner and recovery path.

## Break-glass / root authority

Founder/root credentials are exceptional.

```text
ordinary authorised capability
→ scoped service/repository identity
→ trusted runtime when genuinely required
→ root/break-glass only with explicit current approval
```

A root credential must never become the easiest default path. After temporary privileged work, verify the resulting state and tear down any temporary bridge or elevated permission.

## Credential lifecycle

Every non-ephemeral credential should have:

- owner;
- purpose;
- storage location **by name**, never value;
- minimum scope;
- provisioning method;
- rotation trigger/cadence;
- revocation path;
- dependency/consumer map where material.

Do not invent a secret when native identity or stable non-sensitive configuration is enough.

## Public-example safety

ARC examples must use placeholders and generic identifiers. Never publish:

- real passwords/tokens/private keys;
- copied client/candidate/personnel evidence;
- internal confidential mail/calendar/file contents;
- production database rows;
- private specialist-system exports;
- live root/runtime credentials even if partially masked.

## Verification

Security acceptance is evidence-based:

- inspect repository visibility and intended data class;
- inspect workflow `permissions` where Actions can mutate;
- confirm credential values are absent from tracked public files/examples;
- confirm privileged runtimes are optional and bounded;
- confirm temporary privilege/bridges were removed;
- confirm current live owner state after a sensitive mutation.

ARC's deterministic checks are guardrails, not a substitute for provider/system security controls or professional security review where risk requires it.
