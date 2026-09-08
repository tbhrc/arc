---
name: document-intake
description: Default FolderDesk intake for any file or document a user gives an agent. Preserve/file the source, ingest only useful material, route durable meaning/tasks to the correct owner, preserve provenance, and verify later retrieval.
---

# Document Intake — File It, Learn It, Find It Again

Use this Skill **by default whenever a user gives the agent a file/document** unless a more specific domain Skill owns the intake.

FolderDesk is not complete when an agent merely reads a file in the current chat. The source and its useful organisational meaning must survive the session.

## Default route

```text
RECEIVE
→ FILE SOURCE
→ INVENTORY / IDENTIFY
→ EXTRACT USEFUL CONTENT
→ CLASSIFY
→ ROUTE KNOWLEDGE + TASKS
→ PRESERVE PROVENANCE
→ VERIFY RETRIEVAL
→ STOP
```

## Rules

1. **File the source** — preserve the original document in the organisation's declared private-file owner/project folder when an authorised write route exists. Do not bulk-copy private binaries into public GitHub. If the source is already durably stored, reuse it and preserve its stable locator instead of duplicating it.
2. **Identify it deterministically** — record enough metadata to distinguish the document: source/provider, stable id or path/locator where available, filename/title, type and useful modified/version marker. This is inventory, not ingestion.
3. **Ingest useful material** — extract/read the material needed for the user's work. Do not report a file as ingested merely because it was listed or inventoried.
4. **Classify and route** — place durable business meaning with the correct canonical owner. Reusable operating HOW belongs in the organisation's Skills owner. Neutral identity belongs with the organisation's identity/data owner where applicable. Domain facts stay with the domain owner.
5. **Create/attach tasks when the document implies work** — actions, deadlines, decisions or follow-ups should become durable task/work state in the organisation's normal task owner rather than remaining trapped in chat.
6. **Preserve provenance** — retained facts/summaries/actions must point back to the source locator/id/path so another agent can verify them.
7. **Verify retrieval** — before calling intake complete, prove that a future agent can find both (a) the source document or durable source locator and (b) the useful canonical knowledge/task state derived from it using a reasonable filename/topic/person/project query.
8. **No duplicate corpus** — do not create a new global vector database, document lake, daemon or duplicate knowledge store merely for intake. Use the organisation's existing file owner, canonical owners and search/retrieval surfaces.

## Completion test

A file intake is GREEN only when all are true:

- original source is durably filed or already durably stored with a preserved locator;
- useful content was actually extracted when needed;
- durable meaning/tasks were routed to the correct owner;
- provenance is preserved;
- retrieval was tested successfully.

If any one is missing, report the exact incomplete stage rather than saying the file is "saved" or "remembered".

## Reference implementation

The TBHRC/iMPLEMENTAi reference implementation uses LOOP3 for bounded ingestion and LIB1 for canonical placement. Other organisations should keep equivalent behaviour in their own canonical Skills system without depending on TBHRC-private business data.
