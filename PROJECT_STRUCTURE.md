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
