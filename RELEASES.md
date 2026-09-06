# ARC Release Contract

Formal ARC releases are the known-good upstream anchors used by deployment, upgrade and safe-harbour recovery.

## Tag convention

```text
vMAJOR.MINOR.PATCH
```

A formal release must point to an exact merged `main` commit and must not be created from an unmerged branch.

## What a release guarantees

At publication time, the tagged ARC repository state:

- passed the normal ARC repository verification/CI gates;
- has a declared ARC semantic version in `VERSION`;
- states the estate-manifest schema(s) it supports;
- contains aligned Repository Router, Atlas, manifest, bootstrap, verification and compatibility contracts;
- has release notes identifying material architecture changes and known boundaries.

A release is an architecture/recovery anchor, not a guarantee that a particular client's external systems or backups are healthy.

## What release notes must record

```text
ARC version/tag
exact source commit
estate-manifest schema support
material architecture changes
compatibility / migration notes
verification evidence
known limitations / external-owner responsibilities
```

## Safe-harbour relationship

ARC **1.x** supports estate-manifest schema `1.0` unless a later release explicitly states otherwise.

```text
formal ARC release/tag
+
validated non-secret estate manifest
+
external owner backups/reprovisioning
-> recovery plan
-> explicit repository restore apply
-> external owner restoration/reconnection
-> full ARC verification
```

See [contracts/safe-harbour.md](contracts/safe-harbour.md).

## Published releases

- `v0.3.0` — Safe Harbour; first formal safe-harbour release.
- `v1.0.0` — Blank-Slate Reproduction Proven; first formal 1.x public release.

## Current release candidate

ARC `v1.1.0` is the Repository Router alignment release candidate.

It materially aligns ARC with the current TBHRC Agent Operating System while preserving the existing portability/recovery model:

- root `AGENTS.md` is the first-hop Repository Router;
- generated repositories receive the compact Router contract rather than the legacy ARC Agent Contract;
- Fast Links are progressive pointers;
- owner lookup is conditional;
- Workflow owns Direct / Hybrid / Controlled execution level;
- Multi-Agent Orchestrator owns delegation and genuine parallel coordination only;
- deployment/adoption, destructive recovery, public-proof and real end-to-end workflow proofs have been re-run and accepted;
- estate-manifest schema remains `1.0`;
- private/live external state and credential recovery remain external-owner responsibilities.

Known compatibility boundary: current covered behaviour passes the full 23-test suite on Python 3.9.6, but official ARC support remains Python 3.10+ because `doctor` rejects `<3.10` and CI currently validates Python 3.12 only.

The formal `v1.1.0` release must point to the final reconciled `main` commit after normal ARC CI passes. Do not retag or rewrite `v1.0.0`.