#!/usr/bin/env python3
"""Upgrade installed Conversation Governor directly from a GitHub ref.

Run this from any Codex shell working directory. The repository is fixed to
the canonical project; the script does not execute downloaded shell snippets.
The fetched project's installer performs the backed-up skill replacement.
Host hooks remain subject to Codex's normal trust/approval process.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPOSITORY_URL = "https://github.com/open-modeling/ai-aided-hive-engineering.git"
DEFAULT_REF = "feature/conversation-governor-communication-only"
PACKAGE_PATH = Path("skills/conversation-governor")
EXPECTED_URI = "skill:ai-devmode.conversation-governor"
_REF_PATTERN = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9._/-]*$")


def validate_ref(value):
    """Reject arguments and invalid Git ref syntax without shell expansion."""
    if (not _REF_PATTERN.fullmatch(value) or ".." in value or "//" in value
            or value.endswith(("/", ".", ".lock")) or "/." in value):
        raise ValueError("Invalid source ref. Use a branch, tag, or commit SHA.")
    return value


def _git(args, *, timeout=120):
    binary = shutil.which("git")
    if not binary:
        raise ValueError("Git is required to upgrade from GitHub.")
    command = [binary, *args]
    try:
        return subprocess.run(command, text=True, capture_output=True,
                              timeout=timeout, check=True).stdout.strip()
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip().splitlines()
        raise ValueError("Git operation failed: " +
                         (detail[-1] if detail else "unknown Git error")) from exc


def fetch_package(workdir, ref):
    """Fetch exactly the requested ref into an isolated checkout."""
    ref = validate_ref(ref)
    checkout = workdir / "checkout"
    checkout.mkdir(exist_ok=True)
    _git(["-C", str(checkout), "init", "-q"])
    _git(["-C", str(checkout), "fetch", "--depth=1", REPOSITORY_URL, ref])
    _git(["-C", str(checkout), "checkout", "-q", "--detach", "FETCH_HEAD"])
    sha = _git(["-C", str(checkout), "rev-parse", "HEAD"])
    source = checkout / PACKAGE_PATH
    manifest_path = source / "skill-api.json"
    if not (source / "SKILL.md").is_file() or not manifest_path.is_file():
        raise ValueError("Fetched ref does not contain Conversation Governor.")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        raise ValueError("Fetched skill metadata cannot be read.") from exc
    if (manifest.get("skill_uri") != EXPECTED_URI
            or manifest.get("lifecycle_classification") != "stateless"
            or not (source / "scripts" / "install_verbose.py").is_file()):
        raise ValueError("Fetched source does not match expected skill identity.")
    return source, sha


def upgrade(*, ref=DEFAULT_REF, project=None, dest=None, verbose=True,
            prepare_hook=True):
    """Return a structured result; do not treat smoke tests as host evidence."""
    if project is None:
        project = Path.cwd()
    project = Path(project).resolve()
    if not project.is_dir():
        raise ValueError("Project directory does not exist: " + str(project))
    if dest is None:
        codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
        dest = codex_home / "skills" / "conversation-governor"
    dest = Path(dest).resolve()
    with tempfile.TemporaryDirectory(prefix="conversation-governor-fetch-") as d:
        source, sha = fetch_package(Path(d), ref)
        command = [sys.executable, str(source / "scripts" / "install_verbose.py"),
                   "--source", str(source), "--dest", str(dest),
                   "--upgrade", "--project", str(project)]
        if verbose:
            command.append("--verbose")
        if not prepare_hook:
            command.append("--no-hook")
        try:
            completed = subprocess.run(command, text=True, capture_output=True,
                                       timeout=120, check=False)
        except subprocess.TimeoutExpired as exc:
            raise ValueError("Installation helper timed out.") from exc
        if completed.returncode != 0:
            detail = (completed.stderr or "").strip()
            raise ValueError("Installation helper failed: " +
                             (detail or ("exit code " + str(completed.returncode))))
        try:
            installed = json.loads(completed.stdout)
        except ValueError as exc:
            raise ValueError("Installation helper returned invalid JSON.") from exc
        if not isinstance(installed, dict):
            raise ValueError("Installation helper returned an unexpected response.")
        return {"source_commit": sha, "source_ref": ref,
                "repository": REPOSITORY_URL, **installed}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default=DEFAULT_REF,
                        help="GitHub branch, tag, or full commit SHA.")
    parser.add_argument("--project", type=Path, default=Path.cwd(),
                        help="Codex project root for optional project-local hooks.")
    parser.add_argument("--dest", type=Path,
                        help="Skill installation path (default: CODEX_HOME/skills).")
    parser.add_argument("--verbose", action="store_true",
                        help="Run synthetic diagnostics; set up advisory hooks unless --no-hook.")
    parser.add_argument("--no-hook", action="store_true",
                        help="Do not add or modify project-local hook registration.")
    args = parser.parse_args(argv)
    try:
        result = upgrade(ref=args.ref, project=args.project, dest=args.dest,
                         verbose=args.verbose, prepare_hook=not args.no_hook)
    except (OSError, ValueError, TimeoutError) as exc:
        print("Conversation Governor GitHub upgrade: " + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
