#!/usr/bin/env python3
"""Bygg preview-PDF:er för allt som ska skrivas ut."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
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


def svg_to_pdf(svg: Path, pdf: Path) -> None:
    try:
        import cairosvg  # type: ignore
    except ImportError as exc:
        raise RuntimeError("cairosvg saknas. Installera med: pip install cairosvg") from exc
    pdf.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.output_dir).resolve()
    release = latest_release(root)

    validation = subprocess.run([sys.executable, "scripts/ci_validate_project.py", "."], cwd=root)
    if validation.returncode != 0:
        return validation.returncode

    if out.exists():
        shutil.rmtree(out)
    (out / "print" / "pdf").mkdir(parents=True)
    (out / "docs").mkdir(parents=True)

    print(f"Bygger preview från {release.relative_to(root)}")

    # Regenerera print-PDF:er från release-SVG:erna.
    for svg in sorted((release / "print" / "svg").glob("*.svg")):
        pdf = out / "print" / "pdf" / f"{svg.stem}.pdf"
        print(f"SVG → PDF: {svg.relative_to(root)} -> {pdf.relative_to(out)}")
        svg_to_pdf(svg, pdf)

    # Bygg regelboks-PDF från aktuell docs/rulebook.md.
    if shutil.which("pandoc") and shutil.which("xelatex"):
        subprocess.check_call([sys.executable, "scripts/build_rulebook_pdf.py"], cwd=root)
    else:
        print("Pandoc/xelatex saknas; använder befintlig regelboks-PDF från release.", file=sys.stderr)

    rulebook_pdf = release / "docs" / "rulebook.pdf"
    if not rulebook_pdf.exists():
        raise RuntimeError(f"Regelboks-PDF saknas: {rulebook_pdf}")
    shutil.copy2(rulebook_pdf, out / "docs" / "rulebook.pdf")

    # Kopiera stödjande release-info.
    for name in ("README.md", "RELEASE_MANIFEST.json"):
        src = release / name
        if src.exists():
            shutil.copy2(src, out / name)

    summary = out / "BUILD_SUMMARY.md"
    pdfs = sorted([p.relative_to(out).as_posix() for p in out.rglob("*.pdf")])
    summary.write_text(
        "# Fyrens väktare – print preview\n\n"
        f"Källa: `{release.relative_to(root)}`\n\n"
        "PDF-filer:\n"
        + "\n".join(f"- `{p}`" for p in pdfs)
        + "\n",
        encoding="utf-8",
    )

    print(f"Preview skapad i {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
