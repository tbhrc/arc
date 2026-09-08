from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

readme = ROOT / "README.md"
r = readme.read_text(encoding="utf-8")
r = r.replace("## Start here — give this to your agent", "## Start here — Give this to your agent", 1)
r = r.replace("remember what matters, retrieve it later, and produce finished business work", "remember what matters, find it again later, and produce finished business work", 1)
r = r.replace("## What FolderDesk gives you", "## What you get", 1)
readme.write_text(r, encoding="utf-8")

test = ROOT / "tests" / "test_issue_52_client_experience.py"
t = test.read_text(encoding="utf-8")
t = t.replace('self.assertIn("Start here — give this to your agent", text)', 'self.assertIn("Start here — Give this to your agent", text)', 1)
t = t.replace('self.assertIn("Discover and connect the systems", text)', 'self.assertIn("Infer, then connect, the systems", text)', 1)
test.write_text(t, encoding="utf-8")
