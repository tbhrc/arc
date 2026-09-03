# Atlas Modes

Atlas selects one mode before choosing an ARC action. **Plan is not permission to mutate.** Existing business owners and specialist systems are reused deliberately unless a verified migration decision says otherwise.

| Mode | Use it for | Default action |
|---|---|---|
| `onboard` | New ARC estate or first business profile | Gather only irreducible inputs, generate `arc.json`, run doctor and plan before apply. |
| `adopt` | Existing business with repositories, SOPs, automations or specialist systems | Inventory first; classify each relevant owner as KEEP, INTEGRATE, MIGRATE, RESEARCH or RETIRE. Never replace a working owner merely to match an example profile. |
| `audit` | Non-mutating architecture/ownership review | Inspect current ARC contracts and configured target state; use `plan --inspect-target` where available and report gaps without mutation. |
| `health` | Current-state diagnosis | Use current verification contracts and observable evidence. Do not claim richer lifecycle health checks before ARC.7 implements them. |
| `upgrade` | Moving an existing estate toward a newer ARC release | Identify current version/contracts and produce a plan only. Deterministic release-to-estate upgrade machinery belongs to ARC.4/ARC.7 as it becomes available. |
| `recover` | Restore/redeployment planning after loss or migration | Use known releases, manifests and declared owners only. Never invent backups or secret values. Deterministic safe-harbour export/restore is owned by ARC.4. |
| `next` | Operator asks what to do now | Read current owner truth, Stage/Issue state and verification evidence, then return the single smallest safe next action. |

## Existing-estate classification

Use these labels during `adopt` and where useful during `audit`:

- **KEEP** — correct owner and no architectural change required.
- **INTEGRATE** — keep the owner but add ARC navigation/contracts around it.
- **MIGRATE** — move only when there is a clear ownership or capability reason.
- **RESEARCH** — recurring capability gap needs discovery/proving before implementation.
- **RETIRE** — redundant or unsafe owner should be removed through its own controlled change.

## Authority gate

```text
understand / inspect
-> plan
-> explicit human/operator apply authority
-> mutation
-> verify real state
```

Credentials being present never imply apply authority.
