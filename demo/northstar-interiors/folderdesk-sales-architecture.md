# Northstar Interiors — FolderDesk Sales Architecture

> **Synthetic demo fixture.** Northstar Interiors is fictional. No real client, candidate, contact, commercial or private TBHRC data is used here.

## Objective

Turn one ordinary business instruction into structured, durable execution that survives the chat and can be continued by another authorised person or AI.

## Smallest viable architecture

```text
Sales user
→ FolderDesk AI interface
→ sales Skill / process rule
→ CRM + company operating canon
→ approved actions / workflows
→ verified CRM / work-state update
→ management visibility
```

## Operating flow

1. A sales user states the business outcome in plain language.
2. FolderDesk identifies the relevant operating rule and durable owner.
3. The request becomes a structured implementation/work item rather than a disposable chat answer.
4. Approved tools act on the relevant business systems.
5. Durable state is written back to the owning system and linked from the controlling work item.
6. The result is verified once against the real backend state.
7. Another authorised operator can resume from the same state without reconstructing the conversation.

## Phase 0 boundaries

The demo proves:
- continuity beyond a chat session;
- organised routing of work and truth;
- authorised execution that leaves observable state;
- a verifiable handoff point for the next operator.

It does **not** claim:
- guaranteed ROI or productivity uplift;
- complete CRM implementation;
- full autonomous business operation;
- every possible FolderDesk integration;
- production acceptance by a real external client.

## Exact next actions

1. Confirm the target CRM and source-of-truth owner for the real customer deployment.
2. Map the smallest sales workflow and approval boundary.
3. Connect only the systems required for that first workflow.
4. Run one bounded proof using synthetic/test data.
5. Verify the resulting CRM/work state and management visibility.
6. Expand only after the first workflow passes acceptance.

## Demo proof

Controlling issue: https://github.com/tbhrc/folderdesk/issues/54

**Before:** one plain-language request.  
**After:** structured work, a durable architecture artifact and exact next actions.

**FolderDesk:** instruction → organised execution → durable proof.
