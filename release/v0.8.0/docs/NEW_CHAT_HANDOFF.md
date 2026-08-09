# Fortsätt projektet i ny chat

Detta dokument är en snabb överlämning för att fortsätta arbetet med **Fyrens väktare** i en ny chat.

## Senaste rekommenderade projektversion

Använd denna zip som bas:

- `fyrens-vaktare-v0.7.7-output-cleaned.zip`

Den bygger på v0.7.5 och innehåller:

Äldre genererade outputfiler har rensats bort. Projektet behåller nu bara de aktuella rekommenderade printfilerna i `output/`.
- REGLERV4-STARTBALANS
- resursbyte på samma plats
- styled printmaterial
- aktuell manual-like simulator
- A6-kort med fetstil före kolon
- spelplan utan separat Platstyper-ruta

## Kort projektstatus

**Fyrens väktare** är ett kooperativt print-and-play familjespel för 2–4 spelare, cirka 20–30 minuter.

Spelarna ska bygga en fyr innan Mörker når 0.

Kärnloop:
1. flytta
2. utforska plats
3. bära resurser
4. byta resurser med spelare på samma plats
5. bygga på Fyrplatsen
6. hantera Nattfas och hotkort

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

Brädet är medvetet regelneutralt:
- rutor visar platstyp, färg och ikon
- A6-kortet är primär spelreferens
- ingen separat Platstyper-ruta på spelplanen

## Aktuell simulator

Använd denna som standard vid framtida balansjämförelser:

```bash
python scripts/simulate_manual_like.py --games 5000 --players 2 3 4 --food-policy save --ruin-policy situational
```

Simulatorn är en sanity-simulering av en fokuserad mänsklig grupp, inte facit.

Senaste etablerade baslinje för ungefärlig jämförelse:

```text
2p: cirka 28.8 %
3p: cirka 44.3 %
4p: cirka 54.1 %
```

Dessa siffror är vägledande, inte slutgiltiga.

## Simuleringslogik framåt

Standard:
- `food-policy save`
- `ruin-policy situational`

`situational` betyder att Ruin används när:
- spelaren är tomhänt
- Ruin ligger nära
- gruppen är tidigt ute eller ligger efter

Denna logik valdes eftersom den ligger närmare manuell simulering än tidigare Team-AI och gamla direktrutter.

## Visuell stil

Stilen är sparad i:

- `data/visual-style.yaml`
- `assets/style/tile-icons/`
- `scripts/render_styled_printables.py`
- `docs/visual-style-system-v0.7.1.md`

Vid framtida ändringar:
1. ändra källdata i `data/*.yaml`
2. behåll eller justera `data/visual-style.yaml`
3. kör `scripts/render_styled_printables.py`
4. kontrollera SVG-output

## Senaste viktiga outputfiler

Styled printmaterial:

- `output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.7.5-styled.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.7.5-styled.svg`
- `output/print/board/board-a4-REGLERV4-STARTBALANS-v0.7.2-styled.svg`
- `output/print/cards/fyndkort-a4-4x4-v0.7.3-styled.svg`
- `output/print/cards/hotkort-a4-4x4-v0.7.3-styled.svg`

## Viktiga tidigare slutsatser

### Fyrplatsens placering
Fyrplatsens placering påverkar resultatet mycket. Nuvarande r2c3 är tematiskt bra men ganska hård. Behåll den för första fysiska test. Om spelet känns för svårt kan Fyrplatsen vara en stark balansspak.

### Ruinplacering
Nuvarande Ruiner r1c3 + r4c2 är en rimlig balanspunkt. En är tillgänglig, en kräver mer avstickare. Behåll före bordstest.

### Grottplacering
Nuvarande Grottor r1c5 + r2c5 gör Ljuskärnan till en tydlig slutexpedition och är en viktig orsak till svårigheten. Om slutet känns för svårt vid bordet kan en liten lättare variant vara att flytta en Grotta närmare Fyrplatsen, men inte före första test.

## Rekommenderat nästa steg

Gör fysisk test innan fler balansändringar.

Första testmål:
- förstår spelarna målet snabbt?
- använder de A6-kortet?
- hittar de resursbyte på samma plats?
- sparar de mat till Nattvakt?
- känns Grotta som spännande risk eller som straff?
- når spelet Ljuskärnan?
- känns 4p för lätt eller lagom?

## När projektet fortsätter

Be den nya chatten att börja med:

> Läs `docs/NEW_CHAT_HANDOFF.md`, `PROJECT_STATUS.md`, `CHANGELOG.md`, `data/rules.yaml`, `data/board.yaml`, `data/cards.yaml` och `data/visual-style.yaml`. Använd `scripts/simulate_manual_like.py` med `--ruin-policy situational` som standard för balansjämförelser.

## Riktlinje

Ändra helst källfiler först:
- `data/*.yaml`
- `docs/*.md`
- `scripts/*.py`

Behandla SVG-filer i `output/` som genererade filer om det finns källa/script.
