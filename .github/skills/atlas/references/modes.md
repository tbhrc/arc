# Atlas Modes

Atlas selects one mode before choosing an ARC action. Existing business owners and specialist systems are reused deliberately unless a verified migration decision says otherwise. Ordinary already-authorised bounded work executes directly; planning is a visibility tool, not a mandatory approval ceremony.

| Mode | Use it for | Default action |
|---|---|---|
| `onboard` | New ARC estate or first business profile | Gather only irreducible inputs, generate `arc.json`, use doctor/plan when useful, then execute ordinary authorised bootstrap directly. |
| `adopt` | Existing business with repositories, SOPs, automations or specialist systems | Inspect only what matters; classify relevant owners as KEEP, INTEGRATE, MIGRATE, RESEARCH or RETIRE. Never replace a working owner merely to match an example profile. |
| `audit` | Non-mutating architecture/ownership review | Inspect current ARC contracts and configured target state; use `plan --inspect-target` where useful and report gaps without mutation. |
| `health` | Current-state diagnosis | Use current `VERIFY.md`, CLI verification and observable evidence. |
| `upgrade` | Moving an existing estate toward a newer ARC release | Identify the current ARC version, formal release and manifest schema; make the smallest justified migration and verify it. |
| `recover` | Safe-harbour export, restore planning and bounded redeployment | Use `export` and `restore-plan`; destructive `restore --apply` remains explicitly gated because recovery crosses a real risk boundary. External owner backups/credentials remain separate. |
| `next` | Operator asks what to do now | Read current owner truth, Stage/Issue state and verification evidence, then execute or return the single smallest next action. |

## Existing-estate classification

Use these labels during `adopt` and where useful during `audit`:

- **KEEP** — correct owner and no architectural change required.
- **INTEGRATE** — keep the owner but add ARC navigation/contracts around it.
- **MIGRATE** — move only when there is a clear ownership or capability reason.
- **RESEARCH** — recurring capability gap needs discovery/proving before implementation.
- **RETIRE** — redundant or unsafe owner should be removed through its own controlled change.

## Ordinary authority rule

```text
current instruction already authorises ordinary bounded work
-> select mutating mode deliberately (`--apply` where applicable)
-> execute
-> verify real state
```

Do not ask the human again merely because state will change. `--apply` is a mutation-mode selector, not a second approval request.

Fresh authority is required only when the next step crosses a real boundary: destructive overwrite/delete/force/recovery, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.

Credentials being present never imply authority by themselves.

## Recovery route

After an ARC estate is healthy, create a safe-harbour architecture snapshot:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
```

To understand recovery without mutation:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Recovery is a genuine destructive-risk boundary. After repository reconstruction is explicitly authorised:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

`restore --apply` does **not** restore private files, CRM/ERP/ATS/accounting records, credential values, trusted-runtime machine state or derived memory contents. Follow `contracts/safe-harbour.md` and restore/reconnect those owners separately.
