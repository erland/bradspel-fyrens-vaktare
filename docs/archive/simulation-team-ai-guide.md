# Simuleringsguide – team-AI

Det här skriptet bygger vidare på simulator v2 och lägger till tre mer realistiska kooperativa strategier:

- `team_planner`
- `delayed_crystal`
- `opportunistic_ruin`

## Varför behövs det?

De tidigare strategierna spelade för individuellt. **Fyrens väktare** kräver lagkoordinering:

- rätt resurser måste samlas
- rätt spelare måste leverera dem till Fyrplatsen
- Grotta bör användas när kristaller faktiskt behövs
- Ruin bör oftast vara ett opportunistiskt sidospår

## Körning

```bash
python scripts/simulate_team_ai.py --games 5000 --players 2 3 4 --seed 20260709 --sanity
```

## Strategier

### team_planner

Normal kooperativ plan:

1. bygg nästa Fyrdel
2. leverera resurser som redan bärs
3. samla saknad resurs
4. samla mat bara när Mörker är lågt och Basen saknar mat

### delayed_crystal

Som `team_planner`, men undviker kristalljakt tills Ljuskärnan är nästa Fyrdel.

### opportunistic_ruin

Som `team_planner`, men besöker Ruin när det är billigt och Mörker inte är för lågt.

## Output

```text
output/simulations_team_ai/simulation-results-team-ai.csv
output/simulations_team_ai/simulation-summary-team-ai.csv
output/simulations_team_ai/simulation-summary-team-ai.md
```

## Begränsning

Detta är fortfarande inte en människa. Använd resultaten för trendanalys och jämför sedan med fysiskt speltest.
