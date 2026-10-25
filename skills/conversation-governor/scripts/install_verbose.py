#!/usr/bin/env python3
"""Install or inspect Conversation Governor with optional A02 hook diagnostics.

This is a project-owned companion to Codex's stock skill-installer, not a
replacement for it. --verbose runs an offline smoke test. --prepare-hook
writes an explicitly requested, nonblocking project-local diagnostic hook.
Only a real trusted Codex session can establish host invocation.
"""
import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile

SKILL_NAME = "conversation-governor"
MARKER = "CG_A02_VERBOSE_INSTALL_001"


def skill_root():
    return Path(__file__).resolve().parents[1]


def destination():
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills" / SKILL_NAME


def _is_skill(path):
    if not (path / "SKILL.md").is_file() or not (path / "skill-api.json").is_file():
        return False
    try:
        meta = json.loads((path / "skill-api.json").read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return False
    return (meta.get("skill_uri") == "skill:ai-devmode.conversation-governor"
            and meta.get("lifecycle_classification") == "stateless")


def _diagnostics_match(source, target):
    """Identify stale installed diagnostics even when manifest versions match."""
    for item in ("scripts/install_verbose.py", "scripts/codex_hook_probe.py",
                 "scripts/hook_adapter.py"):
        left, right = source / item, target / item
        if not left.is_file() or not right.is_file():
            return False
        if left.read_bytes() != right.read_bytes():
            return False
    return True


def install(source, target, upgrade=False):
    """Install a package or explicitly upgrade, preserving an untouched backup."""
    if not _is_skill(source):
        raise ValueError("The source is not a valid Conversation Governor skill.")
    if target.exists():
        if not _is_skill(target):
            raise ValueError("Destination exists but is not the expected skill: " + str(target))
        if not upgrade or source == target:
            return {"status": "already_installed", "backup": None}
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".conversation-governor-stage-", dir=target.parent))
    backup_dir = None
    try:
        for item in source.iterdir():
            if item.name == "__pycache__":
                continue
            to = staging / item.name
            if item.is_dir():
                shutil.copytree(item, to, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            else:
                shutil.copy2(item, to)
        if not _is_skill(staging) or not _diagnostics_match(source, staging):
            raise ValueError("Staged skill validation failed.")
        if target.exists():
            # Keep the entire old skill as a rollback copy; do not delete it.
            backup_dir = Path(tempfile.mkdtemp(
                prefix=".conversation-governor-backup-", dir=target.parent))
            backup = backup_dir / SKILL_NAME
            target.rename(backup)
            try:
                staging.rename(target)
            except OSError:
                backup.rename(target)
                raise
            return {"status": "upgraded", "backup": str(backup)}
        staging.rename(target)
        return {"status": "installed", "backup": None}
    finally:
        if staging.exists():
            shutil.rmtree(staging)
        if backup_dir is not None and backup_dir.exists() and not any(backup_dir.iterdir()):
            backup_dir.rmdir()


def _smoke(path):
    """Synthetic tests only. No host call is made or certified."""
    script = path / "scripts" / "codex_hook_probe.py"
    adapter = path / "scripts" / "hook_adapter.py"
    if not script.is_file() or not adapter.is_file():
        raise ValueError("Required diagnostic scripts are not installed.")
    good = {"hook_event_name": "PreToolUse",
            "tool_name": "collaboration.spawn_agent",
            "tool_input": {"message": "Reply with " + MARKER + "."}}
    proc = subprocess.run(
        [sys.executable, str(script), "--inspect", "--sentinel", MARKER],
        input=json.dumps(good), capture_output=True, text=True, timeout=10, check=False,
    )
    if proc.returncode != 0:
        raise ValueError("Probe smoke test failed (exit code {}).".format(proc.returncode))
    response = json.loads(proc.stdout)
    if (response.get("status") != "candidate"
            or response.get("sentinel_visible") is not True
            or response.get("host_verified") is not False):
        raise ValueError("Probe smoke test returned an unexpected result.")
    checks = []
    for name, expected in (("SendMessage", "registered"),
                           ("TaskList", "excluded"),
                           ("mcp__codex_tui__send_message_to_thread", "unverified")):
        event = {"hook_event_name": "PreToolUse",
                 "tool_name": name, "tool_input": {"message": "Synthetic data"}}
        result = subprocess.run(
            [sys.executable, str(adapter), "--coverage"],
            input=json.dumps(event), capture_output=True,
            text=True, timeout=10, check=False,
        )
        observed = json.loads(result.stdout)
        if result.returncode != 0 or observed.get("status") != expected:
            raise ValueError("Coverage smoke test failed for " + name)
        checks.append({"tool": name, "status": expected,
                       "host_verified": observed.get("host_verified")})
    return {"probe": "passed_synthetic_only", "coverage": checks,
            "host_invocation": "not_tested"}


def _hook_command(source):
    script = (source / "scripts" / "codex_hook_probe.py").resolve()
    return " ".join(shlex.quote(p) for p in
                    (sys.executable, str(script), "--marker", "--observe-unmapped",
                     "--sentinel", MARKER))


def _our_handler(source):
    return {"type": "command", "command": _hook_command(source),
            "statusMessage": "Conversation Governor A02 observation (advisory only)"}


def _hook_path(project):
    return project / ".codex" / "hooks.json"


def _has_our_hook(config):
    for group in config.get("hooks", {}).get("PreToolUse", []):
        for handler in group.get("hooks", []):
            command = handler.get("command", "")
            if (handler.get("type") == "command"
                    and "codex_hook_probe.py" in command
                    and "--observe-unmapped" in command
                    and "CG_A02_VERBOSE_INSTALL_001" in command):
                return True
    return False


def _read_hooks(path):
    if not path.exists():
        return {"hooks": {}}
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict) or not isinstance(obj.get("hooks", {}), dict):
        raise ValueError("Existing hooks.json is not a valid hook configuration.")
    groups = obj.get("hooks", {}).get("PreToolUse", [])
    if not isinstance(groups, list):
        raise ValueError("Existing PreToolUse groups are invalid.")
    return obj


def _atomic_json(path, document):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=path.parent, prefix=".hooks-",
                                     suffix=".json", encoding="utf-8",
                                     delete=False) as fd:
        tmp = Path(fd.name)
        json.dump(document, fd, indent=2, ensure_ascii=False)
        fd.write("\n")
    try:
        tmp.replace(path)
    finally:
        if tmp.exists():
            tmp.unlink()


def configure_hook(project, source):
    """Add a temporary diagnostic to the project, preserving other entries."""
    path = _hook_path(project)
    config = _read_hooks(path)
    if _has_our_hook(config):
        return "already_prepared"
    hooks = config.setdefault("hooks", {})
    hooks.setdefault("PreToolUse", []).append({"hooks": [_our_handler(source)]})
    _atomic_json(path, config)
    return "prepared_requires_codex_trust"


def remove_hook(project):
    """Remove only our synthetic A02 diagnostic, preserve unrelated handlers."""
    path = _hook_path(project)
    if not path.exists():
        return "not_present"
    config = _read_hooks(path)
    groups = config.get("hooks", {}).get("PreToolUse", [])
    changed = False
    remaining = []
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("hooks"), list):
            raise ValueError("Malformed PreToolUse handler group.")
        handlers = []
        for entry in group["hooks"]:
            if _has_our_hook({"hooks": {"PreToolUse": [{"hooks": [entry]}]}}):
                changed = True
            else:
                handlers.append(entry)
        if handlers:
            remaining.append({**group, "hooks": handlers})
    if not changed:
        return "not_present"
    config["hooks"]["PreToolUse"] = remaining
    _atomic_json(path, config)
    return "removed"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=skill_root(),
                        help="Canonical skill source directory.")
    parser.add_argument("--dest", type=Path, default=destination(),
                        help="Codex skill installation directory.")
    parser.add_argument("--project", type=Path, default=Path.cwd(),
                        help="Project root for optional local hook configuration.")
    parser.add_argument("--verbose", action="store_true",
                        help="Install or inspect; run local smoke tests and report hook status.")
    parser.add_argument("--upgrade", action="store_true",
                        help="Explicitly replace an older installed skill and retain a backup.")
    parser.add_argument("--prepare-hook", action="store_true",
                        help="Prepare a project-local, advisory A02 hook (default with --verbose).")
    parser.add_argument("--no-hook", action="store_true",
                        help="Skip project-local hook installation during --verbose.")
    parser.add_argument("--remove-hook", action="store_true",
                        help="Remove the project-local A02 probe hook only.")
    args = parser.parse_args(argv)
    source = args.source.resolve()
    target = args.dest.resolve()
    project = args.project.resolve()
    if args.prepare_hook and args.remove_hook:
        parser.error("--prepare-hook and --remove-hook are mutually exclusive.")
    if args.prepare_hook and args.no_hook:
        parser.error("--prepare-hook and --no-hook are mutually exclusive.")
    if not project.is_dir():
        parser.error("--project must be an existing directory.")
    try:
        if args.remove_hook:
            change = remove_hook(project)
            print(json.dumps({"hook_configuration": change,
                              "host_verified": False}))
            return 0
        change = install(source, target, upgrade=args.upgrade)
        installed_current = _diagnostics_match(source, target)
        info = json.loads((target / "skill-api.json").read_text(encoding="utf-8"))
        result = {"installation": change["status"], "path": str(target),
                  "skill_uri": info["skill_uri"], "version": info["version"],
                  "installed_current": installed_current,
                  "requires_upgrade": not installed_current,
                  "backup": change["backup"], "host_verified": False}
        if args.verbose:
            # Inspect current source when the installed copy is older. Avoid
            # misrepresenting source-only results as installed behavior.
            diagnostic_root = target if installed_current else source
            result["diagnostic_source"] = ("installed" if installed_current else
                                            "source_only_not_installed")
            result["offline"] = _smoke(diagnostic_root)
        prepare = args.prepare_hook or (args.verbose and not args.no_hook)
        if prepare:
            if not installed_current:
                raise ValueError(
                    "Installed skill is older than the verbose diagnostics. "
                    "Run with --upgrade --verbose --prepare-hook to replace it "
                    "explicitly and retain a backup.")
            result["hook_configuration"] = configure_hook(project, target)
        else:
            hooks = _read_hooks(_hook_path(project))
            result["hook_configuration"] = (
                "diagnostic_entry_present_unverified" if _has_our_hook(hooks)
                else "not_prepared")
        result["hook_requires_trust"] = result["hook_configuration"] in (
            "prepared_requires_codex_trust", "diagnostic_entry_present_unverified",
            "already_prepared")
        result["next_step"] = (
            "Installed skill is older than source. Re-run with --upgrade --verbose "
            "to replace it explicitly and retain a backup; --prepare-hook additionally "
            "prepares a temporary hook."
            if not installed_current else
            "Review and trust in Codex /hooks, then make a real harmless Agent "
            "tool call; only real hook invocation can verify host coverage."
            if result["hook_configuration"] != "not_prepared" else
            "Use --prepare-hook for an opt-in project-local probe, "
            "then approve in Codex /hooks.")
        print(json.dumps(result, indent=2 if args.verbose else None))
        return 0
    except (OSError, ValueError, TimeoutError, subprocess.TimeoutExpired) as exc:
        print("Conversation Governor verbose installer: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
