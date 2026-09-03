# Portability Contract

ARC is portable when a new business can reproduce the operating behaviour without receiving another organisation's secrets, private data or stale copies of live state.

Portable:

- architecture;
- repository roles;
- Skills patterns;
- agent entrypoints;
- bootstrap/verification;
- non-secret configuration schema;
- integration contracts;
- ownership model;
- public reference implementations.

Not portable by copying:

- secret values;
- customer/personnel files;
- production databases;
- organisation-specific root identities;
- mutable business truth;
- licensed/private assets without redistribution rights.

Use profiles/adapters to map provider and business differences without forking the core architecture unnecessarily.
