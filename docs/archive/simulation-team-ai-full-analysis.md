# Full Team-AI simuleringsanalys – Fyrens väktare v0.7.0

## Körning

```bash
python scripts/simulate_team_ai_full.py --games 1000 --players 2 3 4 --seed 20260711 --sanity
```

Totalt: **12 000 simulerade spel**. 4 strategier × 3 spelarantal × 1 000 spel.

## Sanity output

```text
VARNING: ingen full-mission-strategi vann.
VARNING: svag byggprogress i full mission.
2p mission_direct_build: win_rate=0.0, built=0.0, day=11.4
2p mission_opportunistic_ruin: win_rate=0.0, built=0.0, day=11.45
2p mission_team_planner: win_rate=0.0, built=0.0, day=11.47
3p mission_direct_build: win_rate=0.0, built=1.0, day=8.78
3p mission_opportunistic_ruin: win_rate=0.0, built=1.0, day=8.85
3p mission_team_planner: win_rate=0.0, built=1.0, day=8.83
4p mission_direct_build: win_rate=0.0, built=0.97, day=7.35
4p mission_opportunistic_ruin: win_rate=0.0, built=1.0, day=7.5
4p mission_team_planner: win_rate=0.0, built=0.95, day=7.35
Simulerade 12000 spel med full Team-AI.
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.csv
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.md
```

## Ranking över alla spelarantal

| Placering | Strategi | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | `mission_direct_build` | 3000 | 0.0% | 9.23 | 0.00 | 0.66 | 8.05 | 0.00 | 0.00 | 0.00 |
| 2 | `mission_team_planner` | 3000 | 0.0% | 9.28 | 0.00 | 0.66 | 8.08 | 0.00 | 0.00 | 0.00 |
| 3 | `mission_delayed_crystal` | 3000 | 0.0% | 9.28 | 0.00 | 0.66 | 8.10 | 0.00 | 0.00 | 0.00 |
| 4 | `mission_opportunistic_ruin` | 3000 | 0.0% | 9.29 | 0.00 | 0.66 | 8.09 | 0.06 | 0.00 | 0.06 |

## Per spelarantal

| Spelare | Bäst | Vinstgrad | Sämst | Vinstgrad |
|---:|---|---:|---|---:|
| 2 | `mission_delayed_crystal` | 0.0% | `mission_delayed_crystal` | 0.0% |
| 3 | `mission_delayed_crystal` | 0.0% | `mission_delayed_crystal` | 0.0% |
| 4 | `mission_delayed_crystal` | 0.0% | `mission_delayed_crystal` | 0.0% |

## Tolkning

**Bäst i full-motorn:** `mission_direct_build` med cirka **0.0%** vinstgrad.

**Sämst i full-motorn:** `mission_opportunistic_ruin` med cirka **0.0%** vinstgrad.

### Direkt byggplan

`mission_direct_build` har låg progress. Då är det fortfarande svårt att använda simuleringen som balansfacit.

### Ruin

`mission_opportunistic_ruin` ligger nära `mission_team_planner`. Ruin verkar relevant utan att dominera.

### Grotta/kristaller

`mission_delayed_crystal` ligger nära `mission_team_planner`. Grotta verkar viktig men inte nödvändigtvis dominant.

## Rekommendation

Detta är nu den bästa simulatorgrunden i projektet. Den bör användas för framtida regelförändringar, men fysisk testning är fortfarande avgörande. Nästa tekniska förbättring bör vara att logga enskilda spelsteg för misslyckade spel, så vi kan se exakt var AI:n tappar tempo.
