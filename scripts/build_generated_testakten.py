#!/usr/bin/env python3
"""Regenerate all generated test-archive artifacts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_TIMEOUT_SECONDS = 300
BUILDERS = [
    Path("scripts/build_jura_und_wissenschaft_testakten.py"),
    Path("scripts/build_leitungsfunktionen_testakten.py"),
]


def main() -> int:
    for rel in BUILDERS:
        script = ROOT / rel
        if not script.exists():
            raise SystemExit(f"missing build script: {rel}")
        print(f"==> {rel}", flush=True)
        subprocess.run([sys.executable, str(script)], cwd=ROOT, check=True, timeout=BUILD_TIMEOUT_SECONDS)
    print("all generated test archives rebuilt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
