# Generic Business Profile

Use this profile to deploy FolderDesk into a new business or client without importing TBHRC-specific names or provider assumptions.

## Recommended path

1. Use Atlas or `scripts/folderdesk.py onboard` to generate `folderdesk.json`.
2. Confirm the target GitHub owner, primary workspace name and visibility.
3. For a managed-client deployment, set `deployment_context.scope` to `tenant` and supply the canonical `tenant_id`; for shared architecture use `scope: shared`.
4. Declare business domains as logical in-repository context. Do not create a repository per department/domain by default.
5. Reuse existing external systems/connectors as live owners of their records.
6. Use `doctor` and `plan --inspect-target` when useful; if ordinary bounded deployment is already authorised, run `bootstrap --apply` directly.
7. Seed starter Skills under `.folderdesk/skills/` with `scripts/seed_foundation.py --apply` when useful.
8. Run one real workflow and verify a useful result before calling the deployment useful.
9. Add another repository later only when a concrete ownership, access/security, independent lifecycle/release, concurrency/isolation or mature-capability boundary earns separation.

`--apply` selects mutating mode. It is not a ceremonial second approval step. Fresh authority is required only at a real destructive/root/private-data/spend/legal/client-commitment boundary.

## Multi-tenant deployment context

Managed-client profiles must carry explicit deployment context. Generate it directly when onboarding:

```bash
python3 scripts/folderdesk.py onboard \
  --non-interactive \
  --business-name "Client Name" \
  --owner client-github-org \
  --tenant-id canonical-tenant-id \
  --entity-ref canonical-owner-entity-ref \
  --output folderdesk.json
```

Equivalent profile contract:

```json
"deployment_context": {
  "scope": "tenant",
  "tenant_id": "<canonical-tenant-id>",
  "entity_ref": "<optional-canonical-owner-entity-ref>"
}
```

`tenant_id` and `entity_ref` are references supplied by canonical organisation/DB owners; FolderDesk does not allocate a parallel client/identity code system. A non-client shared profile uses `"scope": "shared"` and no `tenant_id`. Safe-harbour export/recovery preserves this context.

## Domains are not repositories

Example:

```json
"domains": [
  {"name": "sales", "label": "Sales", "description": "Sales context inside the workspace."},
  {"name": "delivery", "label": "Delivery", "description": "Delivery context inside the workspace."}
]
```

Domains help route context and work. They do not automatically create repositories, agents, databases or SaaS products.

## Optional repository expansion

The default profile contains exactly one repository with `role: "workspace"`.

If a separate repository later becomes genuinely useful, add it explicitly to `repositories[]`. Typical earned boundaries are:

- separate access/privacy/security;
- independent product/release lifecycle;
- genuine concurrent/isolated execution;
- public distribution separate from private work;
- mature reusable capability with a distinct owner.

## Skills-first foundation

Inspect when useful:

```bash
python3 scripts/seed_foundation.py --config folderdesk.json
```

Execute ordinary authorised seeding directly:

```bash
python3 scripts/seed_foundation.py --config folderdesk.json --apply
```

By default FolderDesk creates only missing starter Skills under `.folderdesk/skills/` in the primary workspace and never overwrites existing files. If an explicit repository with `role: "skills"` is later configured, that repository becomes the Skills target.

The profile intentionally contains no secret fields or live business data.
