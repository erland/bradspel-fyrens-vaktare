#!/usr/bin/env python3
"""Paketera en print-and-play-release för GitHub Releases.

Bygger först allt från källor med scripts/build_print_and_play.py.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def zip_dir(source: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--release-name", default="local")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.output_dir).resolve()
    release_name = args.release_name

    validation = subprocess.run([sys.executable, "scripts/ci_validate_project.py", "."], cwd=root)
    if validation.returncode != 0:
        return validation.returncode

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    with tempfile.TemporaryDirectory() as tmp:
        package_root = Path(tmp) / f"fyrens-vaktare-{release_name}-print-and-play"
        subprocess.check_call(
            [
                sys.executable,
                "scripts/build_print_and_play.py",
                "--output-dir",
                str(package_root),
                "--release-name",
                release_name,
            ],
            cwd=root,
        )

        zip_path = out / f"fyrens-vaktare-{release_name}-print-and-play.zip"
        zip_dir(package_root, zip_path)

        assets_dir = out / "pdf-assets"
        assets_dir.mkdir()
        for pdf in sorted((package_root / "print" / "pdf").glob("*.pdf")):
            shutil.copy2(pdf, assets_dir / pdf.name)
        shutil.copy2(package_root / "docs" / "rulebook.pdf", assets_dir / "rulebook.pdf")

        assets = [zip_path.name] + [f"pdf-assets/{p.name}" for p in sorted(assets_dir.glob("*.pdf"))]
        (out / "ASSETS.md").write_text(
            "# Release assets\n\n" + "\n".join(f"- `{a}`" for a in assets) + "\n",
            encoding="utf-8",
        )

    print(f"Releasepaket skapat i {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
