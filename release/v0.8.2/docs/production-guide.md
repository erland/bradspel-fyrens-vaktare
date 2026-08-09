# Produktionsguide v0.1

## Produktionsmål

Detta är en enkel testversion, inte en färdig grafisk produkt.

## Rekommenderad utskrift

- Papper: vanligt A4
- Färg: svartvitt eller låg färg
- Kort: 4 × 4 per A4
- Kortbaksidor: nej
- Laminering: frivilligt, men inte nödvändigt för första testet

## Kort

Fyndkort och hotkort bör skrivas ut som små prototypkort.

Layoutbeslut:

- 16 kort per A4
- ca 45 × 65 mm per kort beroende på marginaler
- ingen illustration
- tydlig rubrik
- effekttext ca 7.5–8 pt om printark genereras

## Resurser

För v0.1 kan resurser vara:

- papperslappar
- kuber
- pärlor
- mynt
- markörer från annat spel

## Testutskrift

Innan hela spelet skrivs ut:

1. Skriv ut en testsida med kort.
2. Kontrollera att texten är läsbar på bordet.
3. Kontrollera att korten är enkla att klippa.
4. Justera layout innan slututskrift.

## Kortark v0.3

Första printarket för korten använder:

- A4 stående
- 4 × 4 kort per ark
- cirka 45 × 65 mm per kort
- 2 ark totalt:
  - 1 ark för fyndkort
  - 1 ark för hotkort

### Rekommenderad testutskrift

1. Skriv ut ett kortark i skala 100 %.
2. Kontrollera att texten känns läsbar i hand.
3. Klipp ut 2–3 kort och testa att hålla dem under spel.
4. Om texten känns för liten kan vi senare byta till 3 × 3-layout.

## Reviderad kortlayout v0.3.1

Den första 4×4-layouten hade för liten text och för mycket luft på korten.

I v0.3.1 har kortarken ritats om med:

- större rubriker
- större effekttext
- tätare intern layout

### Viktigt test

Skriv gärna ut **ett enda ark** först och kontrollera:

- känns texten läsbar i handen?
- känns korten fortfarande för små?
- vill vi hålla fast vid 4×4, eller byta till 3×3?

## Kortlayout v0.3.2

Efter visuell feedback har kortarken ritats om igen.

Den viktigaste förändringen är att layouten nu är **innehållsstyrd**:

- kort med kort text får större text
- kort med längre text skalas ned så att allt får plats
- headern tar mindre plats än tidigare

### Rekommenderat test

Skriv ut ett fyndark och ett hotark i 100 % skala och kontrollera:

- läsbarhet i handen
- om någon korttext fortfarande känns för liten
- om 4×4-formatet nu känns rimligt

## Kortlayout v0.4 styled

v0.4 lägger till en mer professionell, men fortfarande tonersnål, SVG-layout.

### Egenskaper

- 4 × 4 kort per A4
- ljusa bakgrunder för hemmaskrivare
- diskreta SVG-mönster i stället för tunga bitmapbilder
- Fynd och Hot har olika stilprofiler
- effekttext är topjusterad i ett tydligt textfält
- outputen genereras från data och mall

### Testutskrift

Skriv ut ett ark i 100 % skala och kontrollera:

1. Läsbarhet
2. Tonerförbrukning
3. Om mönstren stör texten
4. Om skärlinjer/ramar är tydliga

## Kortlayout v0.4.1 styled

v0.4.1 är en proportionell förbättring av v0.4.

### Förbättring
- högre huvud/rubrikfält
- bättre vertikal spacing i titelområdet
- samma 4×4-format och samma stilprofil

### Rekommenderad kontroll
- känns rubriken tydligare och mindre hoptryckt?
- ligger titeln lagom långt från separationslinjen?
- ser långa och korta titlar jämnt balanserade ut?

## A6-referenskort v0.5

Projektet har nu ett första referenskort.

### Filer
- `output/print/reference/reference-card-a6-v0.5.svg`
- `output/print/reference/reference-card-a4-4up-v0.5.svg`

### Rekommenderad användning
- använd **A6-filen** om du vill skriva ut ett enskilt kort
- använd **A4 4-up-filen** om flera spelare ska få eget referenskort

### Kontrollera vid testutskrift
1. att texten är läsbar på armlängds avstånd
2. att de viktigaste reglerna räcker för att spela utan regelboken
3. att kortet inte känns överlastat

## A6-referenskort v0.5.1

v0.5.1 är en proportionell omritning av referenskortet.

### Förbättringar
- mindre rubriker
- mindre brödtext
- bättre balans mellan paneler och textinnehåll
- fortsatt A6 liggande + A4 4-up

### Kontrollera vid test
1. att all text är läsbar
2. att panelerna känns tydliga
3. att kortet faktiskt fungerar som snabbreferens

## A6-referenskort v0.5.2 (stående)

v0.5.2 är ett formatprov där referenskortet byter från liggande till stående A6.

### Filer
- `output/print/reference/reference-card-a6-portrait-v0.5.2.svg`
- `output/print/reference/reference-card-a4-4up-portrait-v0.5.2.svg`

### Kontrollera vid granskning/test
1. att all text håller sig inom panelerna
2. att punktlistor blir lättare att följa
3. att stående format känns bättre vid spelbordet

## A6-referenskort v0.5.3 (stående, två spalter)

v0.5.3 är ett formatprov mellan liggande och enspaltigt stående.

### Kontrollera vid granskning
1. håller sig texten inom panelerna?
2. känns tvåspaltslayouten lättare att skanna?
3. känns detta bättre än v0.5.2 enspalt?

## A6-referenskort v0.5.4 (stående, två spalter)

v0.5.4 förbättrar tvåspaltsversionen genom att låta texten använda nästan hela panelbredden.

### Kontrollera vid granskning
1. att högra delen av varje panel inte längre känns tom
2. att texten ryms inom panelerna
3. att panelhöjderna känns balanserade
4. att textstorleken är tillräcklig för fysisk utskrift

## A6-referenskort v0.5.5 (stående, två spalter)

v0.5.5 är en proportionell finjustering av tvåspaltsversionen.

### Kontrollera vid granskning
1. om huvudfältet nu känns bättre balanserat
2. om `Tur i korthet` känns lagom högt
3. om `Handlingar` fortfarande rymmer texten trots lägre ruta
4. om textblocket känns lugnare när det inte går lika nära kanterna

## A6-referenskort v0.5.6 (stående, två spalter)

v0.5.6 skalar upp innehållet något och använder mer av kortets höjd.

### Kontrollera vid granskning
1. om textstorleken nu känns bättre
2. om fet stil före kolon hjälper läsbarheten
3. om panelerna rymmer texten trots större typografi
4. om bottenytan nu används bättre

## A6-referenskort v0.5.7 (stående, två spalter)

v0.5.7 försöker balansera alla rutor utifrån innehållets verkliga mängd text.

### Kontrollera vid granskning
1. om `Platser & resurser` känns bättre med kolon i stället för likhetstecken
2. om bottenluften ser jämnare ut mellan rutorna
3. om radavstånd och punktavstånd känns lugnare
4. om panelerna fortfarande rymmer texten väl

## Spelbräde v0.6.0 (styled A4)

Brädet har nu en styled SVG-version som matchar kort och referenskort.

### Kontrollera vid granskning
1. läsbarhet på armlängds avstånd
2. om tile-texter är tillräckligt stora
3. om mörkerspåret är lätt att använda
4. om färgerna fungerar i vanlig hemmaskrivare

## Spelbräde v0.6.1 (styled flat A4)

v0.6.1 är en förenklad board-variant med högre kompatibilitet i SVG-läsare.

### Kontrollera vid granskning
1. att brädet inte längre skiftar till svart i din läsare
2. att den smalare högerspalten räcker
3. att A6-kortet kompenserar för borttagen legend och byggpanel
4. att brickstorleken känns bättre

## Spelbräde v0.6.2 (styled flat A4)

v0.6.2 är den renaste board-varianten hittills.

### Kontrollera vid granskning
1. att endast mörkerspåret i högerspalten känns tillräckligt
2. att den större spelplanen är tydligare
3. att brädet återges stabilt i din SVG-läsare


## Uppdatering v0.6.3 – Stigregel

Brädet och A6-referenskortet har uppdaterats så att Stig nu fungerar som snabb rörelse.

Vid testutskrift, kontrollera att:
1. Stig-rutorna tydligt visar `Från Stig: +1 steg`
2. A6-referenskortet visar Stigregeln i `Platser & resurser`

## [PLAN2] Steg 2 – A6-referenskort

Skriv ut ett nytt A6-referenskort för [REGLERV3]:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0.svg`

För fyra referenskort på ett A4-ark:

- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0.svg`

A6-kortet innehåller startvärden för antal spelare. Om startvärden justeras senare ska A6-kortet skrivas ut på nytt, medan brädet kan vara oförändrat.

## Uppdaterat A6-kort – v0.7.0 rev1

Efter layoutfeedback används följande A6-kort för [REGLERV3]:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev1.svg`

A4-ark med fyra exemplar:

- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev1.svg`

## Uppdaterat A6-kort – v0.7.0 rev3

Använd främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev3.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev3.svg`

## Uppdaterat A6-kort – v0.7.0 rev4

Använd främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev4.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev4.svg`

## Uppdaterat A6-kort – v0.7.0 rev5

Efter visuell kontroll används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev5.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev5.svg`

## Uppdaterat A6-kort – v0.7.0 rev6

Efter omfördelning av tomrum används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev6.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev6.svg`

## Uppdaterat A6-kort – v0.7.0 rev7

Efter höjdminskning används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev7.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev7.svg`

## Uppdaterat A6-kort – v0.7.0 rev8

Efter byggplatsförtydligande används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev8.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev8.svg`

## Uppdaterat A6-kort – v0.7.0 rev9

Efter justering av Fyren-rutan används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev9.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev9.svg`

## Uppdaterat A6-kort – v0.7.0 rev10

Efter namnbyte till `Utforska` används främst:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev10.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev10.svg`

## PLAN2 Steg 3 – Bräde

Det uppdaterade brädet finns här:

- `output/print/board/board-a4-REGLERV3-v0.7.0.svg`
- `output/preview/board-a4-REGLERV3-v0.7.0.svg`

### Utskrift

- Skriv ut i liggande A4.
- Använd faktisk storlek / 100 % om möjligt.
- Testa först i låg kvalitet.
- Brädet är en flat SVG utan filter eller drop shadow.
- Mörkerspåret är generiskt 9–0. Startvärden finns på A6-kortet.

## PLAN2 Steg 3.1 – Bräde

Det uppdaterade brädet finns här:

- `output/print/board/board-a4-REGLERV3-v0.7.0-rev2.svg`
- `output/preview/board-a4-REGLERV3-v0.7.0-rev2.svg`

### Utskrift

- Skriv ut i liggande A4.
- Använd faktisk storlek / 100 % om möjligt.
- Testa först i låg kvalitet.
- Brädet är en flat SVG utan filter eller drop shadow.
- Mörkerspåret är vertikalt längst till höger.
- A6-kortet används för regler och platseffekter.

## PLAN2 Steg 4 – Playtestpaket

För första speltestet används:

- `docs/rulebook.md`
- `docs/first-playtest-checklist.md`
- `docs/playtest-guide.md`
- `docs/playtest-log.md`
- `output/print/board/board-a4-REGLERV3-v0.7.0-rev2.svg`
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev12.svg`

### Rekommendation

Skriv ut brädet och A6-kortet först. Kontrollera att Mörkerspåret, rutnamnen och A6-texten är läsbara innan kort och övriga komponenter skrivs ut.

## Kortsynkade testark

Efter kortsynkning används följande textbaserade kortark för speltest:

- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync.svg`

Skriv ut dessa om äldre kortark fortfarande nämner `Samla`, `Vila` eller äldre Mörkerformuleringar.


## Kortsynkning rev1 – FYN-008

`FYN-008 Starka verktyg` har ändrats till:

```text
Få 1 valfri resurs utom kristall.
```

Nya kortark:

- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync-1.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync-1.svg`

## Strukturerade regler

Reglerna finns även i `data/rules.yaml`. Detta påverkar inte utskrift direkt, men hjälper till att hålla print-output synkad.

## Simulering

Simuleringsskriptet påverkar inte utskrift, men kan användas inför regeländringar:

- `scripts/simulate_strategies.py`
- `docs/simulation-guide.md`
