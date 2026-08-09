# AI-fixanalys – leverans/Grund–Torn

## Vad som ändrades

Trace visade att spelare kunde stå på Fyrplatsen med delresurser och slösa handlingar på att försöka använda Fyrplatsen utan att kunna bygga. De kunde dessutom tappa resurser till hotkort innan mängden blev komplett.

Ändringar i `scripts/simulate_team_ai_full.py`:

- Grotta kan nu väljas som stenplats när sten behövs.
- Spelare som står på Fyrplatsen med delresurs men laget fortfarande saknar resurser skickas ut för att hämta mer i stället för att slösa handlingar.
- Leveransuppdrag nollställs om spelaren redan står på Fyrplatsen och bygget inte kan göras.

## Körning efter fix

```bash
python scripts/simulate_team_ai_full.py --games 1000 --players 2 3 4 --seed 20260730 --sanity
```

Konsoloutput:

```text
VARNING: ingen full-mission-strategi vann.
VARNING: svag byggprogress i full mission.
2p mission_direct_build: win_rate=0.0, built=0.0, day=11.4
2p mission_opportunistic_ruin: win_rate=0.0, built=0.0, day=11.45
2p mission_team_planner: win_rate=0.0, built=0.0, day=11.47
3p mission_direct_build: win_rate=0.0, built=0.32, day=9.0
3p mission_opportunistic_ruin: win_rate=0.0, built=0.23, day=9.13
3p mission_team_planner: win_rate=0.0, built=0.3, day=9.05
4p mission_direct_build: win_rate=0.0, built=0.15, day=7.58
4p mission_opportunistic_ruin: win_rate=0.0, built=0.17, day=7.63
4p mission_team_planner: win_rate=0.0, built=0.15, day=7.58
Simulerade 12000 spel med full Team-AI.
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.csv
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.md
```

## Ranking efter fix

| Placering | Strategi | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `mission_delayed_crystal` | 3000 | 0.0% | 9.42 | 0.00 | 0.15 | 8.21 | 0.00 | 0.00 | 0.00 |
| 2 | `mission_direct_build` | 3000 | 0.0% | 9.35 | 0.00 | 0.14 | 8.15 | 0.00 | 0.00 | 0.00 |
| 3 | `mission_opportunistic_ruin` | 3000 | 0.0% | 9.43 | 0.00 | 0.14 | 8.20 | 0.08 | 0.00 | 0.08 |
| 4 | `mission_team_planner` | 3000 | 0.0% | 9.42 | 0.00 | 0.13 | 8.19 | 0.00 | 0.00 | 0.00 |

## Auto-trace efter fix

```bash
python scripts/auto_trace_sampler.py --seed-start 20260730 --seed-count 200
```

Konsoloutput:

```text
Sökte 2400 simuleringar.
Hittade kategorier: built_0, built_1
Skrev output/auto_traces/auto-trace-summary.md
```

# Automatisk trace-sampling

Sökta simuleringar: **2400**.

| Kategori | Spelare | Strategi | Seed | Resultat | Fyrdelar | Dag | Mörker | Hot | Fynd | Grottkristaller | Ruinbesök |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| built_0 | 2 | `mission_direct_build` | 20260730 | loss | 0 | 12 | 0 | 11 | 0 | 0 | 0 |
| built_1 | 3 | `mission_direct_build` | 20261532 | loss | 1 | 10 | 0 | 8 | 0 | 0 | 0 |
| built_2 | - | - | - | hittades inte | - | - | - | - | - | - | - |
| win | - | - | - | hittades inte | - | - | - | - | - | - | - |

## Slutsats

Fixen är tekniskt korrekt men räcker inte för att göra AI:n stark. Då behöver nästa förbättring fokusera på snabbare resursinsamling/leverans eller justera hur hotkort påverkar burna byggresurser.
