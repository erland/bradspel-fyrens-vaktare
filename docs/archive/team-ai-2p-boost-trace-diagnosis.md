# Trace-diagnos – Team-AI 2p-boost

Testar varför senaste full-Team-AI inte bygger Grund trots 2p-boost:

- 2 spelare
- Mörker 10
- 6 mat i Basen
- Ljuskärna 2 kristaller

## Körda traces

- `mission_direct_build` seed `20260801` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14
- `mission_team_planner` seed `20260801` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14
- `mission_delayed_crystal` seed `20260801` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14
- `mission_opportunistic_ruin` seed `20260801` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14
- `mission_direct_build` seed `20260802` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14
- `mission_direct_build` seed `20260803` – rc `0` – Resultat: loss, byggt=0, Mörker=0, dag=14

## Kort diagnos

Alla representativa spår slutar med **0 byggda Fyrdelar**. Det bekräftar att felet ligger före balansfrågan om Ljuskärnan: AI:n får inte ens till Grund.

Det mest sannolika felet i full-Team-AI är uppdragslogiken för 2p: spelarna tilldelas inte en stabil sekvens där de samlar 3 sten, levererar till Fyrplatsen och använder en Bygga-handling. I praktiken tappar den sitt Grund-uppdrag eller omdirigeras innan byggkravet uppfylls.

## Relevanta spår

### trace-boost-2p-mission_delayed_crystal-seed20260801.md

# Trace – 2p-boost 2p mission_delayed_crystal seed 20260801

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_delayed_crystal, seed=20260801
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +2; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:6
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:6->mat:6
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); blocked move toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=5, night; darkness 7->5; hot +1; base mat:6->mat:6
- Dag 5 DAY_START: byggt=0, Mörker=5, 
- Dag 5 TURN_START P1: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

### trace-boost-2p-mission_direct_build-seed20260801.md

# Trace – 2p-boost 2p mission_direct_build seed 20260801

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_direct_build, seed=20260801
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +2; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:6
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:6->mat:6
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); blocked move toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=5, night; darkness 7->5; hot +1; base mat:6->mat:6
- Dag 5 DAY_START: byggt=0, Mörker=5, 
- Dag 5 TURN_START P1: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

### trace-boost-2p-mission_direct_build-seed20260802.md

# Trace – 2p-boost 2p mission_direct_build seed 20260802

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_direct_build, seed=20260802
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +1; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:5
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:5->mat:5
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=6, night; darkness 7->6; hot +1; base mat:5->mat:5
- Dag 5 DAY_START: byggt=0, Mörker=6, 
- Dag 5 TURN_START P1: byggt=0, Mörker=6, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); blocked move toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=6, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

### trace-boost-2p-mission_direct_build-seed20260803.md

# Trace – 2p-boost 2p mission_direct_build seed 20260803

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_direct_build, seed=20260803
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +1; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); blocked move toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:6
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:6->mat:6
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=6, night; darkness 7->6; hot +1; base mat:6->mat:6
- Dag 5 DAY_START: byggt=0, Mörker=6, 
- Dag 5 TURN_START P1: byggt=0, Mörker=6, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=6, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=6, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

### trace-boost-2p-mission_opportunistic_ruin-seed20260801.md

# Trace – 2p-boost 2p mission_opportunistic_ruin seed 20260801

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_opportunistic_ruin, seed=20260801
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +2; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:6
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:6->mat:6
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); blocked move toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=5, night; darkness 7->5; hot +1; base mat:6->mat:6
- Dag 5 DAY_START: byggt=0, Mörker=5, 
- Dag 5 TURN_START P1: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

### trace-boost-2p-mission_team_planner-seed20260801.md

# Trace – 2p-boost 2p mission_team_planner seed 20260801

Resultat: **loss**. Fyrdelar byggda: **0**. Slut-Mörker: **0**. Dag: **14**.

## Händelser

- Dag 1 START: byggt=0, Mörker=10, strategy=mission_team_planner, seed=20260801
- Dag 1 DAY_START: byggt=0, Mörker=10, 
- Dag 1 TURN_START P1: byggt=0, Mörker=10, assigned=COLLECT sten x2 @(0, 3)
- Dag 1 ACTION P1 A1: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P1 A2: byggt=0, Mörker=10, COLLECT sten x2 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 TURN_START P2: byggt=0, Mörker=10, assigned=COLLECT sten x1 @(0, 3)
- Dag 1 ACTION P2 A1: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Bas->Skog toward (0, 3)
- Dag 1 ACTION P2 A2: byggt=0, Mörker=10, COLLECT sten x1 @(0, 3); move Skog->Skog toward (0, 3)
- Dag 1 NIGHT: byggt=0, Mörker=9, night; darkness 10->9; hot +2; base mat:6->mat:6
- Dag 2 DAY_START: byggt=0, Mörker=9, 
- Dag 2 TURN_START P1: byggt=0, Mörker=9, assigned=COLLECT sten x2 @(0, 3)
- Dag 2 ACTION P1 A1: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P1 A2: byggt=0, Mörker=9, COLLECT sten x2 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 TURN_START P2: byggt=0, Mörker=9, assigned=COLLECT sten x1 @(0, 3)
- Dag 2 ACTION P2 A1: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Skog->Ruin toward (0, 3)
- Dag 2 ACTION P2 A2: byggt=0, Mörker=9, COLLECT sten x1 @(0, 3); move Ruin->Berg toward (0, 3)
- Dag 2 NIGHT: byggt=0, Mörker=8, night; darkness 9->8; hot +1; base mat:6->mat:6
- Dag 3 DAY_START: byggt=0, Mörker=8, 
- Dag 3 TURN_START P1: byggt=0, Mörker=8, assigned=COLLECT sten x2 @(0, 3)
- Dag 3 ACTION P1 A1: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); explore/use Berg
- Dag 3 ACTION P1 A2: byggt=0, Mörker=8, COLLECT sten x2 @(0, 3); move Berg->Stig toward (1, 2)
- Dag 3 TURN_START P2: byggt=0, Mörker=8, assigned=COLLECT sten x1 @(0, 3)
- Dag 3 ACTION P2 A1: byggt=0, Mörker=8, COLLECT sten x1 @(0, 3); explore/use Berg -> switch to deliver
- Dag 3 ACTION P2 A2: byggt=0, Mörker=8, DELIVER sten x1 @(1, 2); move Berg->Stig toward (1, 2)
- Dag 3 NIGHT: byggt=0, Mörker=7, night; darkness 8->7; hot +1; base mat:6->mat:6
- Dag 4 DAY_START: byggt=0, Mörker=7, 
- Dag 4 TURN_START P1: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P1 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); blocked move toward (1, 2)
- Dag 4 ACTION P1 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 TURN_START P2: byggt=0, Mörker=7, assigned=DELIVER sten x1 @(1, 2)
- Dag 4 ACTION P2 A1: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Stig->Fyrplats toward (1, 2)
- Dag 4 ACTION P2 A2: byggt=0, Mörker=7, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 4 NIGHT: byggt=0, Mörker=5, night; darkness 7->5; hot +1; base mat:6->mat:6
- Dag 5 DAY_START: byggt=0, Mörker=5, 
- Dag 5 TURN_START P1: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P1 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)
- Dag 5 ACTION P1 A2: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Fyrplats->Ruin toward (0, 3)
- Dag 5 TURN_START P2: byggt=0, Mörker=5, assigned=DELIVER sten x1 @(1, 2)
- Dag 5 ACTION P2 A1: byggt=0, Mörker=5, DELIVER sten x1 @(1, 2); move Ruin->Fyrplats toward (1, 2)

## Slutsats

2p-boost-regeln är inte problemet här. Den manuella simuleringen visade att regeln kan ge spelbarhet, medan full-Team-AI misslyckas redan vid Grund. Nästa tekniska fix bör därför vara en särskild `scripted_2p_direct_route` i Team-AI-scriptet, som hårdkodar en enkel mänsklig plan:

1. båda spelare går till Berg,
2. samla totalt 3 sten,
3. båda går till Fyrplatsen,
4. bygg Grund,
5. en går trä, en går sten,
6. bygg Torn,
7. båda går Grotta för 2 kristaller.

Den skulle fungera som sanity-check. Om den vinner ungefär som den manuella simuleringen är Team-AI-planeraren svag. Om den också förlorar är regler/hot fortfarande för hårda.
