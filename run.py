#!/usr/bin/env python3
"""Run validate, docs, and generate using this directory's piip_config.yaml."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

CONFIG = Path(__file__).resolve().parent / "piip_config.yaml"


def main() -> int:
    commands = (
        ["validate"],
        ["docs"],
        ["generate"],
    )
    for extra in commands:
        cmd = [sys.executable, "-m", "piip", *extra, "--config", str(CONFIG)]
        print("+", " ".join(cmd), flush=True)
        result = subprocess.run(cmd, check=False)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
