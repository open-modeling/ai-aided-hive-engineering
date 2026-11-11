"""Checks for independent distribution and consistent source metadata."""
import json
from pathlib import Path
import shutil
import subprocess
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
        self.assertTrue((ROOT / "LICENSE").is_file())
        if (REPO / "LICENSE").is_file():
            self.assertEqual((ROOT / "LICENSE").read_bytes(), (REPO / "LICENSE").read_bytes())
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
    def test_repackage_standalone_installation(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            standalone = temp / "isolated" / "conversation-governor"
            shutil.copytree(ROOT, standalone, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            output = temp / "standalone.zip"
            process = subprocess.run(
                [sys.executable, str(standalone / "scripts/package_skill.py"),
                 "--repository-root", str(temp / "no-repository"),
                 "--output", str(output)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(
                    archive.read("conversation-governor/LICENSE"),
                    (standalone / "LICENSE").read_bytes(),
                )

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
            if target.startswith(("https://", "http://")):
                continue
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
        self.assertIn("Apply to every message", description)
        self.assertIn("Review incoming meaning", description)
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
        self.assertIn("## Conversation-specific extensions", language_rules)
        self.assertIn("ASD-STE100 Issue 9", language_rules)
        self.assertIn("https://www.asd-ste100.org/", language_rules)
        self.assertNotIn("STE_downloads.html", language_rules)
        self.assertIn("For other languages", language_rules)
        self.assertIn("active project's authorized", language_rules)
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
        self.assertIn("Apply [ASD-STE100 Issue 9]", skill)
        self.assertIn("Start reviewed human-facing prose with `✓ `.", skill)
        self.assertIn("Keep Agent message tags", skill)
        self.assertIn("## Review indicator", communication)
        self.assertIn("keep `[INFORMATION]` or `[DIRECTION]` on the first line", communication)
        self.assertIn("host evidence establishes automatic enforcement", communication)
        self.assertIn("host-native interactive questions", communication)
        self.assertIn("Avoid plain-text multiple-choice menus.", communication)
        self.assertIn("CG-FR-03 | **MUST** | request targeted clarification", baseline)
        self.assertIn("using host-native interactive questions when available and appropriate.", baseline)
        self.assertIn("The receiving agent performs the task through its host.", communication)
        self.assertIn("Host permission controls govern task execution.", dictionary)
        self.assertIn("## Conformance evidence", language)
        self.assertIn("designated formal language reviews", language)
        self.assertIn("report the assessment as partial", language)
        self.assertIn("## Maintenance scope", operations)
        self.assertIn("runtime outputs consist of messages", baseline)
        self.assertIn("## Conversation-specific extensions", language)
        self.assertIn("ASD-STE100 Issue 9", language)
        self.assertIn("https://www.asd-ste100.org/", language)
        self.assertEqual(
            [item["id"] for item in api["capabilities"]],
            ["control-language", "control-messages", "accept-direction"],
        )
        for path in ("scripts/install_verbose.py", "scripts/package_skill.py",
                     "scripts/hook_adapter.py", "references/operations.md"):
            self.assertTrue((ROOT / path).is_file(), path)

if __name__ == "__main__":
    unittest.main()
