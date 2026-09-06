# ARC Deployment Manifest

This manifest defines the logical components required for an ARC deployment. Exact product/provider choices are configurable.

| Component | Required? | Default implementation | Owns | Verification |
|---|---|---|---|---|
| Operating desk | Yes | GitHub | durable work, architecture and automation evidence | repository access works |
| Skills canon | Yes | `skills` repository | reusable HOW | agent can find and read a canonical Skill |
| Foundational Skills | Yes for new Skills repos | `starter/skills/` + `scripts/seed_foundation.py` | first-day routing, GitHub workflow, Skill authoring, Research escalation | inspection lists starter Skills; authorised apply creates only missing files without asking twice |
| Research | Yes | `research` repository | external evidence, comparisons, proving | one research record can route to an owner |
| Operations hub | Yes | `ops` repository | cross-business architecture/operating decisions | agent can identify domain owners |
| Business modules | Optional | `modules/` catalogue | capability selection + ownership pattern | only selected modules appear in profile/plan |
| Agent provider routes | At least one | provider-neutral capability contract | authorised agent execution route | one authorised capable route can complete the intended work and verify it |
| Runtime routes | At least one capable route | simplest existing authorised route | execution environment | intended work completes without unnecessary hops or infrastructure |
| Domain owners | Yes | configurable repositories/systems | current business/product facts | one source of truth per declared field/class |
| Agent instructions | Yes | `AGENTS.md` + platform instructions | repository-wide operating behaviour | cold agent can route work correctly |
| Atlas front door | Yes | ARC Atlas Skill + `/atlas` prompt | onboarding, adoption, audit, health, upgrade/recovery routing and next-action guidance | cold agent selects a mode and reaches execution without hidden context or ritual approval loops |
| ARC profile | Yes | generated `arc.json` | non-secret target topology/ownership configuration | `onboard` produces valid config and refuses implicit destructive overwrite |
| Estate safe harbour | Recommended after healthy deployment | `arc.py export` + formal ARC release | non-secret architecture snapshot + recovery references | manifest schema validates and round-trips into a restore plan |
| Atlas portable distribution | Recommended | `scripts/package_atlas.py` -> `dist/skill.zip` | transport of the same canonical Atlas Skill | package contains canonical Skill, metadata and mode reference; no second editable canon |
| Private file store | Yes for confidential work | provider chosen by business | private/client/personnel files | private data does not need public repo storage |
| Specialist systems | As needed | CRM/ERP/ATS/accounting/etc. | declared structured state | ownership map identifies each live field owner |
| Research escalation | As needed | research + operating rule | recurring problem-to-platform investigation | agent can recognise a broader capability gap when one exists |
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

It may also declare business-neutral selections:

```json
"modules": ["research"],
"providers": ["capable-agent"],
"runtimes": ["github-hosted-actions"]
```

The module/provider/runtime fields describe capability choices without making any vendor or route architectural canon. See [modules](modules/README.md), [providers](providers/README.md) and [runtimes](runtimes/README.md).

Domain repositories are configured per business. Atlas can generate the profile through `scripts/arc.py onboard`; `plan --inspect-target` is available when useful to distinguish configured repositories that already exist (**REUSE**) from missing ones (**CREATE**). It is not a mandatory human approval checkpoint before ordinary already-authorised deployment.

For an established business, repository existence alone does not decide ownership. Atlas may additionally classify existing systems and process owners as **KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE** when that materially helps the decision.

## First-day Skills foundation

A newly created Skills repository should not remain empty. Inspection is available:

```bash
python3 scripts/seed_foundation.py --config arc.json
```

When ordinary bounded seeding is already authorised, execute directly:

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

`--apply` selects mutating mode. It does not require a second human confirmation.

The foundation contains generic starter Skills for owner routing, GitHub work control, Skill authoring and Research escalation. Existing target Skill files are never overwritten. After deployment, the target organisation's Skills repository becomes its editable canon; ARC does not continuously sync these starter templates over local improvements.

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

It deliberately excludes credential values, private-file contents, CRM/ERP/ATS/accounting records, database contents, trusted-runtime machine state and derived memory contents.

Use:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current restore apply is bounded GitHub repository reconstruction: existing configured repositories remain unchanged and only missing configured repositories are created. External owners remain responsible for their own backup/restore and credential reprovisioning. See [Safe-Harbour Contract](contracts/safe-harbour.md).

## Authority rule

Ordinary authorised bounded work executes directly. ARC must not convert ordinary mutation into a precautionary approval loop.

Fresh authority is reserved for actions that actually cross a consequential boundary: destructive overwrite/delete/force, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

## Atlas lifecycle boundary

ARC exposes the seven Atlas modes: onboard, adopt, audit, health, upgrade, recover and next.

- current health uses `VERIFY.md` and observable state;
- formal releases + manifest schema give `upgrade` a known version/compatibility anchor;
- recovery uses the safe-harbour export/restore-plan/bounded-restore contract.

## Promotion rule

When the deployed architecture gains a foundational capability:

1. prove it in its correct owner;
2. update the reusable method in the organisation's Skills canon;
3. update ARC only when the portable architecture/bootstrap/recovery contract materially changes;
4. update the Course when the learning path materially changes.

Preserve continuity only when it materially helps future work. An Issue is one available surface, not a mandatory runtime prerequisite.
