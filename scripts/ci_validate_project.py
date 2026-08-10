#!/usr/bin/env python3
"""CI-validering för Fyrens väktare.

Kontrollerar att projektets viktigaste källor, releasefiler och utskriftsfiler
hänger ihop. Skriptet är avsett att köras både lokalt och i GitHub Actions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

EXPECTED_PRINT_PDFS = {
    "board-a4.pdf",
    "reference-card-a6.pdf",
    "reference-card-a4-4up.pdf",
    "fyndkort-a4-4x4.pdf",
    "hotkort-a4-4x4.pdf",
}

EXPECTED_PRINT_SVGS = {
    name.replace(".pdf", ".svg") for name in EXPECTED_PRINT_PDFS
}

REQUIRED_ROOT_PATHS = (
    "README.md",
    "PROJECT_STATUS.md",
    "CHANGELOG.md",
    "PROJECT_HANDOFF.json",
    "docs/rulebook.md",
    "docs/quickstart.md",
    "docs/production-guide.md",
    "docs/first-playtest-checklist.md",
    "docs/playtest-guide.md",
    "data/game.yaml",
    "data/board.yaml",
    "data/cards.yaml",
    "data/reference-card.yaml",
    "data/visual-style.yaml",
    "data/ink-friendly-style.yaml",
    "scripts/build_rulebook_pdf.py",
    "scripts/apply_ink_friendly_reference_and_board.py",
)

REQUIRED_WORKFLOWS = (
    ".github/workflows/01-validate.yml",
    ".github/workflows/02-build-preview.yml",
    ".github/workflows/03-release.yml",
)

LOCAL_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def add_warning(warnings: list[str], message: str) -> None:
    warnings.append(message)
    print(f"WARNING: {message}", file=sys.stderr)


def version_key(path: Path) -> tuple[int, ...]:
    m = re.fullmatch(r"v(\d+(?:\.\d+)*)", path.name)
    if not m:
        return ()
    return tuple(int(part) for part in m.group(1).split("."))


def latest_release(root: Path, errors: list[str]) -> Path | None:
    release_root = root / "release"
    if not release_root.exists():
        add_error(errors, "release/-katalogen saknas.")
        return None
    candidates = [p for p in release_root.iterdir() if p.is_dir() and version_key(p)]
    if not candidates:
        add_error(errors, "Ingen release/vX.Y.Z-katalog hittades.")
        return None
    return sorted(candidates, key=version_key)[-1]


def read_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except ImportError:
        raise RuntimeError("PyYAML saknas. Installera med: pip install pyyaml")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    for md in sorted(root.rglob("*.md")):
        rel_parts = set(md.relative_to(root).parts)
        if ".git" in rel_parts or "archive" in rel_parts or "build" in rel_parts:
            continue
        text = md.read_text(encoding="utf-8")
        for target in LOCAL_LINK_RE.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target)
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                add_error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")


def validate_rulebook(root: Path, errors: list[str]) -> None:
    text = (root / "docs/rulebook.md").read_text(encoding="utf-8")
    forbidden_patterns = {
        r"\*\*Version:\*\*": "Synlig versionsrad ska inte finnas i regelboken.",
        r"##\s*Utskrift\b": "Utskriftsavsnitt ska inte ligga i spelarregelboken.",
        r"##\s*Första speltest\b": "Speltestavsnitt ska inte ligga i spelarregelboken.",
        r"första spelbara prototypen": "Prototypformulering ska inte ligga i spelarregelboken.",
    }
    for pattern, message in forbidden_patterns.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            add_error(errors, message)


def validate_data(root: Path, errors: list[str], warnings: list[str]) -> None:
    try:
        board = read_yaml(root / "data/board.yaml")
        cards = read_yaml(root / "data/cards.yaml")
        ref = read_yaml(root / "data/reference-card.yaml")
    except Exception as exc:
        add_error(errors, f"Kunde inte läsa YAML-data: {exc}")
        return

    layout = board.get("grid", {}).get("layout", [])
    rows = board.get("grid", {}).get("rows")
    cols = board.get("grid", {}).get("columns")
    if len(layout) != rows:
        add_error(errors, f"board.yaml: antal layout-rader ({len(layout)}) matchar inte rows ({rows}).")
    for i, row in enumerate(layout, start=1):
        if len(row) != cols:
            add_error(errors, f"board.yaml: rad {i} har {len(row)} kolumner, väntat {cols}.")

    values = board.get("darkness_track", {}).get("values", [])
    if 10 not in values or 0 not in values:
        add_error(errors, "board.yaml: Mörkerspåret bör innehålla både 10 och 0.")

    card_list = cards.get("cards", [])
    ids = [c.get("id") for c in card_list]
    if len(ids) != len(set(ids)):
        add_error(errors, "cards.yaml: kort-id:n är inte unika.")
    decks = {}
    for c in card_list:
        decks[c.get("deck")] = decks.get(c.get("deck"), 0) + 1
        for key in ("id", "name", "deck", "type", "effect"):
            if not c.get(key):
                add_error(errors, f"cards.yaml: kort saknar {key}: {c!r}")
    if decks.get("fynd") != 12:
        add_error(errors, f"cards.yaml: väntade 12 fyndkort, hittade {decks.get('fynd', 0)}.")
    if decks.get("hot") != 12:
        add_error(errors, f"cards.yaml: väntade 12 hotkort, hittade {decks.get('hot', 0)}.")

    section_titles = [s.get("title") for s in ref.get("sections", [])]
    for needed in ("Start", "Tur & handlingar", "Mat", "Basen", "Nattfas", "Platser", "Fyren"):
        if needed not in section_titles:
            add_error(errors, f"reference-card.yaml: saknar sektion {needed!r}.")

    # Några kända regelord som ska finnas i regelboken och/eller A6-underlag.
    rulebook_text = (root / "docs/rulebook.md").read_text(encoding="utf-8")
    for term in ("Mörker", "Nattvakt", "medtagen mat", "Fyrplatsen", "Ljuskärna"):
        if term not in rulebook_text:
            add_error(errors, f"Regelboken saknar viktigt begrepp: {term}")


def validate_release(root: Path, release: Path, errors: list[str], warnings: list[str]) -> None:
    manifest_path = release / "RELEASE_MANIFEST.json"
    if not manifest_path.exists():
        add_error(errors, f"{release.relative_to(root)} saknar RELEASE_MANIFEST.json.")
        return

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add_error(errors, f"{manifest_path.relative_to(root)} är ogiltig JSON: {exc}")
        return

    if manifest.get("release") != release.name:
        add_error(errors, f"Manifest release={manifest.get('release')!r} matchar inte katalogen {release.name!r}.")

    pdf_dir = release / "print" / "pdf"
    svg_dir = release / "print" / "svg"
    docs_dir = release / "docs"

    for d in (pdf_dir, svg_dir, docs_dir):
        if not d.exists():
            add_error(errors, f"Release-katalog saknas: {d.relative_to(root)}")

    if pdf_dir.exists():
        pdfs = {p.name for p in pdf_dir.glob("*.pdf")}
        missing = EXPECTED_PRINT_PDFS - pdfs
        extra = pdfs - EXPECTED_PRINT_PDFS
        if missing:
            add_error(errors, "Release saknar print-PDF: " + ", ".join(sorted(missing)))
        if extra:
            add_warning(warnings, "Release har extra print-PDF: " + ", ".join(sorted(extra)))

    if svg_dir.exists():
        svgs = {p.name for p in svg_dir.glob("*.svg")}
        missing = EXPECTED_PRINT_SVGS - svgs
        if missing:
            add_error(errors, "Release saknar print-SVG: " + ", ".join(sorted(missing)))

    for rel in manifest.get("print_files", {}).get("pdf", []):
        if not (release / rel).exists():
            add_error(errors, f"Manifest pekar på saknad PDF: {release.name}/{rel}")
    for rel in manifest.get("print_files", {}).get("svg", []):
        if not (release / rel).exists():
            add_error(errors, f"Manifest pekar på saknad SVG: {release.name}/{rel}")
    for rel in manifest.get("docs", []):
        if not (release / rel).exists():
            add_error(errors, f"Manifest pekar på saknat dokument: {release.name}/{rel}")

    rulebook_pdf = docs_dir / "rulebook.pdf"
    if not rulebook_pdf.exists() or rulebook_pdf.stat().st_size < 10_000:
        add_error(errors, f"Regelboks-PDF saknas eller är misstänkt liten: {rulebook_pdf.relative_to(root)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        add_error(errors, f"Projektroten finns inte: {root}")
        return 1

    for rel in REQUIRED_ROOT_PATHS:
        if not (root / rel).exists():
            add_error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    for rel in REQUIRED_WORKFLOWS:
        if not (root / rel).exists():
            add_error(errors, f"GitHub Actions workflow saknas: {rel}")

    release = latest_release(root, errors)
    if release is not None:
        print(f"Validerar senaste release: {release.relative_to(root)}")
        validate_release(root, release, errors, warnings)

    if not errors:
        validate_rulebook(root, errors)
        validate_data(root, errors, warnings)
        validate_markdown_links(root, errors)

    if warnings:
        print(f"\nValidering klar med {len(warnings)} varning(ar).")
    if errors:
        print(f"\nValidering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print("\nOK: Projektet validerar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
