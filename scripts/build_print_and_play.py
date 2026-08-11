#!/usr/bin/env python3
"""Bygg komplett print-and-play-paket från källor.

Detta är den centrala lokala byggscriptet som även används av GitHub Actions.
Det läser från källor i data/docs/scripts/assets och skriver till en valfri
output-katalog, normalt dist/print-and-play.

Inget i output/ eller release/ behövs som källa.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import render_styled_printables as styled  # noqa: E402
from apply_ink_friendly_reference_and_board import (  # noqa: E402
    apply_board_style,
    apply_reference_style,
    build_reference_4up,
)

PRINT_SVGS = {
    "board-a4.svg",
    "reference-card-a6.svg",
    "reference-card-a4-4up.svg",
    "fyndkort-a4-4x4.svg",
    "hotkort-a4-4x4.svg",
}


def svg_to_pdf(svg: Path, pdf: Path) -> None:
    try:
        import cairosvg  # type: ignore
    except ImportError as exc:
        raise RuntimeError("cairosvg saknas. Installera med: pip install cairosvg") from exc
    pdf.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2pdf(url=str(svg), write_to=str(pdf))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_if_exists(src: Path, dst: Path) -> None:
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def build_svgs(out: Path, label: str) -> list[Path]:
    svg_dir = out / "print" / "svg"
    svg_dir.mkdir(parents=True, exist_ok=True)

    # Spelplan och A6 skapas först från renderer-källan och transformeras sedan
    # till ink-friendly-variant. Release/ eller output/ används inte som input.
    ref_svg = apply_reference_style(styled.build_reference_svg(), label=label)
    board_svg = apply_board_style(styled.build_board_svg(), label=label)

    files = {
        "reference-card-a6.svg": ref_svg,
        "reference-card-a4-4up.svg": build_reference_4up(ref_svg),
        "board-a4.svg": board_svg,
        "fyndkort-a4-4x4.svg": styled.build_card_sheet("fynd"),
        "hotkort-a4-4x4.svg": styled.build_card_sheet("hot"),
    }

    written: list[Path] = []
    for name, text in files.items():
        path = svg_dir / name
        write_text(path, text)
        written.append(path)

    return written


def build_pdfs(out: Path, svgs: list[Path]) -> list[Path]:
    pdf_dir = out / "print" / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdfs = []
    for svg in svgs:
        pdf = pdf_dir / f"{svg.stem}.pdf"
        print(f"SVG → PDF: {svg.relative_to(out)} -> {pdf.relative_to(out)}")
        svg_to_pdf(svg, pdf)
        pdfs.append(pdf)
    return pdfs


def build_rulebook(out: Path) -> Path:
    pdf = out / "docs" / "rulebook.pdf"
    subprocess.check_call(
        [sys.executable, "scripts/build_rulebook_pdf.py", "--output", str(pdf)],
        cwd=str(ROOT),
    )
    return pdf


def copy_docs(out: Path) -> None:
    for rel in [
        "docs/rulebook.md",
        "docs/quickstart.md",
        "docs/production-guide.md",
        "docs/first-playtest-checklist.md",
        "docs/playtest-guide.md",
    ]:
        copy_if_exists(ROOT / rel, out / rel)


def write_release_metadata(out: Path, release_name: str) -> None:
    manifest = {
        "release": release_name,
        "purpose": "Print-and-play-paket genererat från projektkällor.",
        "generated_from_sources": True,
        "print_files": {
            "pdf": [
                "print/pdf/board-a4.pdf",
                "print/pdf/reference-card-a6.pdf",
                "print/pdf/reference-card-a4-4up.pdf",
                "print/pdf/fyndkort-a4-4x4.pdf",
                "print/pdf/hotkort-a4-4x4.pdf",
            ],
            "svg": [
                "print/svg/board-a4.svg",
                "print/svg/reference-card-a6.svg",
                "print/svg/reference-card-a4-4up.svg",
                "print/svg/fyndkort-a4-4x4.svg",
                "print/svg/hotkort-a4-4x4.svg",
            ],
        },
        "docs": [
            "docs/rulebook.pdf",
            "docs/rulebook.md",
            "docs/quickstart.md",
            "docs/production-guide.md",
            "docs/first-playtest-checklist.md",
            "docs/playtest-guide.md",
        ],
        "source_of_truth": {
            "rules": "data/rules.yaml",
            "board": "data/board.yaml",
            "cards": "data/cards.yaml",
            "reference_card": "data/reference-card.yaml",
            "visual_style": "data/visual-style.yaml",
            "ink_friendly_style": "data/ink-friendly-style.yaml",
            "print_renderer": "scripts/render_styled_printables.py",
            "ink_friendly_transform": "scripts/apply_ink_friendly_reference_and_board.py",
            "package_builder": "scripts/build_print_and_play.py",
            "rulebook_pdf_builder": "scripts/build_rulebook_pdf.py",
        },
    }
    write_text(out / "RELEASE_MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=2))

    readme = f"""# Fyrens väktare – print-and-play {release_name}

Det här paketet är genererat från projektets källfiler.

## Skriv ut från PDF

- `print/pdf/board-a4.pdf`
- `print/pdf/reference-card-a6.pdf`
- `print/pdf/reference-card-a4-4up.pdf`
- `print/pdf/fyndkort-a4-4x4.pdf`
- `print/pdf/hotkort-a4-4x4.pdf`
- `docs/rulebook.pdf`

## SVG

SVG-filerna i `print/svg/` är genererade exportfiler och kan användas för kontroll,
vidare export eller felsökning.

## Källor

De verkliga källorna finns inte i det här releasepaketet utan i projekt-repot:

- `data/`
- `docs/`
- `scripts/`
- `assets/`
- `templates/`

Bygg om paketet lokalt med:

```bash
python scripts/build_print_and_play.py --output-dir dist/print-and-play --release-name {release_name}
```
"""
    write_text(out / "README.md", readme)


def validate_built_package(out: Path) -> None:
    missing = []
    for rel in [
        "README.md",
        "RELEASE_MANIFEST.json",
        "docs/rulebook.pdf",
        "print/pdf/board-a4.pdf",
        "print/pdf/reference-card-a6.pdf",
        "print/pdf/reference-card-a4-4up.pdf",
        "print/pdf/fyndkort-a4-4x4.pdf",
        "print/pdf/hotkort-a4-4x4.pdf",
        "print/svg/board-a4.svg",
        "print/svg/reference-card-a6.svg",
        "print/svg/reference-card-a4-4up.svg",
        "print/svg/fyndkort-a4-4x4.svg",
        "print/svg/hotkort-a4-4x4.svg",
    ]:
        path = out / rel
        if not path.exists() or (path.is_file() and path.stat().st_size == 0):
            missing.append(rel)
    if missing:
        raise RuntimeError("Byggpaketet saknar filer: " + ", ".join(missing))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=str(ROOT / "dist" / "print-and-play"))
    parser.add_argument("--release-name", default="local")
    parser.add_argument("--clean", action="store_true", default=True)
    args = parser.parse_args()

    out = Path(args.output_dir).resolve()
    if args.clean and out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    label = "ink-friendly"
    print(f"Bygger print-and-play från källor till {out}")

    svgs = build_svgs(out, label=label)
    build_pdfs(out, svgs)
    build_rulebook(out)
    copy_docs(out)
    write_release_metadata(out, args.release_name)
    validate_built_package(out)

    print(f"Klart: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
