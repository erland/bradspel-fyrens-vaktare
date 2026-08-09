#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, importlib.util, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
full_path = HERE / "simulate_team_ai_full.py"
spec = importlib.util.spec_from_file_location("simulate_team_ai_full_base", full_path)
full = importlib.util.module_from_spec(spec)
sys.modules["simulate_team_ai_full_base"] = full
spec.loader.exec_module(full)

def find_examples(players_list, strategies, seed_start, seed_count):
    wanted = {
        "built_0": lambda r: r["result"] == "loss" and int(r["built_parts"]) == 0,
        "built_1": lambda r: r["result"] == "loss" and int(r["built_parts"]) == 1,
        "built_2": lambda r: r["result"] == "loss" and int(r["built_parts"]) == 2,
        "win": lambda r: r["result"] == "win",
    }
    found = {}
    checked = 0
    for players in players_list:
        for strategy in strategies:
            for offset in range(seed_count):
                seed = seed_start + checked + offset
                row = full.simulate_one(players, strategy, seed)
                checked += 1
                for key, pred in wanted.items():
                    if key not in found and pred(row):
                        found[key] = {
                            "category": key, "players": players, "strategy": strategy,
                            "seed": seed, "result": row["result"], "built_parts": row["built_parts"],
                            "days": row["days"], "darkness_end": row["darkness_end"],
                            "hot_draws": row["hot_draws"], "fynd_draws": row["fynd_draws"],
                            "cave_crystals": row["cave_crystals"], "ruin_visits": row["ruin_visits"],
                        }
                if len(found) == len(wanted):
                    return found, checked
    return found, checked

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed-start", type=int, default=20260720)
    ap.add_argument("--seed-count", type=int, default=200)
    ap.add_argument("--players", type=int, nargs="*", default=[2,3,4], choices=[2,3,4])
    ap.add_argument("--strategies", nargs="*", default=[
        "mission_direct_build", "mission_team_planner", "mission_delayed_crystal", "mission_opportunistic_ruin"
    ])
    ap.add_argument("--outdir", default="output/auto_traces")
    args = ap.parse_args()
    found, checked = find_examples(args.players, args.strategies, args.seed_start, args.seed_count)
    outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    rows = [found[k] for k in ["built_0","built_1","built_2","win"] if k in found]
    if rows:
        with (outdir / "auto-trace-summary.csv").open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    md = ["# Automatisk trace-sampling\n\n", f"Sökta simuleringar: **{checked}**.\n\n"]
    md.append("| Kategori | Spelare | Strategi | Seed | Resultat | Fyrdelar | Dag | Mörker | Hot | Fynd | Grottkristaller | Ruinbesök |\n")
    md.append("|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|\n")
    for key in ["built_0","built_1","built_2","win"]:
        ex = found.get(key)
        if ex:
            md.append(f"| {key} | {ex['players']} | `{ex['strategy']}` | {ex['seed']} | {ex['result']} | {ex['built_parts']} | {ex['days']} | {ex['darkness_end']} | {ex['hot_draws']} | {ex['fynd_draws']} | {ex['cave_crystals']} | {ex['ruin_visits']} |\n")
        else:
            md.append(f"| {key} | - | - | - | hittades inte | - | - | - | - | - | - | - |\n")
    (outdir / "auto-trace-summary.md").write_text("".join(md), encoding="utf-8")
    print(f"Sökte {checked} simuleringar.")
    print(f"Hittade kategorier: {', '.join(found.keys()) if found else 'inga'}")
    print(f"Skrev {outdir / 'auto-trace-summary.md'}")

if __name__ == "__main__":
    main()
