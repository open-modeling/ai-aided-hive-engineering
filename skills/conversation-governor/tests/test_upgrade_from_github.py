import importlib.util
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("cg_updater", ROOT / "scripts" / "upgrade_from_github.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)

class GitHubUpgradeTests(unittest.TestCase):
    def test_ref_validation(self):
        for value in ("feature/conversation-governor-communication-only",
                      "f01de0bee3d227bf5208c44971e8dd089498597e", "core-v5.0.0"):
            self.assertEqual(module.validate_ref(value), value)
        for value in ("--upload-pack=x", "../x", "x//y", "a.lock", "a/.b", ""):
            with self.assertRaises(ValueError):
                module.validate_ref(value)

    def test_fetch_verifies_identity(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)
            source=root/"checkout"/"skills"/"conversation-governor"
            source.mkdir(parents=True)
            (source/"SKILL.md").write_text("skill")
            (source/"scripts").mkdir()
            (source/"scripts"/"install_verbose.py").write_text("script")
            (source/"skill-api.json").write_text(json.dumps({
                "skill_uri":module.EXPECTED_URI,"lifecycle_classification":"stateless"}))
            with patch.object(module,"_git",side_effect=["", "", "", "abc123"]) as fake:
                found,sha=module.fetch_package(root,"feature/test")
            self.assertEqual(found,source)
            self.assertEqual(sha,"abc123")
            self.assertEqual(fake.call_count,4)

    def test_upgrade_delegates_to_installer(self):
        with tempfile.TemporaryDirectory() as d:
            from subprocess import CompletedProcess
            project=pathlib.Path(d)
            source=project/"source"
            source.mkdir()
            (source/"scripts").mkdir()
            (source/"scripts"/"install_verbose.py").write_text("x")
            with patch.object(module,"fetch_package",return_value=(source,"abcdef")), \
                 patch.object(module.subprocess,"run",return_value=CompletedProcess(
                     [],0,stdout=json.dumps({"installation":"upgraded","backup":"saved","host_verified":False}),stderr="")) as run:
                result=module.upgrade(ref="feature/test",project=project,dest=project/"dest")
            self.assertEqual(result["source_commit"],"abcdef")
            command=run.call_args.args[0]
            self.assertIn("--upgrade",command)
            self.assertIn("--verbose",command)
            self.assertNotIn("--no-hook",command)
            self.assertFalse(result["host_verified"])
