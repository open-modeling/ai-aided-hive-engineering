"""Checks for independent distribution and consistent source metadata."""
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
import sys
sys.path.insert(0, str(ROOT / "scripts"))
from package_skill import build

class PackageTests(unittest.TestCase):
    def test_packaged_standards_and_license(self):
        with tempfile.TemporaryDirectory() as temp:
            path = build(REPO, Path(temp) / "conversation-governor.zip")
            with zipfile.ZipFile(path) as z:
                names = set(z.namelist())
                prefix = "conversation-governor/"
                for item in ("LICENSE", "SKILL.md", "skill-api.json", "references/dictionary.md",
                             "standards/ads/00_governance_and_bootstrap.md",
                             "standards/ads/language-core/LMC-02_terminology_and_meaning_control.md",
                             "standards/ads/skill-architecture/SA-02_skill_architecture_framework.md"):
                    self.assertIn(prefix + item, names)
                self.assertTrue(all(name.startswith(prefix) for name in names))
    def test_activation_rules_and_references(self):
        import re
        from urllib.parse import unquote
        source = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        body = source.split("---", 2)[2]
        self.assertIn("# Conversation Governor", body)
        for heading in ("## Purpose", "## Rules", "## Maintenance"):
            self.assertIn(heading, body)
        self.assertLess(len(body), 1100)
        self.assertNotIn("skill:ai-devmode.conversation-governor", body)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
            filename, _, fragment = target.partition("#")
            path = ROOT / unquote(filename)
            self.assertTrue(path.is_file(), "Missing activation reference: " + target)
            if fragment:
                headings = path.read_text(encoding="utf-8").lower()
                self.assertIn("## " + fragment.replace("-", " "), headings)

    def test_identity_and_host_display(self):
        text = (ROOT / "SKILL.md").read_text()
        host = (ROOT / "agents/openai.yaml").read_text()
        api = json.loads((ROOT / "skill-api.json").read_text())
        self.assertIn('display_name: "Conversation Governor"', text)
        self.assertIn('display_name: "Conversation Governor"', host)
        self.assertIn("allow_implicit_invocation: true", host)
        self.assertIn('skill_version: "' + api["version"] + '"', text)
        self.assertEqual(api["name"], "conversation-governor")
        description = text.split("description: >-", 1)[1].split("\nlicense:", 1)[0]
        self.assertIn("Use whenever an AI agent receives", description)
        self.assertIn("in any language", description)
        for internal_term in ("ADS", "ASD-STE100", "ISO"):
            self.assertNotIn(internal_term, description)
        self.assertIn("every agent message", host)
        self.assertEqual(len(api["applicability"]["when_to_use"]), 2)
        self.assertIn("in any language", api["applicability"]["when_to_use"][0])
        self.assertIn("handoffs", api["applicability"]["when_to_use"][1])
        language_rules = (ROOT / "references/language-rules.md").read_text(encoding="utf-8")
        self.assertIn("## Language applicability", language_rules)
        self.assertIn("For other languages", language_rules)
        self.assertIn("English-specific vocabulary and grammar restrictions only to English", language_rules)
        baseline = (ROOT / "requirements/BASELINE.md").read_text(encoding="utf-8")
        self.assertIn("CG-LR-01 | **MUST** | apply applicable ADS", baseline)
        self.assertIn("CG-LR-02 | **MUST** | apply project-authorized ASD-STE100", baseline)

    def test_runtime_scope_and_maintenance(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        communication = (ROOT / "references/communication.md").read_text(encoding="utf-8")
        dictionary = (ROOT / "references/dictionary.md").read_text(encoding="utf-8")
        language = (ROOT / "references/language-rules.md").read_text(encoding="utf-8")
        operations = (ROOT / "references/operations.md").read_text(encoding="utf-8")
        baseline = (ROOT / "requirements/BASELINE.md").read_text(encoding="utf-8")
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))

        self.assertIn("The receiving agent does the task through its host.", skill)
        self.assertIn("The receiving agent performs the task through its host.", communication)
        self.assertIn("Host permission controls govern task execution.", dictionary)
        self.assertIn("designated language review process maintains", language)
        self.assertIn("## Maintenance scope", operations)
        self.assertIn("runtime outputs consist of messages", baseline)
        self.assertIn("## ASD-STE100 language review", language)
        self.assertIn("approved words, meanings, and parts of speech", language)
        self.assertIn("technical nouns and verbs", language)
        self.assertIn("required reference that was unavailable", language)
        self.assertEqual(
            [item["id"] for item in api["capabilities"]],
            ["control-language", "control-messages", "accept-direction"],
        )
        for path in ("scripts/install_verbose.py", "scripts/package_skill.py",
                     "scripts/hook_adapter.py", "references/operations.md"):
            self.assertTrue((ROOT / path).is_file(), path)

if __name__ == "__main__":
    unittest.main()
