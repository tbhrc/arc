import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "reconcile_tbhrc_reference.py"
spec = importlib.util.spec_from_file_location("reconcile_tbhrc_reference", MODULE_PATH)
reconcile = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(reconcile)


class ReconcileTBHRCReferenceTests(unittest.TestCase):
    def test_router_membership_parity_uses_names_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            router = root / "router.json"
            reference = root / "reference.json"
            router.write_text(json.dumps({"tbhrc/skills": "x", "tbhrc/folderdesk": "y"}), encoding="utf-8")
            reference.write_text(json.dumps({
                "target": {"owner": "tbhrc"},
                "repositories": [
                    {"name": "skills", "role": "skills", "visibility": "private"},
                    {"name": "folderdesk", "role": "portable-architecture", "visibility": "public"},
                ],
            }), encoding="utf-8")
            self.assertEqual(reconcile.router_repositories(router), {"tbhrc/skills", "tbhrc/folderdesk"})
            self.assertEqual(reconcile.reference_repositories(reference)[1], {"tbhrc/skills", "tbhrc/folderdesk"})

    def test_verify_skill_links_detects_only_missing_targets(self):
        with tempfile.TemporaryDirectory() as tmp:
            skills = Path(tmp)
            (skills / "alpha").mkdir()
            (skills / "alpha" / "SKILL.md").write_text("# Alpha\n", encoding="utf-8")
            links = [
                {"document": "AGENTS.md", "kind": "tree", "path": "alpha", "url": "u1"},
                {"document": "AGENTS.md", "kind": "blob", "path": "alpha/SKILL.md", "url": "u2"},
                {"document": "AGENTS.md", "kind": "tree", "path": "missing", "url": "u3"},
            ]
            broken = reconcile.verify_skill_links(skills, links)
            self.assertEqual([row["path"] for row in broken], ["missing"])

    def test_material_skill_links_deduplicates_per_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            doc = Path(tmp) / "README.md"
            url = "https://github.com/tbhrc/skills/tree/main/ecosystem-librarian"
            doc.write_text(f"[One]({url}) and [Two]({url})\n", encoding="utf-8")
            links = reconcile.material_skill_links((doc,))
            self.assertEqual(len(links), 1)
            self.assertEqual(links[0]["path"], "ecosystem-librarian")


if __name__ == "__main__":
    unittest.main()
