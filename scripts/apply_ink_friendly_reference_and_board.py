#!/usr/bin/env python3
"""Ink-friendly transform för A6-referens och spelplan.

Filen innehåller rena hjälpfunktioner som används av build_print_and_play.py.
Den kan även köras lokalt med explicita in- och utvägar.
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def body_of_svg(svg_text: str) -> str:
    start = svg_text.find(">") + 1
    end = svg_text.rfind("</svg>")
    return svg_text[start:end].strip()


def apply_reference_style(text: str, label: str = "ink-friendly") -> str:
    replacements = {
        '#f2ead7': '#ffffff',
        '#f8f0df': '#fffdf8',
        '#5b452b': '#ede6da',
        '#fff7e9': '#2d261d',
        '#f0e4c9': '#6b6257',
        '#7e6a4d': '#8a8176',
        '#fff9ee': '#ffffff',
        '#fffaf0': '#2d261d',
        '#b88c3a': '#f4e3b8',
        '#5f5769': '#ece8f3',
        '#6f8a4a': '#e4efd8',
        '#5e8d7e': '#ddeee8',
        '#b79d48': '#f5ebc8',
        '#c08f34': '#f6e7c9',
        '#7e6b9f': '#ece8f8',
        '#fff8eb': '#ffffff',
        '#f8f2ff': '#ffffff',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace('styled v0.7.5', label)
    text = text.replace('styled v0.7.1', label)
    return text


def build_reference_4up(a6_text: str) -> str:
    inner = body_of_svg(a6_text)
    positions = [(10, 10), (121, 10), (10, 164), (121, 164)]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="210.00mm" height="297.00mm" viewBox="0 0 210.00 297.00">']
    parts.append('<rect x="0" y="0" width="210" height="297" fill="#ffffff"/>')
    for x, y in positions:
        parts.append(f'<g transform="translate({x:.2f},{y:.2f})">')
        parts.append(inner)
        parts.append('</g>')
    parts.append('</svg>')
    return "\n".join(parts)


def apply_board_style(text: str, label: str = "ink-friendly") -> str:
    replacements = {
        '#f2ead7': '#ffffff',
        '#f8f0df': '#fffdf8',
        '#5b452b': '#ede6da',
        '#fff8eb': '#2d261d',
        '#e6d6b7': '#6b6257',
        '#fff9ee': '#ffffff',
        '#dce8c7': '#eef5e6',
        '#efe7b1': '#faf5df',
        '#eadcc8': '#f5efe8',
        '#dfddd7': '#f4f3ef',
        '#f5e6e1': '#fbf1ee',
        '#f6f1ea': '#faf7f2',
        '#f8f2ff': '#faf8ff',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace('styled v0.7.2', label)
    text = text.replace('styled v0.7.1', label)
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference-in")
    parser.add_argument("--reference-out")
    parser.add_argument("--reference-4up-out")
    parser.add_argument("--board-in")
    parser.add_argument("--board-out")
    parser.add_argument("--label", default="ink-friendly")
    args = parser.parse_args()

    if args.reference_in and args.reference_out:
        ref = apply_reference_style(Path(args.reference_in).read_text(encoding="utf-8"), args.label)
        Path(args.reference_out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.reference_out).write_text(ref, encoding="utf-8")
        if args.reference_4up_out:
            Path(args.reference_4up_out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.reference_4up_out).write_text(build_reference_4up(ref), encoding="utf-8")

    if args.board_in and args.board_out:
        board = apply_board_style(Path(args.board_in).read_text(encoding="utf-8"), args.label)
        Path(args.board_out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.board_out).write_text(board, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
