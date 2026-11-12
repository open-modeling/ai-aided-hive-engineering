import json
import os
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_verbose import install, _smoke, configure_hook, remove_hook, _read_hooks, _diagnostics_match, destination, _release_entry

class VerboseInstallerTests(unittest.TestCase):
    def test_default_discovery_path_and_codex_home_override(self):
        with tempfile.TemporaryDirectory() as d:
            home = pathlib.Path(d)
            with patch.dict(os.environ, {}, clear=True):
                with patch("pathlib.Path.home", return_value=home):
                    self.assertEqual(
                        destination(),
                        home / ".agents" / "skills" / "conversation-governor",
                    )
                    with patch.dict(os.environ, {"CODEX_HOME": str(home / "custom-codex")}):
                        self.assertEqual(
                            destination(),
                            home / "custom-codex" / "skills" / "conversation-governor",
                        )

    def test_installed_rules_and_license_are_compared(self):
        with tempfile.TemporaryDirectory() as d:
            target = pathlib.Path(d) / "skills" / "conversation-governor"
            self.assertEqual(install(ROOT, target)["status"], "installed")
            for name in ("SKILL.md", "references/language-rules.md",
                         "references/communication.md", "LICENSE"):
                with self.subTest(file=name):
                    installed = target / name
                    original = installed.read_bytes()
                    installed.write_bytes(original + b"\n")
                    self.assertFalse(_diagnostics_match(ROOT, target))
                    installed.write_bytes(original)
                    self.assertTrue(_diagnostics_match(ROOT, target))
            (target / "references/hooks.md").unlink()
            self.assertFalse(_diagnostics_match(ROOT, target))

    def test_release_entry_served_by_installer(self):
        version = json.loads((ROOT / "skill-api.json").read_text())["version"]
        self.assertIn("## " + version, _release_entry(ROOT, version))
        with tempfile.TemporaryDirectory() as d:
            project = pathlib.Path(d)
            target = project / "installed" / "conversation-governor"
            cmd = [sys.executable, str(ROOT / "scripts/install_verbose.py"),
                   "--source", str(ROOT), "--dest", str(target),
                   "--project", str(project), "--no-hook"]
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            report = json.loads(first.stdout)
            self.assertIsNone(report["previous_version"])
            self.assertEqual(report["version"], version)
            self.assertIn("## " + version, report["release_entry"])
            self.assertTrue(pathlib.Path(report["changelog_path"]).is_file())
            upgrade = subprocess.run(cmd + ["--upgrade"], capture_output=True, text=True)
            self.assertEqual(upgrade.returncode, 0, upgrade.stderr)
            second = json.loads(upgrade.stdout)
            self.assertEqual(second["installation"], "upgraded")
            self.assertEqual(second["previous_version"], version)
            self.assertTrue(pathlib.Path(second["backup"]).is_dir())

    def test_copy_and_existing_install(self):
        with tempfile.TemporaryDirectory() as d:
            target=pathlib.Path(d)/"installed"/"conversation-governor"
            self.assertEqual(install(ROOT,target)["status"],"installed")
            self.assertEqual(install(ROOT,target)["status"],"already_installed")
            self.assertEqual(json.loads((target/"skill-api.json").read_text())["version"],json.loads((ROOT/"skill-api.json").read_text())["version"])

    def test_existing_stale_install_upgrade_and_backup(self):
        with tempfile.TemporaryDirectory() as d:
            target=pathlib.Path(d)/"skills"/"conversation-governor"
            self.assertEqual(install(ROOT,target)["status"],"installed")
            probe=target/"scripts"/"codex_hook_probe.py"
            probe.unlink()
            self.assertFalse(_diagnostics_match(ROOT,target))
            self.assertEqual(install(ROOT,target)["status"],"already_installed")
            self.assertFalse(probe.exists())
            result=install(ROOT,target,upgrade=True)
            self.assertEqual(result["status"],"upgraded")
            self.assertTrue(probe.exists())
            self.assertTrue(pathlib.Path(result["backup"]).exists())
            self.assertFalse((pathlib.Path(result["backup"])/"scripts"/"codex_hook_probe.py").exists())
            self.assertTrue(_diagnostics_match(ROOT,target))

    def test_stale_verbose_explains_upgrade_instead_of_failing(self):
        with tempfile.TemporaryDirectory() as d:
            project=pathlib.Path(d)
            target=project/"skills"/"conversation-governor"
            install(ROOT,target)
            (target/"scripts"/"codex_hook_probe.py").unlink()
            script=ROOT/"scripts"/"install_verbose.py"
            args=[sys.executable,str(script),"--source",str(ROOT),
                  "--dest",str(target),"--project",str(project),"--verbose","--no-hook"]
            p=subprocess.run(args,text=True,capture_output=True)
            self.assertEqual(p.returncode,0,p.stderr)
            out=json.loads(p.stdout)
            self.assertTrue(out["requires_upgrade"])
            self.assertEqual(out["diagnostic_source"],"source_only_not_installed")
            self.assertEqual(out["offline"]["probe"],"passed_synthetic_only")
            self.assertFalse((target/"scripts"/"codex_hook_probe.py").exists())
            upgraded=subprocess.run(args+["--upgrade"],text=True,capture_output=True)
            self.assertEqual(upgraded.returncode,0,upgraded.stderr)
            self.assertEqual(json.loads(upgraded.stdout)["installation"],"upgraded")

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
                              "--verbose","--no-hook"],text=True,capture_output=True)
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
