# Strukturerade regler – Fyrens väktare

`data/rules.yaml` är en strukturerad sammanfattning av REGLERV4-STARTBALANS.

Den ersätter inte regelboken, men hjälper projektet att hålla följande filer synkade:

- `docs/rulebook.md`
- `data/reference-card.yaml`
- `data/board.yaml`
- `data/cards.yaml`
- print-output i `output/`

## Innehåll

`data/rules.yaml` innehåller:

- mål och förlustvillkor
- setup per spelarantal
- turstruktur
- handlingar
- platseffekter
- Basen
- Fyren och byggkostnader
- Mörker och Nattfas
- korttiming
- viktiga synkade kort: FYN-008, FYN-012 och HOT-011

## Rekommenderad användning

När regler ändras framöver, uppdatera först:

1. `docs/rulebook.md`
2. `data/rules.yaml`
3. berörda datafiler, till exempel `data/cards.yaml` eller `data/reference-card.yaml`
4. genererad output
