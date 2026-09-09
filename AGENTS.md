# AGENTS.md — Repository Router

<!-- ROUTER_SHARED_LIFECYCLE_START -->
**Issue Gate:** Every substantive or durable work unit requires a master controlling Issue; create new substantive Issues from the canonical [Durable Work template](https://github.com/tbhrc/skills/blob/main/.github/ISSUE_TEMPLATE/durable-work.md).

**FolderDesk Lifecycle / Lever:** For substantive ideas/work originating in conversation, use the canonical [Lifecycle Lever](https://github.com/tbhrc/skills/blob/main/github-agent-workflow/scripts/lifecycle_set.py) owned by the [Lifecycle of FolderDesk](https://github.com/tbhrc/skills/blob/main/docs/lifecycle/folderdesk-lifecycle.md): search/reuse first; create exactly once at the truthful initial `idea` or `discussion` stage with priority in the same mutation; later choose the semantic stage through the Lever/native adapter rather than reconstructing label mechanics; lifecycle metadata is evidence/navigation, never runtime permission.

**Close Gate:** Before closing any Issue, read and reconcile its current body; every required `## Checklist` and `## Acceptance Criteria` item must be `[x]`, otherwise keep the Issue open.
<!-- ROUTER_SHARED_LIFECYCLE_END -->
Read this first. Follow only the link needed for the task; do not preload documentation.

**FolderDesk by iMPLEMENTAi owns the portable, non-secret deployment and recovery architecture for reproducing a working Business AI Operating System; mutable live business/system truth stays with its current owner.**

**Core Fast Links:** [Workflow](https://github.com/tbhrc/skills/tree/main/github-agent-workflow) · [Client Experience](starter/skills/client-experience/SKILL.md) · [LOOP3 File Ingestion](https://github.com/tbhrc/skills/tree/main/loop-data-source-ingestion) · [LIB1 Librarian](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian) · [Document Strategy](https://github.com/tbhrc/skills/blob/main/governance/strategies/strategy-cold-start-context-reduction.md) · [Founder Output](https://github.com/tbhrc/skills/blob/main/github-agent-workflow/SKILL.md#founder-facing-output) · [Anti-Friction Security](https://github.com/tbhrc/skills/blob/main/governance/policies/real-boundary-security-and-friction.md) · [Sniper](https://github.com/tbhrc/skills/blob/main/human-ai-operations-map/references/ai-sniper-entry-map.md) · [Multi-Agent Orchestrator](https://github.com/tbhrc/skills/tree/main/github-multi-agent-orchestrator)

**Repository Fast Links:** [README](README.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [FolderDesk Parity](.github/workflows/reconcile-public-skills.yml) · [Public Skill Allowlist](profiles/tbhrc-reference/public-skill-export.json) · [Issues](https://github.com/tbhrc/folderdesk/issues)

## Route

- **Prior cross-session/cross-agent context could materially change the work, you are about to ask the user to repeat material context, or established internal structure/ownership/policy/process is requested but its canonical source/path is unknown** → use [Hindsight Memory](https://github.com/tbhrc/skills/tree/main/hindsight-shared-memory-operator) for focused recall/canon discovery when available; for unknown canon, **search existing GitHub canon first** (Hindsight semantic discovery or direct GitHub search), then fetch/read current owner truth. **Do not reconstruct established canon from local fragments before this search.** Skip for self-contained, current-file-only or direct current-state work where the owner/path is already known.
- **Client-facing onboarding, status or business artifact** → use [Client Experience](starter/skills/client-experience/SKILL.md): treat GitHub as backend infrastructure, learn/adapt tone + output expectations, request brand guidelines or representative documents, discover useful connectors, and default natural business-document outputs to polished DOCX/PDF. Keep technical evidence out of normal client replies.
- **User gives you a file/document** → default to [LOOP3](https://github.com/tbhrc/skills/tree/main/loop-data-source-ingestion) + [LIB1](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian): preserve/file the source in its declared private-file owner, ingest useful material, route durable meaning/tasks to the correct owner with provenance, and verify later retrieval. Inventory alone is not ingestion; do not leave the only useful copy/meaning trapped in chat.
- **Known owner + bounded task** → execute with the most-specific Skill/tool.
- **Owner/source unclear** → use Sniper once, then execute.
- **Any task that will create, file, move, rename or supersede a durable document/output** → run [LIB1](https://github.com/tbhrc/skills/tree/main/ecosystem-librarian) first for canonical placement, semantic vocabulary and material inbound/outbound Fast Links; then hand execution to the owning Skill/workflow. LIB1 is not an approval gate.
- **Ordinary authorised work** → Level 0 Direct.
- **Creating/updating/reviewing a Skill** → use [Skill Builder](https://github.com/tbhrc/skills/tree/main/github-skill-builder) after LIB1 resolves placement/identity; it owns Skill lifecycle and loads Document Strategy/Policies conditionally.
- **Creating/materially restructuring non-Skill agent-consumed operational documentation** → after LIB1 resolves placement/semantics/links, use Workflow + [Document Strategy](https://github.com/tbhrc/skills/blob/main/governance/strategies/strategy-cold-start-context-reduction.md) only for substantive document architecture.
- **Cross-repository work** → use any existing authorised cross-repository route that can perform the task; do not invent another credential.
- **Genuine specialist/parallel need** → use the Multi-Agent Orchestrator only when one direct stream is insufficient.
- **Real consequential boundary** → apply only the smallest effective control protecting that boundary.

## Rules

- **Issue-backed by default.** A master controlling Issue backs every substantive or durable unit of work. Reuse the existing master controlling Issue when it materially helps continuity; create additional Issues only when continuation, handoff, audit/founder visibility, cross-agent work or material chat-only decisions make it useful, and link every such Issue back to the master controlling Issue. If no controlling Issue exists anywhere org-wide for the work, create a new master controlling Issue before proceeding. Do not open or update an Issue for `go`/`continue`/`retry`/`next`, or before every mutation when nothing material changed — continuation against an existing Issue needs no new Issue and no ceremony update. Metadata is never runtime permission, and issue-less substantive work is not permitted.
- Do not require a controlling Issue for ordinary bounded work. Create/use one when durable continuity, coordination or recovery actually benefits from it.
- Material founder/user changes to objective, scope, acceptance, architecture/decision, blocker or continuation state must not remain trapped only in chat; capture them once in the Issue or better owner truth at the natural checkpoint.
- Do not pause authorised execution merely to synchronise Issue metadata. If a controlling Issue exists or was warranted, reconcile it before completion or handoff.
- **Founder scan speed.** Follow the [Workflow founder-facing output convention](https://github.com/tbhrc/skills/blob/main/github-agent-workflow/SKILL.md#founder-facing-output): concise `🟢 GREEN` / `🟠 AMBER` / `🔴 RED` status, `✅` for confirmed completed items, evidence-backed percentages only, and a clickable `Issue: #N` footer when applicable.
- **Friction masquerading as security is prohibited.**
- **Security and compliance controls must earn their place.** Do not narrow repository scope, permissions, runtime reach or tool access merely because “least privilege”, isolation, hardening, or a generic security/compliance convention suggests it. First prove the concrete current threat, obligation or boundary, the material gap in existing controls, and that the proposed restriction is the smallest effective control. Where that proof exists, implement the control; where it does not, retain authenticated purpose-fit authority sufficient for the intended function.
- Use authenticated identity, **purpose-fit authority sufficient for the intended function**, real validation/secret/data protections, and one decisive outcome verification.
- Do not narrow repository scope, permissions, runtime reach or tool access merely because “least privilege” or “hardening” sounds safer.
- Human approval is reserved for genuine consequential boundaries: root/super-admin authority changes, destructive/irreversible actions, spend, legal/compliance commitments, private-data disclosure or material external/client commitments.
- Production-specific controls apply only to actual production-impacting actions.
- Preserve unrelated newer work and avoid concurrent mutation collisions where they are real.
- Never expose secrets, credentials or unnecessary private data.
- Verify the requested outcome once, reconcile material durable state when applicable, then stop.

**`main` keeps progress. KISSS keeps speed. Security protects real boundaries, not paperwork.**