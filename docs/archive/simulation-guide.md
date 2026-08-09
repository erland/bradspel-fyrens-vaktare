# Simuleringsguide – Fyrens väktare

## Syfte

Projektet har nu ett enkelt simuleringsskript:

```text
scripts/simulate_strategies.py
```

Skriptet kan köra många automatiska spel med olika strategier och skriva ut jämförande data.

Det här är **inte** en perfekt digital version av spelet. Det är ett balansverktyg för att se trender efter regeländringar.

## Körning

Från projektroten:

```bash
python scripts/simulate_strategies.py --games 1000 --players 2 3 4 --seed 42
```

För snabb testkörning:

```bash
python scripts/simulate_strategies.py --games 100 --players 3 --seed 1
```

## Output

Skriptet skriver:

```text
output/simulations/simulation-results.csv
output/simulations/simulation-summary.csv
output/simulations/simulation-summary.md
```

## Strategier

Nuvarande strategier:

- `balanced` – blandad strategi
- `safe_night` – prioriterar mat i Basen och Nattvakt
- `action_food` – använder mat för extra handlingar
- `crystal_rush` – prioriterar Grotta/kristaller
- `ruin_focus` – prioriterar Ruin/fyndkort

Strategierna dokumenteras även i:

```text
data/simulation-strategies.yaml
```

## Viktiga begränsningar

Simuleringen är förenklad.

Den modellerar:

- spelare
- karta
- rörelse
- Utforska
- byggkostnader
- Mörker
- Nattfas
- förenklade fyndkort
- förenklade hotkort
- några olika strategier

Den modellerar inte perfekt:

- alla mänskliga samarbetsbeslut
- exakt kortordning över flera rundor
- smart planering flera turer framåt
- alla positionella nyanser
- spelarnas diskussioner

Använd därför simuleringen för att jämföra **relativa skillnader**, inte som slutgiltig balans.

## Rekommenderad användning efter regeländring

1. Ändra regler/data.
2. Uppdatera simuleringsskriptet om regeln påverkar spelmotorn.
3. Kör 500–2000 spel per strategi.
4. Jämför vinstgrad, snittdag och Mörker vid slut.
5. Välj högst 1–3 ändringar.
6. Bekräfta med fysiskt speltest.
