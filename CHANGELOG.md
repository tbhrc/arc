# Changelog

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
