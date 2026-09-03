import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SecurityContractTests(unittest.TestCase):
    def test_governance_contract_covers_core_boundaries(self):
        text = (ROOT / "contracts/governance.md").read_text(encoding="utf-8")
        for phrase in (
            "Repository visibility",
            "Branch and merge baseline",
            "Actions permissions",
            "Runner trust boundary",
            "Break-glass / root authority",
            "Credential lifecycle",
        ):
            self.assertIn(phrase, text)

    def test_integration_catalogue_covers_required_classes(self):
        text = (ROOT / "integrations/README.md").read_text(encoding="utf-8")
        for phrase in (
            "Email / calendar / identity",
            "Private files",
            "CRM / sales",
            "ATS / HRIS",
            "Finance / accounting / ERP",
            "Website / CMS / DNS",
            "Database / warehouse / BI",
            "Memory / knowledge",
            "Trusted runtime",
        ):
            self.assertIn(phrase, text)

    def test_specialist_system_contract_preserves_live_owner(self):
        text = (ROOT / "components/specialist-systems/README.md").read_text(encoding="utf-8")
        self.assertIn("system that owns the live state remains authoritative", (ROOT / "integrations/README.md").read_text(encoding="utf-8"))
        self.assertIn("never mirror the specialist system", text)
        self.assertIn("least-privilege identity", text)

    def test_default_arc_workflow_is_read_only(self):
        text = (ROOT / ".github/workflows/validate-arc.yml").read_text(encoding="utf-8")
        self.assertRegex(text, re.compile(r"permissions:\s*\n\s*contents:\s*read"))

    def test_public_examples_do_not_contain_obvious_private_key_or_token_values(self):
        paths = [
            ROOT / "profiles/generic-business/arc.example.json",
            ROOT / "README.md",
            ROOT / "ATLAS.md",
            ROOT / "BOOTSTRAP.md",
            ROOT / "integrations/README.md",
        ]
        forbidden = (
            "-----BEGIN PRIVATE KEY-----",
            "github_pat_",
            "ghp_",
            "sk-proj-",
        )
        for path in paths:
            text = path.read_text(encoding="utf-8")
            for marker in forbidden:
                self.assertNotIn(marker, text, f"forbidden credential-like marker in {path}")

    def test_security_policy_links_detailed_contracts(self):
        text = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
        self.assertIn("contracts/governance.md", text)
        self.assertIn("contracts/secrets.md", text)
        self.assertIn("root/break-glass", text)


if __name__ == "__main__":
    unittest.main()
