#!/usr/bin/env python3
"""Checks that the config still matches the scripts it drives.

- every `script-binding uosc/<name>` in input.conf exists in uosc
- every key in script-opts/uosc.conf and script-opts/thumbfast.conf is a real option
- every bundled JSON file parses

Run from the repository root: python3 .github/scripts/check.py
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def table_keys(source: str, opener: str) -> set[str]:
    """Keys of a Lua table literal that starts with `opener` and ends at a line holding only `}`."""
    start = source.index(opener)
    end = source.index("\n}", start)
    return set(re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=", source[start:end], re.M))


def conf_keys(path: str) -> list[str]:
    keys = []
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            keys.append(line.split("=", 1)[0].strip())
    return keys


def main() -> int:
    errors: list[str] = []

    uosc = read("scripts/uosc/main.lua")
    bindings = set(re.findall(r"bind_command\(\s*['\"]([^'\"]+)['\"]", uosc))
    for name in sorted(set(re.findall(r"script-binding\s+uosc/([\w-]+)", read("input.conf")))):
        if name not in bindings:
            errors.append(f"input.conf: uosc has no binding named '{name}'")

    for conf, source, opener in (
        ("script-opts/uosc.conf", uosc, "defaults = {"),
        ("script-opts/thumbfast.conf", read("scripts/thumbfast.lua"), "local options = {"),
    ):
        known = table_keys(source, opener)
        for key in conf_keys(conf):
            if key not in known:
                errors.append(f"{conf}: unknown option '{key}'")

    for path in sorted(ROOT.glob("scripts/**/*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON ({error})")

    for error in errors:
        print(f"::error::{error}" if "GITHUB_ACTIONS" in os.environ else error)
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
