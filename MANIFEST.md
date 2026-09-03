# ARC Deployment Manifest

This manifest defines the logical components required for an ARC deployment. Exact product/provider choices are configurable.

| Component | Required? | Default implementation | Owns | Verification |
|---|---|---|---|---|
| Operating desk | Yes | GitHub | durable work, architecture, Issues/PRs, automation evidence | repository access + Issue/PR path works |
| Skills canon | Yes | `skills` repository | reusable HOW | agent can find and read a canonical Skill |
| Research | Yes | `research` repository | external evidence, comparisons, proving | one research record can route to an owner |
| Operations hub | Yes | `ops` repository | cross-business architecture/operating decisions | agent can identify domain owners |
| Domain owners | Yes | configurable repositories/systems | current business/product facts | one source of truth per declared field/class |
| Agent instructions | Yes | `AGENTS.md` + platform instructions | repository-wide operating behaviour | cold agent can route work correctly |
| Atlas front door | Yes | ARC Atlas Skill + `/atlas` prompt | onboarding, adoption, audit, health, upgrade/recovery routing and next-action guidance | cold agent selects a mode and produces a plan without hidden context |
| ARC profile | Yes | generated `arc.json` | non-secret target topology/ownership configuration | `onboard` produces valid config and refuses implicit overwrite |
| Estate safe harbour | Recommended after healthy deployment | `arc.py export` + formal ARC release | non-secret architecture snapshot + recovery references | manifest schema validates and round-trips into a restore plan |
| Atlas portable distribution | Recommended | `scripts/package_atlas.py` -> `dist/skill.zip` | transport of the same canonical Atlas Skill | package contains canonical Skill, metadata and mode reference; no second editable canon |
| Private file store | Yes for confidential work | provider chosen by business | private/client/personnel files | private data does not need public repo storage |
| Specialist systems | As needed | CRM/ERP/ATS/accounting/etc. | declared structured state | ownership map identifies each live field owner |
| Research escalation | Yes | research + operating rule | recurring problem-to-platform investigation | agent can recognise a broader capability gap |
| Trusted runtime | Optional | `ai-engine` repository/runtime | privileged machine/runtime access | only used when normal execution is insufficient |
| Memory | Optional | chosen memory layer | derived context | memory is treated as non-canonical |
| CI/verification | Yes | GitHub Actions + local checks | deterministic repository health | validation runs without secrets |
| Course | Recommended | GitHub Course | learning and reproduction methodology | learner can understand architecture independently |

## Core deployment set

The default generic profile declares:

```text
skills
research
ops
ai-engine   # optional trusted-runtime owner
```

Domain repositories are configured per business. Atlas can generate the profile through `scripts/arc.py onboard`, then `plan --inspect-target` distinguishes configured repositories that already exist (**REUSE**) from missing ones (**CREATE**) before apply.

For an established business, repository existence alone does not decide ownership. Atlas additionally classifies existing systems and process owners as **KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE**.

## Estate manifest schema 1.0

ARC safe harbour is **architecture recovery**, not a copy of live external data.

A schema `1.0` estate manifest records:

```text
manifest schema
ARC version/release reference
target business/GitHub ownership metadata
repository/domain names + roles + visibility + required state
declared private-file owner/provider name
declared specialist system names
declared memory/runtime architecture references
optional observed REUSE / CREATE / UNKNOWN repository state
compatibility metadata
explicit recovery exclusions + manual prerequisites
```

It deliberately excludes:

```text
credential values
private-file contents
CRM / ERP / ATS / accounting records
database contents
trusted-runtime machine state
derived memory contents
```

Use:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
# only after explicit authority:
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

The apply boundary is conservative GitHub repository reconstruction only. External owners remain responsible for their own backup/restore and credential reprovisioning. See [Safe-Harbour Contract](contracts/safe-harbour.md).

## Atlas lifecycle boundary

ARC exposes the seven Atlas modes: onboard, adopt, audit, health, upgrade, recover and next.

- current health uses `VERIFY.md` and observable state;
- formal releases + manifest schema give `upgrade` a known version/compatibility anchor;
- recovery uses the safe-harbour export/restore-plan/bounded-restore contract;
- ARC.7 owns richer estate drift, health and automated release-to-estate upgrade lifecycle.

## Promotion rule

When the deployed architecture gains a foundational capability:

1. prove it in its correct owner;
2. update the reusable method in the organisation's Skills canon;
3. update ARC only when the portable architecture/bootstrap/recovery contract materially changes;
4. update the Course when the learning path materially changes.

Material ARC programme progress must be durable in the controlling GitHub Issue rather than a chat-only handoff.
