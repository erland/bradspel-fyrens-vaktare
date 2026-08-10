# Regelboksanalys – v0.8.3

Syftet med den här genomgången var att göra regelboken lättare att läsa för en ny spelare, stärka spelets berättelse och minska risken för missförstånd vid blindtest.

## Bedömning före ändring

Regeltexten var i grunden spelbar och relativt tydlig, men några saker kunde störa en ny spelare:

- kapitelnumreringen gjorde dokumentet mer tekniskt än nödvändigt
- innehållsförteckningen i PDF:en var överflödig för en kort regelbok
- berättelsen var bra men kunde tydligare kopplas till spelhandlingarna
- begreppen Basen, medtagen mat, Fyrplatsen och Mörker behövde förklaras tidigt
- Nattfas/Nattvakt kunde läsas som två separata saker innan de definierades
- kort som påverkar “nästa” handling behövde en praktisk hanteringsregel
- utskriftsavsnittet pekade på gamla output-filer

## Ändringar gjorda i v0.8.3

- Tog bort numrering i rubriker.
- Tog bort innehållsförteckning i PDF-exporten.
- Förstärkte berättelsen så Skog, Berg, Äng, Grotta, Fyren och Mörker hänger ihop tematiskt.
- Lade till avsnittet **Viktiga begrepp** tidigt i regelboken.
- Skrev om Nattfasen så valet om Nattvakt blir tydligare.
- Förtydligade att mat till Nattvakt och Kall natt är separata kostnader.
- Förtydligade att fynd-/hotkort med “nästa gång” ligger synliga tills effekten används.
- Lade till exempel för Nattvakt + Kall natt.
- Uppdaterade första speltestets observationspunkter.
- Uppdaterade utskriftsavsnittet till aktuell release.

## Konsistenskontroll

Regeltexten använder nu mer konsekvent:

- **Mörker** som spelets tidsgräns
- **Basen** som plats/förråd
- **mat i Basen** för Nattvakt och hotkort
- **medtagen mat** för extra handling
- **Fyrplatsen** som enda plats där Fyren byggs
- **Nattfas** som rundans slutsteg
- **Nattvakt** som valet att betala mat för att inte sänka Mörker

## Kvar att validera i speltest

Följande behöver fortfarande kontrolleras vid fysiskt test:

- om nya spelare förstår skillnaden mellan mat i Basen och medtagen mat
- om spelare spontant använder resursbyte på samma plats
- om Nattvakt/Kall natt känns tydligt när båda sker samma natt
- om Grotta känns som ett meningsfullt riskval
- om A6-kortet räcker som bordshjälp efter första rundan

## Slutsats

Regelboken bör nu vara mer blindtestbar än tidigare. Den är fortfarande kort nog för print-and-play, men har tydligare begrepp, starkare berättelse och färre tolkningsglapp.


## Tillägg v0.8.4

Regelboken rensades från arbets- och produktionsspråk.

Ändringar:
- tog bort formuleringen “första spelbara prototypen”
- ersatte den med “Spelet innehåller”
- behöll print-and-play-exempel för resursmarkörer, men utan att kalla spelet prototyp
- tog bort avsnitten **Första speltest** och **Utskrift** från spelarregelboken
- flyttade implicit test-/utskriftsansvar till projektets separata dokument:
  - `production-guide.md`
  - `first-playtest-checklist.md`
  - `playtest-guide.md`
  - `release/v0.8.4/README.md`

Bedömning:
- Regelboken känns mer som en färdig spelregelbok.
- Spelaren slipper information som inte behövs under spel.
- Projektet behåller fortfarande test- och utskriftsinformation i rätt dokument.


## Tillägg v0.8.5

Regelboken rensades ytterligare från intern versionsinformation.

Ändringar:
- tog bort den synliga versionsraden i början av regelboken
- tog bort release-/versionsvisning från PDF-titelsidan
- förenklade PDF-subtiteln till endast “Regelbok”

Bedömning:
- Regelboken känns mer som en spelarkomponent än ett projektdokument.
- Versionshantering finns fortfarande kvar i projektets README, CHANGELOG, PROJECT_STATUS och release-manifest.
