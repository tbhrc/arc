# Generic Business Profile

Use this profile to deploy ARC into a new business or client without importing TBHRC-specific names or provider assumptions.

## Recommended path

1. Use Atlas or `scripts/arc.py onboard` to generate `arc.json`.
2. Set/confirm the target GitHub owner and visibility.
3. Rename/add domain repositories to match how the business actually owns work.
4. Select only the optional business modules that have a real owner/use case.
5. Declare at least one normal capable-agent route and one normal runtime route.
6. Keep the trusted runtime optional unless a genuine machine/privilege gap exists.
7. Run `doctor`, `plan --inspect-target`, then `bootstrap --apply` only after review.
8. Seed the first-day Skills foundation with `scripts/seed_foundation.py` after reviewing its plan.
9. Use Atlas to complete owner mapping, specialist-system integration and agent onboarding.
10. Run one real workflow and verify durable evidence before calling the deployment useful.

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

Provider names are deployment choices, not architecture canon. Runtime choice follows the least-privilege ladder. See [`providers/`](../../providers/README.md) and [`runtimes/`](../../runtimes/README.md).

## Skills-first foundation

Plan:

```bash
python3 scripts/seed_foundation.py --config arc.json
```

Apply only after review:

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

ARC creates only missing generic starter Skills and never overwrites existing target Skill files.

The profile intentionally does not contain secret fields or live business data.
