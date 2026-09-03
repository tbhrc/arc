# Atlas Modes

Atlas selects one mode before choosing an ARC action. **Plan is not permission to mutate.** Existing business owners and specialist systems are reused deliberately unless a verified migration decision says otherwise.

| Mode | Use it for | Default action |
|---|---|---|
| `onboard` | New ARC estate or first business profile | Gather only irreducible inputs, generate `arc.json`, run doctor and plan before apply. |
| `adopt` | Existing business with repositories, SOPs, automations or specialist systems | Inventory first; classify each relevant owner as KEEP, INTEGRATE, MIGRATE, RESEARCH or RETIRE. Never replace a working owner merely to match an example profile. |
| `audit` | Non-mutating architecture/ownership review | Inspect current ARC contracts and configured target state; use `plan --inspect-target` where available and report gaps without mutation. |
| `health` | Current-state diagnosis | Use current `VERIFY.md`, CLI verification and observable evidence. Richer estate health/drift reporting remains owned by ARC.7. |
| `upgrade` | Moving an existing estate toward a newer ARC release | Identify the current ARC version, formal release and manifest schema; produce a migration plan. Automated release-to-estate upgrade machinery remains owned by ARC.7. |
| `recover` | Safe-harbour export, restore planning and bounded redeployment | Use `export` to create a non-secret estate manifest, `restore-plan` to understand recovery, and `restore --apply` only for explicitly authorised GitHub repository reconstruction. External owner backups/credentials remain separate. |
| `next` | Operator asks what to do now | Read current owner truth, Stage/Issue state and verification evidence, then return the single smallest safe next action. |

## Existing-estate classification

Use these labels during `adopt` and where useful during `audit`:

- **KEEP** — correct owner and no architectural change required.
- **INTEGRATE** — keep the owner but add ARC navigation/contracts around it.
- **MIGRATE** — move only when there is a clear ownership or capability reason.
- **RESEARCH** — recurring capability gap needs discovery/proving before implementation.
- **RETIRE** — redundant or unsafe owner should be removed through its own controlled change.

## Recovery route

After an ARC estate is healthy, create a safe-harbour architecture snapshot:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

To understand recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Only after the recovery plan is understood and repository reconstruction is explicitly authorised:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

`restore --apply` does **not** restore private files, CRM/ERP/ATS/accounting records, credential values, trusted-runtime machine state or derived memory contents. Follow `contracts/safe-harbour.md` and restore/reconnect those owners separately.

## Authority gate

```text
understand / inspect
-> plan
-> explicit human/operator apply authority
-> bounded mutation
-> verify real state
```

Credentials being present never imply apply authority.
