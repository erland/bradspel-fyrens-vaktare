from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

A6_INPUT = ROOT / "release/v0.8.0/print/svg/reference-card-a6.svg"
BOARD_INPUT = ROOT / "release/v0.8.0/print/svg/board-a4.svg"

REF_OUT = ROOT / "output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.8.1-styled-inkfriendly.svg"
REF4_OUT = ROOT / "output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.8.1-styled-inkfriendly.svg"
BOARD_OUT = ROOT / "output/print/board/board-a4-REGLERV4-STARTBALANS-v0.8.1-styled-inkfriendly.svg"
PREVIEW_OUT = ROOT / "output/preview/board-a4-REGLERV4-STARTBALANS-v0.8.1-styled-inkfriendly.svg"

def body_of_svg(svg_text: str) -> str:
    start = svg_text.find(">") + 1
    end = svg_text.rfind("</svg>")
    return svg_text[start:end].strip()

def apply_reference_style(text: str) -> str:
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
        '#f8f2ff': '#ffffff'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace('styled v0.7.5', 'ink-friendly v0.8.1')
    return text

def build_reference_4up(a6_text: str) -> str:
    inner = body_of_svg(a6_text)
    positions = [(10,10), (121,10), (10,164), (121,164)]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="210.00mm" height="297.00mm" viewBox="0 0 210.00 297.00">']
    parts.append('<rect x="0" y="0" width="210" height="297" fill="#ffffff"/>')
    for x, y in positions:
        parts.append(f'<g transform="translate({x:.2f},{y:.2f})">')
        parts.append(inner)
        parts.append('</g>')
    parts.append('</svg>')
    return "\n".join(parts)

def apply_board_style(text: str) -> str:
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
    text = text.replace('styled v0.7.2', 'ink-friendly v0.8.1')
    return text

def main():
    ref_text = apply_reference_style(A6_INPUT.read_text(encoding='utf-8'))
    REF_OUT.parent.mkdir(parents=True, exist_ok=True)
    REF_OUT.write_text(ref_text, encoding='utf-8')
    REF4_OUT.write_text(build_reference_4up(ref_text), encoding='utf-8')

    board_text = apply_board_style(BOARD_INPUT.read_text(encoding='utf-8'))
    BOARD_OUT.parent.mkdir(parents=True, exist_ok=True)
    BOARD_OUT.write_text(board_text, encoding='utf-8')
    PREVIEW_OUT.parent.mkdir(parents=True, exist_ok=True)
    PREVIEW_OUT.write_text(board_text, encoding='utf-8')

if __name__ == '__main__':
    main()
