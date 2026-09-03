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

The plan must resolve the configured Skills repository and list the generic starter Skills without making a remote change. Apply remains a separate explicit authority gate. Existing target Skill files must never be overwritten automatically.

## Safe-harbour baseline

```bash
python3 scripts/arc.py export --config /tmp/arc-test.json --output /tmp/arc-estate.json
python3 scripts/arc.py restore-plan --manifest /tmp/arc-estate.json
```

The estate manifest must use supported schema `1.0`, reconstruct valid ARC topology, contain architecture/owner references only, and explicitly exclude credential values, private-file contents, specialist-system records, database contents, trusted-runtime machine state and derived memory contents.

`restore --apply` is not part of routine CI because it is a real mutation gate. It remains explicitly authorised and bounded to conservative GitHub repository reconstruction.

## Portable Atlas packaging

```bash
python3 scripts/package_atlas.py
```

The resulting `dist/skill.zip` must contain canonical Atlas Skill, metadata and mode reference from this repository.

## Human/agent acceptance

A cold agent should be able to answer:

- What is this business/environment trying to achieve?
- Which Atlas mode applies now?
- Where are reusable Skills and current owner truth?
- Which optional modules, providers and runtimes are selected?
- Which specialist system owns each live field/state involved?
- Which identity/connector is authorised and at what scope?
- Which configured repositories are REUSE versus CREATE?
- Which existing owners are KEEP / INTEGRATE / MIGRATE / RESEARCH / RETIRE?
- Which data must stay outside public repositories?
- What mutation has actually been authorised?
- When is a trusted runtime or root/break-glass path justified?
- How will the live specialist-system result be verified?
- Which release/estate manifest and external recovery owners describe recovery?

## Required gates

### Gate A — navigation
- Atlas/front-door instructions are discoverable.
- Core repositories have useful README/agent contracts.
- Cross-system handoffs expose a return/onward route.

### Gate B — truth ownership
- At least one real workflow has explicit Skill owner and fact/state owner.
- Private files and specialist-system state are not duplicated as fake GitHub canon.
- Existing correct owners are kept/integrated rather than flattened to an ARC example.

### Gate C — execution and authority
- An authorised agent can execute one bounded task through normal tools.
- A plan or available credential is not treated as mutation authority.
- Bootstrap/restore apply gates remain explicit.
- Privileged runtime is used only for an actual runtime gap and has separate verification.

### Gate D — research
- A recurring operational problem can route to Research and return a Test/Adopt/Watch/Reject decision.

### Gate E — specialist integrations
- Every connected specialist system has a declared live owner, business owner, allowed agent actions, identity/connector name, minimum scope and verification method.
- Email/calendar/directory, private files, CRM, ATS/HRIS, finance/ERP, website/DNS, database/BI, service, memory and runtime integrations follow the common owner contract where used.
- A write is verified from the actual specialist system after mutation.
- GitHub durable evidence does not become a mirror of the external database.

### Gate F — security/governance
- No credential values or secret-like configuration fields are committed to ARC profile/manifest/public examples.
- Repository visibility matches the intended data class.
- Material production/security/automation repositories use proportional branch/ruleset/review protection.
- Actions default to read-only permissions and elevate only required scopes.
- Self-hosted/VPS/local privileged runners are not exposed to arbitrary untrusted PR execution.
- Routine agents do not use founder/root credentials.
- Root/break-glass use requires explicit current authority and temporary bridges/privilege are torn down and verified.
- Credential lifecycle has owner, minimum scope, rotation trigger and revocation path.

### Gate G — safe harbour
- A formal ARC release/tag identifies known-good state.
- Estate manifest validates and can round-trip to a restore plan.
- External owner recovery responsibilities are explicit.

### Gate H — portability
- Optional modules are selected explicitly rather than forced.
- A new Skills repo can receive the generic starter foundation plan-first.
- Existing target Skills are never overwritten automatically.
- Multiple capable agent/provider routes can satisfy the same owner/verification contract.
- GitHub-hosted execution is sufficient for ordinary deterministic work where appropriate; trusted runtimes remain optional exceptions.

### Gate I — learning and continuity
- One real workflow has run end to end.
- Reusable learning has been promoted to the correct owner.
- Material Stage/programme state is recorded in the controlling GitHub Issue.
- A fresh agent can continue from GitHub alone without a hidden chat transcript.

## Definition of healthy

ARC is healthy when a fresh human or capable agent can navigate from a business need to the correct method, live owner, narrow authorised integration/runtime route and verifiable evidence without relying on one person's memory or hidden chat.

ARC is recoverable when the same operator can pair a known-good ARC release with a valid non-secret estate manifest and the external owners' own backups/reprovisioning paths to reconstruct and re-verify the architecture.
