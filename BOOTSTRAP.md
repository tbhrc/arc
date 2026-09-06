# Bootstrap ARC

ARC bootstrap is inspectable before mutation, but inspection is not a mandatory approval ceremony.

**Fast links:** [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Manifest](MANIFEST.md) · [Verify](VERIFY.md) · [Router](AGENTS.md)

## 1. Create the profile

Use Atlas or:

```bash
python3 scripts/arc.py onboard --output arc.json
```

A capable agent that already knows the required facts can use `onboard --non-interactive`.

`onboard` writes local configuration only.

## 2. Resolve only required ownership facts

Establish only what deployment actually needs:

- target GitHub owner;
- repository visibility;
- required domain owners;
- canonical Skills home;
- private-file owner;
- specialist-system owners;
- runtime/provider route where relevant.

Do not put secret values in `arc.json`.

## 3. Inspect when useful

```bash
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
```

`plan` is a visibility tool, not runtime permission.

Where target state is observable:

```text
REUSE  — repository exists; leave unchanged
CREATE — repository is missing; create in mutating mode
```

## 4. Execute ordinary authorised deployment

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

`--apply` selects mutating mode. It does not create a second approval requirement.

Bootstrap:

- reuses existing repositories unchanged;
- creates missing configured repositories;
- does not copy credentials;
- does not migrate private business data;
- does not rewrite specialist systems.

Additional human authority is reserved for genuine consequential boundaries such as root/super-admin changes, destructive or irreversible mutation, material spend, legal/compliance commitment, private-data disclosure or material external/client commitment.

## 5. Repository Router

Each new repository receives a compact root `AGENTS.md` Repository Router plus thin Atlas entrypoints.

Known bounded work should go directly to the smallest relevant Skill/owner. Load owner lookup, Workflow or Multi-Agent Orchestrator only when the task actually needs them.

Fast Links are pointers, not preload instructions.

## 6. Continuity only when useful

Issues, PRs, plans and evidence may help continuity, coordination, review or recovery. They are optional and never runtime permission for ordinary authorised work.

ARC does not require a named Anti-Drift field, controlling Issue, checklist or evidence object. Preserve the requested outcome in the smallest useful form only when continuity is genuinely needed.

## 7. Seed starter Skills

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

Starter Skills exist only to make a blank environment usable. They must remain thin bootstrap pointers and must not become a competing editable operating canon.

For the TBHRC reference implementation, current operating doctrine remains in [`tbhrc/skills`](https://github.com/tbhrc/skills). Another organisation should establish and evolve its own canonical Skills repository after deployment.

Existing target Skill files are never overwritten automatically.

## 8. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Use [VERIFY.md](VERIFY.md) for observable acceptance only.

## 9. Prove one real workflow

A useful deployment proves:

```text
request
→ Repository Router
→ relevant Skill / owner truth
→ authorised execution
→ verify real state
→ continuity only when useful
```

## 10. Export Safe Harbour

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The estate manifest is architecture metadata and owner references, not a backup of private files, specialist-system data, credentials, runtime machine state or memory contents.

## 11. Recover

Inspect when useful:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Reconstruct missing configured repositories:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current restore reuses existing configured repositories unchanged and creates only missing configured repositories. External owners recover their own data and credentials separately.

## KISSS

Do not add another workflow, gate, Issue requirement, approval step, provider layer or duplicated operating rule merely to make bootstrap look more governed.
