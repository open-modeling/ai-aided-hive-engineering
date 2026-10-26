"""Regression checks for consistent human-facing skill metadata."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_verbose import install, _diagnostics_match


class DisplayNameTests(unittest.TestCase):
    def test_consistent_identity(self):
        metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        frontmatter = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
        self.assertIn('display_name: "Conversation Governor"', metadata)
        self.assertIn('display_name: "Conversation Governor"', frontmatter)
        self.assertIn("allow_implicit_invocation: true", metadata)
        self.assertIn("name: conversation-governor", frontmatter)
        self.assertIn('skill_version: "' + api["version"] + '"', frontmatter)
        self.assertEqual(api["name"], "conversation-governor")
        self.assertEqual(api["skill_uri"], "skill:ai-devmode.conversation-governor")

    def test_install_and_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            self.assertTrue(_diagnostics_match(ROOT, target))
            (target / "agents/openai.yaml").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))
            self.assertEqual(install(ROOT, target)["status"], "already_installed")
            result = install(ROOT, target, upgrade=True)
            self.assertEqual(result["status"], "upgraded")
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

if __name__ == "__main__":
    unittest.main()
