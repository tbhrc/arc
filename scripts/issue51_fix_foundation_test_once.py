from pathlib import Path

path = Path('tests/test_foundation.py')
text = path.read_text(encoding='utf-8')
text = text.replace('self.assertEqual(len(rows), 4)', 'self.assertEqual(len(rows), 5)', 1)
needle = '        self.assertIn("research-escalation/SKILL.md", paths)\n'
insert = '        self.assertIn("document-intake/SKILL.md", paths)\n'
if insert not in text:
    if needle not in text:
        raise SystemExit('foundation test insertion point not found')
    text = text.replace(needle, needle + insert, 1)
path.write_text(text, encoding='utf-8')
