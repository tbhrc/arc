# ARC Safe-Harbour Contract

ARC safe harbour reconstructs the **portable operating architecture**. It is not a backup product for every external system.

## Recovery equation

```text
known-good ARC release
+
non-secret ARC estate manifest
+
external-owner backups and credentials restored separately
=
reconstructable ARC operating estate
```

## ARC estate manifest owns

The exported manifest may contain only portable architecture metadata:

- manifest schema version;
- ARC version/release reference;
- target business name and GitHub owner/type/visibility metadata;
- repository/domain names, roles, descriptions, required/optional state and visibility;
- declared private-file provider/owner by name only;
- declared specialist systems by name only;
- declared memory/trusted-runtime architecture references;
- optional observed repository existence state;
- compatibility and recovery-boundary metadata.

It must not contain copied live records or credential values.

## External owners remain external

ARC references these owners but does not back up their contents:

| Owner class | ARC manifest stores | Recovery responsibility |
|---|---|---|
| GitHub repositories | topology/roles and optional observed existence | ARC can recreate missing configured repositories; repository content/history requires GitHub/source backup where applicable |
| Private file store | provider/owner name only | restore files through the provider's approved backup/versioning controls |
| CRM / ERP / ATS / accounting | system names/ownership only | restore through the owning system/vendor backup process |
| Credential / secret store | no values | reprovision credentials through the approved identity/secret-management process |
| Trusted runtime | declared repository/role only | restore machine/runtime state through its own owner/runbook |
| Memory | declared provider/role only | rebuild/restore only according to the memory owner's contract; never let it outrank canon |

## Export rule

`arc.py export` is non-mutating. It starts from a valid `arc.json` and may optionally inspect configured GitHub repository existence. Export must fail if secret-like configuration fields are present.

The manifest is architecture evidence, not proof that external backups exist.

## Restore-plan rule

`arc.py restore-plan` is non-mutating. It must identify:

- target GitHub owner;
- repositories that are already present versus missing where observable;
- repository roles and visibility;
- external owners that must be restored/reconnected separately;
- credential/manual prerequisites;
- the verification path after reconstruction.

## Restore apply boundary

`arc.py restore --apply` is intentionally narrow. It may only use ARC's existing conservative repository bootstrap path to recreate missing configured GitHub repositories and seed their ARC contracts.

It must not:

- restore or copy private files;
- write CRM/ERP/ATS/accounting records;
- create credential values;
- grant broad organisation privileges;
- recreate VPS/Mac/runtime state;
- overwrite existing repositories;
- claim the estate is recovered before `VERIFY.md` passes.

## Compatibility

Manifest schema `1.0` is the initial safe-harbour contract. ARC must validate the schema before restore planning/apply. A future incompatible manifest schema requires an explicit migration path rather than silent guessing.

The manifest records the ARC version that exported it. Release notes must state which manifest schema the release supports.

## Release guarantee

A formal ARC release guarantees only that the tagged ARC repository state and its declared manifest schema passed that release's repository verification at publication time.

A release does **not** guarantee:

- that a client's external backups are current;
- that credentials remain valid;
- that third-party APIs/providers have not changed;
- that live business data is present;
- that a trusted runtime machine still exists.

Recovery is complete only after repository reconstruction, external-owner restoration/reconnection and the full ARC verification contract succeed.
