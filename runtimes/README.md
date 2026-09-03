# ARC Runtime Portability

ARC prefers the **least privileged execution route that can safely complete the work**.

## Runtime ladder

```text
normal connected API / MCP / browser / GitHub capability
→ GitHub-hosted Actions when deterministic repository automation is enough
→ local CLI/profile only when the required capability exists there
→ self-hosted Mac/Linux runner for machine-bound execution
→ VPS/trusted runtime for genuine privileged or persistent runtime gaps
```

## Supported runtime patterns

| Runtime | Best use | Default? |
|---|---|---|
| GitHub-hosted Actions | deterministic CI, validation, bounded automation | yes where sufficient |
| Local CLI/profile | authorised operator/agent toolchain | situational |
| Self-hosted Mac/Linux | machine-specific tools, local profiles, hardware/network access | exception |
| VPS | persistent services or privileged infrastructure | exception |

## Rules

- A trusted runtime is not an agent brain or universal control plane.
- Do not route ordinary work through AI Engine/VPS merely because it is available.
- Keep privileged credentials out of public ARC configuration.
- Runtime choice must be visible in the target ownership/configuration plan.
- Every privileged route needs an owner, authority boundary, verification and revocation/teardown path.
- Provider and runtime are orthogonal: changing an AI provider should not require redesigning the runtime architecture.
