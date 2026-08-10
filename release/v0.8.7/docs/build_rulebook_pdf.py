#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess
import sys
import shutil

ROOT = Path(__file__).resolve().parents[1]
RULEBOOK = ROOT / "docs" / "rulebook.md"
RELEASE = ROOT / "release" / "v0.8.7"
OUT = RELEASE / "docs" / "rulebook.pdf"
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
  - \\titleformat{\\section}{\\Large\\bfseries\\color{fyrbrown}}{\\thesection}{0.7em}{}
  - \\titleformat{\\subsection}{\\large\\bfseries\\color{fyrbrown}}{\\thesubsection}{0.7em}{}
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

def main() -> int:
    if not shutil.which("pandoc"):
        print("Pandoc saknas. Installera pandoc för att bygga regelboks-PDF.", file=sys.stderr)
        return 1
    if not shutil.which("xelatex"):
        print("xelatex saknas. Installera TeX Live / xelatex för PDF-export.", file=sys.stderr)
        return 1

    BUILD.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)

    body = RULEBOOK.read_text(encoding="utf-8")
    body = re.sub(r"^# Fyrens väktare – regler\s*", "", body)

    PANDOC_MD.write_text(FRONTMATTER + "\n" + body, encoding="utf-8")

    cmd = [
        "pandoc", str(PANDOC_MD),
        "-o", str(OUT),
        "--pdf-engine=xelatex",
        "--highlight-style=tango",
    ]
    subprocess.check_call(cmd, cwd=str(ROOT))
    print(f"Skapade {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
