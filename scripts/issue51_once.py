from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

README = r'''# FolderDesk by iMPLEMENTAi — Your Business AI Operating System

FolderDesk gives your business a **GitHub-first operating desk for humans and AI agents**. It provides the reusable structure, routing, Skills model, deployment and recovery patterns needed to turn capable AI tools into an organised operating environment rather than a collection of disconnected chats.

You keep your own business data, accounts and credentials with their proper owners. FolderDesk supplies the portable operating structure that connects the work.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [Get Started](BOOTSTRAP.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Releases](RELEASES.md) · [Agent Router](AGENTS.md)

## What you get

- a persistent GitHub operating desk for human + AI work;
- reusable Skills instead of repeatedly explaining the same process;
- clear owners for business truth, work and decisions;
- agent routing across repositories, tools and specialist systems;
- a clean way to add connectors, MCP, runtimes, memory and automations;
- deployment, verification and recovery without copying your private business data into FolderDesk;
- an architecture that can grow toward the full **[Ultimate Features](FEATURES.md)** catalogue as you connect the capabilities you need.

## Step 1 — Connect GitHub

**GitHub is the first requirement.** FolderDesk uses GitHub as the durable operating desk where repositories, Skills, Issues, decisions and agent handoffs live.

Before bootstrap, make sure the human or AI agent doing the deployment can access the target GitHub organisation/account and is authenticated for the repository actions you want FolderDesk to perform.

With the CLI, the quick check is:

```bash
gh auth status
```

Then continue with [Get Started / Bootstrap](BOOTSTRAP.md).

## Give this to your agent

Copy and paste this into the AI agent you want to use for deployment:

```text
Open https://github.com/tbhrc/folderdesk and help me deploy FolderDesk into my GitHub organisation.
Read the root AGENTS.md first, then use the smallest relevant FolderDesk guidance.
First confirm that you can access and operate on my target GitHub organisation/account.
Then onboard and bootstrap FolderDesk, keeping me informed as each repository is checked, reused or created and showing the remaining-time estimate during bootstrap.
Do not copy TBHRC private business data or secrets. Use FolderDesk as the portable structure and create/adapt my organisation's own owners and Skills.
After deployment, show me verification status, connection readiness and the next useful capability to activate.
```

That is the intended front door. You do not need to understand the implementation files before asking a capable agent to operate FolderDesk for you.

## How deployment works

At a high level:

```text
connect GitHub
→ describe your organisation
→ FolderDesk plans the repository/owner structure
→ bootstrap streams progress as repositories are reused or created
→ seed the starter Skills
→ verify
→ connect the external tools/runtimes you want
→ start real work
```

FolderDesk reuses existing configured repositories unchanged and creates only missing configured repositories. It does not copy credentials, private files or specialist-system records into the public package.

### CLI path

Create your local deployment profile:

```bash
python3 scripts/arc.py onboard --output arc.json
```

Check GitHub and optional connector readiness:

```bash
python3 scripts/arc.py doctor --config arc.json --connectors
```

Inspect the target when useful:

```bash
python3 scripts/arc.py plan --config arc.json --inspect-target
```

Bootstrap:

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
python3 scripts/seed_foundation.py --config arc.json --apply
python3 scripts/arc.py verify --config arc.json
```

During `bootstrap --apply`, FolderDesk reports the current repository, completed/total count, elapsed time and an estimated remaining time after the first repository check. It should not appear to go silent while GitHub work is happening.

## For agents and operators

FolderDesk also contains a compact machine-facing operating contract:

```text
request
→ root AGENTS.md Repository Router
→ smallest relevant Skill / owner
→ simplest authorised execution route
→ verify real state once
→ preserve material durable context when needed
→ stop
```

Fast Links are pointers, not preload instructions. Reusable HOW belongs in the organisation's canonical Skills repository; live mutable business truth remains with its real owner.

## Safe Harbour

FolderDesk can export a non-secret architecture map for recovery:

```bash
python3 scripts/arc.py export --config arc.json --output arc-estate.json --inspect-target
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

When authorised, missing configured repositories can be reconstructed with:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

External owners recover their own files, records, credentials and runtime state through their own systems.

## What FolderDesk does not do

FolderDesk does **not** copy your editable live business truth, private files, specialist-system records, credentials, runtime machine state or memory contents into this public repository.

It also does not require a daemon, queue, control plane or approval ritual just to perform ordinary authorised work.

## KISSS

> **The operating system must not become the work.**

Prefer the direct route, existing Skill, existing owner or existing tool before adding more machinery.

**`main` keeps progress. KISSS keeps speed. Security protects real boundaries, not paperwork.**
'''

BOOTSTRAP = r'''# Bootstrap FolderDesk

FolderDesk bootstrap is designed for a first-time human user **and** a capable AI agent. The first requirement is GitHub access; after that, the deployment can be driven by the agent or by the CLI.

**Fast links:** **[Ultimate Features](FEATURES.md)** · [README](README.md) · [Atlas](ATLAS.md) · [Architecture](ARCHITECTURE.md) · [Verify](VERIFY.md) · [Safe Harbour](MANIFEST.md) · [Agent Router](AGENTS.md)

## 1. Connect GitHub first

FolderDesk uses GitHub as the durable operating desk. Before bootstrap, confirm that the human or agent performing deployment can access the target GitHub organisation/account.

CLI check:

```bash
gh auth status
```

If GitHub is not connected/authenticated, fix that before `bootstrap --apply`.

## 2. Create the deployment profile

Use Atlas or:

```bash
python3 scripts/arc.py onboard --output arc.json
```

A capable agent that already knows the required facts can use `onboard --non-interactive`.

`onboard` writes local configuration only.

## 3. Resolve only required ownership facts

Establish only what deployment actually needs:

- target GitHub owner;
- repository visibility;
- required domain owners;
- canonical Skills home;
- private-file owner;
- specialist-system owners;
- runtime/provider route where relevant.

Do not put secret values in `arc.json`.

## 4. Inspect readiness when useful

```bash
python3 scripts/arc.py doctor --config arc.json --connectors
python3 scripts/arc.py plan --config arc.json --inspect-target
```

`doctor --connectors` gives a read-only view of GitHub and declared connector/MCP/runtime readiness. `plan` is visibility, not runtime permission.

Where target state is observable:

```text
REUSE  — repository exists; leave unchanged
CREATE — repository is missing; create in mutating mode
```

## 5. Bootstrap with streamed progress

```bash
python3 scripts/arc.py bootstrap --config arc.json --apply
```

Before repository work begins, FolderDesk states the target and total configured repositories. During the run it reports:

- current repository number / total;
- which repository is being checked;
- whether it was reused or created;
- elapsed time;
- estimated remaining time after the first repository check.

The remaining-time figure is a live estimate based on completed repository checks, not a fixed promise. Its purpose is to keep the user informed instead of leaving a silent bootstrap.

Bootstrap:

- reuses existing repositories unchanged;
- creates missing configured repositories;
- does not copy credentials;
- does not migrate private business data;
- does not rewrite specialist systems.

`--apply` selects mutating mode. It does not create a second approval requirement.

## 6. Repository Router

Each new repository receives a compact root `AGENTS.md` Repository Router plus thin Atlas entrypoints.

Known bounded work should go directly to the smallest relevant Skill/owner. Fast Links are pointers, not preload instructions.

## 7. Seed starter Skills

```bash
python3 scripts/seed_foundation.py --config arc.json --apply
```

Starter Skills exist only to make a blank environment usable. They remain thin bootstrap pointers; the deployed organisation should establish and evolve its own canonical Skills repository.

Existing target Skill files are never overwritten automatically.

## 8. Verify

```bash
python3 scripts/arc.py verify --config arc.json
```

Use [VERIFY.md](VERIFY.md) for observable acceptance.

## 9. Give the deployed system to your agent

After bootstrap, tell your agent:

```text
Work from my FolderDesk GitHub estate. Read the root AGENTS.md of the repository you enter before doing work. Use the smallest relevant Skill/owner, verify the real outcome once, and keep durable work in GitHub rather than only in chat.
```

## 10. Prove one real workflow

A useful deployment proves:

```text
request
→ Repository Router
→ relevant Skill / owner truth
→ authorised execution
→ verify real state
→ preserve material durable context when needed
```

## 11. Export Safe Harbour

```bash
python3 scripts/arc.py export \
  --config arc.json \
  --output arc-estate.json \
  --inspect-target
```

The estate manifest is architecture metadata and owner references, not a backup of private files, specialist-system data, credentials, runtime machine state or memory contents.

## 12. Recover

Inspect when useful:

```bash
python3 scripts/arc.py restore-plan --manifest arc-estate.json --inspect-target
```

Reconstruct missing configured repositories:

```bash
python3 scripts/arc.py restore --manifest arc-estate.json --apply
```

Current restore reuses existing configured repositories unchanged and creates only missing configured repositories. External owners recover their own data and credentials separately.

## KISSS

Do not add another workflow, gate, approval step, provider layer or duplicated operating rule merely to make bootstrap look more governed.
'''

RELEASES = r'''# FolderDesk Release Contract

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
'''

(ROOT / 'README.md').write_text(README, encoding='utf-8')
(ROOT / 'BOOTSTRAP.md').write_text(BOOTSTRAP, encoding='utf-8')
(ROOT / 'RELEASES.md').write_text(RELEASES, encoding='utf-8')

arc_path = ROOT / 'scripts' / 'arc.py'
text = arc_path.read_text(encoding='utf-8')

if 'import time\n' not in text:
    text = text.replace('import subprocess\nimport sys\n', 'import subprocess\nimport sys\nimport time\n', 1)

text = text.replace('print(f"ARC onboarding profile written: {path}")', 'print(f"FolderDesk onboarding profile written: {path}")')
text = text.replace('print(f"ARC doctor for {data[\'target\'][\'owner\']}")', 'print(f"FolderDesk doctor for {data[\'target\'][\'owner\']}")')
text = text.replace('print("ARC deployment plan")', 'print("FolderDesk deployment plan")')
text = text.replace('"message": f"Seed ARC {path}"', '"message": f"Seed FolderDesk {path}"')

old_bootstrap = '''def command_bootstrap(data: dict[str, Any], apply: bool) -> int:\n    if not apply:\n        print("ARC bootstrap preview: no mutation selected. Use --apply to create missing repositories.")\n        return command_plan(data)\n    if not gh_authenticated():\n        raise ArcError("GitHub CLI (gh) must be available and authenticated for --apply")\n    target = data["target"]\n    navigation = navigation_from_config(data)\n    for repo in repos_from_config(data):\n        create_repo(target["owner"], target.get("owner_type", "org"), repo, navigation)\n    print("Repository bootstrap complete. External owner data and credential values were intentionally not modified.")\n    return 0\n'''
new_bootstrap = '''def command_bootstrap(data: dict[str, Any], apply: bool) -> int:\n    if not apply:\n        print("FolderDesk bootstrap preview: no mutation selected. Use --apply to create missing repositories.")\n        return command_plan(data)\n    if not gh_authenticated():\n        raise ArcError("GitHub is FolderDesk's first requirement. Connect/authenticate GitHub before bootstrap --apply.")\n    target = data["target"]\n    navigation = navigation_from_config(data)\n    repos = repos_from_config(data)\n    total = len(repos)\n    started = time.monotonic()\n    print("FolderDesk bootstrap starting.")\n    print(f"GitHub connection: confirmed. Target: {target['owner']}.")\n    print(f"Work ahead: {total} configured repositories will be checked one by one.")\n    print("Time estimate: remaining time will be calculated after the first repository check; progress will stream continuously.")\n    for index, repo in enumerate(repos, start=1):\n        full = f"{target['owner']}/{repo['name']}"\n        print(f"[{index}/{total}] Checking {full}...")\n        create_repo(target["owner"], target.get("owner_type", "org"), repo, navigation)\n        elapsed = max(time.monotonic() - started, 0.0)\n        average = elapsed / index\n        remaining = max(average * (total - index), 0.0)\n        print(f"[{index}/{total}] Complete | elapsed {elapsed:.1f}s | estimated remaining {remaining:.1f}s")\n    elapsed = max(time.monotonic() - started, 0.0)\n    print(f"FolderDesk bootstrap complete in {elapsed:.1f}s. External owner data and credential values were intentionally not modified.")\n    return 0\n'''
if old_bootstrap not in text:
    raise SystemExit('command_bootstrap block not found')
text = text.replace(old_bootstrap, new_bootstrap, 1)

text = text.replace('description="ARC deployment and recovery utility"', 'description="FolderDesk deployment and recovery utility"')
arc_path.write_text(text, encoding='utf-8')

test_path = ROOT / 'tests' / 'test_issue_51_client_ux.py'
test_path.write_text(r'''import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("folderdesk_issue51", ROOT / "scripts" / "arc.py")
arc = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(arc)


class Issue51ClientUxTests(unittest.TestCase):
    def data(self):
        return arc.build_onboarding_config(business_name="Acme", owner="acme")

    def test_bootstrap_streams_progress_and_remaining_time(self):
        out = io.StringIO()
        ticks = iter([100.0, 102.0, 104.0, 106.0, 108.0, 108.0])
        with mock.patch.object(arc, "gh_authenticated", return_value=True), \
             mock.patch.object(arc, "create_repo", return_value=True), \
             mock.patch.object(arc.time, "monotonic", side_effect=lambda: next(ticks)), \
             contextlib.redirect_stdout(out):
            rc = arc.command_bootstrap(self.data(), True)
        rendered = out.getvalue()
        self.assertEqual(rc, 0)
        self.assertIn("FolderDesk bootstrap starting", rendered)
        self.assertIn("GitHub connection: confirmed", rendered)
        self.assertIn("Work ahead: 4 configured repositories", rendered)
        self.assertIn("[1/4] Checking acme/skills", rendered)
        self.assertIn("estimated remaining", rendered)
        self.assertIn("[4/4] Complete", rendered)
        self.assertIn("FolderDesk bootstrap complete", rendered)

    def test_bootstrap_requires_github_in_human_language(self):
        with mock.patch.object(arc, "gh_authenticated", return_value=False):
            with self.assertRaisesRegex(arc.ArcError, "GitHub is FolderDesk's first requirement"):
                arc.command_bootstrap(self.data(), True)

    def test_public_front_door_is_human_first(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Step 1 — Connect GitHub", readme)
        self.assertIn("Give this to your agent", readme)
        self.assertIn("[Ultimate Features](FEATURES.md)", readme)
        self.assertIn("what you get", readme.lower())

    def test_release_contract_uses_folderdesk_product_name(self):
        releases = (ROOT / "RELEASES.md").read_text(encoding="utf-8")
        self.assertTrue(releases.startswith("# FolderDesk Release Contract"))
        self.assertNotIn("# ARC Release Contract", releases)
        self.assertIn("formal FolderDesk release/tag", releases)


if __name__ == "__main__":
    unittest.main()
''', encoding='utf-8')

# Align the older exact-string tests with the current public product identity.
test_arc = ROOT / 'tests' / 'test_arc.py'
t = test_arc.read_text(encoding='utf-8')
t = t.replace('"ARC bootstrap preview: no mutation selected. Use --apply to create missing repositories."', '"FolderDesk bootstrap preview: no mutation selected. Use --apply to create missing repositories."')
t = t.replace('self.assertEqual(description, "ARC deployment and recovery utility")', 'self.assertEqual(description, "FolderDesk deployment and recovery utility")')
test_arc.write_text(t, encoding='utf-8')
