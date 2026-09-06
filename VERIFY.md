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

## First-day Skills baseline

```bash
python3 scripts/seed_foundation.py --config /tmp/arc-test.json
```

The inspection path must resolve the configured Skills repository and list the generic starter Skills without making a remote change. When the current instruction already authorises ordinary bounded seeding, `--apply` may be selected directly without another human confirmation.

The starter set must include owner routing, GitHub work control, Skill authoring and Research escalation, and existing target Skill files must never be overwritten.

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

`restore --apply` is not part of routine CI because destructive recovery is a genuine mutation boundary. It remains explicitly authorised and bounded to conservative GitHub repository reconstruction.

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
- Which optional business modules are selected and who owns them?
- Which provider and runtime routes are authorised for ordinary work?
- Which repository/system owns the current facts for this task?
- Which configured repositories will be REUSED versus CREATED?
- Which existing owners should be KEPT, INTEGRATED, MIGRATED, RESEARCHED or RETIRED?
- Where should durable work be recorded?
- What private data must stay outside public repositories?
- When should Research be triggered?
- When is a trusted runtime required rather than normal execution?
- What ordinary bounded work is already authorised by the current instruction?
- What real risk boundaries still require fresh authority?
- Which formal ARC release and estate-manifest schema describe this architecture?
- Which external owners require separate backup/recovery?
- How is deployment or recovery completion verified?

## Repository Router cold-start acceptance

For ordinary deployed-repository work, root `AGENTS.md` is the first-hop Repository Router. Verification must prove progressive loading rather than broad preload:

- a known bounded task reaches the smallest relevant Skill/owner directly;
- owner lookup is loaded only when the owner/source is unclear;
- Workflow is loaded only when execution-level selection genuinely requires it;
- Multi-Agent Orchestrator is loaded only when delegation, specialist work or genuine parallelism is required;
- Fast Links are pointers, not mandatory reads;
- the normal cold-start instruction path stays within the current <=200-line Agent OS budget;
- unnecessary reads, routing hops, duplicated operating instructions or precautionary approval loops are treated as verification failures, not harmless overhead.

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
- The current user/founder instruction is sufficient authority for ordinary bounded work; the agent does not ask twice.
- `--apply` is treated as a deliberate mutation-mode selector, not a ceremonial second approval step.
- Fresh authority is requested only at a real boundary: destructive overwrite/delete/force/recovery, root or credential use, material spend, private/confidential data movement, legal/compliance commitment, production-destructive action, or material external/client commitment.
- `bootstrap` remains non-mutating without `--apply`, but ordinary authorised bootstrap may select `--apply` directly.
- `restore --apply` remains separately gated because destructive recovery crosses a real risk boundary.
- If privileged runtime is configured, it is used only for an actual runtime gap and has its own verification.

### Gate D — research
- A recurring operational problem can be routed to Research.
- Research can return a qualified Test/Adopt/Watch/Reject decision to the correct owner.

### Gate E — security
- No credential values or secret-like configuration fields are committed to `arc.json` or the estate manifest.
- Routine agents do not use founder/root credentials.
- Repository/public/private boundaries match the deployment plan.
- Security controls do not create a duplicate approval loop for ordinary already-authorised work.

### Gate F — safe harbour
- A formal ARC release/tag identifies a known-good ARC repository state.
- An estate manifest validates against the supported schema.
- The manifest can round-trip into a valid ARC topology and restore plan.
- External owner recovery responsibilities are explicit.
- Repository reconstruction plus external owner restoration/reconnection is followed by complete ARC verification.

### Gate G — portability
- Optional business modules are selected explicitly rather than forced.
- A newly created Skills repository can receive the generic starter foundation through the smallest authorised path.
- Existing target Skills are reused and never overwritten automatically.
- At least two capable agent/provider routes can satisfy the same owner/Skill/verification contract without changing ARC architecture.
- GitHub-hosted execution is sufficient for ordinary deterministic work when appropriate.
- Self-hosted/local/VPS runtime routes remain optional exceptions for genuine capability or privilege gaps.
- Provider choice and runtime choice are independent decisions.

### Gate H — learning and continuity
- One real workflow has run end to end.
- Reusable learning has been promoted to the correct Skill/architecture owner.
- Material ARC Stage/programme state is recorded in the controlling GitHub Issue with branch, evidence, blockers and exact next action.
- A fresh agent can continue the active Stage from GitHub alone without a hidden chat transcript.

## Definition of healthy

ARC is healthy when a fresh human or capable agent can navigate from a business need to the correct method, owner, provider/runtime execution route and evidence without relying on one person's memory, a hidden chat transcript, or unnecessary approval rituals.

ARC is recoverable when that same operator can pair a known-good ARC release with a valid non-secret estate manifest and the external owners' own backups/reprovisioning paths to reconstruct and re-verify the operating architecture.
