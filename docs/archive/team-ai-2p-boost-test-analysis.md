# Team-AI-test – 2p-boost

Test av senaste `simulate_team_ai_full.py`-familjen med 2p-regelvarianten:

- 2 spelare
- Mörker 10
- 6 mat i Basen
- Ljuskärna: 2 kristaller
- Ingen Basbygge-regel

För att inte skriva över grundscriptet skapades en separat testkopia:

```text
scripts/simulate_team_ai_full_2p_boost.py
```

## Körning

```bash
python scripts/simulate_team_ai_full_2p_boost.py --games 5000 --players 2 --seed 20260801 --sanity
```

## Konsoloutput

```text
VARNING: ingen full-mission-strategi vann.
VARNING: svag byggprogress i full mission.
2p mission_direct_build: win_rate=0.0, built=0.0, day=13.82
2p mission_opportunistic_ruin: win_rate=0.0, built=0.0, day=13.87
2p mission_team_planner: win_rate=0.0, built=0.0, day=13.85
3p mission_direct_build: win_rate=0.0, built=0.32, day=9.0
3p mission_opportunistic_ruin: win_rate=0.0, built=0.23, day=9.13
3p mission_team_planner: win_rate=0.0, built=0.3, day=9.05
4p mission_direct_build: win_rate=0.0, built=0.15, day=7.58
4p mission_opportunistic_ruin: win_rate=0.0, built=0.17, day=7.63
4p mission_team_planner: win_rate=0.0, built=0.15, day=7.58
Simulerade 20000 spel med full Team-AI.
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.csv
Skrev output/simulations_team_ai_full/simulation-summary-team-ai-full.md
```

## Stderr

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 720, in _warm_feature_flows
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/spreadsheet_warmup.py", line 704, in _warm_collaboration_flows
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/generated/interface/models.py", line 30820, in hydrate_crdt_from_proto
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/rpc/remote.py", line 749, in __call__
  File "/tmp/tmp.yTcnQsZYiA/artifact_tool_v2-2.8.4/artifact_tool/rpc/client.py", line 150, in call
artifact_tool.rpc.client.RemoteError: hydrateCrdtFromProto requires an empty collaborative document.
```

## Resultattabell

| Strategi | Spelare | Spel | Vinstgrad | Snittdag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `mission_delayed_crystal` | 2 | 5000 | 0.00% | 13.88 | 0.00 | 0.00 | 13.14 | 0.00 | 0.00 | 0.00 |
| `mission_direct_build` | 2 | 5000 | 0.00% | 13.82 | 0.00 | 0.00 | 13.09 | 0.00 | 0.00 | 0.00 |
| `mission_opportunistic_ruin` | 2 | 5000 | 0.00% | 13.87 | 0.00 | 0.00 | 13.13 | 0.00 | 0.00 | 0.00 |
| `mission_team_planner` | 2 | 5000 | 0.00% | 13.88 | 0.00 | 0.00 | 13.14 | 0.00 | 0.00 | 0.00 |

## Kort slutsats

Ingen Team-AI-strategi vann. Snittbyggprogress för bästa strategi var **0.00** Fyrdelar. Det tyder på att senaste Team-AI fortfarande inte klarar 2p även när reglerna mildras.
