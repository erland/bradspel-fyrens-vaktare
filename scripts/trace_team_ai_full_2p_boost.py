#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, importlib.util, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
base_path = HERE / "simulate_team_ai_full_2p_boost.py"
spec = importlib.util.spec_from_file_location("simulate_team_ai_full_2p_boost_base", base_path)
base = importlib.util.module_from_spec(spec)
sys.modules["simulate_team_ai_full_2p_boost_base"] = base
spec.loader.exec_module(base)

def resources_str(d):
    return ",".join(f"{k}:{v}" for k, v in d.items() if v) or "-"

def mission_str(m):
    if not m:
        return "-"
    bits = [getattr(m, "kind", "-")]
    if getattr(m, "resource", None):
        bits.append(str(m.resource))
    if getattr(m, "amount", 0):
        bits.append(f"x{m.amount}")
    if getattr(m, "target", None):
        bits.append(f"@{m.target}")
    return " ".join(bits)

def snapshot(state, event, player_index=None, action_index=None, note=""):
    row = {
        "day": state.day,
        "event": event,
        "player": "" if player_index is None else player_index + 1,
        "action": "" if action_index is None else action_index + 1,
        "part": state.current_part(),
        "built_parts": state.built,
        "darkness": state.darkness,
        "base": resources_str(state.base),
        "hot_draws": state.hot_draws,
        "fynd_draws": state.fynd_draws,
        "cave_crystals": state.cave_crystals,
        "ruin_visits": state.ruin_visits,
        "note": note,
    }
    for i, p in enumerate(state.players, 1):
        row[f"p{i}_pos"] = base.loc(p.pos)
        row[f"p{i}_xy"] = str(p.pos)
        row[f"p{i}_carried"] = resources_str(p.carried)
        row[f"p{i}_mission"] = mission_str(p.mission)
    return row

def trace_one(players, strategy, seed, max_days=18, outdir="output/traces_2p_boost"):
    rng = base.random.Random(seed)
    state = base.State(
        pc=players,
        rng=rng,
        darkness=base.START_DARKNESS[players],
        base={r: 0 for r in base.RES},
        players=[base.Player() for _ in range(players)],
        fynd=base.Deck.make(base.FYND, rng),
        hot=base.Deck.make(base.HOT, rng),
    )
    state.base["mat"] = base.START_FOOD[players]

    rows = [snapshot(state, "START", note=f"strategy={strategy}, seed={seed}")]
    while not state.won and not state.lost and state.day <= max_days:
        rows.append(snapshot(state, "DAY_START"))

        for pi, p in enumerate(state.players):
            base.assign_missions(state, strategy)
            rows.append(snapshot(state, "TURN_START", pi, note=f"assigned={mission_str(p.mission)}"))

            actions = 2
            if base.should_use_food(state, p, strategy):
                p.carried["mat"] -= 1
                actions += 1
                rows.append(snapshot(state, "FOOD_EXTRA_ACTION", pi, note="spent carried mat for +1 action"))

            for ai in range(actions):
                if state.won or state.lost:
                    break

                old_pos = p.pos
                old_carried = dict(p.carried)
                old_built = state.built
                old_darkness = state.darkness
                old_hot = state.hot_draws
                old_fynd = state.fynd_draws
                old_cave = state.cave_crystals
                old_ruin = state.ruin_visits
                old_mission = mission_str(p.mission)

                target = base.mission_target(state, p, strategy)
                if target is None:
                    action_note = "no target"
                elif p.pos != target:
                    if state.effects.get("blocked", 0) > 0:
                        state.effects["blocked"] = 0
                        p.pos = base.step(p.pos, target)
                        action_note = f"blocked move toward {target}"
                    else:
                        base.move(p, target)
                        action_note = f"move {base.loc(old_pos)}->{base.loc(p.pos)} toward {target}"
                else:
                    place = base.loc(p.pos)
                    base.explore(state, p, strategy)
                    action_note = f"explore/use {place}"
                    if p.mission.kind == "COLLECT" and p.mission.resource and p.carried.get(p.mission.resource, 0) >= p.mission.amount:
                        p.mission = base.Mission("DELIVER", p.mission.resource, p.carried[p.mission.resource], base.LIGHTHOUSE)
                        action_note += " -> switch to deliver"

                if state.built > old_built:
                    action_note += f"; BUILT {state.built}"
                if state.darkness != old_darkness:
                    action_note += f"; darkness {old_darkness}->{state.darkness}"
                if state.hot_draws > old_hot:
                    action_note += f"; hot +{state.hot_draws-old_hot}"
                if state.fynd_draws > old_fynd:
                    action_note += f"; fynd +{state.fynd_draws-old_fynd}"
                if state.cave_crystals > old_cave:
                    action_note += "; took crystal"
                if state.ruin_visits > old_ruin:
                    action_note += "; visited ruin"
                rows.append(snapshot(state, "ACTION", pi, ai, note=f"{old_mission}; {action_note}"))

            rows.append(snapshot(state, "TURN_END", pi))
            if state.won or state.lost:
                break

        if state.won or state.lost:
            break
        old_darkness = state.darkness
        old_hot = state.hot_draws
        old_base = dict(state.base)
        base.night(state, strategy)
        rows.append(snapshot(state, "NIGHT", note=f"night; darkness {old_darkness}->{state.darkness}; hot +{state.hot_draws-old_hot}; base {resources_str(old_base)}->{resources_str(state.base)}"))
        state.day += 1

    result = "win" if state.won else "loss"
    rows.append(snapshot(state, "END", note=f"result={result}; built={state.built}; darkness={state.darkness}; day={state.day}"))

    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    base_name = f"trace-boost-{players}p-{strategy}-seed{seed}"
    csv_path = out / f"{base_name}.csv"
    md_path = out / f"{base_name}.md"

    fieldnames = list(rows[0].keys())
    for row in rows:
        for k in row.keys():
            if k not in fieldnames:
                fieldnames.append(k)
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    md = [f"# Trace – 2p-boost {players}p {strategy} seed {seed}\n\n"]
    md.append(f"Resultat: **{result}**. Fyrdelar byggda: **{state.built}**. Slut-Mörker: **{state.darkness}**. Dag: **{state.day}**.\n\n")
    md.append("## Händelser\n\n")
    for row in rows:
        if row["event"] in ["START", "DAY_START", "TURN_START", "ACTION", "NIGHT", "END"]:
            md.append(f"- Dag {row['day']} {row['event']}{' P'+str(row['player']) if row['player'] else ''}{' A'+str(row['action']) if row['action'] else ''}: byggt={row['built_parts']}, Mörker={row['darkness']}, {row['note']}\n")
    md.append("\n## Diagnos\n\n")
    if state.built == 0:
        md.append("AI:n bygger inte Grund. Läs särskilt om spelarna når Berg, samlar sten, byter till leveransuppdrag och om de faktiskt använder Fyrplatsen för Bygga.\n")
    elif state.built == 1:
        md.append("AI:n bygger Grund men fastnar före Torn.\n")
    elif state.built == 2:
        md.append("AI:n når Ljuskärnan men vinner inte.\n")
    else:
        md.append("AI:n vinner.\n")
    md_path.write_text("".join(md), encoding="utf-8")
    return csv_path, md_path, state

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--players", type=int, default=2, choices=[2,3,4])
    ap.add_argument("--strategy", default="mission_direct_build")
    ap.add_argument("--seed", type=int, default=20260801)
    ap.add_argument("--max-days", type=int, default=18)
    ap.add_argument("--outdir", default="output/traces_2p_boost")
    args = ap.parse_args()
    csv_path, md_path, state = trace_one(args.players, args.strategy, args.seed, args.max_days, args.outdir)
    print(f"Skrev {csv_path}")
    print(f"Skrev {md_path}")
    print(f"Resultat: {'win' if state.won else 'loss'}, byggt={state.built}, Mörker={state.darkness}, dag={state.day}")

if __name__ == "__main__":
    main()
