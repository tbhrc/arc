# ARC Runtime Portability

ARC prefers the **simplest authorised execution route that can actually complete the work**.

Authority must be **purpose-fit**: enough to perform the intended function without adding irrelevant capability. Do not choose a weaker route merely because it appears more restrictive.

## Runtime routes

```text
normal connected API / MCP / browser / GitHub capability when it can complete the task
→ GitHub-hosted Actions when deterministic repository automation is useful
→ local CLI/profile when the required capability exists there
→ self-hosted Mac/Linux runner when machine-bound execution is required
→ VPS/trusted runtime when persistent or privileged execution is required
```

This is a capability map, not a mandatory escalation ladder. Start with the route that already has the required authorised capability.

## Supported runtime patterns

| Runtime | Best use |
|---|---|
| GitHub-hosted Actions | deterministic CI, validation and repository automation |
| Local CLI/profile | authorised operator/agent toolchain |
| Self-hosted Mac/Linux | machine-specific tools, local profiles, hardware/network access |
| VPS | persistent services or privileged infrastructure |

## Rules

- A trusted runtime is not an agent brain or universal control plane.
- Reuse an existing authorised route before creating a new bridge, credential or runtime.
- Do not route work through an extra hop merely because that hop exists.
- Do not reject Mac/VPS/local execution merely because a less-capable route looks more restricted.
- Keep secret values out of public ARC configuration.
- Protect actual privileged boundaries; do not manufacture approval or repository-scope restrictions for ordinary authorised work.
- Provider and runtime are orthogonal: changing an AI provider should not require redesigning the runtime architecture.

**Security rule:** use the least restrictive effective guardrail. Runtime restrictions must protect a concrete current boundary, not hypothetical users or generic least-privilege doctrine.
