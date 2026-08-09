# Scripted 2p direct route – sanity-analys

Detta steg testar en hårdkodad mänsklig minimiplan med 2p-boost:

- 2 spelare
- Mörker 10
- 6 mat i Basen
- Ljuskärna 2 kristaller
- inga Basbygge-resurser

Syftet är att avgöra om problemet ligger i reglerna eller i full-Team-AI-planeraren.

## Körning 1: spara mat till Nattvakt

```bash
python scripts/simulate_scripted_2p_direct_route.py --games 5000 --seed 20260810 --policy save_food
```

```text
Skrev output/scripted_2p_direct_route/scripted-2p-direct-route-results.csv
Skrev output/scripted_2p_direct_route/scripted-2p-direct-route-summary.md
Vinstgrad: 30.26%
Snitt byggda delar: 2.30
Nådde minst 2 delar: 99.96%
```

# Scripted 2p direct route – resultat

Regler: 2p, Mörker 10, 6 mat, Ljuskärna 2, inga Basbygge-resurser.

- Spel: **5000**
- Policy: **save_food**
- Vinstgrad: **30.26%**
- Snitt byggda delar: **2.30**
- Nådde minst 2 delar: **99.96%**
- Snittdag vid vinst: **11.94**
- Snitt-Mörker kvar vid vinst: **1.37**


## Körning 2: en tempo-mat per spelare

```bash
python scripts/simulate_scripted_2p_direct_route.py --games 5000 --seed 20260810 --policy one_food_each --outdir output/scripted_2p_direct_route_food
```

```text
Skrev output/scripted_2p_direct_route_food/scripted-2p-direct-route-results.csv
Skrev output/scripted_2p_direct_route_food/scripted-2p-direct-route-summary.md
Vinstgrad: 14.48%
Snitt byggda delar: 2.13
Nådde minst 2 delar: 98.74%
```

# Scripted 2p direct route – resultat

Regler: 2p, Mörker 10, 6 mat, Ljuskärna 2, inga Basbygge-resurser.

- Spel: **5000**
- Policy: **one_food_each**
- Vinstgrad: **14.48%**
- Snitt byggda delar: **2.13**
- Nådde minst 2 delar: **98.74%**
- Snittdag vid vinst: **10.97**
- Snitt-Mörker kvar vid vinst: **1.16**


## Slutsats

Den scriptade rutten vinner i en meningsfull andel spel. Det betyder att 2p-boost-regeln är spelbar i modellen och att full-Team-AI-planeraren är problemet.

Nästa praktiska designbeslut bör bygga på den scriptade rutten och manuella simuleringen, inte på full-Team-AI, tills Team-AI-planeraren är reparerad.
