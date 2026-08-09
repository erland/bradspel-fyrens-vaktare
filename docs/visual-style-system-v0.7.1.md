# Visuellt system – styled refresh v0.7.1

Det här dokumentet beskriver den gemensamma stilen för **A6-kort**, **spelplan** och **kortark**.

## Syfte

Målet är att kunna göra framtida regeländringar utan att behöva uppfinna den visuella stilen på nytt.
Därför är stilen nu sparad i tre lager:

1. **`data/visual-style.yaml`**  
   Samlad källa för färgpalett, komponentstil och platstyper.

2. **`assets/style/tile-icons/*.svg`**  
   Separata SVG-ikoner för varje platstyp:
   - Skog
   - Berg
   - Äng
   - Grotta
   - Ruin
   - Stig
   - Bas
   - Fyrplats

3. **`scripts/render_styled_printables.py`**  
   Renderar styled-versioner av:
   - A6-referenskort
   - A4 4-up referenskort
   - spelplan
   - fyndkort 4x4
   - hotkort 4x4

## Designprinciper

- **Gemensam färgvärld**: varm prototypkänsla med lätt pergamentbakgrund.
- **Tydlig hierarki**: mörka rubrikfält, ljusa innehållsytor, konsekventa panelramar.
- **Regeloberoende spelplan**: spelplanen visar främst platstyp + ikon, medan detaljregler ligger på A6-kortet.
- **Ikonstöd per ruta**: varje platstyp har en egen liten SVG-ikon så skillnaden inte bara sitter i texten.
- **Kort i 4x4**: senaste styled-varianten för kortarken är nu anpassad till 4x4-layout.

## Genererade filer

Scriptet skriver ut följande styled-filer:

- `output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.7.1-styled.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.7.1-styled.svg`
- `output/print/board/board-a4-REGLERV4-STARTBALANS-v0.7.1-styled.svg`
- `output/preview/board-a4-REGLERV4-STARTBALANS-v0.7.1-styled.svg`
- `output/print/cards/fyndkort-a4-4x4-v0.7.1-styled.svg`
- `output/print/cards/hotkort-a4-4x4-v0.7.1-styled.svg`

## Användning framåt

Om ni ändrar regler, korttext eller spelplansdata:

1. uppdatera innehållet i `data/*.yaml`
2. behåll eller justera `data/visual-style.yaml`
3. kör `scripts/render_styled_printables.py`

På så sätt kan samma stil återanvändas utan att manuellt göra om layouten varje gång.


## Justering v0.7.2

- Platstyper-rutan togs bort från spelplanen för att undvika redundant referensinformation.
- Spelplanen förlitar sig nu helt på rutornas ikon + namn, medan reglerna ligger på A6-kortet.


## v0.8.0 – Ink-friendly kortvariant

Aktuell rekommenderad kortstil för fynd- och hotkort är justerad för hemmautskrift:

- dekorativa cirklar längst ned på korten är borttagna
- större del av kortytan är vit
- färg är koncentrerad till rubrikfält, ram och små accenter
- effektpanelen är mycket ljus för bättre läsbarhet och lägre tonerförbrukning

### Praktisk princip

- **SVG** är fortsatt master/output-format
- **PDF** används som rekommenderat utskriftsformat
- styled-korten ska vara visuellt tydliga men fortfarande relativt tonersnåla

### Nuvarande kortprofil

- fyndkort: varm, ljus och ink-friendly
- hotkort: stram, tydlig och ink-friendly



## Ink-friendly expansion v0.8.1

Den toner-snålare varianten bygger på samma visuella språk som den styled versionen,
men flyttar större delen av färgvikten från stora bakgrundsytor till:

- rubrikfält
- ramar
- ikoner
- små färgaccenter

Principer:
- vit eller nästan vit huvudbakgrund
- ljusare sektions- och tile-bakgrunder
- mörk text på ljus yta
- färgkodning bevaras, men i lättare vikt

Se även:
- `data/ink-friendly-style.yaml`
- `scripts/apply_ink_friendly_reference_and_board.py`
