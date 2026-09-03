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
- contains aligned Atlas, manifest, bootstrap, verification and compatibility contracts;
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

For ARC 0.3.x, the supported estate-manifest schema is `1.0`.

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

## First formal release

ARC `v0.3.0` is intended to be the first formal public release after ARC.4 merges and the merged commit passes normal ARC CI. The release must not be published until that verification is complete.
