# Guide – automatisk trace-sampling

`auto_trace_sampler.py` söker efter representativa spel:

- `built_0`: förlust med 0 byggda Fyrdelar
- `built_1`: förlust med 1 byggd Fyrdel
- `built_2`: förlust med 2 byggda Fyrdelar
- `win`: vinst om det finns

Kör:

```bash
python scripts/auto_trace_sampler.py --seed-start 20260720 --seed-count 200
```

Output:

```text
output/auto_traces/auto-trace-summary.csv
output/auto_traces/auto-trace-summary.md
```
