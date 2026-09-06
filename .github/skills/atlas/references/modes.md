# Atlas Modes

Atlas selects the smallest useful mode from current evidence. Existing owners are reused unless a concrete migration decision requires change. Ordinary already-authorised bounded work executes directly.

| Mode | Use it for | Default action |
|---|---|---|
| `onboard` | New ARC estate or first business profile | Gather only irreducible inputs, generate `arc.json`, inspect when useful, then execute authorised bootstrap. |
| `adopt` | Existing business | Inspect only what matters; prefer KEEP / INTEGRATE over replacement. |
| `audit` | Architecture/ownership review | Inspect current truth and report only material gaps. |
| `health` | Current-state diagnosis | Use observable evidence and relevant verification. |
| `upgrade` | Move toward a newer ARC release | Make the smallest justified migration and verify it. |
| `recover` | Export, restore planning and bounded redeployment | Reuse existing repositories unchanged; create only missing configured repositories when `--apply` selects mutation. External owner backups/credentials remain separate. |
| `next` | Decide what to do now | Use current owner truth and return or execute the single smallest useful next action. |

## Existing-estate classification

Use only when it helps the decision:

- **KEEP** — correct owner; no change needed.
- **INTEGRATE** — keep the owner and add only useful ARC navigation/contracts.
- **MIGRATE** — move only for a concrete ownership/capability reason.
- **RESEARCH** — investigate a recurring capability gap before implementation.
- **RETIRE** — remove a genuinely redundant or unsafe owner through its correct change path.

## Authority

```text
current instruction authorises ordinary bounded work
→ select mutation mode when needed
→ execute
→ verify
```

Do not ask again merely because state changes. `--apply` is a mutation selector, not a second approval request.

Fresh authority is required only if the next action actually crosses a consequential boundary such as destructive overwrite/delete/force, root/super-admin use, material spend, private/confidential data movement, legal/compliance commitment or material external/client commitment.

## Recovery

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current restore leaves existing configured repositories unchanged and creates only missing configured repositories. It does not restore private files, specialist-system records, credentials, runtime machine state or memory contents; those remain with their owning systems.

If a future recovery implementation actually deletes, overwrites or force-updates material state, protect that specific action only.
