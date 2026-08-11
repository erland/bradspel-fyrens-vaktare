#!/usr/bin/env python3
"""CI-validering för Fyrens väktare.

Validerar projektkällor och byggscript. Release- och output-kataloger krävs
inte, eftersom de genereras från källorna av scripts/build_print_and_play.py.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

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
    "scripts/render_styled_printables.py",
    "scripts/apply_ink_friendly_reference_and_board.py",
    "scripts/build_print_and_play.py",
    "scripts/ci_build_print_preview.py",
    "scripts/ci_package_release.py",
)

REQUIRED_WORKFLOWS = (
    ".github/workflows/01-validate.yml",
    ".github/workflows/02-build-preview.yml",
    ".github/workflows/03-release.yml",
)

GENERATED_DIRS = ("output", "release", "dist", "build")
LOCAL_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def add_error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)


def add_warning(warnings: list[str], message: str) -> None:
    warnings.append(message)
    print(f"WARNING: {message}", file=sys.stderr)


def read_yaml(path: Path):
    try:
        import yaml  # type: ignore
    except ImportError:
        raise RuntimeError("PyYAML saknas. Installera med: pip install pyyaml")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_markdown_links(root: Path, errors: list[str], warnings: list[str]) -> None:
    for md in sorted(root.rglob("*.md")):
        rel_parts = set(md.relative_to(root).parts)
        if rel_parts.intersection({".git", "archive", "build", "dist", "output", "release"}):
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

            if candidate.exists():
                continue

            # Dokumentation får nämna genererade release-/dist-filer utan att de
            # finns i repo. Det är inte en trasig källa.
            if target.startswith(("release/", "output/", "dist/")):
                add_warning(warnings, f"Markdown-länk pekar på genererad fil som inte finns i repo: {md.relative_to(root)} -> {target}")
                continue

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

    for term in ("Mörker", "Nattvakt", "medtagen mat", "Fyrplatsen", "Ljuskärna"):
        if term not in text:
            add_error(errors, f"Regelboken saknar viktigt begrepp: {term}")


def validate_data(root: Path, errors: list[str]) -> None:
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

    decks: dict[str, int] = {}
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


def validate_generated_dirs(root: Path, errors: list[str], warnings: list[str]) -> None:
    for dirname in GENERATED_DIRS:
        path = root / dirname
        if path.exists():
            add_warning(warnings, f"{dirname}/ finns i arbetskopian men ska inte versioneras. Den bör ligga i .gitignore.")

    gitignore = root / ".gitignore"
    if not gitignore.exists():
        add_error(errors, ".gitignore saknas.")
        return
    text = gitignore.read_text(encoding="utf-8")
    for pattern in ("output/", "release/", "dist/", "build/"):
        if pattern not in text:
            add_error(errors, f".gitignore saknar {pattern}")


def validate_build_script_smoke(root: Path, errors: list[str]) -> None:
    # Snabb syntax-/importkontroll utan att bygga PDF.
    for script in [
        "scripts/build_print_and_play.py",
        "scripts/build_rulebook_pdf.py",
        "scripts/ci_build_print_preview.py",
        "scripts/ci_package_release.py",
    ]:
        result = subprocess.run([sys.executable, "-m", "py_compile", script], cwd=root)
        if result.returncode != 0:
            add_error(errors, f"Python-syntaxfel i {script}")


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

    validate_rulebook(root, errors)
    validate_data(root, errors)
    validate_generated_dirs(root, errors, warnings)
    validate_markdown_links(root, errors, warnings)
    validate_build_script_smoke(root, errors)

    if warnings:
        print(f"\nValidering klar med {len(warnings)} varning(ar).")
    if errors:
        print(f"\nValidering misslyckades med {len(errors)} fel.", file=sys.stderr)
        return 1

    print("\nOK: Projektkällorna validerar. Release/output genereras av scripts och GitHub Actions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
