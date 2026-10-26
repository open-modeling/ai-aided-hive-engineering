"""Regression checks for human-facing skill metadata and update detection."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_verbose import install, _diagnostics_match


class DisplayNameTests(unittest.TestCase):
    def test_canonical_identity_is_unchanged(self):
        metadata = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertRegex(metadata, r'(?m)^interface:$')
        self.assertRegex(metadata, r'(?m)^  display_name: "Conversation Governor"$')
        frontmatter = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        self.assertRegex(frontmatter, r'(?m)^name: conversation-governor
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
        self.assertEqual(api["name"], "conversation-governor")
        self.assertEqual(api["skill_uri"], "skill:ai-devmode.conversation-governor")

    def test_fresh_install_copies_display_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

    def test_old_install_missing_display_metadata_requires_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            (target / "agents/openai.yaml").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))
            self.assertEqual(install(ROOT, target)["status"], "already_installed")
            self.assertFalse((target / "agents/openai.yaml").exists())
            result = install(ROOT, target, upgrade=True)
            self.assertEqual(result["status"], "upgraded")
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertFalse((pathlib.Path(result["backup"]) / "agents/openai.yaml").exists())
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

if __name__ == '__main__':
    unittest.main()
)
        self.assertRegex(frontmatter, r'(?m)^  display_name: "Conversation Governor"
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
        self.assertEqual(api["name"], "conversation-governor")
        self.assertEqual(api["skill_uri"], "skill:ai-devmode.conversation-governor")

    def test_fresh_install_copies_display_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

    def test_old_install_missing_display_metadata_requires_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            (target / "agents/openai.yaml").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))
            self.assertEqual(install(ROOT, target)["status"], "already_installed")
            self.assertFalse((target / "agents/openai.yaml").exists())
            result = install(ROOT, target, upgrade=True)
            self.assertEqual(result["status"], "upgraded")
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertFalse((pathlib.Path(result["backup"]) / "agents/openai.yaml").exists())
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

if __name__ == '__main__':
    unittest.main()
)
        self.assertRegex(frontmatter, r'(?m)^  skill_version: "0.4.0-dev"
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
        self.assertEqual(api["name"], "conversation-governor")
        self.assertEqual(api["skill_uri"], "skill:ai-devmode.conversation-governor")

    def test_fresh_install_copies_display_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

    def test_old_install_missing_display_metadata_requires_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            (target / "agents/openai.yaml").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))
            self.assertEqual(install(ROOT, target)["status"], "already_installed")
            self.assertFalse((target / "agents/openai.yaml").exists())
            result = install(ROOT, target, upgrade=True)
            self.assertEqual(result["status"], "upgraded")
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertFalse((pathlib.Path(result["backup"]) / "agents/openai.yaml").exists())
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

if __name__ == '__main__':
    unittest.main()
)
        self.assertIn("allow_implicit_invocation: true", metadata)
        api = json.loads((ROOT / "skill-api.json").read_text(encoding="utf-8"))
        self.assertEqual(api["name"], "conversation-governor")
        self.assertEqual(api["skill_uri"], "skill:ai-devmode.conversation-governor")

    def test_fresh_install_copies_display_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

    def test_old_install_missing_display_metadata_requires_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            target = pathlib.Path(directory) / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            (target / "agents/openai.yaml").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))
            self.assertEqual(install(ROOT, target)["status"], "already_installed")
            self.assertFalse((target / "agents/openai.yaml").exists())
            result = install(ROOT, target, upgrade=True)
            self.assertEqual(result["status"], "upgraded")
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertFalse((pathlib.Path(result["backup"]) / "agents/openai.yaml").exists())
            self.assertEqual((target / "agents/openai.yaml").read_bytes(),
                             (ROOT / "agents/openai.yaml").read_bytes())
            self.assertTrue(_diagnostics_match(ROOT, target))

if __name__ == '__main__':
    unittest.main()
