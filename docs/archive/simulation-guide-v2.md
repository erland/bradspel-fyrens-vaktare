# Simuleringsguide v2 – Fyrens väktare

Rekommenderad simulator framåt:

```bash
python scripts/simulate_strategies_v2.py --games 5000 --players 2 3 4 --seed 20260708 --sanity
```

## Förbättringar jämfört med v1

1. Spelare fastnar inte på Fyrplatsen med fel eller för få resurser.
2. Gruppen använder en enkel lagbaserad behovsanalys.
3. Fyndkort och hotkort dras ur riktiga lekar med slänghög och omblandning.
4. `--sanity` gör en snabb kontroll av att simulatorn kan producera vinster och byggprogress.

V2 är fortfarande förenklad och ska användas för trendanalys, inte som ersättning för speltest.
