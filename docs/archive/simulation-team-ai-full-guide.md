# Simuleringsguide – full Team-AI

`simulate_team_ai_full.py` är första simulatorn i projektet med en faktisk uppdragsmotor.

## Nytt

- uppdrag med målantal
- reserverade resurser
- fasbaserad byggplan
- hård byggprioritet
- smartare matanvändning
- Grotta som kristallfas
- Ruin som sidouppdrag när det inte stör huvudplanen

## Strategier

- `mission_direct_build`
- `mission_team_planner`
- `mission_delayed_crystal`
- `mission_opportunistic_ruin`

## Körning

```bash
python scripts/simulate_team_ai_full.py --games 1000 --players 2 3 4 --seed 20260711 --sanity
```

## Output

```text
output/simulations_team_ai_full/simulation-results-team-ai-full.csv
output/simulations_team_ai_full/simulation-summary-team-ai-full.csv
output/simulations_team_ai_full/simulation-summary-team-ai-full.md
```
