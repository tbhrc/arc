from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"missing expected text in {path}: {old[:80]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


# README handoff: explicit inference from clues, with Google as canonical example.
replace_once(
    ROOT / "README.md",
    "Ask which systems I already use for files, email/calendar, CRM, ERP/accounting, messaging and other important work. Recommend the smallest useful connector set and connect what I approve using the easiest native/dedicated route available.",
    "Use clues I already give you before asking broad connector questions. If I say where my files, email, CRM, ERP/accounting or other work lives, immediately infer the obvious high-value native connector and recommend connecting it. For example, if I say my documents are in Google, prioritise Google Workspace / Google Drive so you can use my authorised existing documents for filing, retrieval, brand/style learning and business context instead of asking me to upload or explain everything manually. Then ask only for the remaining systems you cannot infer. Recommend the smallest useful connector set and connect what I approve using the easiest native/dedicated route available.",
)
replace_once(
    ROOT / "README.md",
    "- connector-aware operation across the systems you already use;",
    "- proactive connector inference from what you already tell the agent — e.g. documents in Google → prioritise Google Workspace / Drive instead of making you spoon-feed context;",
)

# Bootstrap: make evidence-driven connector inference the first rule.
replace_once(
    ROOT / "BOOTSTRAP.md",
    "## 3. Discover and connect the systems the client already uses\n\nAsk what currently owns:",
    "## 3. Infer, then connect, the systems the client already uses\n\n**Do not start with a generic app questionnaire when the client has already supplied a clue.** Convert explicit business context into the obvious connector recommendation immediately.\n\nCanonical example:\n\n```text\nclient: \"our documents are in Google\"\n→ infer Google Workspace / Google Drive\n→ explain that connecting it lets FolderDesk inspect authorised existing documents, learn business/brand context, file and retrieve work, and avoid redundant manual uploads\n→ connect/authorise it using the lowest-friction native/dedicated route available\n→ inventory/ingest only the relevant authorised scope\n→ ask only about remaining systems that are still unknown\n```\n\nApply the same principle to Microsoft 365/OneDrive/SharePoint, email/calendar, CRM, ERP/accounting, messaging and other named systems.\n\nOnly after using existing clues, ask what still owns:",
)
replace_once(
    ROOT / "BOOTSTRAP.md",
    "Recommend the **smallest useful connector set for real work now**. Prefer native/dedicated authorised connectors. Reuse existing systems rather than replacing them.",
    "Recommend the **smallest useful connector set for real work now**, prioritising connectors that unlock the most existing context with the least client effort. Prefer native/dedicated authorised connectors. Reuse existing systems rather than replacing them. If a named source can supply documents/context directly once authorised, connect it before asking the client to manually reproduce that context.",
)

# Atlas narrative and Skill.
replace_once(
    ROOT / "ATLAS.md",
    "- Discover the systems they already use and connect the smallest useful set through native/dedicated routes where possible.",
    "- Infer connectors from clues already supplied. If the client says their documents are in Google, prioritise Google Workspace / Drive immediately so authorised existing documents can provide filing, retrieval, business and brand context before requesting redundant uploads. Apply the same logic to other clearly named owner systems. Then ask only about systems still unknown.",
)
replace_once(
    ROOT / ".github/skills/atlas/SKILL.md",
    "4. **Systems/connectors:** file store, email/calendar, CRM, ERP/accounting, messaging and other important systems. Recommend/connect the smallest useful set using native/dedicated authorised routes.",
    "4. **Systems/connectors:** infer before asking. When the client names where work already lives, immediately prioritise the obvious high-value native connector. Example: documents in Google → Google Workspace / Drive first, so authorised existing documents can supply filing/retrieval/business/brand context rather than forcing manual uploads. Then ask only about file store, email/calendar, CRM, ERP/accounting, messaging or other systems still unknown. Recommend/connect the smallest useful set using native/dedicated authorised routes.",
)

# Client-experience starter Skill.
replace_once(
    ROOT / "starter/skills/client-experience/SKILL.md",
    "5. **Discover connectors.** Ask which systems own files, email/calendar, CRM, ERP/accounting, messaging and important business data. Recommend the smallest useful connector set. Prefer native/dedicated authorised connectors; do not ask for raw credential values.",
    "5. **Infer connectors before asking.** Use explicit client clues as routing signals. If they say their documents are in Google, immediately recommend/prioritise Google Workspace / Drive so authorised existing documents can provide filing, retrieval, business and brand context; do not make them re-upload or re-explain what the connector can supply. Apply the same rule to clearly named Microsoft 365/OneDrive/SharePoint, CRM, ERP/accounting, email/calendar, messaging and other systems. Ask only about systems still unknown. Prefer the smallest useful native/dedicated connector set; never ask for raw credential values.",
)

# Features catalogue.
replace_once(
    ROOT / "FEATURES.md",
    "| Client experience | Existing-system/connector discovery and smallest-useful-set activation | Core/Connected | Native/dedicated connectors + owner systems |",
    "| Client experience | Proactive connector inference from client clues; named source → high-value native connector | Core/Connected | Atlas + Client Experience Skill |\n| Client experience | Google Workspace / Drive priority when client says documents are in Google | Core/Connected | Google Workspace / Drive connector + document intake |\n| Client experience | Existing-system/connector discovery and smallest-useful-set activation | Core/Connected | Native/dedicated connectors + owner systems |",
)

# Generated client Router inherits proactive inference.
replace_once(
    ROOT / "scripts/arc.py",
    "ask for brand guidelines or representative documents, discover the smallest useful connector set, keep technical evidence behind the scenes, and deliver polished DOCX/PDF when that is the natural business output.",
    "ask for brand guidelines or representative documents, proactively infer connectors from clues already supplied (for example documents in Google → prioritise Google Workspace / Drive), discover the remaining smallest useful connector set, keep technical evidence behind the scenes, and deliver polished DOCX/PDF when that is the natural business output.",
)

# Regression test additions.
test = ROOT / "tests" / "test_issue_52_client_experience.py"
text = test.read_text(encoding="utf-8")
text = text.replace(
    'self.assertIn("smallest useful connector set", text)\n        self.assertIn("polished DOCX and/or PDF", text)',
    'self.assertIn("smallest useful connector set", text)\n        self.assertIn("documents are in Google", text)\n        self.assertIn("Google Workspace / Google Drive", text)\n        self.assertIn("before asking the client to manually reproduce that context", text)\n        self.assertIn("polished DOCX and/or PDF", text)',
    1,
)
text = text.replace(
    'self.assertIn("polished DOCX", skill)\n        self.assertIn("Avoid status theatre", skill)',
    'self.assertIn("polished DOCX", skill)\n        self.assertIn("documents are in Google", skill)\n        self.assertIn("Google Workspace / Drive", skill)\n        self.assertIn("Avoid status theatre", skill)',
    1,
)
text = text.replace(
    'self.assertIn("Existing-system/connector discovery", text)\n        self.assertIn("Polished DOCX/PDF default", text)',
    'self.assertIn("Proactive connector inference from client clues", text)\n        self.assertIn("Google Workspace / Drive priority", text)\n        self.assertIn("Existing-system/connector discovery", text)\n        self.assertIn("Polished DOCX/PDF default", text)',
    1,
)
test.write_text(text, encoding="utf-8")
