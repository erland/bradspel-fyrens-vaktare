# Kortark v0.4.1 – styled SVG

## Syfte

v0.4.1 förbättrar v0.4 genom att ge kortens huvud/rubrik mer vertikalt utrymme.

## Teknisk modell

```text
data/cards.yaml
data/card-styles.yaml
scripts/generate_card_sheets_svg.py
        ↓
output/print/cards/*-v0.4.1-styled.svg
```

## Vad som ändrats

- högre rubrikfält
- bättre vertikal balans i kortets övre del
- kortnamn får mer luft
- effektfältet börjar lite längre ned

## Varför

Skärmdumpsfeedback visade att titelfältet kändes för hoptryckt i v0.4.  
v0.4.1 behåller samma stil men förbättrar proportionerna.

## v0.7.0 – Kortsynkade textark

Följande textbaserade speltestark är skapade efter REGLERV3-synkning:

- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync.svg`

Dessa är enkla 3×4-ark för speltest. De ersätter inte framtida slutlig kortlayout.


## Kortsynkning rev1 – FYN-008

`FYN-008 Starka verktyg` har ändrats till:

```text
Få 1 valfri resurs utom kristall.
```

Nya kortark:

- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync-1.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync-1.svg`
