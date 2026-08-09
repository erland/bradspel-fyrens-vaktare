# Simuleringsguide – team-AI v3

`simulate_team_ai_v3.py` lägger till de rekommenderade jämförelsestrategierna:

- `team_planner_v3`
- `scripted_direct_build`
- `delayed_crystal_v3`

## Syfte

V3 ska ge bättre kontrollfrågor:

- Kan en rak byggplan fungera?
- Är fördröjd kristalljakt bättre än flexibel plan?
- Verkar sidospår som Ruin hjälpa eller störa?

## Viktig teknisk notering

Den här v3-versionen är ett pragmatiskt jämförelselager ovanpå `simulate_team_ai.py`. Den förbättrar analysstrukturen och strategijämförelsen, men är inte ännu en full omskrivning av spelmotorn.

## Körning

```bash
python scripts/simulate_team_ai_v3.py --games 1000 --players 2 3 4 --seed 20260710 --sanity
```
