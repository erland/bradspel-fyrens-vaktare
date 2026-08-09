# Valideringsanteckningar för regler

Det här är en lättviktig valideringsspecifikation för `data/rules.yaml`.

## Kontrollpunkter

- Alla handlingar i `turn.actions` ska finnas under `actions`.
- Alla platser i `actions.explore.location_effects` ska finnas i `data/board.yaml`.
- `darkness.loss_at` ska vara `0`.
- `lighthouse.parts` ska innehålla Grund, Torn och Ljuskärna.
- Ljuskärnan ska ha `triggers_win: true`.
- FYN-008, FYN-012 och HOT-011 ska matcha `data/cards.yaml`.
- Fyndkort ska vara markerade som direkt lösta när de dras.
