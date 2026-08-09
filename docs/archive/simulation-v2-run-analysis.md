# Simuleringsanalys v2 – Fyrens väktare v0.7.0

Körning: `python scripts/simulate_strategies_v2.py --games 5000 --players 2 3 4 --seed 20260708 --sanity`

Totalt: **75 000 simulerade spel**.

## Sanity output

```text
VARNING: ingen strategi vann.
VARNING: svag byggprogress.
Simulerade 75000 spel med simulator v2.
Skrev output/simulations_v2/simulation-summary-v2.csv
Skrev output/simulations_v2/simulation-summary-v2.md
```

## Ranking över alla spelarantal

| Placering | Strategi | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hotkort | Fyndkort |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | `action_food` | 15000 | 0.0% | 9.39 | 0.00 | 0.03 | 8.15 | 0.00 |
| 2 | `balanced` | 15000 | 0.0% | 9.48 | 0.00 | 0.12 | 8.28 | 0.00 |
| 3 | `ruin_focus` | 15000 | 0.0% | 9.72 | 0.00 | 0.27 | 8.01 | 3.59 |
| 4 | `safe_night` | 15000 | 0.0% | 9.73 | 0.00 | 0.00 | 8.54 | 0.00 |
| 5 | `crystal_rush` | 15000 | 0.0% | 9.07 | -0.06 | 0.02 | 9.93 | 0.00 |

## Per spelarantal

| Spelare | Bäst | Vinstgrad | Sämst | Vinstgrad |
|---:|---|---:|---|---:|
| 2 | `action_food` | 0.0% | `action_food` | 0.0% |
| 3 | `action_food` | 0.0% | `action_food` | 0.0% |
| 4 | `action_food` | 0.0% | `action_food` | 0.0% |

## Detaljer

| Spelare | Strategi | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hotkort | Fyndkort |
|---:|---|---:|---:|---:|---:|---:|---:|
| 2 | `action_food` | 0.0% | 11.41 | 0.00 | 0.00 | 10.35 | 0.00 |
| 2 | `balanced` | 0.0% | 11.51 | 0.00 | 0.00 | 10.49 | 0.00 |
| 2 | `crystal_rush` | 0.0% | 11.06 | -0.04 | 0.00 | 12.10 | 0.00 |
| 2 | `ruin_focus` | 0.0% | 11.69 | 0.00 | 0.14 | 10.24 | 2.84 |
| 2 | `safe_night` | 0.0% | 11.85 | 0.00 | 0.00 | 10.86 | 0.00 |
| 3 | `action_food` | 0.0% | 9.08 | 0.00 | 0.04 | 7.83 | 0.00 |
| 3 | `balanced` | 0.0% | 9.20 | 0.00 | 0.16 | 7.98 | 0.00 |
| 3 | `crystal_rush` | 0.0% | 8.73 | -0.06 | 0.03 | 9.56 | 0.00 |
| 3 | `ruin_focus` | 0.0% | 9.44 | 0.00 | 0.30 | 7.68 | 3.66 |
| 3 | `safe_night` | 0.0% | 9.49 | 0.00 | 0.00 | 8.27 | 0.00 |
| 4 | `action_food` | 0.0% | 7.67 | 0.00 | 0.05 | 6.26 | 0.00 |
| 4 | `balanced` | 0.0% | 7.74 | 0.00 | 0.20 | 6.37 | 0.00 |
| 4 | `crystal_rush` | 0.0% | 7.43 | -0.07 | 0.04 | 8.12 | 0.00 |
| 4 | `ruin_focus` | 0.0% | 8.04 | 0.00 | 0.38 | 6.11 | 4.26 |
| 4 | `safe_night` | 0.0% | 7.84 | 0.00 | 0.00 | 6.50 | 0.00 |

## Slutsats

**Bäst i v2:** `action_food` med cirka **0.0%** vinstgrad.

**Sämst i v2:** `crystal_rush` med cirka **0.0%** vinstgrad.

### Grotta

`crystal_rush` ligger nära `balanced`, vilket tyder på att Grotta är relevant utan att automatiskt dominera.

### Ruin

`ruin_focus` ligger nära `balanced`, vilket tyder på att Ruin är relevant och ungefär rätt lockande.

## Rekommendation

Använd v2 som bas för framtida simuleringar. Gör inte regeländringar enbart från simdata; bekräfta särskilt Grotta/Ruin i fysiskt speltest.
