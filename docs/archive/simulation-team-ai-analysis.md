# Team-AI simuleringsanalys – Fyrens väktare v0.7.0

## Körning

```bash
python scripts/simulate_team_ai.py --games 5000 --players 2 3 4 --seed 20260709 --sanity
```

Totalt: **120 000 simulerade spel**. 8 strategier × 3 spelarantal × 5 000 spel.

## Sanity output

```text
OK: minst en teamstrategi kan vinna.
VARNING: svag byggprogress även med team-AI.
2p delayed_crystal: win_rate=0.0, built=0.0, day=11.45
2p opportunistic_ruin: win_rate=0.0, built=0.81, day=12.07
2p team_planner: win_rate=0.0, built=0.0, day=11.52
3p delayed_crystal: win_rate=0.0, built=1.0, day=8.91
3p opportunistic_ruin: win_rate=0.0, built=1.42, day=10.22
3p team_planner: win_rate=0.0, built=0.99, day=8.85
4p delayed_crystal: win_rate=0.0, built=0.96, day=7.66
4p opportunistic_ruin: win_rate=0.11, built=1.71, day=8.58
4p team_planner: win_rate=0.0, built=0.9, day=7.65
Simulerade 120000 spel med team-AI simulator.
Skrev output/simulations_team_ai/simulation-summary-team-ai.csv
Skrev output/simulations_team_ai/simulation-summary-team-ai.md
```

## Ranking över alla spelarantal

| Placering | Strategi | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `opportunistic_ruin` | 15000 | 3.1% | 10.37 | 0.08 | 1.33 | 7.60 | 11.41 | 0.22 | 11.41 |
| 2 | `action_food` | 15000 | 0.0% | 9.30 | 0.00 | 0.58 | 8.10 | 0.00 | 0.00 | 0.00 |
| 3 | `delayed_crystal` | 15000 | 0.0% | 9.33 | 0.00 | 0.66 | 8.19 | 0.00 | 0.00 | 0.00 |
| 4 | `balanced` | 15000 | 0.0% | 9.34 | 0.00 | 0.67 | 8.15 | 0.00 | 0.00 | 0.00 |
| 5 | `team_planner` | 15000 | 0.0% | 9.35 | 0.00 | 0.64 | 8.20 | 0.00 | 0.00 | 0.00 |
| 6 | `ruin_focus` | 15000 | 0.0% | 9.65 | 0.00 | 0.75 | 7.94 | 3.54 | 0.00 | 3.54 |
| 7 | `safe_night` | 15000 | 0.0% | 9.72 | 0.00 | 0.00 | 8.54 | 0.00 | 0.00 | 0.00 |
| 8 | `crystal_rush` | 15000 | 0.0% | 7.17 | -0.51 | 0.00 | 25.39 | 0.00 | 18.05 | 0.00 |

## Per spelarantal

| Spelare | Bäst | Vinstgrad | Sämst | Vinstgrad |
|---:|---|---:|---|---:|
| 2 | `action_food` | 0.0% | `action_food` | 0.0% |
| 3 | `opportunistic_ruin` | 1.8% | `action_food` | 0.0% |
| 4 | `opportunistic_ruin` | 7.6% | `action_food` | 0.0% |

## Detaljtabell

| Spelare | Strategi | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | `action_food` | 0.0% | 11.39 | 0.00 | 0.00 | 10.34 | 0.00 | 0.00 | 0.00 |
| 2 | `balanced` | 0.0% | 11.52 | 0.00 | 0.00 | 10.48 | 0.00 | 0.00 | 0.00 |
| 2 | `crystal_rush` | 0.0% | 8.82 | -0.49 | 0.00 | 27.81 | 0.00 | 18.52 | 0.00 |
| 2 | `delayed_crystal` | 0.0% | 11.48 | 0.00 | 0.00 | 10.45 | 0.00 | 0.00 | 0.00 |
| 2 | `opportunistic_ruin` | 0.0% | 12.09 | 0.00 | 0.85 | 9.68 | 8.60 | 0.00 | 8.60 |
| 2 | `ruin_focus` | 0.0% | 11.61 | 0.00 | 0.25 | 10.22 | 2.27 | 0.00 | 2.27 |
| 2 | `safe_night` | 0.0% | 11.85 | 0.00 | 0.00 | 10.85 | 0.00 | 0.00 | 0.00 |
| 2 | `team_planner` | 0.0% | 11.47 | 0.00 | 0.00 | 10.44 | 0.00 | 0.00 | 0.00 |
| 3 | `opportunistic_ruin` | 1.8% | 10.18 | 0.03 | 1.48 | 7.30 | 12.09 | 0.28 | 12.09 |
| 3 | `action_food` | 0.0% | 8.95 | 0.00 | 0.84 | 7.74 | 0.00 | 0.00 | 0.00 |
| 3 | `balanced` | 0.0% | 8.94 | 0.00 | 1.00 | 7.74 | 0.00 | 0.00 | 0.00 |
| 3 | `crystal_rush` | 0.0% | 7.00 | -0.33 | 0.00 | 25.98 | 0.00 | 18.82 | 0.00 |
| 3 | `delayed_crystal` | 0.0% | 8.93 | 0.00 | 1.00 | 7.80 | 0.00 | 0.00 | 0.00 |
| 3 | `ruin_focus` | 0.0% | 9.34 | -0.00 | 0.96 | 7.59 | 3.81 | 0.00 | 3.81 |
| 3 | `safe_night` | 0.0% | 9.48 | 0.00 | 0.00 | 8.27 | 0.00 | 0.00 | 0.00 |
| 3 | `team_planner` | 0.0% | 8.95 | 0.00 | 1.00 | 7.79 | 0.00 | 0.00 | 0.00 |
| 4 | `opportunistic_ruin` | 7.6% | 8.85 | 0.20 | 1.66 | 5.81 | 13.53 | 0.38 | 13.53 |
| 4 | `action_food` | 0.0% | 7.56 | 0.00 | 0.91 | 6.22 | 0.00 | 0.00 | 0.00 |
| 4 | `balanced` | 0.0% | 7.56 | 0.00 | 1.00 | 6.24 | 0.00 | 0.00 | 0.00 |
| 4 | `crystal_rush` | 0.0% | 5.70 | -0.70 | 0.00 | 22.39 | 0.00 | 16.81 | 0.00 |
| 4 | `delayed_crystal` | 0.0% | 7.59 | 0.00 | 0.97 | 6.32 | 0.00 | 0.00 | 0.00 |
| 4 | `ruin_focus` | 0.0% | 7.99 | -0.00 | 1.04 | 6.01 | 4.54 | 0.01 | 4.54 |
| 4 | `safe_night` | 0.0% | 7.83 | 0.00 | 0.00 | 6.49 | 0.00 | 0.00 | 0.00 |
| 4 | `team_planner` | 0.0% | 7.62 | 0.00 | 0.91 | 6.36 | 0.00 | 0.00 | 0.00 |

## Tolkning

**Bäst i körningen:** `opportunistic_ruin` med cirka **3.1%** vinstgrad.

**Sämst i körningen:** `crystal_rush` med cirka **0.0%** vinstgrad.

### Grotta

`delayed_crystal` ligger nära `team_planner`, vilket tyder på att Grotta är relevant men inte behöver rushas från start.

### Ruin

`opportunistic_ruin` är starkare än `team_planner`, vilket tyder på att Ruin är mycket attraktiv även som sidospår.

Ren `ruin_focus` är sämre än opportunistisk Ruin, vilket stödjer att Ruin inte bör vara huvudmotor varje spel.

## Rekommendation inför nästa iteration

- Använd `simulate_team_ai.py` som huvudsimulator framåt.
- Behåll gamla v2 för jämförelse, men använd team-AI när du vill analysera strategier.
- Gör inga regeländringar automatiskt från simresultatet; använd det för att formulera speltestfrågor.
- Nästa fysiska test bör särskilt observera om spelare spontant spelar mer som `team_planner`, `delayed_crystal` eller `opportunistic_ruin`.
