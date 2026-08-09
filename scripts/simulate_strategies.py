#!/usr/bin/env python3
"""
Simulering för Fyrens väktare v0.7.0.

Syfte:
- Snabbt jämföra hur olika enkla strategier fungerar efter regeländringar.
- Inte ersätta speltest. Simuleringen är en grov modell av spelet.

Kör exempel:
  python scripts/simulate_strategies.py --games 1000 --players 3 --seed 42

Output:
  output/simulations/simulation-summary.csv
  output/simulations/simulation-results.csv
  output/simulations/simulation-summary.md
"""

from __future__ import annotations

import argparse
import csv
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple, Optional


BOARD = [
    ["Skog", "Skog", "Ruin", "Berg", "Grotta"],
    ["Bas", "Stig", "Fyrplats", "Stig", "Grotta"],
    ["Stig", "Äng", "Stig", "Berg", "Stig"],
    ["Äng", "Ruin", "Äng", "Stig", "Skog"],
]

POSITIONS = {BOARD[r][c] + f"_{r}_{c}": (r, c) for r in range(4) for c in range(5)}
START = (1, 0)      # Bas
LIGHTHOUSE = (1, 2) # Fyrplats

START_DARKNESS = {2: 9, 3: 8, 4: 7}
START_FOOD = {2: 4, 3: 2, 4: 1}

BUILD_ORDER = [
    ("Grund", {"sten": 3}),
    ("Torn", {"trä": 3, "sten": 2}),
    ("Ljuskärna", {"kristall": 3}),
]

RESOURCES = ["trä", "sten", "mat", "kristall"]


@dataclass
class Player:
    pos: Tuple[int, int] = START
    carried: Dict[str, int] = field(default_factory=lambda: {r: 0 for r in RESOURCES})


@dataclass
class GameState:
    players_count: int
    rng: random.Random
    darkness: int
    base: Dict[str, int]
    players: List[Player]
    built_index: int = 0
    day: int = 1
    hot_draws: int = 0
    fynd_draws: int = 0
    lost: bool = False
    won: bool = False
    notes: List[str] = field(default_factory=list)

    def total_resource(self, res: str) -> int:
        return self.base.get(res, 0) + sum(p.carried.get(res, 0) for p in self.players)

    def resources_at_lighthouse(self) -> Dict[str, int]:
        totals = {r: 0 for r in RESOURCES}
        for p in self.players:
            if p.pos == LIGHTHOUSE:
                for r, n in p.carried.items():
                    totals[r] += n
        return totals


def dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    r, c = pos
    out = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 5:
            out.append((nr, nc))
    return out


def loc(pos: Tuple[int, int]) -> str:
    return BOARD[pos[0]][pos[1]]


def step_towards(pos: Tuple[int, int], target: Tuple[int, int]) -> Tuple[int, int]:
    ns = neighbors(pos)
    return min(ns, key=lambda p: dist(p, target))


def spend_from_players_at_lighthouse(state: GameState, cost: Dict[str, int]) -> bool:
    available = state.resources_at_lighthouse()
    if any(available.get(r, 0) < n for r, n in cost.items()):
        return False

    for r, needed in cost.items():
        remaining = needed
        for p in state.players:
            if p.pos != LIGHTHOUSE:
                continue
            take = min(remaining, p.carried.get(r, 0))
            p.carried[r] -= take
            remaining -= take
            if remaining <= 0:
                break
    return True


def maybe_build(state: GameState) -> bool:
    if state.built_index >= len(BUILD_ORDER):
        return False
    name, cost = BUILD_ORDER[state.built_index]
    if spend_from_players_at_lighthouse(state, cost):
        state.built_index += 1
        if state.built_index >= len(BUILD_ORDER):
            state.won = True
        return True
    return False


def draw_fynd(state: GameState, player: Player) -> None:
    state.fynd_draws += 1
    # Förenklad fyndmodell baserad på 12 aktuella fyndkort.
    roll = state.rng.randint(1, 12)
    if roll == 1:
        player.carried["kristall"] += 1
    elif roll == 2:
        # Gammal kista: välj 2 trä eller 1 valfri. Simulering väljer behov.
        need = current_need(state)
        if need == "trä":
            player.carried["trä"] += 2
        elif need in RESOURCES:
            player.carried[need] += 1
        else:
            player.carried["trä"] += 2
    elif roll == 3:
        player.carried["sten"] += 2
    elif roll == 4:
        player.carried["mat"] += 2
    elif roll == 5:
        player.carried["trä"] += 2
    elif roll == 6:
        # Direkt rörelse, abstraherat: flytta mot Fyrplats.
        player.pos = step_towards(player.pos, LIGHTHOUSE)
        if dist(player.pos, LIGHTHOUSE) > 0:
            player.pos = step_towards(player.pos, LIGHTHOUSE)
    elif roll == 7:
        # Ljuslykta: ignorerar nästa hot. Abstraheras som +0.25 säkerhet.
        state.notes.append("lykta")
    elif roll == 8:
        # Starka verktyg, uppdaterad direkt effekt.
        need = current_need(state)
        if need in ["trä", "sten", "mat"]:
            player.carried[need] += 1
        else:
            player.carried["sten"] += 1
    elif roll == 9:
        # Byggplan: nästa bygge kostar mindre. Abstraheras som 1 sten om relevant annars trä.
        need = current_need(state)
        if need in ["trä", "sten"]:
            player.carried[need] += 1
        else:
            player.carried["sten"] += 1
    elif roll == 10:
        # Gammal karta: mildrar hot. Abstraheras som note.
        state.notes.append("karta")
    elif roll == 11:
        need = current_need(state)
        if need in RESOURCES:
            state.base[need] = state.base.get(need, 0) + 1
        else:
            state.base["mat"] = state.base.get("mat", 0) + 1
    elif roll == 12:
        # Morgonljus
        start = START_DARKNESS[state.players_count]
        state.darkness = min(start, state.darkness + 1)


def draw_hot(state: GameState) -> None:
    state.hot_draws += 1
    # Ljuslykta/karta kan mildra ett hot.
    if "lykta" in state.notes:
        state.notes.remove("lykta")
        return
    if "karta" in state.notes and state.rng.random() < 0.5:
        state.notes.remove("karta")
        return

    roll = state.rng.randint(1, 12)
    if roll == 1:
        lose_resource_on_location(state, "Skog")
    elif roll == 2:
        # Ras i grottan: nästa grottsamling svagare. Abstraheras som inget.
        pass
    elif roll == 3:
        # Kall natt
        if state.base.get("mat", 0) > 0:
            state.base["mat"] -= 1
        else:
            state.darkness -= 1
    elif roll == 4:
        # Vilsen i dimman. Abstraheras som liten tidskostnad genom mörker-risk.
        if state.rng.random() < 0.35:
            state.darkness -= 1
    elif roll == 5:
        for p in state.players:
            if loc(p.pos) == "Berg" and p.carried.get("sten", 0) > 0:
                p.carried["sten"] -= 1
    elif roll == 6:
        state.darkness -= 1
    elif roll == 7:
        for p in state.players:
            if p.pos != START:
                if p.carried.get("mat", 0) > 0:
                    p.carried["mat"] -= 1
                else:
                    lose_any_resource(p)
    elif roll == 8:
        # Förlorade verktyg. Abstraheras som risk att tappa en produktionsresurs.
        p = state.rng.choice(state.players)
        lose_any_resource(p)
    elif roll == 9:
        # Blockerad stig. Abstraheras som liten mörker-risk.
        if state.rng.random() < 0.25:
            state.darkness -= 1
    elif roll == 10:
        if state.built_index >= 1:
            paid = False
            for p in state.players:
                if p.carried.get("kristall", 0) > 0:
                    p.carried["kristall"] -= 1
                    paid = True
                    break
            if not paid:
                state.darkness -= 1
    elif roll == 11:
        # Oroligt läger: nästa Nattvakt dyrare. Abstraheras som note.
        state.notes.append("orligt_lager")
    elif roll == 12:
        draw_hot(state)


def lose_resource_on_location(state: GameState, location: str) -> None:
    for p in state.players:
        if loc(p.pos) == location:
            lose_any_resource(p)


def lose_any_resource(p: Player) -> None:
    for r in ["kristall", "sten", "trä", "mat"]:
        if p.carried.get(r, 0) > 0:
            p.carried[r] -= 1
            return


def current_need(state: GameState) -> Optional[str]:
    if state.built_index >= len(BUILD_ORDER):
        return None
    _, cost = BUILD_ORDER[state.built_index]
    available = state.resources_at_lighthouse()
    for r, n in cost.items():
        if available.get(r, 0) < n:
            return r
    return None


def best_target_for_need(need: Optional[str], strategy: str, rng: random.Random) -> Tuple[int, int]:
    if need == "trä":
        return rng.choice([(0, 0), (0, 1), (3, 4)])
    if need == "sten":
        return rng.choice([(0, 3), (2, 3)])
    if need == "mat":
        return rng.choice([(2, 1), (3, 0), (3, 2)])
    if need == "kristall":
        return rng.choice([(0, 4), (1, 4)])
    if strategy == "ruin_focus":
        return rng.choice([(0, 2), (3, 1)])
    return LIGHTHOUSE


def explore(state: GameState, player: Player, strategy: str) -> None:
    place = loc(player.pos)
    if place == "Skog":
        player.carried["trä"] += 1
    elif place == "Berg":
        player.carried["sten"] += 1
    elif place == "Äng":
        player.carried["mat"] += 1
    elif place == "Grotta":
        # Strategi styr hur ofta kristall tas.
        if strategy in ["crystal_rush", "balanced"] or current_need(state) == "kristall":
            player.carried["kristall"] += 1
            draw_hot(state)
        else:
            player.carried["sten"] += 1
    elif place == "Ruin":
        draw_fynd(state, player)
    elif place == "Bas":
        # Lämna mat/resurser i basen. Resurser för bygge måste senare bäras till Fyrplatsen.
        for r in RESOURCES:
            if r == "mat" or strategy == "safe_night":
                state.base[r] += player.carried[r]
                player.carried[r] = 0
    elif place == "Fyrplats":
        maybe_build(state)


def choose_action(state: GameState, player: Player, strategy: str) -> str:
    if state.won or state.lost:
        return "none"

    if player.pos == LIGHTHOUSE and maybe_build(state):
        return "built"

    need = current_need(state)

    # If carrying needed resources, go to Fyrplats.
    if any(player.carried.get(r, 0) > 0 for r in ["trä", "sten", "kristall"]):
        if player.pos != LIGHTHOUSE:
            player.pos = step_towards(player.pos, LIGHTHOUSE)
            return "move"
        else:
            maybe_build(state)
            return "build"

    # Food strategy: sometimes gather food for night watch.
    if strategy == "safe_night" and state.base.get("mat", 0) < 2:
        target = best_target_for_need("mat", strategy, state.rng)
    elif strategy == "ruin_focus" and state.rng.random() < 0.45:
        target = state.rng.choice([(0, 2), (3, 1)])
    else:
        target = best_target_for_need(need, strategy, state.rng)

    if player.pos != target:
        # Stig simplified: if on Stig, move two steps toward target.
        steps = 2 if loc(player.pos) == "Stig" else 1
        for _ in range(steps):
            if player.pos != target:
                player.pos = step_towards(player.pos, target)
        return "move"

    explore(state, player, strategy)
    return "explore"


def take_turn(state: GameState, player: Player, strategy: str) -> None:
    actions = 2

    # Extra action usage.
    if strategy in ["action_food", "balanced"] and player.carried.get("mat", 0) > 0:
        player.carried["mat"] -= 1
        actions += 1

    for _ in range(actions):
        if state.won or state.lost:
            return
        choose_action(state, player, strategy)


def night_phase(state: GameState, strategy: str) -> None:
    # Nattvakt decision.
    use_watch = False
    if strategy == "safe_night":
        use_watch = state.base.get("mat", 0) >= (2 if "orligt_lager" in state.notes else 1)
    elif strategy == "balanced":
        use_watch = state.darkness <= 4 and state.base.get("mat", 0) >= (2 if "orligt_lager" in state.notes else 1)
    elif strategy == "action_food":
        use_watch = state.darkness <= 2 and state.base.get("mat", 0) >= (2 if "orligt_lager" in state.notes else 1)
    else:
        use_watch = False

    if use_watch:
        cost = 2 if "orligt_lager" in state.notes else 1
        state.base["mat"] -= cost
        if "orligt_lager" in state.notes:
            state.notes.remove("orligt_lager")
    else:
        state.darkness -= 1

    if state.darkness <= 0:
        state.lost = True
        return

    draw_hot(state)
    if state.darkness <= 0:
        state.lost = True


def simulate_one(players_count: int, strategy: str, seed: int, max_days: int = 30) -> Dict[str, object]:
    rng = random.Random(seed)
    state = GameState(
        players_count=players_count,
        rng=rng,
        darkness=START_DARKNESS[players_count],
        base={r: 0 for r in RESOURCES},
        players=[Player() for _ in range(players_count)],
    )
    state.base["mat"] = START_FOOD[players_count]

    while not state.won and not state.lost and state.day <= max_days:
        for p in state.players:
            take_turn(state, p, strategy)
            if state.won or state.lost:
                break
        if state.won or state.lost:
            break
        night_phase(state, strategy)
        state.day += 1

    if not state.won and not state.lost:
        state.lost = True

    return {
        "players": players_count,
        "strategy": strategy,
        "seed": seed,
        "result": "win" if state.won else "loss",
        "days": state.day,
        "darkness_end": state.darkness,
        "built_parts": state.built_index,
        "hot_draws": state.hot_draws,
        "fynd_draws": state.fynd_draws,
        "base_food_end": state.base.get("mat", 0),
        "base_wood_end": state.base.get("trä", 0),
        "base_stone_end": state.base.get("sten", 0),
        "base_crystal_end": state.base.get("kristall", 0),
    }


def summarize(rows: List[Dict[str, object]]) -> List[Dict[str, object]]:
    groups: Dict[Tuple[int, str], List[Dict[str, object]]] = {}
    for row in rows:
        groups.setdefault((int(row["players"]), str(row["strategy"])), []).append(row)

    out = []
    for (players, strategy), vals in sorted(groups.items()):
        wins = [v for v in vals if v["result"] == "win"]
        out.append({
            "players": players,
            "strategy": strategy,
            "games": len(vals),
            "win_rate": round(len(wins) / len(vals), 3),
            "avg_days": round(sum(int(v["days"]) for v in vals) / len(vals), 2),
            "avg_days_wins": round(sum(int(v["days"]) for v in wins) / len(wins), 2) if wins else "",
            "avg_darkness_end": round(sum(int(v["darkness_end"]) for v in vals) / len(vals), 2),
            "avg_built_parts": round(sum(int(v["built_parts"]) for v in vals) / len(vals), 2),
            "avg_hot_draws": round(sum(int(v["hot_draws"]) for v in vals) / len(vals), 2),
            "avg_fynd_draws": round(sum(int(v["fynd_draws"]) for v in vals) / len(vals), 2),
        })
    return out


def write_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, summary: List[Dict[str, object]]) -> None:
    lines = ["# Simuleringssammanfattning\n\n"]
    lines.append("Detta är en grov simulering för att jämföra strategier, inte ett facit för balans.\n\n")
    lines.append("| Spelare | Strategi | Spel | Vinst% | Snittdagar | Snittdagar vid vinst | Snitt Mörker slut | Snitt Fyrdelar | Hotkort | Fyndkort |\n")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in summary:
        lines.append(
            f"| {r['players']} | {r['strategy']} | {r['games']} | {float(r['win_rate'])*100:.1f}% | "
            f"{r['avg_days']} | {r['avg_days_wins']} | {r['avg_darkness_end']} | "
            f"{r['avg_built_parts']} | {r['avg_hot_draws']} | {r['avg_fynd_draws']} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", type=int, default=500)
    parser.add_argument("--players", type=int, nargs="*", default=[2, 3, 4], choices=[2, 3, 4])
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--outdir", type=str, default="output/simulations")
    parser.add_argument("--strategies", nargs="*", default=["balanced", "safe_night", "action_food", "crystal_rush", "ruin_focus"])
    args = parser.parse_args()

    rows = []
    n = 0
    for players in args.players:
        for strategy in args.strategies:
            for i in range(args.games):
                n += 1
                rows.append(simulate_one(players, strategy, args.seed + n))

    outdir = Path(args.outdir)
    summary = summarize(rows)
    write_csv(outdir / "simulation-results.csv", rows)
    write_csv(outdir / "simulation-summary.csv", summary)
    write_markdown(outdir / "simulation-summary.md", summary)

    print(f"Simulerade {len(rows)} spel.")
    print(f"Skrev {outdir / 'simulation-summary.csv'}")
    print(f"Skrev {outdir / 'simulation-summary.md'}")


if __name__ == "__main__":
    main()
