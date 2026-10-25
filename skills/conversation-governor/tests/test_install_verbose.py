import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_verbose import install, _smoke, configure_hook, remove_hook, _read_hooks

class VerboseInstallerTests(unittest.TestCase):
    def test_copy_and_existing_install(self):
        with tempfile.TemporaryDirectory() as d:
            target=pathlib.Path(d)/"installed"/"conversation-governor"
            self.assertEqual(install(ROOT,target),"installed")
            self.assertEqual(install(ROOT,target),"already_installed")
            self.assertEqual(json.loads((target/"skill-api.json").read_text())["version"],"0.3.0-dev")

    def test_verbose_smoke(self):
        result=_smoke(ROOT)
        self.assertEqual(result["probe"],"passed_synthetic_only")
        self.assertEqual(result["host_invocation"],"not_tested")
        self.assertEqual([r["status"] for r in result["coverage"]],
                         ["registered","excluded","unverified"])

    def test_hook_creation_idempotent_and_remove_preserves_others(self):
        with tempfile.TemporaryDirectory() as d:
            project=pathlib.Path(d)
            path=project/".codex"/"hooks.json"
            path.parent.mkdir()
            path.write_text(json.dumps({"hooks":{"PreToolUse":[
                {"hooks":[{"type":"command","command":"echo unrelated"}]}]},"metadata":"keep"}))
            self.assertEqual(configure_hook(project,ROOT),"prepared_requires_codex_trust")
            self.assertEqual(configure_hook(project,ROOT),"already_prepared")
            data=_read_hooks(path)
            self.assertEqual(len(data["hooks"]["PreToolUse"]),2)
            self.assertEqual(remove_hook(project),"removed")
            final=_read_hooks(path)
            self.assertEqual(final["metadata"],"keep")
            self.assertEqual(len(final["hooks"]["PreToolUse"]),1)
            self.assertEqual(final["hooks"]["PreToolUse"][0]["hooks"][0]["command"],"echo unrelated")

    def test_cli_verbose_without_activation(self):
        with tempfile.TemporaryDirectory() as d:
            project=pathlib.Path(d)
            target=project/"skill"
            script=ROOT/"scripts"/"install_verbose.py"
            p=subprocess.run([sys.executable,str(script),"--source",str(ROOT),
                              "--dest",str(target),"--project",str(project),
                              "--verbose"],text=True,capture_output=True)
            self.assertEqual(p.returncode,0,p.stderr)
            result=json.loads(p.stdout)
            self.assertEqual(result["hook_configuration"],"not_prepared")
            self.assertFalse(result["host_verified"])
            self.assertEqual(result["offline"]["probe"],"passed_synthetic_only")
            self.assertFalse((project/".codex"/"hooks.json").exists())

    def test_optin_marker_for_unmapped_pretooluse(self):
        script=ROOT/"scripts"/"codex_hook_probe.py"
        event={"hook_event_name":"PreToolUse","tool_name":"OtherTool","tool_input":{}}
        p=subprocess.run([sys.executable,str(script),"--marker","--observe-unmapped"],
                         input=json.dumps(event),capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stderr)
        out=json.loads(p.stdout)["hookSpecificOutput"]
        self.assertIn("observed_unmapped_tool",out["additionalContext"])
        self.assertNotIn("permissionDecision",out)
