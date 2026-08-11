# Fortsätt projektet i ny chat

Detta dokument är en snabb överlämning för att fortsätta arbetet med **Fyrens väktare**.

## Senaste rekommenderade projektversion

Använd denna zip som bas:

- `fyrens-vaktare-v0.8.8-repo-cleanup.zip`

## Projektstatus

**Fyrens väktare** är ett kooperativt print-and-play familjespel för 2–4 spelare, cirka 20–30 minuter.

Spelarna ska bygga en fyr innan Mörker når 0.

Aktuell struktur:
- `data/`, `docs/`, `scripts/`, `assets/`, `templates/` och `.github/` är källor.
- `output/`, `release/`, `dist/` och `build/` är genererade och ska inte versioneras.
- Print-and-play-paket byggs från källorna med `scripts/build_print_and_play.py`.

## Aktuella grundvärden

```text
2 spelare: Mörker 10, 6 mat i Basen
3 spelare: Mörker 10, 4 mat i Basen
4 spelare: Mörker 10, 4 mat i Basen

Grund: 3 sten
Torn: 3 trä + 2 sten
Ljuskärna: 2 kristaller
```

Ingen Basbygge-regel. Billigare Torn är inte standard.

## Viktiga regler

- Fast turordning.
- Varje spelare får 2 handlingar per tur.
- En gång per tur kan spelaren betala 1 medtagen mat för +1 handling.
- Mat i Basen används till Nattvakt och Kall natt.
- Medtagen mat används till extra handling.
- Resurser kan bytas gratis mellan spelare på samma plats.
- Basens förråd kan inte användas på distans för att bygga.
- Bygga sker på Fyrplatsen.
- Nattfas:
  1. Sänk Mörker 1 steg eller betala 1 mat från Basens förråd.
  2. Dra och lös 1 hotkort.

## Nuvarande spelplan

```text
Rad 1: Skog | Skog | Ruin     | Berg | Grotta
Rad 2: Bas  | Stig | Fyrplats | Stig | Grotta
Rad 3: Stig | Äng  | Stig     | Berg | Stig
Rad 4: Äng  | Ruin | Äng      | Stig | Skog
```

## Lokala byggkommandon

Validera källorna:

```bash
python scripts/ci_validate_project.py .
```

Bygg komplett print-and-play-paket:

```bash
python scripts/build_print_and_play.py --output-dir dist/print-and-play --release-name local
```

Bygg preview som Actions gör:

```bash
python scripts/ci_build_print_preview.py --output-dir dist/preview --release-name local-preview
```

Paketera release-assets lokalt:

```bash
python scripts/ci_package_release.py --output-dir dist/release --release-name vX.Y.Z
```

## GitHub Actions

- `.github/workflows/01-validate.yml`
- `.github/workflows/02-build-preview.yml`
- `.github/workflows/03-release.yml`

Preview och release bygger från källorna, inte från incheckade PDF/SVG-filer i `release/`.

## Viktiga filer

- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/production-guide.md`
- `docs/release-policy.md`
- `data/rules.yaml`
- `data/board.yaml`
- `data/cards.yaml`
- `data/reference-card.yaml`
- `data/visual-style.yaml`
- `data/ink-friendly-style.yaml`
- `scripts/render_styled_printables.py`
- `scripts/apply_ink_friendly_reference_and_board.py`
- `scripts/build_rulebook_pdf.py`
- `scripts/build_print_and_play.py`
- `scripts/ci_validate_project.py`
- `scripts/ci_build_print_preview.py`
- `scripts/ci_package_release.py`
