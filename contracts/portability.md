# Portability Contract

ARC is portable when a new business can reproduce the operating behaviour without receiving another organisation's credentials, private data or stale copies of live state.

## Portable ARC material

- architecture;
- repository roles/topology;
- Skills patterns and pointers;
- agent entrypoints;
- bootstrap/verification/recovery contracts;
- non-secret configuration schema;
- estate-manifest schema and non-secret ownership metadata;
- integration contracts;
- ownership model;
- public reference implementations;
- formal ARC release/tag references.

## Not portable by copying

- credential values;
- customer/personnel/private-file contents;
- CRM/ERP/ATS/accounting records;
- production databases;
- organisation-specific root identities;
- trusted-runtime machine state;
- mutable business truth;
- derived memory contents as substitute canon;
- licensed/private assets without redistribution rights.

## Safe-harbour portability

A portable ARC recovery package is:

```text
formal known-good ARC release/tag
+
validated non-secret estate manifest
+
external owner backups/reprovisioning handled by those owners
```

The estate manifest may identify external providers/systems by name so the recovery plan knows where state belongs. It must not absorb their record contents or credential values.

Use `scripts/arc.py export` to create the architecture manifest and `restore-plan` to understand the recovery requirements. `restore --apply` is limited to conservative GitHub repository reconstruction. See [safe-harbour.md](safe-harbour.md).

Use profiles/adapters to map provider and business differences without forking the core architecture unnecessarily.
