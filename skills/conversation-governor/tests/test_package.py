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
    def test_identity_and_host_display(self):
        text = (ROOT / "SKILL.md").read_text()
        host = (ROOT / "agents/openai.yaml").read_text()
        api = json.loads((ROOT / "skill-api.json").read_text())
        self.assertIn('display_name: "Conversation Governor"', text)
        self.assertIn('display_name: "Conversation Governor"', host)
        self.assertIn("allow_implicit_invocation: true", host)
        self.assertIn('skill_version: "' + api["version"] + '"', text)
        self.assertEqual(api["name"], "conversation-governor")

if __name__ == "__main__":
    unittest.main()
