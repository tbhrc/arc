# ARC Verification Contract

Deployment is incomplete until the intended operating loop works.

## Automated baseline

```bash
python3 scripts/arc.py verify-self
python3 scripts/arc.py doctor --config arc.json
python3 scripts/arc.py verify --config arc.json
```

## Human/agent acceptance

A cold agent should be able to enter the deployed environment and answer:

- What is this business/environment trying to achieve?
- Where are reusable Skills?
- Which repository/system owns the current facts for this task?
- Where should durable work be recorded?
- What private data must stay outside public repositories?
- When should Research be triggered?
- When is a trusted runtime required rather than normal execution?
- How is completion verified?

## Required gates

### Gate A — navigation
- Atlas/front-door instructions are discoverable.
- Every core repository has a useful README and agent contract.
- Cross-repository handoffs have a return/onward route.

### Gate B — truth ownership
- At least one real workflow has an explicit Skill owner and fact/state owner.
- Private files and specialist-system state are not duplicated as fake GitHub canon.

### Gate C — execution
- An authorised agent can execute one bounded task through normal tools.
- If privileged runtime is configured, it is used only for an actual runtime gap and has its own verification.

### Gate D — research
- A recurring operational problem can be routed to Research.
- Research can return a qualified Test/Adopt/Watch/Reject decision to the correct owner.

### Gate E — security
- No secret values are committed.
- Routine agents do not use founder/root credentials.
- Repository/public/private boundaries match the deployment plan.

### Gate F — learning
- One real workflow has run end to end.
- Reusable learning has been promoted to the correct Skill/architecture owner.

## Definition of healthy

ARC is healthy when a fresh human or capable agent can navigate from a business need to the correct method, owner, execution route and evidence without relying on one person's memory or a hidden chat transcript.
