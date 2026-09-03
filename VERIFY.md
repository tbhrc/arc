# ARC Verification Contract

Deployment or recovery is incomplete until the intended operating loop works.

## Automated baseline

```bash
python3 scripts/arc.py verify-self
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py plan --config arc.json --inspect-target
python3 scripts/arc.py verify --config arc.json
```

For first-run onboarding, a non-mutating profile-generation proof can be run with a safe test owner:

```bash
python3 scripts/arc.py onboard \
  --non-interactive \
  --business-name "ARC Test Business" \
  --owner arc-test-business \
  --domains "sales,delivery" \
  --private-files SharePoint \
  --specialist-systems "HubSpot,Xero" \
  --output /tmp/arc-test.json
```

## Safe-harbour baseline

Export architecture without mutation:

```bash
python3 scripts/arc.py export \
  --config /tmp/arc-test.json \
  --output /tmp/arc-estate.json
```

Then prove the manifest can drive a non-mutating recovery plan:

```bash
python3 scripts/arc.py restore-plan --manifest /tmp/arc-estate.json
```

The estate manifest must:

- use supported `manifest_schema: 1.0`;
- identify the ARC version that exported it;
- reconstruct a valid ARC topology/configuration;
- contain architecture/owner references only;
- explicitly exclude credential values, private-file contents, specialist-system records, database contents, trusted-runtime machine state and derived memory contents;
- refuse unsupported schemas and secret-like/known credential material.

`restore --apply` is not part of routine CI because it is a real mutation gate. It must remain explicitly authorised and bounded to conservative GitHub repository reconstruction.

## Portable Atlas packaging

```bash
python3 scripts/package_atlas.py
```

The resulting `dist/skill.zip` must contain the canonical `atlas/SKILL.md`, `atlas/agents/openai.yaml` and `atlas/references/modes.md` from this repository.

## Human/agent acceptance

A cold agent should be able to enter the deployed environment and answer:

- What is this business/environment trying to achieve?
- Which Atlas mode applies now?
- Where are reusable Skills?
- Which repository/system owns the current facts for this task?
- Which configured repositories will be REUSED versus CREATED before apply?
- Which existing owners should be KEPT, INTEGRATED, MIGRATED, RESEARCHED or RETIRED?
- Where should durable work be recorded?
- What private data must stay outside public repositories?
- When should Research be triggered?
- When is a trusted runtime required rather than normal execution?
- What has actually been authorised to mutate?
- Which formal ARC release and estate-manifest schema describe this architecture?
- Which external owners require separate backup/recovery?
- How is deployment or recovery completion verified?

## Required gates

### Gate A — navigation
- Atlas/front-door instructions are discoverable.
- Atlas exposes onboard, adopt, audit, health, upgrade, recover and next modes.
- Every core repository has a useful README and agent contract.
- Cross-repository handoffs have a return/onward route.

### Gate B — truth ownership
- At least one real workflow has an explicit Skill owner and fact/state owner.
- Private files and specialist-system state are not duplicated as fake GitHub canon.
- Existing correct owners are kept/integrated rather than replaced merely to match an ARC example.

### Gate C — execution and authority
- An authorised agent can execute one bounded task through normal tools.
- A plan or available credential is not treated as mutation authority.
- `bootstrap` and `restore` remain non-mutating unless explicit `--apply` authority exists.
- `restore --apply` is limited to configured GitHub repository reconstruction; external owner data is restored separately.
- If privileged runtime is configured, it is used only for an actual runtime gap and has its own verification.

### Gate D — research
- A recurring operational problem can be routed to Research.
- Research can return a qualified Test/Adopt/Watch/Reject decision to the correct owner.

### Gate E — security
- No credential values or secret-like configuration fields are committed to `arc.json` or the estate manifest.
- Routine agents do not use founder/root credentials.
- Repository/public/private boundaries match the deployment plan.

### Gate F — safe harbour
- A formal ARC release/tag identifies a known-good ARC repository state.
- An estate manifest validates against the supported schema.
- The manifest can round-trip into a valid ARC topology and restore plan.
- External owner recovery responsibilities are explicit.
- Repository reconstruction plus external owner restoration/reconnection is followed by complete ARC verification.

### Gate G — learning and continuity
- One real workflow has run end to end.
- Reusable learning has been promoted to the correct Skill/architecture owner.
- Material ARC Stage/programme state is recorded in the controlling GitHub Issue with branch, evidence, blockers and exact next action.
- A fresh agent can continue the active Stage from GitHub alone without a hidden chat transcript.

## Definition of healthy

ARC is healthy when a fresh human or capable agent can navigate from a business need to the correct method, owner, execution route and evidence without relying on one person's memory or a hidden chat transcript.

ARC is recoverable when that same operator can pair a known-good ARC release with a valid non-secret estate manifest and the external owners' own backups/reprovisioning paths to reconstruct and re-verify the operating architecture.
