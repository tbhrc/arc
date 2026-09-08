# FolderDesk Release Contract

Formal **FolderDesk** releases are known-good upstream anchors for deployment, upgrade and Safe Harbour recovery. Release publication is distribution integrity, not runtime permission.

Internal compatibility names such as `scripts/arc.py`, `arc.json`, `arc_version` and historical ARC evidence may remain where changing them would create unnecessary migration risk. The current **product and release identity is FolderDesk**.

## Tag convention

```text
vMAJOR.MINOR.PATCH
```

A formal FolderDesk release points to an exact `main` commit that passed normal executable repository verification.

## What a release guarantees

At publication time, the tagged FolderDesk repository state:

- passed normal repository verification/CI;
- has a declared semantic version in `VERSION`;
- states the estate-manifest schema(s) it supports;
- contains aligned Router, Atlas, manifest, bootstrap and verification contracts;
- records material changes and genuine known limitations.

## Published releases

- `v0.3.0` — FolderDesk Safe Harbour foundation (published before the public product rename; release metadata is now branded FolderDesk).
- `v1.0.0` — FolderDesk Blank-Slate Reproduction Proven (published before the public product rename; release metadata is now branded FolderDesk).

Historical implementation provenance is preserved; current public release titles and descriptions use FolderDesk.

## Current package

The repository `VERSION` is the current package version. New formal releases must use **FolderDesk** in release names and user-facing release notes.

## Safe Harbour relationship

FolderDesk **1.x** supports estate-manifest schema `1.0` unless a later release explicitly states otherwise.

```text
formal FolderDesk release/tag
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
FolderDesk version/tag
exact source commit
estate-manifest schema support
material architecture changes
compatibility / migration notes
verification evidence
genuine known limitations / external-owner responsibilities
```

Do not publish a current release under the old ARC product name.
