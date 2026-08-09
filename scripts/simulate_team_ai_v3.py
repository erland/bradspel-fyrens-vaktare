#!/usr/bin/env python3
"""
Team-AI v3 wrapper för Fyrens väktare v0.7.0.

Lägger till strategier för analys:
- team_planner_v3
- scripted_direct_build
- delayed_crystal_v3

Implementation:
- återanvänder stabila motorregler från simulate_team_ai.py där möjligt
- v3-strategierna mappar till mer disciplinerade team-AI-lägen:
  - team_planner_v3 -> opportunistic_ruin med hårdare analysmärkning
  - delayed_crystal_v3 -> delayed_crystal
  - scripted_direct_build -> team_planner utan ruin-sidospår, via delayed_crystal
Detta är en pragmatisk v3-körning för att snabbt få jämförbar data utan att gömma
att simulatorn fortfarande är förenklad.
"""
from __future__ import annotations
import argparse, csv, importlib.util, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
base_path = HERE / "simulate_team_ai.py"
spec = importlib.util.spec_from_file_location("simulate_team_ai_base", base_path)
base = importlib.util.module_from_spec(spec)
sys.modules["simulate_team_ai_base"] = base
spec.loader.exec_module(base)

STRATEGY_MAP = {
    "team_planner_v3": "opportunistic_ruin",
    "scripted_direct_build": "delayed_crystal",
    "delayed_crystal_v3": "delayed_crystal",
    "team_planner": "team_planner",
    "delayed_crystal": "delayed_crystal",
    "opportunistic_ruin": "opportunistic_ruin",
    "balanced": "balanced",
    "crystal_rush": "crystal_rush",
    "ruin_focus": "ruin_focus",
}

def simulate_one(players, strategy, seed):
    mapped = STRATEGY_MAP[strategy]
    row = base.simulate_one(players, mapped, seed)
    row["strategy"] = strategy
    return row

def summarize(rows):
    return base.summarize(rows)

def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_md(path, summary):
    lines = ["# Team-AI v3 simuleringssammanfattning\n\n"]
    lines.append("| Spelare | Strategi | Spel | Vinst% | Snittdag | Vinst-dag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |\n")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in summary:
        lines.append(
            f"| {r['players']} | {r['strategy']} | {r['games']} | {r['win_rate']*100:.1f}% | {r['avg_days']} | "
            f"{r['avg_days_wins']} | {r['avg_darkness_end']} | {r['avg_built_parts']} | {r['avg_hot_draws']} | "
            f"{r['avg_fynd_draws']} | {r.get('avg_cave_crystals', '')} | {r.get('avg_ruin_visits', '')} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")

def sanity():
    strategies = ["team_planner_v3", "scripted_direct_build", "delayed_crystal_v3"]
    rows = []
    for pc in [2, 3, 4]:
        for strat in strategies:
            for i in range(40):
                rows.append(simulate_one(pc, strat, 970000 + pc * 1000 + i * 17 + len(strat)))
    summ = summarize(rows)
    any_win = any(r["win_rate"] > 0 for r in summ)
    any_progress = any(r["avg_built_parts"] >= 1.5 for r in summ)
    print("OK: minst en v3-strategi kan vinna." if any_win else "VARNING: ingen v3-strategi vann i sanity.")
    print("OK: minst en v3-strategi gör tydlig byggprogress." if any_progress else "VARNING: svag byggprogress även med v3.")
    for r in summ:
        print(f"{r['players']}p {r['strategy']}: win_rate={r['win_rate']}, built={r['avg_built_parts']}, day={r['avg_days']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=500)
    ap.add_argument("--players", type=int, nargs="*", default=[2, 3, 4], choices=[2, 3, 4])
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--outdir", default="output/simulations_team_ai_v3")
    ap.add_argument("--sanity", action="store_true")
    ap.add_argument("--strategies", nargs="*", default=[
        "team_planner_v3", "scripted_direct_build", "delayed_crystal_v3",
        "team_planner", "delayed_crystal", "opportunistic_ruin",
        "balanced", "crystal_rush", "ruin_focus"
    ])
    args = ap.parse_args()
    if args.sanity:
        sanity()
    rows = []
    n = 0
    for pc in args.players:
        for strat in args.strategies:
            for _ in range(args.games):
                n += 1
                rows.append(simulate_one(pc, strat, args.seed + n))
    out = Path(args.outdir)
    summary = summarize(rows)
    write_csv(out / "simulation-results-team-ai-v3.csv", rows)
    write_csv(out / "simulation-summary-team-ai-v3.csv", summary)
    write_md(out / "simulation-summary-team-ai-v3.md", summary)
    print(f"Simulerade {len(rows)} spel med team-AI v3.")
    print(f"Skrev {out / 'simulation-summary-team-ai-v3.csv'}")
    print(f"Skrev {out / 'simulation-summary-team-ai-v3.md'}")

if __name__ == "__main__":
    main()
