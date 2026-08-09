# Release v0.8.3

Det här är en ren release-mapp för aktuell print-and-play-version.

## Skriv ut från

### PDF (rekommenderas)
- `print/pdf/board-a4.pdf`
- `print/pdf/reference-card-a6.pdf`
- `print/pdf/reference-card-a4-4up.pdf`
- `print/pdf/fyndkort-a4-4x4.pdf`
- `print/pdf/hotkort-a4-4x4.pdf`

### SVG (master/export)
- `print/svg/board-a4.svg`
- `print/svg/reference-card-a6.svg`
- `print/svg/reference-card-a4-4up.svg`
- `print/svg/fyndkort-a4-4x4.svg`
- `print/svg/hotkort-a4-4x4.svg`

## Regel- och produktionsdokument

Se `docs/` i denna release-mapp för kopior av de viktigaste spelardokumenten.

## Källor

De verkliga projektkällorna ligger fortfarande i projektroten:

- `data/`
- `docs/`
- `scripts/`
- `assets/`

Ändra inte release-filer manuellt om samma ändring kan göras i källfilerna.
Regenerera i stället output och uppdatera release-mappen.

## Kortuppdatering i v0.8.0

- Fynd- och hotkort har fått en mer ink-friendly layout.
- Dekorativa cirklar längst ned är borttagna.
- Kortytan är huvudsakligen vit för lägre tonerförbrukning.

## A6-kort och spelplan i v0.8.1

- A6-referenskortet har fått en ink-friendly styled variant med vitare bakgrund och ljusare rubrikfält.
- Spelplanen har fått en ink-friendly light-variant med vitare bakgrund och mer toner-snål layout.
- PDF-versioner för uppdaterat A6-kort, 4-up A6-ark och spelplan är regenererade.


## Regelboks-PDF

Regelboken finns som professionellt formaterad PDF:

- `docs/rulebook.pdf`

Den är genererad från `docs/rulebook.md` med Pandoc och XeLaTeX.


## Regelboksuppdatering v0.8.3

Regelboken har uppdaterats för bättre blindtestbarhet:

- ingen innehållsförteckning
- ingen kapitelnumrering
- tydligare berättelse
- tydligare begrepp för Basen, medtagen mat, Fyrplatsen och Mörker
- förtydligad Nattfas/Nattvakt
- praktisk regel för kort som påverkar “nästa” handling

Se även:

- `docs/rulebook-clarity-analysis-v0.8.3.md`
