# Bootstrap FolderDesk

FolderDesk bootstrap is designed for a first-time human user **and** a capable AI agent. The first requirement is GitHub access; after that, the deployment can be driven by the agent or by the CLI.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [README](README.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Agent Router](AGENTS.md)

## 1. Connect GitHub first

FolderDesk uses GitHub as the durable operating desk. Before bootstrap, confirm that the human or agent performing deployment can access the target GitHub organisation/account.

CLI check:

```bash
gh auth status
```

If GitHub is not connected/authenticated, fix that before `bootstrap --apply`.

## 2. Create the deployment profile

Use Atlas or:

```bash
python3 scripts/arc.py onboard --output arc.json
```

A capable agent that already knows the required facts can use `onboard --non-interactive`.

`onboard` writes local configuration only.

## 3. Resolve only required ownership facts

Establish only what deployment actually needs:

- target GitHub owner;
- repository visibility;
- required domain owners;
- canonical Skills home;
- private-file owner;
- specialist-system owners;
- runtime/provider route where relevant.

Do not put secret values in `arc.json`.

## 4. Inspect readiness when useful

```bash
python3 scripts/arc.py doctor --config arc.json --connectors
python3 scripts/arc.py plan --config arc.json --inspect-target
```

`doctor --connectors` gives a read-only view of GitHub and declared connector/MCP/runtime readiness. `plan` is visibility, not runtime permission.

Where target state is observable:

```text
REUSE  — repository exists; leave unchanged
CREATE — repository is missing; create in mutating mode
```

## 5. Bootstrap with streamed progress

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

Before repository work begins, FolderDesk states the target and total configured repositories. During the run it reports:

- current repository number / total;
- which repository is being checked;
- whether it was reused or created;
- elapsed time;
- estimated remaining time after the first repository check.

The remaining-time figure is a live estimate based on completed repository checks, not a fixed promise. Its purpose is to keep the user informed instead of leaving a silent bootstrap.

Bootstrap:

- reuses existing repositories unchanged;
- creates missing configured repositories;
- does not copy credentials;
- does not migrate private business data;
- does not rewrite specialist systems.

`--apply` selects mutating mode. It does not create a second approval requirement.

## 6. Repository Router

Each new repository receives a compact root `AGENTS.md` Repository Router plus thin Atlas entrypoints.

Known bounded work should go directly to the smallest relevant Skill/owner. Fast Links are pointers, not preload instructions.

## 7. Seed starter Skills

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

Starter Skills exist only to make a blank environment usable. FolderDesk also seeds a generic `document-intake` Skill so a client-supplied file is filed, ingested, routed with provenance and retrieval-tested by default from day one. The deployed organisation should evolve its own canonical Skills repository without duplicating business truth.

Existing target Skill files are never overwritten automatically.

## 8. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Use [VERIFY.md](VERIFY.md) for observable acceptance.

## 9. Give the deployed system to your agent

After bootstrap, tell your agent:

```text
Work from my FolderDesk GitHub estate. Read the root AGENTS.md of the repository you enter before doing work. Use the smallest relevant Skill/owner, verify the real outcome once, and keep durable work in GitHub rather than only in chat.
```

## 10. Prove one real workflow

A useful deployment proves:

```text
request
→ Repository Router
→ relevant Skill / owner truth
→ authorised execution
→ verify real state
→ preserve material durable context when needed
```

## 11. Export Safe Harbour

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The estate manifest is architecture metadata and owner references, not a backup of private files, specialist-system data, credentials, runtime machine state or memory contents.

## 12. Recover

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

Do not add another workflow, gate, approval step, provider layer or duplicated operating rule merely to make bootstrap look more governed.
