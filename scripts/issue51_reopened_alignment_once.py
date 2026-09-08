from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

arc_path = ROOT / "scripts" / "arc.py"
arc = arc_path.read_text(encoding="utf-8")
arc = arc.replace(
    "FolderDesk bootstrap preview: no mutation selected. Use --dry-run for a full read-only simulation or --apply to create missing repositories.",
    "FolderDesk bootstrap preview: no mutation selected. Use --apply to create missing repositories.",
    1,
)

pattern = r'''def command_doctor\(data: dict\[str, Any\], \*, connectors: bool = False\) -> int:.*?\n\ndef command_plan'''
replacement = '''def command_doctor(data: dict[str, Any], *, connectors: bool = False) -> int:\n    print(f"FolderDesk doctor for {data['target']['owner']}")\n    ok = True\n    print(f"PASS Python {sys.version_info.major}.{sys.version_info.minor}")\n    if not gh_available():\n        print("FAIL GitHub CLI (gh) not found")\n        ok = False\n    elif gh_authenticated():\n        print("PASS GitHub CLI found and authenticated")\n        target_ok, target_detail = gh_target_operability(data)\n        print(f"{'PASS' if target_ok else 'CHECK'} GitHub target access: {target_detail}")\n    else:\n        print("FAIL GitHub CLI is not authenticated for the intended target")\n        ok = False\n    operational, detail = execution_contract_status(data)\n    print(f"{'PASS' if operational else 'CHECK'} execution/provider/runtime declaration: {detail}")\n    print("PASS configuration schema")\n    if connectors:\n        command_connection_readiness(data)\n    return 0 if ok else 1\n\n\ndef command_plan'''
arc, count = re.subn(pattern, lambda _: replacement, arc, count=1, flags=re.S)
if count != 1:
    raise RuntimeError("could not align command_doctor")

arc = arc.replace(
    '''    providers = data.get("providers", [])\n    runtimes = data.get("runtimes", [])\n    print(f"- Providers: {', '.join(providers) if providers else 'none declared'}")\n    print(f"- Runtimes: {', '.join(runtimes) if runtimes else 'none declared'}")\n''',
    '''    providers = data.get("providers", [])\n    runtimes = data.get("runtimes", [])\n    if providers:\n        for provider in providers:\n            print(f"- Provider: DECLARED {provider}; external wiring UNVERIFIED")\n    else:\n        print("- Provider: none declared")\n    if runtimes:\n        for runtime in runtimes:\n            print(f"- Runtime: DECLARED {runtime}; external wiring UNVERIFIED")\n    else:\n        print("- Runtime: none declared")\n''',
    1,
)
arc = arc.replace(
    '        print(f"GitHub target access: confirmed ({target_detail}).")',
    '        print(f"GitHub connection: confirmed. Target: {target[\'owner\']}.")\n        print(f"GitHub target access: confirmed ({target_detail}).")',
    1,
)
arc = arc.replace(
    '    print(f"GitHub target access: confirmed ({target_detail}).")',
    '    print(f"GitHub connection: confirmed. Target: {target[\'owner\']}.")\n    print(f"GitHub target access: confirmed ({target_detail}).")',
    1,
)
arc_path.write_text(arc, encoding="utf-8")

bootstrap_path = ROOT / "BOOTSTRAP.md"
bootstrap = bootstrap_path.read_text(encoding="utf-8")
bootstrap = bootstrap.replace(
    "## 3. Infer, then connect, wherever the client's data already lives",
    "## 3. Infer, then connect, the systems and data the client already uses",
    1,
)
bootstrap_path.write_text(bootstrap, encoding="utf-8")

capture_path = ROOT / "CAPTURE_RECALL.md"
capture = capture_path.read_text(encoding="utf-8")
capture = capture.replace(
    "FolderDesk does not depend on one model vendor.",
    "FolderDesk is provider-neutral and does not depend on one model vendor.",
    1,
)
capture_path.write_text(capture, encoding="utf-8")

ux_path = ROOT / "tests" / "test_issue_51_client_ux.py"
ux = ux_path.read_text(encoding="utf-8")
old = '''        with mock.patch.object(arc, "gh_authenticated", return_value=True), \\\n             mock.patch.object(arc, "create_repo", return_value=True), \\\n'''
new = '''        with mock.patch.object(arc, "gh_authenticated", return_value=True), \\\n             mock.patch.object(arc, "gh_target_operability", return_value=(True, "confirmed")), \\\n             mock.patch.object(arc, "inspect_repository_state", return_value=[{"name": r["name"], "full_name": f"acme/{r['name']}", "resolved_name": "", "action": "CREATE"} for r in arc.repos_from_config(self.data())]), \\\n             mock.patch.object(arc, "create_repo", return_value=True), \\\n'''
if old not in ux:
    raise RuntimeError("could not align streamed bootstrap test")
ux = ux.replace(old, new, 1)
ux_path.write_text(ux, encoding="utf-8")
