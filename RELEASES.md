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

A release is an architecture/recovery anchor, not a guarantee that a client's external systems or backups are healthy.

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

Current `restore --apply` leaves existing configured repositories unchanged and creates only missing configured repositories.

See [contracts/safe-harbour.md](contracts/safe-harbour.md).

## Published releases

- `v0.3.0` — Safe Harbour; first formal safe-harbour release.
- `v1.0.0` — Blank-Slate Reproduction Proven; first formal 1.x public release.

## Current release candidate

ARC `v1.1.0` is the Repository Router and zero-friction alignment release candidate.

It aligns ARC with the current operating model:

- root `AGENTS.md` is the first-hop Repository Router;
- generated repositories receive the compact Router contract;
- Fast Links are progressive pointers;
- owner lookup is conditional;
- Workflow and Multi-Agent Orchestrator load only when their functions are genuinely needed;
- ordinary authorised mutation executes directly;
- Issues/PRs are continuity/evidence surfaces when useful, not runtime permission;
- recovery is bounded reconstruction rather than a separate approval class;
- generic least-privilege, redundant-provider and approval-control-plane doctrine is not core ARC architecture;
- estate-manifest schema remains `1.0`;
- private/live external state and credential recovery remain external-owner responsibilities.

Compatibility evidence: the covered ARC behavior passed the then-current full 23-test suite on Python **3.9.6**. ARC no longer invents a Python 3.10 requirement through `doctor`; compatibility claims must follow executable evidence.

The formal `v1.1.0` release should point to the final reconciled `main` commit after normal ARC verification passes. Do not retag or rewrite `v1.0.0`.
