# Regelvalidering – Fyrens väktare v0.7.0 [REGLERV4-STARTBALANS]

## Omfattning

Jag har synkat följande regelbärande källor:

- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/reference-card.md`
- `docs/recommended-balance-REGLERV4.md`
- `data/game.yaml`
- `data/rules.yaml`
- `data/buildings.yaml`
- `data/board.yaml`
- `data/reference-card.yaml`

## Kontroller

| Område | Status | Förväntat värde |
|---|---:|---|
| 2 spelare | OK | Mörker 10, 6 mat |
| 3 spelare | OK | Mörker 10, 4 mat |
| 4 spelare | OK | Mörker 10, 4 mat |
| Mörkerspår | OK | 10 till 0 |
| Grund | OK | 3 sten |
| Torn | OK | 3 trä + 2 sten |
| Ljuskärna | OK | 2 kristaller |
| Basbygge | OK | ej infört |
| Bygga | OK | på Fyrplatsen |
| Byta resurser | OK | samma plats, gratis |

## Kommentar

Äldre output och historiska simuleringsspår under `output/` kan fortfarande innehålla REGLERV3-värden. Aktuell REGLERV4-output ligger i filer med `REGLERV4-STARTBALANS` i filnamnet.
