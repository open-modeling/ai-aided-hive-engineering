#!/usr/bin/env python3
"""Build a standalone Conversation Governor package from a local repository."""
import argparse
from pathlib import Path
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
def build(repository_root: Path, output: Path):
    license_file = repository_root / "LICENSE"
    if not license_file.is_file():
        raise ValueError("The local repository LICENSE is required for source distribution.")
    required = ("SKILL.md", "skill-api.json", "CHANGELOG.md",
                "references/dictionary.md", "references/operations.md",
                "standards/ads/00_governance_and_bootstrap.md",
                "standards/ads/skill-architecture/SA-02_skill_architecture_framework.md")
    for name in required:
        if not (ROOT / name).is_file():
            raise ValueError("Required package file is missing: " + name)
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        package = Path(tmp) / "conversation-governor"
        shutil.copytree(ROOT, package, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
        shutil.copy2(license_file, package / "LICENSE")
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(package.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(package.parent).as_posix())
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    print(build(args.repository_root, args.output))
