#!/usr/bin/env python3
"""Paketera en print-and-play-release för GitHub Releases."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
import re


def version_key(path: Path) -> tuple[int, ...]:
    m = re.fullmatch(r"v(\d+(?:\.\d+)*)", path.name)
    return tuple(int(p) for p in m.group(1).split(".")) if m else ()


def latest_release(root: Path) -> Path:
    releases = [p for p in (root / "release").iterdir() if p.is_dir() and version_key(p)]
    if not releases:
        raise RuntimeError("Ingen release/vX.Y.Z-katalog hittades.")
    return sorted(releases, key=version_key)[-1]


def zip_dir(source: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--release-name", default="")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.output_dir).resolve()
    release = latest_release(root)
    release_name = args.release_name or release.name

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    with tempfile.TemporaryDirectory() as tmp:
        preview = Path(tmp) / "print-preview"
        subprocess.check_call(
            [sys.executable, "scripts/ci_build_print_preview.py", "--output-dir", str(preview)],
            cwd=root,
        )

        package_root = Path(tmp) / f"fyrens-vaktare-{release_name}-print-and-play"
        package_root.mkdir(parents=True)

        # Preview-PDF:erna är regenererade och används som releasepaketets print/pdf.
        shutil.copytree(preview / "print", package_root / "print")
        shutil.copytree(release / "print" / "svg", package_root / "print" / "svg", dirs_exist_ok=True)

        (package_root / "docs").mkdir()
        for rel in [
            "docs/rulebook.pdf",
            "docs/rulebook.md",
            "docs/quickstart.md",
            "docs/production-guide.md",
            "docs/first-playtest-checklist.md",
        ]:
            src = release / rel
            if src.exists():
                dst = package_root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)

        for name in ("README.md", "RELEASE_MANIFEST.json"):
            src = release / name
            if src.exists():
                shutil.copy2(src, package_root / name)

        zip_path = out / f"fyrens-vaktare-{release_name}-print-and-play.zip"
        zip_dir(package_root, zip_path)

        # Ladda också ut separata PDF-assets, så GitHub Release kan få direktlänkar.
        assets_dir = out / "pdf-assets"
        assets_dir.mkdir()
        for pdf in sorted((preview / "print" / "pdf").glob("*.pdf")):
            shutil.copy2(pdf, assets_dir / pdf.name)
        shutil.copy2(preview / "docs" / "rulebook.pdf", assets_dir / "rulebook.pdf")

        asset_list = out / "ASSETS.md"
        assets = [zip_path.name] + [f"pdf-assets/{p.name}" for p in sorted(assets_dir.glob("*.pdf"))]
        asset_list.write_text(
            "# Release assets\n\n" + "\n".join(f"- `{a}`" for a in assets) + "\n",
            encoding="utf-8",
        )

    print(f"Releasepaket skapat i {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
