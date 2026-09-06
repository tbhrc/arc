# ARC Agent Provider Portability

ARC is **provider-neutral**. Architecture depends on capability, not one model vendor.

## Capable route

An ARC-capable route needs only what the requested work actually requires, such as:

- current repository/Skill truth;
- the relevant authorised tools/systems;
- enough authority to perform the intended function;
- real-state verification.

Issues, branches, PRs and durable evidence are available when they materially help continuity, review or recovery; they are not mandatory provider requirements.

Do not convert a missing preferred route into a stop condition when another already-authorised route can complete the work. Stop only when the real required capability/authority is unavailable or the next action crosses a genuine consequential boundary.

## Representative routes

| Provider/surface | Typical route | ARC position |
|---|---|---|
| ChatGPT | Skills + connectors/tools | supported capable-agent route |
| OpenAI Codex | repo/CLI execution + Skills | supported implementation route |
| Claude | repository/MCP/CLI capable route | supported capable-agent route |
| GitHub Copilot | GitHub-native agent/IDE route | supported GitHub-native route |
| Other capable agent | satisfy the required capability | allowed; vendor is not canon |

Provider-specific wrappers should remain thin. Do not duplicate ARC architecture or Skills into provider-specific editable copies.

## Failover

```text
required work
→ use an authorised capable route
→ if unavailable, use another already-authorised capable route
→ preserve only actual consequential boundaries
→ verify once
```

Provider substitution must not inherit unnecessary restrictions from an unavailable provider. **Keep the work moving through existing authorised capability.**
