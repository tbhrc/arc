# ARC Agent Provider Portability

ARC is **provider-neutral**. The architecture depends on capability contracts, not on one model vendor.

## Minimum capable-agent contract

An ARC-capable agent route should be able to:

- read current repository/Skill truth;
- follow repository `AGENTS.md` and Atlas routing;
- work with Issues/branches/PRs or an equivalent authorised GitHub capability;
- use connected business systems only within granted authority;
- verify real resulting state;
- leave durable evidence in the correct owner;
- fail closed when required current canon or authority is unavailable.

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
→ preferred authorised provider if available
→ equivalent authorised provider when unavailable/quota-limited
→ deterministic checks remain mandatory
→ record substitution in durable work evidence
```

Provider substitution never lowers ownership, security, verification or approval requirements.
