# Projektstruktur

## Primära källor

- `data/` – strukturerade speldata, regler, kort, bräde och style-system
- `docs/` – aktuella mänskligt läsbara dokument
- `scripts/` – generatorer och simulator
- `assets/` – källgrafik och SVG-ikoner

## Genererade filer

- `output/` – aktuella rekommenderade genererade filer
- `release/` – samlad release-struktur för utskrift och överlämning

## Arkiv

- `docs/archive/` – äldre analyser och tidigare simuleringsspår

## Rekommenderad arbetsgång

1. Ändra källfiler i `data/`, `docs/`, `scripts/` eller `assets/`.
2. Generera nya SVG-filer med `scripts/render_styled_printables.py`.
3. Kör balanssimulering vid regel-/brädesändringar med `scripts/simulate_manual_like.py`.
4. Uppdatera `PROJECT_STATUS.md` och `CHANGELOG.md`.
5. Uppdatera `release/` när en ny utskriftsversion ska delas.


## GitHub Actions

- `.github/workflows/01-validate.yml` – validerar projekt, data, regelbok och releasefiler
- `.github/workflows/02-build-preview.yml` – bygger preview-PDF:er för print-and-play-filer
- `.github/workflows/03-release.yml` – paketerar print-and-play-release vid tagg `v*`
