# Trace-analys – full Team-AI

## Körda spår

- `3p mission_direct_build seed 20260711` – return code `0`
- `4p mission_opportunistic_ruin seed 20260711` – return code `0`
- `2p mission_team_planner seed 20260712` – return code `0`
- `4p mission_direct_build seed 20260713` – return code `0`

## Sammanfattad diagnos

### Trace – 2p mission_team_planner seed 20260712

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **12**.

- AI:n byggde inte ens Grund. Kontrollera om sten samlas men inte levereras, eller om uppdrag nollställs för ofta.

### Trace – 3p mission_direct_build seed 20260711

Resultat: **loss**. Fyrdelar byggda: **1**. Slut-Mörker: **0**. Dag: **9**.

- AI:n byggde Grund men fastnade före/under Torn. Kontrollera trä/sten-fördelning och leveranser till Fyrplatsen.

### Trace – 4p mission_direct_build seed 20260713

Resultat: **loss**. Fyrdelar byggda: **1**. Slut-Mörker: **0**. Dag: **7**.

- AI:n byggde Grund men fastnade före/under Torn. Kontrollera trä/sten-fördelning och leveranser till Fyrplatsen.

### Trace – 4p mission_opportunistic_ruin seed 20260711

Resultat: **loss**. Fyrdelar byggda: **1**. Slut-Mörker: **0**. Dag: **8**.

- AI:n byggde Grund men fastnade före/under Torn. Kontrollera trä/sten-fördelning och leveranser till Fyrplatsen.

## Vad trace-verktyget visar

Det här steget lägger inte fram en slutlig balansdom. Det ger oss ett verktyg för att hitta exakt var AI:n misslyckas.

Om flera spår visar `byggt=0` är nästa AI-bugg sannolikt i Grund-fasen: sten samlas inte, levereras inte eller byggs inte.

Om flera spår visar `byggt=1` är Torn-fasen flaskhalsen: trä/sten-fördelning, leverans eller byggprioritet.

Om flera spår visar `byggt=2` är Ljuskärnan flaskhalsen: kristalltempo, Grotta-risk eller hotkort.

## Rekommenderad nästa tekniska förbättring

Lägg till automatisk trace-sampling:

- hitta ett spel som bygger 0 delar
- hitta ett spel som bygger 1 del
- hitta ett spel som bygger 2 delar
- hitta ett vinnande spel om det finns

Då kan simulatorn själv plocka representativa exempel efter en masskörning.
