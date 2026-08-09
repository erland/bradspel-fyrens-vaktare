#!/usr/bin/env python3
"""
Full Team-AI-motor för Fyrens väktare v0.7.0.

Det här är den första simulatorn i projektet som har en faktisk uppdragsmotor
med målantal, reserverade resurser och fasbaserad byggplan.

Strategier:
- mission_direct_build
- mission_team_planner
- mission_delayed_crystal
- mission_opportunistic_ruin

Kör:
  python scripts/simulate_team_ai_full.py --games 1000 --players 2 3 4 --seed 20260711 --sanity
"""

from __future__ import annotations
import argparse, csv, random
from dataclasses import dataclass, field
from pathlib import Path
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
    def make(cls, cards: List[str], rng: random.Random) -> "Deck":
        pile = cards[:]
        rng.shuffle(pile)
        return cls(pile)

    def draw(self, rng: random.Random) -> str:
        if not self.draw_pile:
            self.draw_pile = self.discard[:]
            self.discard = []
            rng.shuffle(self.draw_pile)
        card = self.draw_pile.pop(0)
        self.discard.append(card)
        return card


@dataclass
class Mission:
    kind: str = "IDLE"
    resource: Optional[str] = None
    amount: int = 0
    target: Optional[Tuple[int, int]] = None

    def is_collect(self) -> bool:
        return self.kind == "COLLECT"

    def is_deliver(self) -> bool:
        return self.kind == "DELIVER"


@dataclass
class Player:
    pos: Tuple[int, int] = START
    carried: Dict[str, int] = field(default_factory=lambda: {r: 0 for r in RES})
    mission: Mission = field(default_factory=Mission)


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
    build_actions: int = 0
    effects: Dict[str, int] = field(default_factory=dict)

    def current_part(self) -> str:
        return BUILD[self.built][0] if self.built < len(BUILD) else "Klar"

    def current_cost(self) -> Dict[str, int]:
        return BUILD[self.built][1] if self.built < len(BUILD) else {}

    def at_fyr(self) -> Dict[str, int]:
        total = {r: 0 for r in RES}
        for p in self.players:
            if p.pos == LIGHTHOUSE:
                for r, n in p.carried.items():
                    total[r] += n
        return total

    def carried_team(self) -> Dict[str, int]:
        total = {r: 0 for r in RES}
        for p in self.players:
            for r, n in p.carried.items():
                total[r] += n
        return total


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

def targets_for(res):
    if res == "trä": return WOOD
    # Grotta can also give sten. This makes early Grund/Torn routing less brittle.
    if res == "sten": return STONE + CAVE
    if res == "kristall": return CAVE
    if res == "mat": return MEADOW
    return [LIGHTHOUSE]

def can_build(s: State) -> bool:
    a = s.at_fyr()
    return bool(s.current_cost()) and all(a.get(r,0) >= n for r,n in s.current_cost().items())

def build(s: State) -> bool:
    if not can_build(s):
        return False
    for r, n in s.current_cost().items():
        rem = n
        for p in s.players:
            if p.pos == LIGHTHOUSE:
                take = min(rem, p.carried.get(r,0))
                p.carried[r] -= take
                rem -= take
                if rem <= 0:
                    break
    s.built += 1
    s.build_actions += 1
    for p in s.players:
        p.mission = Mission()
    if s.built >= len(BUILD):
        s.won = True
    return True

def build_with_discount(s: State) -> bool:
    if build(s):
        return True
    if s.effects.get("discount", 0) <= 0 or not s.current_cost():
        return False
    a = s.at_fyr()
    missing = sum(max(0, n - a.get(r,0)) for r,n in s.current_cost().items())
    if missing == 1:
        for r, n in s.current_cost().items():
            rem = min(n, a.get(r,0))
            for p in s.players:
                if p.pos == LIGHTHOUSE:
                    take = min(rem, p.carried.get(r,0))
                    p.carried[r] -= take
                    rem -= take
                    if rem <= 0:
                        break
        s.effects["discount"] -= 1
        s.built += 1
        s.build_actions += 1
        for p in s.players:
            p.mission = Mission()
        if s.built >= len(BUILD):
            s.won = True
        return True
    return False

def delivery_need(s: State) -> Dict[str, int]:
    at = s.at_fyr()
    return {r: max(0, n - at.get(r,0)) for r,n in s.current_cost().items() if max(0, n - at.get(r,0)) > 0}

def reserved_collect(s: State) -> Dict[str, int]:
    total = {r: 0 for r in RES}
    for p in s.players:
        if p.mission.kind in ["COLLECT", "DELIVER"] and p.mission.resource:
            # Delivered/assigned resources are counted only up to mission amount.
            if p.mission.kind == "DELIVER":
                total[p.mission.resource] += p.carried.get(p.mission.resource, 0)
            else:
                total[p.mission.resource] += max(0, p.mission.amount)
    return total

def missing_after_reserved(s: State) -> Dict[str, int]:
    need = delivery_need(s)
    reserved = reserved_collect(s)
    return {r: max(0, n - reserved.get(r,0)) for r,n in need.items() if max(0, n - reserved.get(r,0)) > 0}

def useful_carried_resource(p: Player, s: State) -> Optional[str]:
    need = delivery_need(s)
    for r in ["kristall", "sten", "trä"]:
        if p.carried.get(r,0) > 0 and need.get(r,0) > 0:
            return r
    return None

def carrying_build(p: Player) -> bool:
    return any(p.carried.get(r,0) > 0 for r in ["trä","sten","kristall"])

def can_help_by_collecting_more_from_lighthouse(p: Player, s: State) -> Optional[str]:
    """
    If a player is already at Fyrplatsen with a useful resource but the team
    still cannot build, standing there and repeatedly using Fyrplatsen wastes
    actions. Let that player go back out and collect one more missing resource.
    """
    if p.pos != LIGHTHOUSE or can_build(s):
        return None
    need = delivery_need(s)
    if not need:
        return None
    # Prefer a resource the player already carries and that is still missing.
    for r in ["sten", "trä", "kristall"]:
        if p.carried.get(r, 0) > 0 and need.get(r, 0) > 0:
            return r
    # Otherwise collect the largest remaining need.
    return max(need.items(), key=lambda x: x[1])[0]

def lose_any(p: Player):
    for r in ["kristall","sten","trä","mat"]:
        if p.carried.get(r,0) > 0:
            p.carried[r] -= 1
            return

def draw_hot(s: State):
    if s.effects.get("ignore_hot",0) > 0:
        s.effects["ignore_hot"] -= 1
        return
    if s.effects.get("mitigate_hot",0) > 0 and s.rng.random() < 0.5:
        s.effects["mitigate_hot"] -= 1
        return

    s.hot_draws += 1
    c = s.hot.draw(s.rng)
    if c == "HOT-001":
        for p in s.players:
            if loc(p.pos) == "Skog": lose_any(p)
    elif c == "HOT-002":
        s.effects["cave_block"] = 1
    elif c == "HOT-003":
        if s.base.get("mat",0) > 0: s.base["mat"] -= 1
        else: s.darkness -= 1
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
                if p.carried["mat"] > 0: p.carried["mat"] -= 1
                else: lose_any(p)
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
        if not paid: s.darkness -= 1
    elif c == "HOT-011":
        s.effects["watch_extra"] = 1
    elif c == "HOT-012":
        draw_hot(s)

def add_res(s: State, p: Player, r: str, n: int = 1):
    if n > 0 and s.effects.get("minus_resource",0) > 0:
        s.effects["minus_resource"] = 0
        n = max(0, n-1)
    p.carried[r] += n

def best_fynd_resource(s: State):
    miss = missing_after_reserved(s)
    if miss:
        return max(miss.items(), key=lambda x: x[1])[0]
    need = delivery_need(s)
    if need:
        return max(need.items(), key=lambda x: x[1])[0]
    return "sten"

def draw_fynd(s: State, p: Player):
    s.fynd_draws += 1
    c = s.fynd.draw(s.rng)
    need = best_fynd_resource(s)
    if c == "FYN-001":
        p.carried["kristall"] += 1
    elif c == "FYN-002":
        if need == "trä": p.carried["trä"] += 2
        elif need in RES: p.carried[need] += 1
        else: p.carried["trä"] += 2
    elif c == "FYN-003":
        p.carried["sten"] += 2
    elif c == "FYN-004":
        p.carried["mat"] += 2
    elif c == "FYN-005":
        p.carried["trä"] += 2
    elif c == "FYN-006":
        move(p, LIGHTHOUSE); move(p, LIGHTHOUSE)
    elif c == "FYN-007":
        s.effects["ignore_hot"] = s.effects.get("ignore_hot",0) + 1
    elif c == "FYN-008":
        p.carried[need if need in ["trä","sten","mat"] else "sten"] += 1
    elif c == "FYN-009":
        s.effects["discount"] = s.effects.get("discount",0) + 1
    elif c == "FYN-010":
        s.effects["mitigate_hot"] = s.effects.get("mitigate_hot",0) + 1
    elif c == "FYN-011":
        s.base[need if need in RES else "mat"] += 1
    elif c == "FYN-012":
        s.darkness = min(START_DARKNESS[s.pc], s.darkness + 1)

def explore(s: State, p: Player, strategy: str):
    place = loc(p.pos)
    if place == "Skog":
        add_res(s, p, "trä")
    elif place == "Berg":
        add_res(s, p, "sten")
    elif place == "Äng":
        add_res(s, p, "mat")
    elif place == "Grotta":
        if s.effects.get("cave_block",0) > 0:
            s.effects["cave_block"] = 0
            return
        take_crystal = s.current_part() == "Ljuskärna"
        if strategy == "mission_crystal_rush":
            take_crystal = True
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
        build_with_discount(s)

def target_for_resource(s: State, p: Player, r: str):
    # Choose nearest good location for this player, not global team.
    return nearest(p.pos, targets_for(r))

def assign_missions(s: State, strategy: str):
    # Reset invalid missions after build changes or if complete.
    for p in s.players:
        if p.mission.kind == "COLLECT" and p.mission.resource and p.carried.get(p.mission.resource,0) >= p.mission.amount:
            p.mission = Mission("DELIVER", p.mission.resource, p.carried[p.mission.resource], LIGHTHOUSE)
        if p.mission.kind == "DELIVER" and (not useful_carried_resource(p, s) or (p.pos == LIGHTHOUSE and not can_build(s))):
            p.mission = Mission()

    # Build priority.
    if can_build(s):
        closest = min(s.players, key=lambda p: dist(p.pos, LIGHTHOUSE))
        closest.mission = Mission("BUILD", target=LIGHTHOUSE)
        return

    # If a player is already on Fyrplatsen with partial resources and cannot
    # build, do not let them waste actions on Fyrplatsen. Send them to collect
    # one more missing resource.
    for p in s.players:
        r_more = can_help_by_collecting_more_from_lighthouse(p, s)
        if r_more and p.mission.kind not in ["COLLECT"]:
            p.mission = Mission("COLLECT", r_more, p.carried.get(r_more, 0) + 1, target_for_resource(s, p, r_more))

    # Deliver useful carried resources, but not for players already standing
    # on Fyrplatsen unless the build is possible.
    for p in s.players:
        if p.pos == LIGHTHOUSE:
            continue
        r = useful_carried_resource(p, s)
        if r:
            p.mission = Mission("DELIVER", r, p.carried[r], LIGHTHOUSE)

    # Food emergency.
    if strategy in ["mission_team_planner", "mission_opportunistic_ruin"] and s.darkness <= 4 and s.base.get("mat",0) == 0:
        candidates = [p for p in s.players if p.mission.kind in ["IDLE", ""] and not carrying_build(p)]
        if candidates:
            p = min(candidates, key=lambda x: dist(x.pos, nearest(x.pos, MEADOW)))
            p.mission = Mission("COLLECT", "mat", 1, nearest(p.pos, MEADOW))

    # Assign missing resources with target amounts.
    miss = missing_after_reserved(s)
    # Direct build and delayed crystal don't chase crystal before core due BUILD order anyway.
    for r, amount in sorted(miss.items(), key=lambda x: -x[1]):
        remaining = amount
        while remaining > 0:
            candidates = [p for p in s.players if p.mission.kind in ["IDLE", ""] and not carrying_build(p)]
            if not candidates:
                break
            p = min(candidates, key=lambda x: dist(x.pos, target_for_resource(s, x, r)))
            bundle = 1 if r == "kristall" else min(2, remaining)
            p.mission = Mission("COLLECT", r, bundle, target_for_resource(s, p, r))
            remaining -= bundle

    # Opportunistic ruin only when it does not block urgent build/delivery.
    if strategy == "mission_opportunistic_ruin" and s.darkness >= 4 and s.current_part() != "Ljuskärna" and not can_build(s):
        if not missing_after_reserved(s):
            candidates = [p for p in s.players if p.mission.kind in ["IDLE", ""] and not carrying_build(p)]
        else:
            candidates = []
        if candidates:
            p = min(candidates, key=lambda x: dist(x.pos, nearest(x.pos, RUIN)))
            if dist(p.pos, nearest(p.pos, RUIN)) <= 1:
                p.mission = Mission("RUIN", target=nearest(p.pos, RUIN))

    # Position idle players for the current/future phase.
    for p in s.players:
        if p.mission.kind in ["IDLE", ""]:
            if carrying_build(p):
                p.mission = Mission("DELIVER", None, 0, LIGHTHOUSE)
            elif s.current_part() == "Grund":
                p.mission = Mission("POSITION", "sten", 0, target_for_resource(s, p, "sten"))
            elif s.current_part() == "Torn":
                # Split idle players between wood and stone.
                res = "trä" if s.rng.random() < 0.6 else "sten"
                p.mission = Mission("POSITION", res, 0, target_for_resource(s, p, res))
            else:
                p.mission = Mission("POSITION", "kristall", 0, target_for_resource(s, p, "kristall"))

def mission_target(s: State, p: Player, strategy: str) -> Optional[Tuple[int,int]]:
    if p.pos == LIGHTHOUSE and build_with_discount(s):
        return None
    if can_build(s):
        return LIGHTHOUSE

    assign_missions(s, strategy)
    m = p.mission
    if m.kind == "BUILD":
        return LIGHTHOUSE
    if m.kind == "DELIVER":
        return LIGHTHOUSE
    if m.kind in ["COLLECT", "POSITION", "RUIN"]:
        return m.target
    return LIGHTHOUSE

def should_use_food(s: State, p: Player, strategy: str) -> bool:
    if p.carried["mat"] <= 0:
        return False
    # Preserve food if base is empty and darkness is low unless this wins/finishes delivery.
    if s.darkness <= 4 and s.base.get("mat",0) == 0 and p.mission.kind != "DELIVER":
        return False
    if can_build(s) and dist(p.pos, LIGHTHOUSE) <= 2:
        return True
    if p.mission.kind == "DELIVER" and dist(p.pos, LIGHTHOUSE) <= 2:
        return True
    if p.mission.kind == "COLLECT" and p.pos == p.mission.target:
        return True
    if s.darkness >= 5 and p.mission.kind in ["COLLECT", "DELIVER"]:
        return True
    return False

def take_action(s: State, p: Player, strategy: str):
    if s.effects.get("fog",0) > 0 and p.pos != START:
        s.effects["fog"] -= 1
        return
    target = mission_target(s, p, strategy)
    if target is None:
        return
    if p.pos != target:
        if s.effects.get("blocked",0) > 0:
            s.effects["blocked"] = 0
            p.pos = step(p.pos, target)
        else:
            move(p, target)
    else:
        explore(s, p, strategy)
        # Convert collect to deliver when amount reached.
        if p.mission.kind == "COLLECT" and p.mission.resource and p.carried.get(p.mission.resource,0) >= p.mission.amount:
            p.mission = Mission("DELIVER", p.mission.resource, p.carried[p.mission.resource], LIGHTHOUSE)

def turn(s: State, p: Player, strategy: str):
    assign_missions(s, strategy)
    actions = 2
    if should_use_food(s, p, strategy):
        p.carried["mat"] -= 1
        actions += 1
    for _ in range(actions):
        if s.won or s.lost:
            return
        take_action(s, p, strategy)

def night(s: State, strategy: str):
    cost = 1 + (1 if s.effects.get("watch_extra",0) > 0 else 0)
    threshold = 3
    if strategy == "mission_direct_build":
        threshold = 2
    use = s.darkness <= threshold and s.base.get("mat",0) >= cost
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

def simulate_one(pc: int, strategy: str, seed: int, max_days: int = 30) -> Dict[str, object]:
    rng = random.Random(seed)
    s = State(
        pc=pc,
        rng=rng,
        darkness=START_DARKNESS[pc],
        base={r:0 for r in RES},
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
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_md(path, summary):
    lines = ["# Full Team-AI simuleringssammanfattning\n\n"]
    lines.append("| Spelare | Strategi | Spel | Vinst% | Snittdag | Vinst-dag | Mörker slut | Fyrdelar | Hot | Fynd | Grottkristaller | Ruinbesök |\n")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
    for r in summary:
        lines.append(
            f"| {r['players']} | {r['strategy']} | {r['games']} | {r['win_rate']*100:.1f}% | {r['avg_days']} | "
            f"{r['avg_days_wins']} | {r['avg_darkness_end']} | {r['avg_built_parts']} | {r['avg_hot_draws']} | "
            f"{r['avg_fynd_draws']} | {r['avg_cave_crystals']} | {r['avg_ruin_visits']} |\n"
        )
    path.write_text("".join(lines), encoding="utf-8")

def sanity():
    rows = []
    for pc in [2,3,4]:
        for strat in ["mission_direct_build", "mission_team_planner", "mission_opportunistic_ruin"]:
            for i in range(60):
                rows.append(simulate_one(pc, strat, 990000 + pc*1000 + i*23 + len(strat)))
    summ = summarize(rows)
    any_win = any(r["win_rate"] > 0 for r in summ)
    any_progress = any(r["avg_built_parts"] >= 2.0 for r in summ)
    print("OK: minst en full-mission-strategi kan vinna." if any_win else "VARNING: ingen full-mission-strategi vann.")
    print("OK: minst en full-mission-strategi når minst 2 Fyrdelar i snitt." if any_progress else "VARNING: svag byggprogress i full mission.")
    for r in summ:
        print(f"{r['players']}p {r['strategy']}: win_rate={r['win_rate']}, built={r['avg_built_parts']}, day={r['avg_days']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=500)
    ap.add_argument("--players", type=int, nargs="*", default=[2,3,4], choices=[2,3,4])
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--outdir", default="output/simulations_team_ai_full")
    ap.add_argument("--sanity", action="store_true")
    ap.add_argument("--strategies", nargs="*", default=[
        "mission_direct_build", "mission_team_planner", "mission_delayed_crystal", "mission_opportunistic_ruin"
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
    write_csv(out / "simulation-results-team-ai-full.csv", rows)
    write_csv(out / "simulation-summary-team-ai-full.csv", summary)
    write_md(out / "simulation-summary-team-ai-full.md", summary)
    print(f"Simulerade {len(rows)} spel med full Team-AI.")
    print(f"Skrev {out / 'simulation-summary-team-ai-full.csv'}")
    print(f"Skrev {out / 'simulation-summary-team-ai-full.md'}")

if __name__ == "__main__":
    main()
