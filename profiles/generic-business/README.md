# Generic Business Profile

Use this profile to deploy ARC into a new business or client without importing TBHRC-specific names or provider assumptions.

## Recommended path

1. Use Atlas or `scripts/arc.py onboard` to generate `arc.json`.
2. Set/confirm the target GitHub owner and visibility.
3. Rename/add domain repositories to match how the business actually owns work.
4. Select only the optional business modules that have a real owner/use case.
5. Declare at least one normal capable-agent route and one normal runtime route.
6. Add a trusted runtime only when the required work genuinely needs that capability.
7. Use `doctor` and `plan --inspect-target` when useful for validation; if the current instruction already authorises ordinary bounded deployment, run `bootstrap --apply` directly without asking again.
8. Seed the first-day Skills foundation with `scripts/seed_foundation.py --apply` when ordinary bounded seeding is already authorised; the non-mutating form remains available for inspection.
9. Use Atlas to complete only the owner mapping, specialist-system integration and agent onboarding actually required.
10. Run one real workflow and verify durable evidence before calling the deployment useful.

`--apply` selects mutating mode. It is not a ceremonial second approval step. Fresh authority is required only at a real destructive/root/private-data/spend/legal/client-commitment boundary.

## Module selection

Example:

```json
"modules": ["sales", "research", "website"]
```

Use the catalogue in [`modules/README.md`](../../modules/README.md). A module does not automatically require a repository or a new SaaS product. Reuse the existing specialist system when it is already the correct owner.

## Provider and runtime portability

Example:

```json
"providers": ["capable-agent"],
"runtimes": ["github-hosted-actions"]
```

Provider names are deployment choices, not architecture canon. Runtime choice follows the **simplest authorised route that can actually complete the work**, with purpose-fit authority sufficient for its intended function. See [`providers/`](../../providers/README.md) and [`runtimes/`](../../runtimes/README.md).

Do not choose a weaker route merely because it appears more restrictive, and do not create an extra credential/bridge when an existing authorised route can do the job.

## Skills-first foundation

Inspect when useful:

```bash
python3 scripts/seed_foundation.py --config arc.json
```

Execute ordinary authorised seeding directly:

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

ARC creates only missing generic starter Skills and never overwrites existing target Skill files.

The profile intentionally does not contain secret fields or live business data.
