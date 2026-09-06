# ARC Release Contract

Formal ARC releases are known-good upstream anchors for deployment, upgrade and safe-harbour recovery. Release publication is distribution integrity, not runtime permission.

## Tag convention

```text
vMAJOR.MINOR.PATCH
```

A formal release points to an exact `main` commit that passed normal executable ARC verification.

## What a release guarantees

At publication time, the tagged ARC repository state:

- passed normal ARC repository verification/CI;
- has a declared semantic version in `VERSION`;
- states the estate-manifest schema(s) it supports;
- contains aligned Router, Atlas, manifest, bootstrap and verification contracts;
- records material changes and genuine known limitations.

## Published releases

- `v0.3.0` — Safe Harbour.
- `v1.0.0` — Blank-Slate Reproduction Proven.

`v1.1.0` was an internal unreleased alignment candidate and is superseded by `v1.2.0`; do not create or backfill a release for it.

## Current release candidate — v1.2.0

ARC `v1.2.0` aligns the portable architecture with the current zero-friction operating model while reducing duplicated canon.

Material changes:

- Anti-Drift/durable-evidence is optional continuity, not architecture or runtime admission;
- no named Anti-Drift Issue structure is required by ARC;
- README/Architecture/Bootstrap now describe the minimum route only;
- starter Workflow and owner-router Skills are thin bootstrap pointers, not competing operating doctrine;
- TBHRC reference doctrine points to current `tbhrc/skills` canon;
- each deployed organisation still owns its own evolving Skills canon;
- ordinary authorised work executes directly and verifies once;
- estate-manifest schema remains `1.0`;
- current restore reuses existing configured repositories unchanged and creates only missing configured repositories;
- private/live external state and credential recovery remain external-owner responsibilities.

## Safe-harbour relationship

ARC **1.x** supports estate-manifest schema `1.0` unless a later release explicitly states otherwise.

```text
formal ARC release/tag
+
validated non-secret estate manifest
+
external owner backups/reprovisioning
→ bounded repository reconstruction
→ external owner restoration/reconnection
→ verification
```

## Release notes

Record only useful facts:

```text
ARC version/tag
exact source commit
estate-manifest schema support
material architecture changes
compatibility / migration notes
verification evidence
genuine known limitations / external-owner responsibilities
```

The formal `v1.2.0` release must point to the final reconciled `main` commit after normal ARC verification passes.
