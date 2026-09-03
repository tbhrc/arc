# Generic Business Profile

Use this profile to deploy ARC into a new business or client without importing TBHRC-specific names.

1. Copy `arc.example.json` to a local `arc.json`.
2. Set the target GitHub owner and visibility.
3. Rename/add domain repositories to match how the business actually owns work.
4. Keep or disable the optional trusted runtime.
5. Run `doctor`, `plan`, then `bootstrap --apply` only after review.
6. Use Atlas to complete owner mapping and agent onboarding.

The profile intentionally does not contain secret fields.
