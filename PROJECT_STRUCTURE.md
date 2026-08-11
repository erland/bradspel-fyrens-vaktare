# Projektstruktur

## Primära källor som ska versioneras

- `data/` – strukturerade speldata, regler, kort, bräde och style-system
- `docs/` – aktuella mänskligt läsbara dokument
- `scripts/` – generatorer, validering och byggscript
- `assets/` – källgrafik och SVG-ikoner
- `templates/` – layoutmallar och framtida mallkällor
- `.github/` – GitHub Actions för validering, preview och release

## Genererade kataloger som inte ska versioneras

- `output/`
- `release/`
- `dist/`
- `build/`

De ska kunna raderas utan informationsförlust och skapas vid behov av lokala script eller GitHub Actions.

## Arkiv

- `docs/archive/` – äldre analyser och tidigare simuleringsspår

## Rekommenderad arbetsgång

1. Ändra källfiler i `data/`, `docs/`, `scripts/`, `templates/` eller `assets/`.
2. Kör validering:
   ```bash
   python scripts/ci_validate_project.py .
   ```
3. Bygg lokal preview:
   ```bash
   python scripts/ci_build_print_preview.py --output-dir dist/preview --release-name local-preview
   ```
4. Paketera lokal release vid behov:
   ```bash
   python scripts/ci_package_release.py --output-dir dist/release --release-name vX.Y.Z
   ```
5. För riktig GitHub Release: skapa och pusha en tagg `v*`.

## GitHub Actions

- `.github/workflows/01-validate.yml` – validerar projektkällor och byggscript
- `.github/workflows/02-build-preview.yml` – bygger preview-PDF:er från källorna
- `.github/workflows/03-release.yml` – paketerar print-and-play-release vid tagg `v*`

## Viktig princip

`release/` och `output/` är inte längre projektkällor. Allt printmaterial byggs från `data/`, `docs/`, `scripts/`, `assets/` och `templates/`.
