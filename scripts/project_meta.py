#!/usr/bin/env python3
from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
META = tomllib.loads((ROOT / "project.toml").read_text(encoding="utf-8"))

def get(path: str):
    value = META
    for part in path.split("."):
        value = value[part]
    return value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: project_meta.py SECTION.KEY")
    value = get(sys.argv[1])
    if isinstance(value, bool):
        print("true" if value else "false")
    else:
        print(value)
