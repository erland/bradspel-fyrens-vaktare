# Trace-guide – full Team-AI

`trace_team_ai_full.py` loggar enskilda simulerade spel steg för steg.

## Syfte

När massimuleringarna visar låg vinstgrad behöver vi se **var AI:n tappar tempo**:

- samlar den resurser men levererar inte?
- står spelare fel?
- byggs Grund/Torn för sent?
- tar kristallfasen för lång tid?
- äter hotkort upp för mycket tempo?
- används mat fel?

## Körning

```bash
python scripts/trace_team_ai_full.py --players 3 --strategy mission_direct_build --seed 20260711
```

Fler exempel:

```bash
python scripts/trace_team_ai_full.py --players 4 --strategy mission_opportunistic_ruin --seed 20260711
python scripts/trace_team_ai_full.py --players 2 --strategy mission_team_planner --seed 20260712
```

## Output

```text
output/traces/trace-...csv
output/traces/trace-...md
```

CSV-filen är detaljerad. Markdown-filen är en kortare läsbar diagnos.

## Tolkning

- Byggt 0 delar: AI:n misslyckas med sten/leverans till Grund.
- Byggt 1 del: AI:n fastnar på Torn.
- Byggt 2 delar: kristallfasen/Grotta/hot är flaskhals.
