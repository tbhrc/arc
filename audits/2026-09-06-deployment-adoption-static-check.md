# ARC deployment/adoption static check — 2026-09-06

Controlling Issue: #42  
Master: #36

## Result

**PRELIMINARY PASS — design/static evidence.** Final executable proof remains required after the generated Router work in #37 settles on `main`.

## Evidence checked

- `scripts/arc.py` classifies inspected repositories as `REUSE` when present and `CREATE` only when missing.
- `BOOTSTRAP.md` defines REUSE as leave-existing-repository-unchanged and CREATE as mutation only after apply authority.
- `MANIFEST.md` describes `plan --inspect-target` as the pre-apply REUSE/CREATE classifier.
- `README.md` states existing repositories are reused rather than overwritten and that credential availability is not mutation authority.
- `.github/prompts/atlas.prompt.md` starts in non-mutating plan mode and says access does not itself authorise mutation.
- `VERIFY.md` requires KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE decisions for existing owners and asks which repositories are REUSED versus CREATED before apply.
- `modules/README.md` says not to create a repository merely because a module exists and to reuse the correct existing specialist system.
- `profiles/generic-business/README.md` preserves the same reuse-first rule.
- `scripts/seed_foundation.py` reuses existing target Skill files and only creates missing ones.
- configuration contracts exclude credential values and allow existing repositories to be reused.

## Static acceptance

| Check | Result |
|---|---|
| Existing repositories default to reuse | PASS |
| Existing systems can remain owners | PASS |
| Plan is not apply authority | PASS |
| Credential availability is not mutation authority | PASS |
| Skills foundation avoids overwriting existing Skills | PASS |
| Private/live state stays outside ARC | PASS |
| Provider/runtime remains implementation choice | PASS |
| New service/daemon/control layer required | NO |

## Remaining proof

Run the real bounded flow against fresh merged `main`:

`onboard -> doctor -> plan --inspect-target -> apply -> verify`

The executable proof must confirm the same behaviour in practice, including existing-repository reuse and explicit apply gating. Do not close #42 on static evidence alone.
