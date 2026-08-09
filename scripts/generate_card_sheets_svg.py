#!/usr/bin/env python3
"""
Generate styled 4x4 card sheets for Fyrens väktare.

Source:
- data/cards.yaml
- data/card-styles.yaml

Output:
- output/print/cards/*-v0.4-styled.svg

This script intentionally uses only SVG shapes, patterns and text.
No bitmap background is required.
"""
from pathlib import Path
import textwrap
import html

# This script is a lightweight source reference for the generated v0.4 files.
# The current committed output was generated from equivalent logic in ChatGPT.
# Future versions can replace this with a full YAML parser if needed.

def escape_xml(text: str) -> str:
    return html.escape(text, quote=False)

def wrap_by_estimate(text: str, font_size: float, width_units: float):
    avg_char = font_size * 0.53
    max_chars = max(8, int(width_units / avg_char))
    return textwrap.wrap(text, width=max_chars)

def note():
    print("Use this file as the starting point for future generator automation.")
    print("Current v0.4 SVGs are stored in output/print/cards/.")

if __name__ == "__main__":
    note()


# v0.4.1 note:
# Header band height increased to improve vertical spacing for titles.
# This iteration was driven by screenshot feedback showing cramped name fields.


# v0.5 note:
# The project now also includes a styled A6 reference card and an A4 4-up sheet.
# Future generator work can unify card sheet and reference card generation.
