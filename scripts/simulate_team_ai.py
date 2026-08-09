#!/usr/bin/env python3
"""
Simulator team-AI för Fyrens väktare v0.7.0.

Bygger vidare på simulator v2 men lägger till mer realistiska kooperativa strategier:

- team_planner
- delayed_crystal
- opportunistic_ruin

Syfte:
- testa om en rimligt koordinerad grupp kan vinna
- analysera om Grotta och Ruin verkar relevanta
- få bättre simdata efter regeländringar

Viktigt:
Detta är fortfarande en förenklad simulator. Den ska användas som beslutsstöd,
inte som ersättning för fysiskt speltest.
"""

from __future__ import annotations
import argparse, csv, random
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

BOARD = [
    ["Skog", "Skog", "Ruin", "Berg", "Grotta"],
    ["Bas", "Stig", "Fyrplats", "Stig", "Grotta"],
    ["Stig", "Äng", "Stig", "Berg", "Stig"],
    ["Äng", "Ruin", "Äng", "Stig", "Skog"],
]
START = (1, 0)
LIGHTHOUSE = (1, 2)
START_DARKNESS = {2: 9, 3: 8, 4: 7}
START_FOOD = {2: 4, 3: 2, 4: 1}
RES = ["trä", "sten", "mat", "kristall"]
BUILD = [
    ("Grund", {"sten": 3}),
    ("Torn", {"trä": 3, "sten": 2}),
    ("Ljuskärna", {"kristall": 3}),
]
FYND = [f"FYN-{i:03d}" for i in range(1, 13)]
HOT = [f"HOT-{i:03d}" for i in range(1, 13)]

WOOD = [(0, 0), (0, 1), (3, 4)]
STONE = [(0, 3), (2, 3)]
CAVE = [(0, 4), (1, 4)]
MEADOW = [(2, 1), (3, 0), (3, 2)]
RUIN = [(0, 2), (3, 1)]


@dataclass
class Deck:
    draw_pile: List[str]
    discard: List[str] = field(default_factory=list)

    @classmethod
    def make(cls, cards, rng):
        pile = cards[:]
        rng.shuffle(pile)
        return cls(pile)

    def draw(self, rng):
        if not self.draw_pile:
            self.draw_pile = self.discard[:]
            self.discard = []
            rng.shuffle(self.draw_pile)
        card = self.draw_pile.pop(0)
        self.discard.append(card)
        return card


@dataclass
class Player:
    pos: Tuple[int, int] = START
    carried: Dict[str, int] = field(default_factory=lambda: {r: 0 for r in RES})
    assignment: str = ""


@dataclass
class State:
    pc: int
    rng: random.Random
    darkness: int
    base: Dict[str, int]
    players: List[Player]
    fynd: Deck
    hot: Deck
    built: int = 0
    day: int = 1
    won: bool = False
    lost: bool = False
    hot_draws: int = 0
    fynd_draws: int = 0
    cave_crystals: int = 0
    cave_stone: int = 0
    ruin_visits: int = 0
    builds: int = 0
    effects: Dict[str, int] = field(default_factory=dict)

    def cost(self):
        return BUILD[self.built][1] if self.built < len(BUILD) else {}

    def part_name(self):
        return BUILD[self.built][0] if self.built < len(BUILD) else "Klar"

    def at_fyr(self):
        t = {r: 0 for r in RES}
        for p in self.players:
            if p.pos == LIGHTHOUSE:
                for r, n in p.carried.items():
                    t[r] += n
        return t

    def team_carried(self):
        t = {r: 0 for r in RES}
        for p in self.players:
            for r, n in p.carried.items():
                t[r] += n
        return t


def loc(pos): return BOARD[pos[0]][pos[1]]
def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])
def neigh(pos):
    r, c = pos
    out = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 4 and 0 <= nc < 5:
            out.append((nr, nc))
    return out
def step(pos, target): return min(neigh(pos), key=lambda p: dist(p, target))
def nearest(pos, targets): return min(targets, key=lambda t: dist(pos, t))

def move(p, target):
    steps = 2 if loc(p.pos) == "Stig" else 1
    for _ in range(steps):
        if p.pos != target:
            p.pos = step(p.pos, target)

def can_build(s):
    a = s.at_fyr()
    return bool(s.cost()) and all(a.get(r, 0) >= n for r, n in s.cost().items())

def build(s):
    if not can_build(s):
        return False
    for r, n in s.cost().items():
        rem = n
        for p in s.players:
            if p.pos == LIGHTHOUSE:
                take = min(rem, p.carried.get(r, 0))
                p.carried[r] -= take
                rem -= take
                if rem <= 0:
                    break
    s.built += 1
    s.builds += 1
    if s.built >= len(BUILD):
        s.won = True
    return True

def build_discount(s):
    if build(s):
        return True
    if s.effects.get("discount", 0) <= 0 or not s.cost():
        return False
    a = s.at_fyr()
    missing = sum(max(0, n - a.get(r, 0)) for r, n in s.cost().items())
    if missing == 1:
        for r, n in s.cost().items():
            rem = min(n, a.get(r, 0))
            for p in s.players:
                if p.pos == LIGHTHOUSE:
                    take = min(rem, p.carried[r])
                    p.carried[r] -= take
                    rem -= take
                    if rem <= 0:
                        break
        s.effects["discount"] -= 1
        s.built += 1
        s.builds += 1
        if s.built >= len(BUILD):
            s.won = True
        return True
    return False

def delivery_need(s):
    a = s.at_fyr()
    return {r: max(0, n - a.get(r, 0)) for r, n in s.cost().items() if max(0, n - a.get(r, 0)) > 0}

def reserved_need(s):
    """Behov efter att resurser på Fyrplatsen och burna lagresurser räknats."""
    d = delivery_need(s)
    team = s.team_carried()
    return {r: max(0, n - team.get(r, 0)) for r, n in d.items() if max(0, n - team.get(r, 0)) > 0}

def relevant_delivery(p, s):
    d = delivery_need(s)
    return any(p.carried.get(r, 0) > 0 and d.get(r, 0) > 0 for r in ["trä", "sten", "kristall"])

def carrying_build_resource(p):
    return any(p.carried.get(r, 0) > 0 for r in ["trä", "sten", "kristall"])

def target_for_resource(res, s, strategy):
    if res == "trä":
        return nearest_to_any_actor(s, WOOD)
    if res == "sten":
        # Before core, prefer Berg unless cave is much nearer or strategy accepts cave.
        if strategy in ["crystal_rush"] or s.part_name() == "Ljuskärna":
            return nearest_to_any_actor(s, STONE + CAVE)
        return nearest_to_any_actor(s, STONE)
    if res == "kristall":
        return nearest_to_any_actor(s, CAVE)
    if res == "mat":
        return nearest_to_any_actor(s, MEADOW)
    return LIGHTHOUSE

def nearest_to_any_actor(s, targets):
    # Pick target that is globally easy for the team.
    return min(targets, key=lambda t: min(dist(p.pos, t) for p in s.players))

def best_resource_to_collect(s, strategy):
    need = reserved_need(s)
    if need:
        if strategy == "delayed_crystal" and s.part_name() != "Ljuskärna" and "kristall" in need:
            # Shouldn't happen before core, but keep safe.
            pass
        return max(need.items(), key=lambda x: x[1])[0]

    d = delivery_need(s)
    if d:
        return max(d.items(), key=lambda x: x[1])[0]

    return None

def threat_level(s):
    return "critical" if s.darkness <= 2 else "low" if s.darkness <= 4 else "safe"

def should_get_food(s, strategy):
    if strategy == "team_planner":
        return s.darkness <= 4 and s.base.get("mat", 0) == 0
    if strategy == "delayed_crystal":
        return s.darkness <= 3 and s.base.get("mat", 0) == 0
    if strategy == "opportunistic_ruin":
        return s.darkness <= 4 and s.base.get("mat", 0) == 0
    if strategy == "safe_night":
        return s.base.get("mat", 0) < 2
    return False

def should_visit_ruin(s, p, strategy, current_target=None):
    if strategy == "ruin_focus":
        return True
    if strategy != "opportunistic_ruin":
        return False
    if s.darkness <= 3:
        return False
    if reserved_need(s):
        # Only detour if very cheap and not during crystal core pressure.
        max_detour = 0 if s.part_name() == "Ljuskärna" else 1
    else:
        max_detour = 1
    nearest_ruin = nearest(p.pos, RUIN)
    if p.pos in RUIN:
        return True
    if current_target is None:
        return dist(p.pos, nearest_ruin) <= 1
    direct = dist(p.pos, current_target)
    detour = dist(p.pos, nearest_ruin) + dist(nearest_ruin, current_target)
    return detour - direct <= max_detour

def lose_any(p):
    for r in ["kristall", "sten", "trä", "mat"]:
        if p.carried.get(r, 0) > 0:
            p.carried[r] -= 1
            return

def draw_hot(s):
    if s.effects.get("ignore_hot", 0) > 0:
        s.effects["ignore_hot"] -= 1
        return
    if s.effects.get("mitigate_hot", 0) > 0 and s.rng.random() < 0.5:
        s.effects["mitigate_hot"] -= 1
        return

    s.hot_draws += 1
    c = s.hot.draw(s.rng)
    if c == "HOT-001":
        for p in s.players:
            if loc(p.pos) == "Skog":
                lose_any(p)
    elif c == "HOT-002":
        s.effects["cave_block"] = 1
    elif c == "HOT-003":
        if s.base.get("mat", 0) > 0:
            s.base["mat"] -= 1
        else:
            s.darkness -= 1
    elif c == "HOT-004":
        s.effects["fog"] = len([p for p in s.players if p.pos != START])
    elif c == "HOT-005":
        for p in s.players:
            if loc(p.pos) == "Berg" and p.carried["sten"] > 0:
                p.carried["sten"] -= 1
    elif c == "HOT-006":
        s.darkness -= 1
    elif c == "HOT-007":
        for p in s.players:
            if p.pos != START:
                if p.carried["mat"] > 0:
                    p.carried["mat"] -= 1
                else:
                    lose_any(p)
    elif c == "HOT-008":
        s.effects["minus_resource"] = 1
    elif c == "HOT-009":
        s.effects["blocked"] = 1
    elif c == "HOT-010" and s.built >= 1:
        paid = False
        for p in s.players:
            if p.carried["kristall"] > 0:
                p.carried["kristall"] -= 1
                paid = True
                break
        if not paid:
            s.darkness -= 1
    elif c == "HOT-011":
        s.effects["watch_extra"] = 1
    elif c == "HOT-012":
        draw_hot(s)

def add_res(s, p, r, n=1):
    if n > 0 and s.effects.get("minus_resource", 0) > 0:
        s.effects["minus_resource"] = 0
        n = max(0, n - 1)
    p.carried[r] += n

def draw_fynd(s, p):
    s.fynd_draws += 1
    c = s.fynd.draw(s.rng)
    need = best_resource_to_collect(s, "team_planner")
    if c == "FYN-001":
        p.carried["kristall"] += 1
    elif c == "FYN-002":
        if need == "trä":
            p.carried["trä"] += 2
        elif need in RES:
            p.carried[need] += 1
        else:
            p.carried["trä"] += 2
    elif c == "FYN-003":
        p.carried["sten"] += 2
    elif c == "FYN-004":
        p.carried["mat"] += 2
    elif c == "FYN-005":
        p.carried["trä"] += 2
    elif c == "FYN-006":
        move(p, LIGHTHOUSE); move(p, LIGHTHOUSE)
    elif c == "FYN-007":
        s.effects["ignore_hot"] = s.effects.get("ignore_hot", 0) + 1
    elif c == "FYN-008":
        # Aktuell direkt effekt: valfri resurs utom kristall.
        if need in ["trä", "sten", "mat"]:
            p.carried[need] += 1
        else:
            p.carried["sten"] += 1
    elif c == "FYN-009":
        s.effects["discount"] = s.effects.get("discount", 0) + 1
    elif c == "FYN-010":
        s.effects["mitigate_hot"] = s.effects.get("mitigate_hot", 0) + 1
    elif c == "FYN-011":
        s.base[need if need in RES else "mat"] += 1
    elif c == "FYN-012":
        s.darkness = min(START_DARKNESS[s.pc], s.darkness + 1)

def explore(s, p, strategy):
    place = loc(p.pos)
    if place == "Skog":
        add_res(s, p, "trä")
    elif place == "Berg":
        add_res(s, p, "sten")
    elif place == "Äng":
        add_res(s, p, "mat")
    elif place == "Grotta":
        if s.effects.get("cave_block", 0) > 0:
            s.effects["cave_block"] = 0
            return
        need = best_resource_to_collect(s, strategy)
        take_crystal = False
        if strategy == "crystal_rush":
            take_crystal = True
        elif strategy == "delayed_crystal":
            take_crystal = s.part_name() == "Ljuskärna"
        else:
            take_crystal = need == "kristall"
        if take_crystal:
            add_res(s, p, "kristall")
            s.cave_crystals += 1
            draw_hot(s)
        else:
            add_res(s, p, "sten")
            s.cave_stone += 1
    elif place == "Ruin":
        s.ruin_visits += 1
        draw_fynd(s, p)
    elif place == "Bas":
        if p.carried["mat"] > 0:
            s.base["mat"] += p.carried["mat"]
            p.carried["mat"] = 0
    elif place == "Fyrplats":
        build_discount(s)

def choose_target_team(s, p, strategy):
    # 1. Build if possible.
    if p.pos == LIGHTHOUSE and build_discount(s):
        p.assignment = "BUILD"
        return None

    # 2. Deliver relevant resources.
    if relevant_delivery(p, s):
        p.assignment = "DELIVER_RESOURCE"
        return LIGHTHOUSE

    # 3. If carrying food and team needs base food, deposit.
    if p.carried.get("mat", 0) > 0 and should_get_food(s, strategy):
        p.assignment = "DELIVER_FOOD"
        return START

    # 4. If stuck at lighthouse and cannot build, leave to collect.
    need = best_resource_to_collect(s, strategy)

    # 5. Emergency food.
    if should_get_food(s, strategy):
        p.assignment = "COLLECT_FOOD"
        return nearest(p.pos, MEADOW)

    # 6. Delayed crystal: ignore early crystal until core unless already carrying it.
    if strategy == "delayed_crystal" and s.part_name() != "Ljuskärna":
        if need == "kristall":
            need = None

    # 7. Opportunistic ruin.
    current_target = target_for_resource(need, s, strategy) if need else LIGHTHOUSE
    if should_visit_ruin(s, p, strategy, current_target):
        p.assignment = "VISIT_RUIN"
        return nearest(p.pos, RUIN)

    # 8. Resource collection.
    if need:
        p.assignment = f"COLLECT_{need}"
        return target_for_resource(need, s, strategy)

    # 9. If carrying any build resource, deliver anyway.
    if carrying_build_resource(p):
        p.assignment = "DELIVER_ANY_BUILD_RESOURCE"
        return LIGHTHOUSE

    # 10. No immediate need: if at lighthouse, wait/build; otherwise go useful.
    if p.pos != LIGHTHOUSE:
        p.assignment = "RALLY_LIGHTHOUSE"
        return LIGHTHOUSE
    p.assignment = "WAIT"
    return None

def choose_target_legacy(s, p, strategy):
    # Old baseline strategies kept for comparison.
    if p.pos == LIGHTHOUSE and build_discount(s):
        return None
    if relevant_delivery(p, s):
        return LIGHTHOUSE
    if strategy == "safe_night":
        if p.carried["mat"] > 0 and p.pos != START:
            return START
        if s.base["mat"] < 2:
            return nearest(p.pos, MEADOW)
    if strategy == "action_food" and p.carried["mat"] == 0 and s.rng.random() < 0.18:
        return nearest(p.pos, MEADOW)
    if strategy == "ruin_focus" and s.rng.random() < 0.35:
        return nearest(p.pos, RUIN)
    need = best_resource_to_collect(s, strategy)
    if strategy == "crystal_rush":
        return nearest(p.pos, CAVE)
    if need:
        return target_for_resource(need, s, strategy)
    if carrying_build_resource(p):
        return LIGHTHOUSE
    return LIGHTHOUSE

def take_action(s, p, strategy):
    if s.effects.get("fog", 0) > 0 and p.pos != START:
        s.effects["fog"] -= 1
        return
    if strategy in ["team_planner", "delayed_crystal", "opportunistic_ruin"]:
        target = choose_target_team(s, p, strategy)
    else:
        target = choose_target_legacy(s, p, strategy)
    if target is None:
        return
    if p.pos != target:
        if s.effects.get("blocked", 0) > 0:
            s.effects["blocked"] = 0
            p.pos = step(p.pos, target)
        else:
            move(p, target)
    else:
        explore(s, p, strategy)

def turn(s, p, strategy):
    actions = 2
    if strategy in ["action_food", "balanced", "team_planner", "delayed_crystal", "opportunistic_ruin"] and p.carried["mat"] > 0:
        # Team AI uses carried food more selectively: only when not emergency base food.
        if not should_get_food(s, strategy) or p.carried["mat"] >= 2:
            p.carried["mat"] -= 1
            actions += 1
    for _ in range(actions):
        if s.won or s.lost:
            return
        take_action(s, p, strategy)

def night(s, strategy):
    cost = 1 + (1 if s.effects.get("watch_extra", 0) > 0 else 0)
    thresholds = {
        "safe_night": 9,
        "balanced": 4,
        "action_food": 2,
        "crystal_rush": 2,
        "ruin_focus": 3,
        "team_planner": 3,
        "delayed_crystal": 3,
        "opportunistic_ruin": 3,
    }
    use = s.darkness <= thresholds.get(strategy, 0) and s.base.get("mat", 0) >= cost
    if use:
        s.base["mat"] -= cost
        s.effects["watch_extra"] = 0
    else:
        s.darkness -= 1
    if s.darkness <= 0:
        s.lost = True
        return
    draw_hot(s)
    if s.darkness <= 0:
        s.lost = True

def simulate_one(pc, strategy, seed, max_days=30):
    rng = random.Random(seed)
    s = State(
        pc=pc,
        rng=rng,
        darkness=START_DARKNESS[pc],
        base={r: 0 for r in RES},
        players=[Player() for _ in range(pc)],
        fynd=Deck.make(FYND, rng),
        hot=Deck.make(HOT, rng),
    )
    s.base["mat"] = START_FOOD[pc]
    while not s.won and not s.lost and s.day <= max_days:
        for p in s.players:
            turn(s, p, strategy)
            if s.won or s.lost:
                break
        if s.won or s.lost:
            break
        night(s, strategy)
        s.day += 1
    if not s.won and not s.lost:
        s.lost = True
    return {
        "players": pc,
        "strategy": strategy,
        "seed": seed,
        "result": "win" if s.won else "loss",
        "days": s.day,
        "darkness_end": s.darkness,
        "built_parts": s.built,
        "hot_draws": s.hot_draws,
        "fynd_draws": s.fynd_draws,
        "cave_crystals": s.cave_crystals,
        "cave_stone": s.cave_stone,
        "ruin_visits": s.ruin_visits,
        "base_food_end": s.base["mat"],
    }

def summarize(rows):
    groups = {}
    for r in rows:
        groups.setdefault((r["players"], r["strategy"]), []).append(r)
    out = []
    for (pc, strat), vals in sorted(groups.items()):
        wins = [v for v in vals if v["result"] == "win"]
        out.append({
            "players": pc,
            "strategy": strat,
            "games": len(vals),
            "win_rate": round(len(wins)/len(vals), 3),
            "avg_days": round(sum(v["days"] for v in vals)/len(vals), 2),
            "avg_days_wins": round(sum(v["days"] for v in wins)/len(wins), 2) if wins else "",
            "avg_darkness_end": round(sum(v["darkness_end"] for v in vals)/len(vals), 2),
            "avg_built_parts": round(sum(v["built_parts"] for v in vals)/len(vals), 2),
            "avg_hot_draws": round(sum(v["hot_draws"] for v in vals)/len(vals), 2),
            "avg_fynd_draws": round(sum(v["fynd_draws"] for v in vals)/len(vals), 2),
            "avg_cave_crystals": round(sum(v["cave_crystals"] for v in vals)/len(vals), 2),
            "avg_cave_stone": round(sum(v["cave_stone"] for v in vals)/len(vals), 2),
            "avg_ruin_visits": round(sum(v["ruin_visits"] for v in vals)/len(vals), 2),
        })
    return out

def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_md(path, summary):
    lines = ["# Team-AI simuleringssammanfattning\n\n"]
    lines.append("| Spelare | Strategi | Spel | Vinst% | Snittdag | Vinst-dag | Mörker slut | Fyrdelar | Hot | Fynd | Kristall från Grotta | Ruinbesök |\n")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in summary:
        lines.append(
            f"| {r['players']} | {r['strategy']} | {r['games']} | {r['win_rate']*100:.1f}% | {r['avg_days']} | "
            f"{r['avg_days_wins']} | {r['avg_darkness_end']} | {r['avg_built_parts']} | {r['avg_hot_draws']} | "
            f"{r['avg_fynd_draws']} | {r['avg_cave_crystals']} | {r['avg_ruin_visits']} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")

def sanity():
    strategies = ["team_planner", "delayed_crystal", "opportunistic_ruin"]
    rows = []
    for pc in [2, 3, 4]:
        for strat in strategies:
            for i in range(100):
                rows.append(simulate_one(pc, strat, 800000 + pc*10000 + i*31 + len(strat)))
    summ = summarize(rows)
    any_win = any(r["win_rate"] > 0 for r in summ)
    any_good_progress = any(r["avg_built_parts"] >= 2.0 for r in summ)
    print("OK: minst en teamstrategi kan vinna." if any_win else "VARNING: ingen teamstrategi vann.")
    print("OK: minst en teamstrategi når minst 2 Fyrdelar i snitt." if any_good_progress else "VARNING: svag byggprogress även med team-AI.")
    for r in summ:
        print(f"{r['players']}p {r['strategy']}: win_rate={r['win_rate']}, built={r['avg_built_parts']}, day={r['avg_days']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=500)
    ap.add_argument("--players", type=int, nargs="*", default=[2, 3, 4], choices=[2, 3, 4])
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--outdir", default="output/simulations_team_ai")
    ap.add_argument("--sanity", action="store_true")
    ap.add_argument("--strategies", nargs="*", default=[
        "team_planner", "delayed_crystal", "opportunistic_ruin",
        "balanced", "safe_night", "action_food", "crystal_rush", "ruin_focus"
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
    write_csv(out / "simulation-results-team-ai.csv", rows)
    write_csv(out / "simulation-summary-team-ai.csv", summary)
    write_md(out / "simulation-summary-team-ai.md", summary)
    print(f"Simulerade {len(rows)} spel med team-AI simulator.")
    print(f"Skrev {out / 'simulation-summary-team-ai.csv'}")
    print(f"Skrev {out / 'simulation-summary-team-ai.md'}")

if __name__ == "__main__":
    main()
