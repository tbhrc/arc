# Changelog

## 0.5.0 — 2026-09-03 — Integrations and Governance

- Expanded specialist-system integration into one portable owner/identity/authority/verification/recovery contract.
- Added integration-class guidance for email/calendar/identity, private files, CRM, ATS/HRIS, finance/ERP, website/CMS/DNS, database/warehouse/BI, support/service, memory/knowledge and trusted runtimes.
- Added the ARC Security and Governance Baseline covering repository visibility, proportional branch/ruleset protection, CODEOWNERS/review ownership, Actions permissions, agent authority and runner trust boundaries.
- Strengthened the credential contract with provisioning, minimum-scope, rotation, revocation, exposure-response and break-glass rules.
- Strengthened the private-files contract so file bytes/permissions/versions remain with the declared private owner.
- Added deterministic security-contract tests for integration coverage, governance sections, read-only default CI permissions and obvious credential-like markers in key public examples.
- Expanded the deployment manifest and verification gates so connected specialist systems and security authority are explicit ARC architecture concerns.

## 0.4.0 — 2026-09-03 — Modular Portability

- Added a business-neutral module catalogue covering CRM/sales, recruitment/HR, finance, marketing, customer service, product/software, research, knowledge/memory, website and reporting/BI.
- Added provider-neutral agent capability contracts so ChatGPT, Codex, Claude, GitHub Copilot or other capable agents can satisfy the same ARC ownership/verification model without becoming architectural canon.
- Added runtime portability guidance for GitHub-hosted Actions, local CLI/profile execution, self-hosted Mac/Linux and VPS/trusted-runtime paths.
- Added a generic first-day Skills foundation with starter Skills for owner routing, GitHub work control, Skill authoring and Research escalation.
- Added `scripts/seed_foundation.py`, which is plan-first and creates only missing target Skill files after explicit `--apply` authority.
- Added unit tests and CI coverage for the Skills foundation plan.
- Extended the generic business profile with optional `modules`, `providers` and `runtimes` selections.
- Expanded bootstrap, manifest and verification contracts so module selection, provider portability and least-privilege runtime choice are explicit deployment concerns.

## 0.3.0 — 2026-09-03 — Safe Harbour

- Added estate-manifest schema `1.0` for non-secret ARC topology, ownership, integration references and optional observed repository state.
- Added `arc.py export` to create a non-mutating architecture manifest from a valid ARC profile.
- Added `arc.py restore-plan` to explain repository reconstruction plus external/manual recovery prerequisites without mutation.
- Added bounded `arc.py restore --apply` for GitHub repository reconstruction only; private files, specialist-system records, credentials, runtime machine state and memory contents remain external-owner responsibilities.
- Added known credential-pattern detection in addition to secret-like configuration-key rejection.
- Added manifest compatibility validation and round-trip reconstruction back into valid ARC configuration.
- Added the Safe-Harbour Contract defining release guarantees, backup boundaries and recovery ownership.
- Fixed target inspection so an unavailable or unauthenticated GitHub CLI reports UNKNOWN rather than incorrectly classifying repositories as CREATE.
- Prepared ARC for its first formal tagged public release from a known-good merged Stage state.

## 0.2.0 — 2026-09-03 — Atlas Universal Front Door

- Expanded Atlas into seven explicit operating modes: onboard, adopt, audit, health, upgrade, recover and next.
- Added `arc.py onboard` so a new business can generate a validated `arc.json` without understanding the schema first.
- Added non-interactive onboarding for capable agents that already hold the required business facts.
- Added pre-apply repository inspection with REUSE / CREATE classification.
- Added existing-estate adoption guidance using KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE.
- Added secret-like configuration-field rejection and explicit config overwrite protection.
- Added portable Atlas Skill packaging from the same canonical `.github/skills/atlas` source, including ChatGPT metadata and mode reference.
- Added durable-continuity rules so material ARC Stage/programme state must live in GitHub Issues rather than a hidden chat transcript.
- Kept health, upgrade and recovery claims bounded to capabilities actually implemented in the current release; ARC.4 and ARC.7 own the richer lifecycle machinery.

## 0.1.0 — 2026-09-03 — Public Foundation

- Established ARC as a public MIT-licensed reproducible human + AI operating architecture.
- Added Atlas as the single onboarding/deployment front door.
- Added a project Agent Skill and prompt-file `/atlas` entrypoint for supported environments.
- Added architecture, manifest, bootstrap, verification and portability contracts.
- Added generic-business and TBHRC-reference deployment profiles.
- Added component guidance for GitHub, Skills, Research, agents, runtimes, memory, private files and specialist systems.
- Added a conservative plan-first bootstrap/verification CLI and CI validation.

Origin: the architecture emerged from the GitHub learning-to-operation migration documented in `tbhrc/gh-course`.
