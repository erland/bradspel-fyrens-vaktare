#!/usr/bin/env python3
"""Bygg preview-PDF:er från källor.

Detta script används av GitHub Actions och kan köras lokalt. Det kräver inte
output/ eller release/ i repo.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--release-name", default="preview")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.output_dir).resolve()

    validation = subprocess.run([sys.executable, "scripts/ci_validate_project.py", "."], cwd=root)
    if validation.returncode != 0:
        return validation.returncode

    if out.exists():
        shutil.rmtree(out)

    subprocess.check_call(
        [
            sys.executable,
            "scripts/build_print_and_play.py",
            "--output-dir",
            str(out),
            "--release-name",
            args.release_name,
        ],
        cwd=root,
    )

    print(f"Preview skapad i {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
