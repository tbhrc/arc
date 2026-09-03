# Changelog

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
