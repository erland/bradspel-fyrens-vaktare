#!/usr/bin/env python3
"""Bygg regelboks-PDF från docs/rulebook.md.

Skriptet skriver som standard till dist/docs/rulebook.pdf, men kan även få en
explicit --output. Det beror inte på output/ eller release/.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RULEBOOK = ROOT / "docs" / "rulebook.md"
BUILD = ROOT / "build" / "rulebook-pdf"
PANDOC_MD = BUILD / "rulebook-pandoc.md"

FRONTMATTER = """---
title: "Fyrens väktare"
subtitle: "Regelbok"
lang: sv-SE
documentclass: article
papersize: a4
fontsize: 10.5pt
geometry:
  - top=22mm
  - bottom=24mm
  - left=22mm
  - right=22mm
mainfont: "DejaVu Serif"
sansfont: "DejaVu Sans"
monofont: "DejaVu Sans Mono"
colorlinks: true
linkcolor: black
urlcolor: black
header-includes:
  - \\usepackage{titlesec}
  - \\usepackage{xcolor}
  - \\usepackage{fancyhdr}
  - \\usepackage{enumitem}
  - \\definecolor{fyrbrown}{HTML}{5B452B}
  - \\definecolor{fyrlight}{HTML}{F4E3B8}
  - \\definecolor{fyrline}{HTML}{826742}
  - \\titleformat{\\section}{\\Large\\bfseries\\color{fyrbrown}}{}{0pt}{}
  - \\titleformat{\\subsection}{\\large\\bfseries\\color{fyrbrown}}{}{0pt}{}
  - \\titlespacing*{\\section}{0pt}{1.4em}{0.55em}
  - \\titlespacing*{\\subsection}{0pt}{1.0em}{0.35em}
  - \\setlist{nosep,leftmargin=*}
  - \\pagestyle{fancy}
  - \\fancyhf{}
  - \\lhead{Fyrens väktare}
  - \\rhead{Regelbok}
  - \\cfoot{\\thepage}
  - \\renewcommand{\\headrulewidth}{0.3pt}
  - \\renewcommand{\\footrulewidth}{0pt}
  - \\usepackage{tcolorbox}
  - \\tcbset{colback=fyrlight!25,colframe=fyrline,arc=2mm,boxrule=0.4pt,left=2mm,right=2mm,top=1mm,bottom=1mm}
---
"""


def build_rulebook_pdf(output: Path) -> Path:
    if not shutil.which("pandoc"):
        raise RuntimeError("Pandoc saknas. Installera pandoc för att bygga regelboks-PDF.")
    if not shutil.which("xelatex"):
        raise RuntimeError("xelatex saknas. Installera TeX Live / xelatex för PDF-export.")

    BUILD.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)

    body = RULEBOOK.read_text(encoding="utf-8")
    body = re.sub(r"^# Fyrens väktare – regler\s*", "", body)

    PANDOC_MD.write_text(FRONTMATTER + "\n" + body, encoding="utf-8")

    cmd = [
        "pandoc", str(PANDOC_MD),
        "-o", str(output),
        "--pdf-engine=xelatex",
        "--highlight-style=tango",
    ]
    subprocess.check_call(cmd, cwd=str(ROOT))
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(ROOT / "dist" / "docs" / "rulebook.pdf"))
    args = parser.parse_args()

    try:
        out = build_rulebook_pdf(Path(args.output).resolve())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Skapade {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
