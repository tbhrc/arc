# FolderDesk Release Contract

Formal **FolderDesk** releases are known-good upstream anchors for deployment, upgrade and Safe Harbour recovery. Release publication is distribution integrity, not runtime permission.

FolderDesk v2 is a deliberate clean break from the old ARC-named prototype contract. Current executable/configuration surfaces use FolderDesk naming only.

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

## Published history

- `v0.3.0` — early Safe Harbour foundation.
- `v1.0.0` — early blank-slate reproduction proof.

## Current release candidate — v2.0.0

`VERSION` already declares `2.0.0` (FolderDesk-native naming and **single-repository-first** deployment contract; additional repositories become explicit optional expansion), but no `v2.0.0` tag/GitHub release has been published yet — `v1.0.0` remains the latest actually-tagged release. Verification (`python3 -m unittest discover -s tests -p 'test_*.py'`) currently reports 3 failures (`test_issue_51_client_ux`, `test_issue_51_document_intake`, `test_issue_52_client_experience`) expecting front-door README copy not yet written. `v2.0.0` should not be tagged until those pass or the expectation is deliberately revised.

Historical commits/audits may retain the terminology that existed at the time. Current product code, configuration and release surfaces do not.

## Current package

The repository `VERSION` is the current package version. New formal releases use **FolderDesk** in release names, code-facing configuration names and user-facing release notes.

## Safe Harbour relationship

FolderDesk **2.x** uses estate-manifest schema `2.0` unless a later release explicitly states otherwise.

```text
formal FolderDesk release/tag
+
validated non-secret estate manifest
+
external owner backups/reprovisioning
→ bounded workspace reconstruction
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
