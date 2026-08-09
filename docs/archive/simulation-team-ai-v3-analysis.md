# Team-AI v3 simuleringsanalys – Fyrens väktare v0.7.0

## Körning

```bash
python scripts/simulate_team_ai_v3.py --games 1000 --players 2 3 4 --seed 20260710 --sanity
```

Totalt: **27 000 simulerade spel**. 9 strategier × 3 spelarantal × 1 000 spel.

## Sanity output

```text
OK: minst en v3-strategi kan vinna.
OK: minst en v3-strategi gör tydlig byggprogress.
2p delayed_crystal_v3: win_rate=0.0, built=0.0, day=11.47
2p scripted_direct_build: win_rate=0.0, built=0.0, day=11.43
2p team_planner_v3: win_rate=0.0, built=0.85, day=12.07
3p delayed_crystal_v3: win_rate=0.0, built=1.0, day=8.78
3p scripted_direct_build: win_rate=0.0, built=1.0, day=8.88
3p team_planner_v3: win_rate=0.0, built=1.38, day=10.35
4p delayed_crystal_v3: win_rate=0.0, built=0.97, day=7.5
4p scripted_direct_build: win_rate=0.0, built=0.9, day=7.53
4p team_planner_v3: win_rate=0.05, built=1.7, day=9.15
Simulerade 27000 spel med team-AI v3.
Skrev output/simulations_team_ai_v3/simulation-summary-team-ai-v3.csv
Skrev output/simulations_team_ai_v3/simulation-summary-team-ai-v3.md
```

## Ranking över alla spelarantal

| Placering | Strategi | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `team_planner_v3` | 3000 | 3.0% | 10.37 | 0.07 | 1.32 | 7.62 | 11.40 | 0.23 | 11.40 |
| 2 | `opportunistic_ruin` | 3000 | 2.9% | 10.37 | 0.07 | 1.32 | 7.60 | 11.40 | 0.22 | 11.40 |
| 3 | `delayed_crystal` | 3000 | 0.0% | 9.31 | 0.00 | 0.65 | 8.18 | 0.00 | 0.00 | 0.00 |
| 4 | `delayed_crystal_v3` | 3000 | 0.0% | 9.33 | 0.00 | 0.66 | 8.20 | 0.00 | 0.00 | 0.00 |
| 5 | `scripted_direct_build` | 3000 | 0.0% | 9.33 | 0.00 | 0.65 | 8.18 | 0.00 | 0.00 | 0.00 |
| 6 | `balanced` | 3000 | 0.0% | 9.35 | 0.00 | 0.66 | 8.16 | 0.00 | 0.00 | 0.00 |
| 7 | `team_planner` | 3000 | 0.0% | 9.36 | 0.00 | 0.64 | 8.21 | 0.00 | 0.00 | 0.00 |
| 8 | `ruin_focus` | 3000 | 0.0% | 9.65 | 0.00 | 0.74 | 7.92 | 3.53 | 0.00 | 3.53 |
| 9 | `crystal_rush` | 3000 | 0.0% | 7.18 | -0.51 | 0.00 | 25.44 | 0.00 | 18.10 | 0.00 |

## Per spelarantal

| Spelare | Bäst | Vinstgrad | Sämst | Vinstgrad |
|---:|---|---:|---|---:|
| 2 | `balanced` | 0.0% | `balanced` | 0.0% |
| 3 | `team_planner_v3` | 2.2% | `balanced` | 0.0% |
| 4 | `opportunistic_ruin` | 7.4% | `balanced` | 0.0% |

## Tolkning

**Bäst i körningen:** `team_planner_v3` med cirka **3.0%** vinstgrad.

**Sämst i körningen:** `crystal_rush` med cirka **0.0%** vinstgrad.

### Scripted baseline

`scripted_direct_build` når svag progress. Då bör vi fortfarande vara försiktiga med balansslutsatser från simulatorn.

### team_planner_v3

`team_planner_v3` ligger nära scripted baseline. Den är användbar som jämförelsestrategi men inte bevisat smartare.

### delayed_crystal_v3

`delayed_crystal_v3` ligger nära `team_planner_v3`. Grotta verkar relevant men behöver inte rushas från start.

## Begränsning

Den här v3-versionen är ett pragmatiskt jämförelselager ovanpå befintlig team-AI. Den lägger till strategier och analys, men är inte ännu en full omskrivning med äkta uppdrag/amount-motor.

## Rekommendation

Använd v3-resultaten för hypoteser inför speltest. Om vi vill göra simulatorn till ett starkare balansverktyg är nästa steg en full implementation av uppdrag med målantal i själva motorn.
