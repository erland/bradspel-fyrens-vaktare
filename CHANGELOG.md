# CHANGELOG

## v0.7.0 – resursbyte på samma plats

### Tillagt
- Spelare på samma plats får fritt ge resurser till varandra.
- Regeln kostar ingen handling.
- A6-referenskortet har fått korttexten: `Samma plats: byt resurser gratis.`

### Uppdaterat
- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/reference-card.md`
- `data/rules.yaml`
- `data/game.yaml`
- `data/reference-card.yaml`
- REGLERV4 A6-output

## v0.7.0 – REGLERV4-STARTBALANS

### Ändrat
- Start-Mörker är nu 10 för 2, 3 och 4 spelare.
- Startmat är nu 6/4/4 för 2/3/4 spelare.
- Ljuskärnan kostar nu 2 kristaller.
- Mörkerspåret i källan är nu 10 till 0.
- Regelbok, snabbstart, referenskortkälla, strukturerade regler och byggdata är synkade.

### Inte ändrat
- Torn kostar fortsatt 3 trä + 2 sten.
- Basbygge är inte infört som standard.

### Tillagt
- `docs/recommended-balance-REGLERV4.md`
- Ny REGLERV4 A6-/A4-referensoutput.
- Ny REGLERV4 brädesoutput med Mörkerspår 10 till 0.

## v0.7.0 – scripted 2p direct route

### Tillagt
- `scripts/simulate_scripted_2p_direct_route.py`
- `docs/scripted-2p-direct-route-analysis.md`
- `output/scripted_2p_direct_route/`
- `output/scripted_2p_direct_route_food/`

### Syfte
- Sanity-checka 2p-boost med hårdkodad mänsklig minimiplan.
- Skilja regelproblem från Team-AI-planeringsproblem.

## v0.7.0 – trace-diagnos för Team-AI 2p-boost

### Tillagt
- `scripts/trace_team_ai_full_2p_boost.py`
- `docs/team-ai-2p-boost-trace-diagnosis.md`
- `output/traces_2p_boost/`

### Resultat
- Full-Team-AI bygger fortfarande 0 Fyrdelar med 2p-boost.
- Problemet ligger i AI-/uppdragslogiken före Grund, inte i Ljuskärnans balans.

## v0.7.0 – Team-AI 2p-boosttest

### Tillagt
- `scripts/simulate_team_ai_full_2p_boost.py`
- `docs/team-ai-2p-boost-test-analysis.md`

### Testad regelvariant
- 2 spelare: Mörker 10
- 2 spelare: 6 mat i Basen
- 2 spelare: Ljuskärna 2 kristaller

## v0.7.0 – AI leveransfix

### Ändrat
- Uppdaterade `scripts/simulate_team_ai_full.py`.
- Grotta kan användas som stenplats när sten behövs.
- Spelare som står på Fyrplatsen med delresurser skickas ut för att hämta mer om bygget inte kan göras.
- Obsoleta leveransuppdrag nollställs tydligare.

### Tillagt
- `docs/ai-delivery-fix-analysis.md`

## v0.7.0 – automatisk trace-sampling

### Tillagt
- `scripts/auto_trace_sampler.py`
- `docs/auto-trace-sampler-guide.md`
- `docs/auto-trace-analysis.md`
- `output/auto_traces/`

### Syfte
- Hitta representativa simulerade spel automatiskt.
- Skapa trace för 0, 1 och 2 byggda Fyrdelar samt vinst om möjligt.

## v0.7.0 – trace-loggning för full Team-AI

### Tillagt
- `scripts/trace_team_ai_full.py`
- `docs/simulation-trace-guide.md`
- `docs/simulation-trace-analysis.md`
- `output/traces/`

### Syfte
- Logga enskilda simulerade spel steg för steg.
- Se var AI:n tappar tempo.
- Identifiera om flaskhalsen ligger i Grund, Torn eller Ljuskärna.

## v0.7.0 – full Team-AI

### Tillagt
- `scripts/simulate_team_ai_full.py`
- `docs/simulation-team-ai-full-guide.md`
- `docs/simulation-team-ai-full-analysis.md`
- `data/simulation-team-ai-full-strategies.yaml`
- `output/simulations_team_ai_full/`

### Förbättrat
- Full uppdragsmotor med målantal.
- Reserverade resurser.
- Fasbaserad byggplan.
- Hård byggprioritet.
- Smartare matanvändning.
- Ny analys med 12 000 simulerade spel.

## v0.7.0 – team-AI v3

### Tillagt
- `scripts/simulate_team_ai_v3.py`
- `docs/simulation-team-ai-v3-guide.md`
- `docs/simulation-team-ai-v3-analysis.md`
- `data/simulation-team-ai-v3-strategies.yaml`
- `output/simulations_team_ai_v3/`

### Förbättrat
- Lade till `team_planner_v3`.
- Lade till `scripted_direct_build`.
- Lade till `delayed_crystal_v3`.
- Lade till ny analys med 27 000 simulerade spel.

## v0.7.0 – team-AI simulator

### Tillagt
- `scripts/simulate_team_ai.py`
- `docs/simulation-team-ai-guide.md`
- `docs/simulation-team-ai-analysis.md`
- `data/simulation-team-ai-strategies.yaml`
- `output/simulations_team_ai/simulation-results-team-ai.csv`
- `output/simulations_team_ai/simulation-summary-team-ai.csv`
- `output/simulations_team_ai/simulation-summary-team-ai.md`
- `output/simulations_team_ai/simulation-analysis-team-ai-120000.md`
- `output/simulations_team_ai/simulation-strategy-ranking-team-ai.csv`

### Förbättrat
- Lade till kooperativa strategier: `team_planner`, `delayed_crystal`, `opportunistic_ruin`.
- Lade till mått för Grottkristaller och Ruinbesök.
- Gjorde ny strategianalys med 120 000 simulerade spel.

## v0.7.0 – simulator v2

### Tillagt
- `scripts/simulate_strategies_v2.py`
- `docs/simulation-guide-v2.md`
- `docs/simulation-v2-run-analysis.md`
- `output/simulations_v2/`

### Förbättrat
- Fyrplats-logik
- Lagbaserad behovsanalys
- Kortleksmodell med draghög/slänghög
- Sanity tests

## v0.7.0 – simuleringsskript

### Tillagt
- `scripts/simulate_strategies.py`
- `docs/simulation-guide.md`
- `data/simulation-strategies.yaml`
- `docs/simulation-run-example.md`
- `output/simulations/simulation-results.csv`
- `output/simulations/simulation-summary.csv`
- `output/simulations/simulation-summary.md`

### Syfte
- Göra det möjligt att simulera flera strategier efter regeländringar.
- Få jämförbar data om vinstgrad, tempo och Mörker.
- Stödja balansarbete före och efter fysiska speltester.

## v0.7.0 – regelvalidering mot A6 och regelbok

### Tillagt
- `docs/rules-sync-validation.md`

### Ändrat
- Lade till output-referenser i `data/rules.yaml`.
- Lade till `Kall natt` som separat specialregel i `data/rules.yaml`.
- Lade till `game_title` i `data/reference-card.yaml`.

### Resultat
- `data/rules.yaml`, `docs/rulebook.md` och `data/reference-card.yaml` är synkade på centrala regler.

## v0.7.0 – strukturerade regler

### Tillagt
- `data/rules.yaml`
- `docs/structured-rules.md`
- `schemas/rules.validation-notes.md`

### Syfte
- Samla REGLERV3 i strukturerad form.
- Minska risken att regelbok, A6, bräde och kort glider isär.
- Förbereda framtida validering.

## v0.7.0 – kortsynkning rev1 – FYN-008 direkt effekt

### Ändrat
- Ändrade `FYN-008 Starka verktyg` till: `Få 1 valfri resurs utom kristall.`
- Förtydligade i regelboken att fyndkort löses direkt när de dras.
- Uppdaterade `data/cards.yaml`, `docs/card-list.md` och `docs/card-sync-notes.md`.

### Tillagt
- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync-1.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync-1.svg`

## v0.7.0 – kortsynkning efter REGLERV3

### Tillagt
- `docs/card-sync-notes.md`
- `docs/card-output-generation-note.md`
- `output/print/cards/fyndkort-a4-3x4-v0.7.0-cardsync.svg`
- `output/print/cards/hotkort-a4-3x4-v0.7.0-cardsync.svg`

### Ändrat
- Synkade `data/cards.yaml` med `Utforska`, borttagen `Vila` och nedräknande Mörker.
- Uppdaterade `docs/card-list.md`.
- Ändrade `FYN-008 Starka verktyg`.
- Ändrade `FYN-012 Morgonljus`.
- Ändrade `HOT-011 Oroligt läger`.
- Uppdaterade produktionsguide, projektstatus och README.

## v0.7.0 – [PLAN2] Steg 4 – playtestpaket

### Tillagt
- `docs/playtest-log.md`
- `docs/playtest-package.md`
- `docs/first-playtest-checklist.md`

### Ändrat
- Uppdaterade `docs/playtest-guide.md` för REGLERV3.
- Uppdaterade `docs/production-guide.md` med första speltestpaketet.
- Uppdaterade `README.md` och `PROJECT_STATUS.md` med testinstruktioner.

### Testfokus
- Kontrollera att `Utforska (se plats)` fungerar.
- Kontrollera att `Bygga (på Fyrplatsen)` är tydligt.
- Kontrollera att brädet fungerar utan tryckta platseffekter.
- Kontrollera att A6-kortet räcker som referens.
- Kontrollera svårighetsgrad via Mörker och mat.

## v0.7.0 – [PLAN2] Steg 3.1 – bräde justerat

### Tillagt
- `output/print/board/board-a4-REGLERV3-v0.7.0-rev2.svg`
- `output/preview/board-a4-REGLERV3-v0.7.0-rev2.svg`

### Ändrat
- Tog bort rutan `Kort påminnelse` från brädet.
- Flyttade Mörkerspåret till vertikalt läge längst till höger.
- Ändrade platsrutorna så att de bara visar typ av ruta, inte vad rutan gör.
- Uppdaterade `data/board.yaml` och `docs/board-notes.md` efter den nya principen.

## v0.7.0 – [PLAN2] Steg 3 – bräde

### Tillagt
- `data/board.yaml`
- `docs/board-notes.md`
- `output/print/board/board-a4-REGLERV3-v0.7.0.svg`
- `output/preview/board-a4-REGLERV3-v0.7.0.svg`

### Ändrat
- Uppdaterade brädet till **Fyrens väktare**.
- Lade in generiskt Mörkerspår `9 8 7 6 5 4 3 2 1 0`.
- Tog bort spelarantal/startvärden från brädet.
- Synkade brädtext med `Utforska` och `Bygga (på Fyrplatsen)`.
- Brädet är flat SVG utan filter/drop shadow.

## v0.7.0 – [PLAN2] Steg 2.12 – namnbyte och berättelseram

### Ändrat
- Bytte titel från `Kubriket: Fyrens väktare` till **Fyrens väktare** i källor och output.
- Lade till en tydligare berättelseram i `docs/rulebook.md`.
- Behöll `Mörker`, `Mörkerspår` och `Mörkermarkör` som tydliga speltermer.
- Förtydligade i regelboken att Mörker representerar skuggorna/natten som närmar sig fyren.

## v0.7.0 – [PLAN2] Steg 2.11 – språklig regelboksgenomgång

### Ändrat
- Skrev om `docs/rulebook.md` språkligt för bättre läsbarhet.
- Gjorde terminologin konsekvent efter bytet från `Samla` till `Utforska`.
- Förtydligade att `Bygga` bara kan göras på Fyrplatsen.
- Förtydligade att resurser måste bäras till Fyrplatsen för att användas vid bygge.
- Förtydligade skillnaden mellan medtagen mat och mat i Basen.
- Lade till tydligare exempel och FAQ.

## v0.7.0 – [PLAN2] Steg 2.10 – Samla byter namn till Utforska

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev10.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev10.svg`
- `output/preview/reference/reference-card-a6-REGLERV3-v0.7.0-rev10.svg`

### Ändrat
- Bytte namn på handlingen `Samla` till `Utforska`.
- `Tur & handlingar` visar nu `Utforska (se plats)`.
- Tog bort den separata förklaringspunkten för handlingen på A6.
- Uppdaterade regelbok och referensmaterial till samma terminologi.

## v0.7.0 – [PLAN2] Steg 2.9 – omstrukturerad Fyren-ruta

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev9.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev9.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev9.svg`

### Ändrat
- I `Fyren` står nu `Fyren byggs på Fyrplatsen:`.
- Fyrens tre delar är indenterade under den raden.
- Vinstpåminnelsen ligger kvar längst ned i rutan.

## v0.7.0 – [PLAN2] Steg 2.8 – Bygga på Fyrplatsen

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev8.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev8.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev8.svg`

### Ändrat
- `Tur & handlingar`: `Bygga` skrivs nu som `Bygga (på Fyrplatsen)`.
- `Basen`: tog bort byggformulering.
- `Fyren`: lade till vinstpåminnelse om att bygga Fyren innan Mörker når 0.
- Reglerna förtydligar att Bygga bara är tillgängligt på Fyrplatsen.

## v0.7.0 – [PLAN2] Steg 2.7 – A6-rutor minskade

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev7.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev7.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev7.svg`

### Ändrat
- Minskade alla rutor utom `Fyren` med cirka 20 procent i höjd.
- Behöll `Fyren` i samma höjd.
- Ingen regeländring jämfört med rev6.

## v0.7.0 – [PLAN2] Steg 2.6 – A6-tomrum omfördelat

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev6.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev6.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev6.svg`

### Ändrat
- Fördelade om tomrum mellan rutorna på A6-kortet.
- Flyttade upp `Fyren` genom jämnare höjder i högerspalten.
- Ingen regeländring jämfört med rev5.

## v0.7.0 – [PLAN2] Steg 2.5 – A6-layout justerad

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev5.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev5.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev5.svg`

### Ändrat
- Justerade vertikala panelhöjder på A6-kortet.
- Minskade tomrum i flera rutor.
- Flyttade upp `Fyren` så att hela rutan ryms.
- Ingen regeländring jämfört med rev4.

## v0.7.0 – [PLAN2] Steg 2.4 – tre handlingar och tydligare platsregler

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev4.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev4.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev4.svg`

### Ändrat
- Tog bort `Utforska` som separat handling.
- Spelaren väljer nu mellan tre handlingar: `Flytta`, `Samla` och `Bygga`.
- `Samla` betyder: använd platsens effekt.
- `Ruin` ger 1 fyndkort via Samla.
- `Grotta` slogs ihop till: `1 sten eller 1 kristall + 1 hotkort`.
- `Stig` förtydligades till: `Flytta upp till 2 steg nästa handling`.

## v0.7.0 – [PLAN2] Steg 2.3 – kortare Nattfas på A6

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev3.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev3.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev3.svg`

### Ändrat
- Nattfasen på A6-kortet kortades ned till:
  1. Sänk Mörker eller betala 1 mat.
  2. Dra 1 hotkort.
- Förlustvillkoret står separat: Mörker 0 = förlust.

## v0.7.0 – [PLAN2] Steg 2.2 – A6 förtydligande

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev2.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev2.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev2.svg`

### Ändrat
- `Tur & handlingar`: visar nu `2 handlingar (3 om 1 medtagen mat används)`.
- `Utforska` förklaras tydligare som handlingen på Ruin som drar 1 fyndkort.
- `Mat` använder nu punkterna `Medtagen mat`, `Mat i basen` och `Kall natt`.
- Terminologin `bärd mat` har ersatts med `medtagen mat`.

## v0.7.0 – [PLAN2] Steg 2.1 – reviderat A6-kort

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0-rev1.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0-rev1.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0-rev1.svg`

### Uppdaterat
- `docs/reference-card.md`
- `docs/production-guide.md`
- `data/reference-card.yaml`
- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/kubriket-regler-REGLERV3.md`
- `data/game.yaml`
- `data/board.yaml`
- `PROJECT_STATUS.md`
- `CHANGELOG.md`

### Ändrat
- Tog bort `Vila` som handling.
- Flyttade Mörkerförklaringen från Start till Nattfas på A6.
- Flyttade Stig till Platser.
- Lade till egen Mat-ruta.
- Renodlade Basen-rutan.
- Gjorde versionsmärkningen mindre framträdande.

## v0.7.0 – [PLAN2] Steg 2 – A6-referenskort för [REGLERV3]

### Tillagt
- `output/print/reference/reference-card-a6-REGLERV3-v0.7.0.svg`
- `output/print/reference/reference-card-a4-4up-REGLERV3-v0.7.0.svg`
- `output/preview/reference-card-a6-REGLERV3-v0.7.0.svg`

### Uppdaterat
- `docs/reference-card.md`
- `docs/production-guide.md`
- `data/reference-card.yaml`
- `PROJECT_STATUS.md`
- `CHANGELOG.md`

### Kommentar
A6-kortet är nu balansbäraren för startmat och Mörkers startposition per spelarantal. Brädet ska i nästa steg göras generiskt med Mörkerspår 9–0.

## v0.7.0 – [PLAN2] Steg 1 – [REGLERV3] regler och data

### Uppdaterat
- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/reference-card.md`
- `data/game.yaml`
- `data/board.yaml`
- `data/reference-card.yaml`
- `PROJECT_STATUS.md`
- `CHANGELOG.md`

### Ändrat
- Införde [REGLERV3] som arbetsregler i projektets källfiler.
- Mörkerspåret räknar nu nedåt från 9 till 0.
- Startposition för Mörker anges per spelarantal:
  - 2 spelare: Mörker 9, 4 startmat
  - 3 spelare: Mörker 8, 2 startmat
  - 4 spelare: Mörker 7, 1 startmat
- Förtydligade fast turordning.
- Förtydligade Stig: bonus gäller bara när Flytta-handlingen börjar på Stig.
- Förtydligade mat:
  - bärd mat ger +1 handling, max 1 gång per tur
  - Basmat kan användas till Nattvakt
- Förtydligade Nattfas:
  - Nattvakt kan stoppa Mörkers vanliga steg
  - hotkort löses fortfarande
  - Mörker 0 innebär förlust

### Återstår
- Steg 2: generera nytt A6-referenskort.
- Steg 3: generera nytt bräde med generiskt 9–0-spår.
- Steg 4: skapa playtestpaket och slutlig zip.

## v0.6.3 – 2026-07-07

### Tillagt
- `output/preview/board-a4-v0.6.3-styled-flat.svg`
- `output/print/board/board-a4-v0.6.3-styled-flat.svg`
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.8.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.8.svg`

### Uppdaterat
- `data/board.yaml`
- `data/reference-card.yaml`
- `docs/rulebook.md`
- `docs/quickstart.md`
- `docs/board-notes.md`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`

### Kommentar
Stig har fått en tydlig spelmekanisk roll: när du flyttar från en Stig får du flytta 1 extra steg. Detta gör Stig till en tempo-ruta i stället för en tom neutral ruta.

## v0.6.2 – 2026-07-07

### Tillagt
- `output/preview/board-a4-v0.6.2-styled-flat.svg`
- `output/print/board/board-a4-v0.6.2-styled-flat.svg`

### Uppdaterat
- `data/board.yaml`
- `docs/board-notes.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `README.md`
- `templates/board/board-a4-styled.svg`

### Kommentar
v0.6.2 tar bort rutan `Se A6-kortet` och låter högerspalten innehålla enbart mörkerspåret. Det ger ett renare spelbräde och lite mer plats åt spelplanen.

## v0.6.1 – 2026-07-07

### Tillagt
- `output/preview/board-a4-v0.6.1-styled-flat.svg`
- `output/print/board/board-a4-v0.6.1-styled-flat.svg`

### Uppdaterat
- `data/board.yaml`
- `docs/board-notes.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `README.md`
- `templates/board/board-a4-styled.svg`

### Kommentar
v0.6.1 förenklar brädet genom att ta bort `Bygga Fyren` och `Snabblegend` från högerspalten, göra spelplanen större och använda en mer kompatibel flat SVG utan filter.

## v0.6.0 – 2026-07-07

### Tillagt
- `output/preview/board-a4-v0.6.0-styled.svg`
- `output/print/board/board-a4-v0.6.0-styled.svg`
- `templates/board/board-a4-styled.svg`

### Uppdaterat
- `data/board.yaml`
- `docs/board-notes.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `README.md`

### Kommentar
Första styled versionen av A4-spelbrädet. Brädet använder nu samma visuella familj som kort och A6-referenskort, med rundade paneler, varm bakgrund, tydligare högerspalt och biomefärger.

## v0.5.7 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.7.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.7.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.7 byter till kolon i `Platser & resurser`, använder fet prefixtext där också, och justerar panelhöjderna utifrån uppskattad texthöjd så att bottenluften blir jämnare mellan rutorna.

## v0.5.6 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.6.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.6.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.6 använder en del av den tidigare tomma nederdelen för att skala upp texten och panelhöjderna. Punktlistor med kolon har även fått fet prefixtext före kolon.

## v0.5.5 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.5.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.5.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.5 finjusterar tvåspaltsversionen med högre huvud, omfördelad panelhöjd och något smalare textkolumn för lugnare textblock.

## v0.5.4 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.4.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.4.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.4 förbättrar tvåspaltsversionen genom att låta texten använda mer av panelbredden och genom att ge mer höjd till paneler som tidigare inte rymde texten.

## v0.5.3 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-2col-v0.5.3.svg`
- `output/print/reference/reference-card-a4-4up-portrait-2col-v0.5.3.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.3 testar stående A6 med två spalter som en kompromiss mellan liggande format och stående enspaltig layout.

## v0.5.2 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-portrait-v0.5.2.svg`
- `output/print/reference/reference-card-a4-4up-portrait-v0.5.2.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `templates/reference/reference-card-a6-styled.svg`

### Kommentar
v0.5.2 testar stående A6 som alternativ till liggande A6. Syftet är att ge punktlistor och sektioner mer vertikalt utrymme.

## v0.5.1 – 2026-07-07

### Tillagt
- `output/print/reference/reference-card-a6-v0.5.1.svg`
- `output/print/reference/reference-card-a4-4up-v0.5.1.svg`

### Uppdaterat
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`

### Kommentar
Referenskortet ritades om efter visuell feedback. v0.5 hade för stora rubriker och för stor text för A6-formatet. v0.5.1 använder mer realistiska proportioner.

## v0.5 – 2026-07-07

### Tillagt
- `data/reference-card.yaml`
- `docs/reference-card.md`
- `templates/reference/reference-card-a6-styled.svg`
- `output/print/reference/reference-card-a6-v0.5.svg`
- `output/print/reference/reference-card-a4-4up-v0.5.svg`

### Uppdaterat
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `scripts/generate_card_sheets_svg.py`

### Kommentar
Projektet har nu ett första A6-referenskort samt ett praktiskt A4-ark med fyra kopior för speltest.

## v0.4.1 – 2026-07-07

### Tillagt
- `output/print/cards/fyndkort-a4-4x4-v0.4.1-styled.svg`
- `output/print/cards/hotkort-a4-4x4-v0.4.1-styled.svg`

### Uppdaterat
- `docs/card-style-notes.md`
- `docs/card-print-sheets.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`
- `scripts/generate_card_sheets_svg.py`

### Kommentar
Rubrikfältet i v0.4 fick konkret visuell feedback. v0.4.1 ökar den vertikala höjden i rubrikområdet för att ge kortnamnen bättre luft och proportioner.

## v0.4 – 2026-07-07

### Tillagt
- `output/print/cards/fyndkort-a4-4x4-v0.4-styled.svg`
- `output/print/cards/hotkort-a4-4x4-v0.4-styled.svg`
- `data/card-styles.yaml`
- `templates/cards/card-sheet-4x4-styled.svg`
- `scripts/generate_card_sheets_svg.py`
- `docs/card-style-notes.md`

### Uppdaterat
- `docs/card-print-sheets.md`
- `docs/production-guide.md`
- `PROJECT_STATUS.md`

### Kommentar
v0.4 introducerar en snyggare men fortfarande print-and-play-vänlig SVG-layout med diskreta mönster, stilvariabler och separata visuella profiler för Fynd och Hot.

## v0.3.2 – 2026-07-07

### Tillagt
- `output/print/cards/fyndkort-a4-4x4-v0.3.2-adaptive.svg`
- `output/print/cards/hotkort-a4-4x4-v0.3.2-adaptive.svg`

### Uppdaterat
- `docs/card-print-sheets.md` med adaptiv layoutbeskrivning
- `docs/production-guide.md` med avsnitt om v0.3.2
- `PROJECT_STATUS.md` till v0.3.2

### Kommentar
Kortarken har ritats om efter konkret visuell feedback. Fokus i denna version är att använda kortytan mycket bättre och låta textstorleken anpassas efter textmängd.

## v0.3.1 – 2026-07-07

### Tillagt
- `output/print/cards/fyndkort-a4-4x4-v0.3.1-tight.svg`
- `output/print/cards/hotkort-a4-4x4-v0.3.1-tight.svg`

### Uppdaterat
- `docs/card-print-sheets.md` med reviderad layoutbeskrivning
- `docs/production-guide.md` med notering om v0.3.1
- `PROJECT_STATUS.md` till v0.3.1

### Kommentar
Kortlayouten har gjorts tätare eftersom den första versionen hade för liten text och för mycket tomrum.

## v0.3 – 2026-07-07

### Tillagt
- `output/print/cards/fyndkort-a4-4x4-v0.3.svg`
- `output/print/cards/hotkort-a4-4x4-v0.3.svg`
- `docs/card-print-sheets.md`
- uppdaterad `data/cards.yaml`
- uppdaterad `data/print-layouts.yaml`

### Uppdaterat
- `docs/production-guide.md` med avsnitt om kortark v0.3
- `PROJECT_STATUS.md` till v0.3

### Kommentar
Första utskriftsklara prototyparken för korten är nu skapade som SVG. Varje A4-ark innehåller 12 spelkort och 4 reservkort.

## v0.2 – 2026-07-07

### Tillagt
- `data/board.yaml` med första enkla A4-spelbrädet
- `docs/board-notes.md` med motiv, designmål och testfokus
- `output/preview/board-a4-v0.2.svg` som enkel förhandsvisning
- `output/board/board-a4-v0.2.txt` med textöversikt av rutnätet

### Uppdaterat
- `README.md` med hänvisning till nya brädfiler
- `PROJECT_STATUS.md` till version v0.2

### Kommentar
Detta är första funktionella spelbrädet och ska behandlas som prototypmaterial för speltest.

## v0.1 – 2026-07-07

### Tillagt
- initial projektstruktur
- regelutkast
- komponentlista
- kortlista
- speldata för kärnkomponenter


## v0.7.1 – Styled refresh

- Lade till gemensamt visuellt system i `data/visual-style.yaml`.
- Lade till separata SVG-ikoner för platstyper i `assets/style/tile-icons/`.
- Lade till scriptet `scripts/render_styled_printables.py` för återanvändbar renderering.
- Genererade nya styled-versioner av:
  - A6-referenskort
  - A4 4-up referenskort
  - spelplan
  - fyndkort A4 4x4
  - hotkort A4 4x4
- Dokumenterade stilen i `docs/visual-style-system-v0.7.1.md`.


## v0.7.2 – Spelplan utan platstyp-ruta

- Tog bort rutan **Platstyper** från den styled spelplanen.
- Behöll spelplanens rutor med ikon + namn för varje platstyp.
- Uppdaterade styled spelplansoutput så att A6-kortet är primär regelsammanfattning.


## v0.7.3 – Kortheader-justering

- Ökade avståndet mellan kort-ID och kortnamn på styled fynd-/hotkort.
- Justerade kortheadern så att ID ligger högre och namnet får tydligare luft.


## v0.7.4 – A6 layoutjustering

- Minskade höjden på rubrikfälten i A6-rutorna.
- Minskat radavståndet något i rutornas brödtext för bättre rymd.
- Justerade startposition för brödtexten så innehållet får mer plats i varje ruta.


## v0.7.5 – A6 typografi och Fyren-indrag

- Gjorde text före första kolon fetstil i A6-referenskortets punktlistor.
- Behöll vinstpunkten i rutan Fyren utan indrag.
- Regenererade styled A6- och A4-4up-versionerna av referenskortet.

## v0.7.6 – New chat handoff

- Lade till `docs/NEW_CHAT_HANDOFF.md`.
- Lade till `PROJECT_HANDOFF.json`.
- Dokumenterade aktuell balans, simulatorstandard, visuellt system och rekommenderade nästa steg för fortsatt arbete i ny chat.

## v0.7.7 – Output cleanup

- Tog bort äldre genererade filer från `output/`.
- Behöll endast aktuell spelplan, aktuella styled kort och aktuellt styled A6-referenskort.
- Uppdaterade `output/README.md` för att dokumentera vilka outputfiler som är aktuella.

## v0.7.8 – Docs archive and release structure

- Flyttade äldre dokument till `docs/archive/`.
- Lade till dokumentindex i `docs/README.md`.
- Lade till arkivindex i `docs/archive/README.md`.
- Skapade `release/v0.8.5/` med aktuella printfiler och centrala dokument.
- Lade till `PROJECT_STRUCTURE.md`.

## v0.7.9 – PDF release output

- Genererade PDF-versioner av spelplan, referenskort och kortark.
- Delade upp `release/v0.8.5/print/` i `svg/` och `pdf/`.
- Uppdaterade `release/v0.8.5/README.md` och `RELEASE_MANIFEST.json`.


## v0.8.0 – Ink-friendly cards

- Tog bort dekorativa cirklar längst ned på fynd- och hotkort.
- Gjorde kortens huvudyta vitare för lägre tonerförbrukning.
- Regenererade releasefiler för kortark i både SVG och PDF.

## v0.8.1 – Ink-friendly reference and board

- Lade till `data/ink-friendly-style.yaml` för att dokumentera toner-snål stil.
- Lade till `scripts/apply_ink_friendly_reference_and_board.py` för att återapplicera stilen.
- Uppdaterade A6-referenskort till en vitare ink-friendly styled variant.
- Uppdaterade spelplan till en vitare ink-friendly light-variant.
- Regenererade releasefiler i både SVG och PDF för A6, A6 4-up och spelplan.

## v0.8.2 – rulebook PDF

- Genererade `release/v0.8.5/docs/rulebook.pdf` med Pandoc/XeLaTeX.
- Uppdaterade `docs/rulebook.md` med aktuell print/release-information.
- Lade till `scripts/build_rulebook_pdf.py`.
- Uppdaterade release-manifest och README.

## v0.8.3 – rulebook clarity pass

- Tog bort TOC och kapitelnumrering från regelboks-PDF.
- Uppdaterade regelboken för bättre nybörjarförståelse och blindtestbarhet.
- Lade till tydligare berättelse och centrala begrepp.
- Förtydligade Nattfas/Nattvakt och kort som påverkar “nästa” handling.
- Lade till regelboksanalys i `docs/rulebook-clarity-analysis-v0.8.3.md`.

## v0.8.4 – rulebook cleanup

- Tog bort prototypformuleringar från spelarregelboken.
- Tog bort första speltest och utskrift från spelarregelboken.
- Regenererade regelboks-PDF utan TOC och kapitelnumrering.
- Uppdaterade release README och manifest.

## v0.8.5 – rulebook no visible version

- Tog bort synlig versionsrad i början av regelboken.
- Förenklade regelboks-PDF:ens titelsida så den inte visar release-/versionsrad.
- Regenererade regelboks-PDF.
