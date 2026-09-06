# ARC Agent Provider Portability

ARC is **provider-neutral**. The architecture depends on capability contracts, not on one model vendor.

## Minimum capable-agent contract

An ARC-capable agent route should be able to:

- read current repository/Skill truth;
- follow repository `AGENTS.md` and Atlas routing;
- work with Issues/branches/PRs or an equivalent authorised GitHub capability;
- use connected business systems within the authority required for the intended function;
- verify real resulting state;
- leave durable evidence in the correct owner;
- recover current canon or choose another already-authorised route when one provider/path is unavailable.

Do not convert a missing preferred route into a stop condition when another authorised route can complete the work. Stop only when the real required authority/capability is unavailable or the action crosses a genuine protected boundary.

## Representative provider routes

| Provider/surface | Typical route | ARC position |
|---|---|---|
| ChatGPT | Skills + connectors/tools | supported capable-agent route |
| OpenAI Codex | repo/CLI execution + Skills | supported implementation route |
| Claude | repository/MCP/CLI capable route | supported capable-agent route |
| GitHub Copilot | GitHub-native agent/IDE route | supported GitHub-native route |
| Other capable agent | must satisfy capability contract | allowed; vendor is not canon |

Provider-specific wrappers should remain thin. Do not duplicate ARC architecture or Skills into provider-specific editable copies.

## Failover

```text
required work
→ use an authorised capable provider/route
→ if unavailable or quota-limited, use an equivalent authorised provider/route
→ preserve only real authority/data/destructive boundaries
→ verify the outcome once
```

Provider substitution must not bypass genuine protected boundaries, but it also must not inherit unnecessary restrictions from the unavailable provider. **Keep the work moving through existing authorised capability.**
