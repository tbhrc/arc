# Generic Business Profile

Use this profile to deploy ARC into a new business or client without importing TBHRC-specific names or provider assumptions.

## Recommended path

1. Use Atlas or `scripts/arc.py onboard` to generate `arc.json`.
2. Set/confirm the target GitHub owner and visibility.
3. For a managed-client deployment, set `deployment_context.scope` to `tenant` and supply the canonical `tenant_id`; for shared architecture use `scope: shared`.
4. Rename/add domain repositories to match how the business actually owns work.
5. Select only the optional business modules that have a real owner/use case.
6. Declare at least one normal capable-agent route and one normal runtime route.
7. Add a trusted runtime only when the required work genuinely needs that capability.
8. Use `doctor` and `plan --inspect-target` when useful for validation; if the current instruction already authorises ordinary bounded deployment, run `bootstrap --apply` directly without asking again.
9. Seed the first-day Skills foundation with `scripts/seed_foundation.py --apply` when ordinary bounded seeding is already authorised; the non-mutating form remains available for inspection.
10. Use Atlas to complete only the owner mapping, specialist-system integration and agent onboarding actually required.
11. Run one real workflow and verify durable evidence before calling the deployment useful.

`--apply` selects mutating mode. It is not a ceremonial second approval step. Fresh authority is required only at a real destructive/root/private-data/spend/legal/client-commitment boundary.

## Multi-tenant deployment context

Managed-client profiles must carry explicit deployment context. Generate it directly when onboarding:

```bash
python3 scripts/arc.py onboard --non-interactive --business-name "Client Name" --owner client-github-org --tenant-id canonical-tenant-id --entity-ref canonical-owner-entity-ref
```

Equivalent profile contract:

```json
"deployment_context": {
  "scope": "tenant",
  "tenant_id": "<canonical-tenant-id>",
  "entity_ref": "<optional-canonical-owner-entity-ref>"
}
```

`tenant_id` and `entity_ref` are references supplied by the canonical organisation/DB owners; FolderDesk does not allocate a parallel client/identity code system. A non-client shared architecture profile uses `"scope": "shared"` and no `tenant_id`. Safe-harbour export/recovery preserves this context.

For an iMPLEMENTAi managed-service estate, multiple tenant profiles may deliberately target the **same GitHub owner and same shared repository/Skills topology** while carrying distinct tenant context. A dedicated client-owned deployment may instead target that client's own GitHub owner. Tenant identity must never be encoded by cloning or renaming the shared architecture.

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
