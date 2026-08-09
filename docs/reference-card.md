# Referenskort – [REGLERV4-STARTBALANS]

**Version:** v0.7.0 – [PLAN2] Steg 1  
**Status:** Källinnehåll för A6-referenskort.

## Aktuell REGLERV4-output

Följande output hör till den rekommenderade startbalansen:

- `output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.7.0.svg`
- `output/preview/reference-card-a6-REGLERV4-STARTBALANS-v0.7.0.svg`


## Start

| Spelare | Startmat | Mörker startar på |
|---:|---:|---:|
| 2 | 6 | 10 |
| 3 | 4 | 10 |
| 4 | 4 | 10 |

Mörker räknar nedåt från 10 till 0. Vid 0 förlorar ni.

## Tur i korthet

- Fast turordning.
- Varje spelare har 2 handlingar.
- Alla spelare spelar, sedan Nattfas.
- Samma plats: byt resurser gratis.

## Handlingar

- **Flytta:** 1 steg ortogonalt.
- **Utforska:** få 1 resurs från platsen.
- **Bygga:** på Fyrplatsen, bygg nästa Fyrdel.

## Gratis på Basen

- Lämna resurser.
- Ta mat från Basförrådet.
- Lämna mat till Basförrådet.

## Stig

När du står på Stig och din nästa handling är Flytta får du flytta upp till 2 steg.

Stig ger inte extra rörelse direkt när du går in på Stig.

## Mat

- **Bärd mat:** betala 1 mat för +1 handling, max 1 gång per tur.
- **Basmat:** betala 1 mat i början av Nattfasen för Nattvakt.

## Nattfas

1. Sänk Mörker 1 steg eller betala 1 mat från Basförrådet.
2. Dra 1 hotkort.

Om Mörker når 0: förlust.

## Bygga Fyren

- **Grund:** 3 sten
- **Torn:** 3 trä + 2 sten
- **Ljuskärna:** 2 kristaller

## Platser

- **Skog:** 1 trä
- **Berg:** 1 sten
- **Äng:** 1 mat
- **Grotta:** 1 sten eller 1 kristall
- **Tar du kristall:** dra 1 hotkort
- **Ruin:** 1 fyndkort
- **Bas:** lämna resurser och ta/lämna mat
- **Fyrplats:** bygg Fyrens delar
- **Stig:** snabb rörelse från Stig


## Genererad output – [PLAN2] Steg 2

Följande A6-output har genererats från [REGLERV3]-innehållet:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0.svg`

A6-kortet är nu balansbäraren för startvärden:

| Spelare | Startmat | Mörker startar på |
|---:|---:|---:|
| 2 | 6 | 10 |
| 3 | 4 | 10 |
| 4 | 4 | 10 |

Brädet ska i nästa steg göras mer generiskt med ett rent Mörkerspår `9 8 7 6 5 4 3 2 1 0`.

## Revision efter layoutfeedback – v0.7.0 rev1

A6-kortet har grupperats om:

- Mörkerpunkten har flyttats från `Start` till `Nattfas`.
- `Vila` är borttagen från A6 och regeltexter.
- `Tur & handlingar` kopplar nu tydligare ihop 2 handlingar med 3 handlingar om mat betalas.
- Handlingarna grupperas som valbara handlingar: Flytta, Utforska och Bygga.
- `Stig` har flyttats in under `Platser`.
- En egen `Mat`-ruta har lagts till.
- `Mat och Bas` har ersatts med `Basen`, med fokus på vad som kan göras på Basen.
- Versionsmärkningen är mindre framträdande.

Ny output:

- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev1.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev1.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev1.svg`

## Revision efter Nattfas-feedback – v0.7.0 rev3

Nattfasen har kortats ned på A6-kortet till:

1. Sänk Mörker eller betala 1 mat.
2. Dra 1 hotkort.

Förlustvillkoret står separat: förlust om Mörker når 0.

## Revision efter handlingsförenkling – v0.7.0 rev4

A6-kortet och reglerna har förenklats:

- `Utforska` är borttagen som separat handling.
- Spelaren väljer nu mellan tre handlingar: `Flytta`, `Samla` och `Bygga`.
- `Samla` betyder: använd platsens effekt.
- `Ruin` ger 1 fyndkort genom Samla.
- `Grotta` är sammanslagen till: `1 sten eller 1 kristall + 1 hotkort`.
- `Stig` är formulerad som: `Flytta upp till 2 steg nästa handling`.

## Revision efter visuell kontroll – v0.7.0 rev5

A6-kortets panelhöjder har justerats efter förhandsgranskning på telefon.

Ändringar:

- minskat tomrum i `Start`, `Tur & handlingar`, `Mat`, `Basen`, `Nattfas` och `Platser`
- flyttat upp `Fyren`
- säkerställt att hela `Fyren`-rutan ryms på A6
- behållit samma regeltext som rev4

## Revision efter fördelning av tomrum – v0.7.0 rev6

A6-kortets rutor har fördelats om efter visuell kontroll.

Ändringar:

- `Start`, `Tur & handlingar` och `Mat` har fått jämnare höjder i vänsterspalten.
- `Basen`, `Nattfas`, `Platser` och `Fyren` har placerats jämnare i högerspalten.
- `Fyren` ligger inte längre lika långt ned.
- Ingen regeländring jämfört med rev5.

## Revision efter höjdminskning – v0.7.0 rev7

Alla rutor utom `Fyren` har minskats med cirka 20 procent i höjd jämfört med rev6.

Syfte:

- få upp `Fyren` tydligare på A6-kortet
- minska risken att `Fyren` hamnar utanför synlig/utskrivbar yta
- behålla samma regeltext som rev6


## Bygga på Fyrplatsen

Du får bara välja handlingen **Bygga** om du står på **Fyrplatsen**.

Bygg Fyren innan Mörker når 0 för att vinna.

## Revision efter byggplatsförtydligande – v0.7.0 rev8

A6-kortet har uppdaterats:

- `Bygga` visas som `Bygga (på Fyrplatsen)` i `Tur & handlingar`.
- `Basen` nämner inte längre byggande.
- `Fyren` har en vinstpåminnelse: bygg Fyren innan Mörker når 0.

## Revision av Fyren-rutan – v0.7.0 rev9

Fyren-rutan har uppdaterats:

- översta raden säger nu `Fyren byggs på Fyrplatsen:`
- delarna i Fyren är indenterade under den raden
- vinstpåminnelsen ligger kvar längst ned

## Revision av handlingsnamn – v0.7.0 rev10

A6-kortet och reglerna använder nu `Utforska` i stället för `Samla`.

Ändringar:

- `Samla` har bytt namn till `Utforska`.
- `Tur & handlingar` visar nu `Utforska (se plats)`.
- Den separata förklaringspunkten för `Samla` har tagits bort från A6.

## Språklig genomgång – v0.7.0 steg 2.11

Regelboken har skrivits om språkligt för att bli mer konsekvent och blindtestbar.

Viktiga förtydliganden:

- `Utforska` används konsekvent som handlingsnamn.
- `Bygga` kan bara göras på Fyrplatsen.
- Resurser i Basen kan inte användas på distans vid bygge.
- Extra handling kräver medtagen mat.
- Nattvakt och Kall natt använder mat från Basens förråd.
