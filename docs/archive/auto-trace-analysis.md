# Auto-trace analys – Fyrens väktare

## Körning

Sökning gjordes in-process med `seed_start=20260720`, `seed_count=200`, spelarantal 2–4 och fyra mission-strategier.

# Automatisk trace-sampling

Sökta simuleringar: **2400**.

| Kategori | Spelare | Strategi | Seed | Resultat | Fyrdelar | Dag | Mörker | Hot | Fynd | Grottkristaller | Ruinbesök |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| built_0 | 2 | `mission_direct_build` | 20260720 | loss | 0 | 11 | 0 | 10 | 0 | 0 | 0 |
| built_1 | 3 | `mission_direct_build` | 20261520 | loss | 1 | 9 | 0 | 8 | 0 | 0 | 0 |
| built_2 | - | - | - | hittades inte | - | - | - | - | - | - | - |
| win | - | - | - | hittades inte | - | - | - | - | - | - | - |

## Tolkning

`built_0` visar Grund-problem, `built_1` visar Torn-problem, `built_2` visar Ljuskärna/Grotta-problem och `win` visar ett lyckat spel om ett sådant finns.

## Praktisk slutsats

Auto-trace-sampling är nu på plats. Sökningen hittade de kategorier som visas i tabellen ovan. Om `built_2` eller `win` saknas inom 2400 försök är det en stark signal att nuvarande full Team-AI sällan når kristallfasen eller vinst.
