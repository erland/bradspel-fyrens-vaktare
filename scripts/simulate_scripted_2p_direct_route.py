#!/usr/bin/env python3
"""
Scripted 2p direct route sanity-check.

Syfte:
Testa om regelvarianten
- 2 spelare
- Mörker 10
- 6 mat i Basen
- Ljuskärna 2 kristaller
är spelbar när rutten spelas som en enkel, mänsklig minimiplan.

Detta är inte en generell AI. Det är ett sanity-test:
om denna vinner men Team-AI misslyckas ligger felet i Team-AI-planeringen.
"""

from __future__ import annotations
import argparse, csv, random, collections
from pathlib import Path

BOARD = [
    ["Skog","Skog","Ruin","Berg","Grotta"],
    ["Bas","Stig","Fyrplats","Stig","Grotta"],
    ["Stig","Äng","Stig","Berg","Stig"],
    ["Äng","Ruin","Äng","Stig","Skog"],
]
START=(1,0)
FYR=(1,2)
BERG=(0,3)
SKOG=(0,1)
GROTTA=(1,4)
HOT=[f"HOT-{i:03d}" for i in range(1,13)]
RES=["trä","sten","mat","kristall"]

def loc(p):
    return BOARD[p[0]][p[1]]

def neighbors(pos):
    r,c=pos
    out=[]
    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr,nc=r+dr,c+dc
        if 0<=nr<4 and 0<=nc<5:
            out.append((nr,nc))
    return out

ALL_POS=[(r,c) for r in range(4) for c in range(5)]

def reachable_one_action_raw(pos):
    if loc(pos)!="Stig":
        return neighbors(pos)
    res=set(neighbors(pos))
    for n in list(res):
        res.update(neighbors(n))
    res.discard(pos)
    return list(res)

REACH={p:reachable_one_action_raw(p) for p in ALL_POS}

def action_dist_compute(start,target):
    if start==target:
        return 0
    q=collections.deque([(start,0)])
    seen={start}
    while q:
        p,d=q.popleft()
        for n in REACH[p]:
            if n==target:
                return d+1
            if n not in seen:
                seen.add(n)
                q.append((n,d+1))
    return 99

DIST={(a,b):action_dist_compute(a,b) for a in ALL_POS for b in ALL_POS}
MOVE={(a,b):(a if a==b else min(REACH[a], key=lambda n: DIST[(n,b)])) for a in ALL_POS for b in ALL_POS}

class Deck:
    def __init__(self, rng):
        self.rng=rng
        self.draw=HOT[:]
        rng.shuffle(self.draw)
        self.discard=[]
    def card(self):
        if not self.draw:
            self.draw=self.discard[:]
            self.discard=[]
            self.rng.shuffle(self.draw)
        c=self.draw.pop(0)
        self.discard.append(c)
        return c

def lose_any(carried):
    for r in ["kristall","sten","trä","mat"]:
        if carried[r]>0:
            carried[r]-=1
            return r
    return None

def simulate(seed=1, start_darkness=10, start_food=6, core_cost=2, policy="save_food", trace=False):
    rng=random.Random(seed)
    deck=Deck(rng)
    players=[
        {"pos":START, "carried":{r:0 for r in RES}},
        {"pos":START, "carried":{r:0 for r in RES}},
    ]
    base={"mat":start_food}
    darkness=start_darkness
    built=0
    day=1
    effects={"cave_block":0,"minus_resource":0,"blocked":0,"fog":0,"watch_extra":0}
    log=[]

    # Optional opening tempo food. The best sanity route usually saves food for Nattvakt.
    if policy=="one_food_each":
        for p in players:
            if base["mat"]>0:
                base["mat"]-=1
                p["carried"]["mat"]+=1

    def L(s):
        if trace:
            log.append(s)

    def at_fyr():
        t={r:0 for r in RES}
        for p in players:
            if p["pos"]==FYR:
                for r,n in p["carried"].items():
                    t[r]+=n
        return t

    def cost():
        if built==0:
            return {"sten":3}
        if built==1:
            return {"trä":3,"sten":2}
        if built==2:
            return {"kristall":core_cost}
        return {}

    def can_build():
        t=at_fyr()
        return built<3 and all(t.get(r,0)>=n for r,n in cost().items())

    def pay_resource(r,n):
        rem=n
        for p in players:
            if p["pos"]==FYR:
                take=min(rem,p["carried"][r])
                p["carried"][r]-=take
                rem-=take
                if rem<=0:
                    break
        return rem==0

    def build():
        nonlocal built
        if not can_build():
            return False
        for r,n in cost().items():
            if not pay_resource(r,n):
                raise RuntimeError("pay mismatch")
        built+=1
        L(f"Dag {day}: BYGGER del {built}")
        return True

    def draw_hot(source):
        nonlocal darkness
        c=deck.card()
        L(f"Dag {day}: Hot från {source}: {c}")
        if c=="HOT-001":
            for p in players:
                if loc(p["pos"])=="Skog":
                    lose_any(p["carried"])
        elif c=="HOT-002":
            effects["cave_block"]=1
        elif c=="HOT-003":
            if base["mat"]>0:
                base["mat"]-=1
            else:
                darkness-=1
        elif c=="HOT-004":
            effects["fog"]=sum(1 for p in players if p["pos"]!=START)
        elif c=="HOT-005":
            for p in players:
                if loc(p["pos"])=="Berg" and p["carried"]["sten"]>0:
                    p["carried"]["sten"]-=1
        elif c=="HOT-006":
            darkness-=1
        elif c=="HOT-007":
            for p in players:
                if p["pos"]!=START:
                    if p["carried"]["mat"]>0:
                        p["carried"]["mat"]-=1
                    else:
                        lose_any(p["carried"])
        elif c=="HOT-008":
            effects["minus_resource"]=1
        elif c=="HOT-009":
            effects["blocked"]=1
        elif c=="HOT-010" and built>=1:
            paid=False
            for p in players:
                if p["carried"]["kristall"]>0:
                    p["carried"]["kristall"]-=1
                    paid=True
                    break
            if not paid:
                darkness-=1
        elif c=="HOT-011":
            effects["watch_extra"]=1
        elif c=="HOT-012":
            draw_hot("Mörkervåg")

    def add_res(p,r):
        n=1
        if effects["minus_resource"]:
            effects["minus_resource"]=0
            n=0
        p["carried"][r]+=n

    def total_carried(r):
        return sum(p["carried"][r] for p in players)

    def target_for(pi):
        p=players[pi]
        if can_build():
            return FYR

        # Phase 1: Grund.
        if built==0:
            if p["carried"]["sten"]>0 and total_carried("sten")>=3:
                return FYR
            if p["carried"]["sten"]>=2:
                return FYR
            return BERG

        # Phase 2: Torn. P1 wood, P2 stone.
        if built==1:
            if pi==0:
                return FYR if p["carried"]["trä"]>=3 else SKOG
            return FYR if p["carried"]["sten"]>=2 else BERG

        # Phase 3: Ljuskärna. Need core_cost crystals total at Fyrplatsen.
        if built==2:
            if p["carried"]["kristall"]>0 and total_carried("kristall")>=core_cost:
                return FYR
            if p["carried"]["kristall"]>=core_cost:
                return FYR
            return GROTTA

        return FYR

    def action(pi):
        p=players[pi]
        if effects["fog"]>0 and p["pos"]!=START:
            effects["fog"]-=1
            L(f"Dag {day} P{pi+1}: dimma, handling förlorad")
            return

        target=target_for(pi)
        if p["pos"]!=target:
            if effects["blocked"]>0:
                effects["blocked"]=0
                p["pos"]=min(neighbors(p["pos"]), key=lambda n: DIST[(n,target)])
                L(f"Dag {day} P{pi+1}: blockerad flytt till {loc(p['pos'])}")
            else:
                old=p["pos"]
                p["pos"]=MOVE[(p["pos"], target)]
                L(f"Dag {day} P{pi+1}: flyttar {loc(old)}->{loc(p['pos'])}")
            return

        place=loc(p["pos"])
        if place=="Fyrplats":
            if not build():
                L(f"Dag {day} P{pi+1}: står på Fyrplatsen, kan inte bygga")
        elif place=="Berg":
            add_res(p,"sten")
            L(f"Dag {day} P{pi+1}: Berg +sten ({p['carried']['sten']})")
        elif place=="Skog":
            add_res(p,"trä")
            L(f"Dag {day} P{pi+1}: Skog +trä ({p['carried']['trä']})")
        elif place=="Grotta":
            if effects["cave_block"]>0:
                effects["cave_block"]=0
                L(f"Dag {day} P{pi+1}: Grotta blockerad")
            else:
                add_res(p,"kristall")
                L(f"Dag {day} P{pi+1}: Grotta +kristall ({p['carried']['kristall']})")
                draw_hot("Grotta")
        else:
            L(f"Dag {day} P{pi+1}: väntar på {place}")

    while day<=24 and built<3 and darkness>0:
        L(f"--- Dag {day}, Mörker {darkness}, Basmat {base['mat']}, byggt {built} ---")
        for pi in [0,1]:
            actions=2
            p=players[pi]
            if p["carried"]["mat"]>0 and policy in ["one_food_each"]:
                if day<=2 or loc(p["pos"]) in ["Berg","Skog","Grotta"] or DIST[(p["pos"], target_for(pi))]==1:
                    p["carried"]["mat"]-=1
                    actions+=1
                    L(f"Dag {day} P{pi+1}: äter mat för +1 handling")
            for _ in range(actions):
                if built>=3 or darkness<=0:
                    break
                action(pi)

        if built>=3:
            break

        cost_watch=1+(1 if effects["watch_extra"] else 0)
        if darkness<=4 and base["mat"]>=cost_watch:
            base["mat"]-=cost_watch
            effects["watch_extra"]=0
            L(f"Natt {day}: Nattvakt {cost_watch}, Mörker {darkness}")
        else:
            old=darkness
            darkness-=1
            L(f"Natt {day}: Mörker {old}->{darkness}")
        if darkness<=0:
            break
        draw_hot("Natt")
        day+=1

    return {
        "seed":seed,
        "policy":policy,
        "result":"win" if built>=3 and darkness>0 else "loss",
        "day":day,
        "built":built,
        "darkness":darkness,
        "base_food":base["mat"],
        "log":log if trace else None,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=5000)
    ap.add_argument("--seed", type=int, default=20260810)
    ap.add_argument("--policy", choices=["save_food","one_food_each"], default="save_food")
    ap.add_argument("--outdir", default="output/scripted_2p_direct_route")
    ap.add_argument("--trace-seed", type=int, default=None)
    args=ap.parse_args()

    out=Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    rows=[]
    for i in range(args.games):
        seed=args.seed+i
        r=simulate(seed, policy=args.policy)
        rows.append({k:v for k,v in r.items() if k!="log"})

    csv_path=out/"scripted-2p-direct-route-results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    wins=[r for r in rows if r["result"]=="win"]
    win_rate=len(wins)/len(rows)
    avg_day=sum(r["day"] for r in wins)/len(wins) if wins else None
    avg_darkness=sum(r["darkness"] for r in wins)/len(wins) if wins else None
    avg_built=sum(r["built"] for r in rows)/len(rows)
    built2plus=sum(1 for r in rows if r["built"]>=2)/len(rows)

    md=[
        "# Scripted 2p direct route – resultat\n\n",
        "Regler: 2p, Mörker 10, 6 mat, Ljuskärna 2, inga Basbygge-resurser.\n\n",
        f"- Spel: **{args.games}**\n",
        f"- Policy: **{args.policy}**\n",
        f"- Vinstgrad: **{win_rate*100:.2f}%**\n",
        f"- Snitt byggda delar: **{avg_built:.2f}**\n",
        f"- Nådde minst 2 delar: **{built2plus*100:.2f}%**\n",
        f"- Snittdag vid vinst: **{avg_day:.2f}**\n" if avg_day is not None else "- Snittdag vid vinst: **-**\n",
        f"- Snitt-Mörker kvar vid vinst: **{avg_darkness:.2f}**\n" if avg_darkness is not None else "- Snitt-Mörker kvar vid vinst: **-**\n",
    ]
    md_path=out/"scripted-2p-direct-route-summary.md"
    md_path.write_text("".join(md), encoding="utf-8")

    # Trace example: first win and first loss with 2+ parts, unless user gives seed.
    trace_seeds=[]
    if args.trace_seed is not None:
        trace_seeds.append(args.trace_seed)
    else:
        for r in rows:
            if r["result"]=="win":
                trace_seeds.append(r["seed"])
                break
        for r in rows:
            if r["result"]=="loss" and r["built"]>=2:
                trace_seeds.append(r["seed"])
                break

    for seed in trace_seeds:
        tr=simulate(seed, policy=args.policy, trace=True)
        kind=tr["result"]
        p=out/f"trace-scripted-2p-{kind}-seed{seed}.md"
        p.write_text(f"# Trace scripted 2p – {kind}, seed {seed}\n\n"+"\n".join(f"- {line}" for line in tr["log"]), encoding="utf-8")

    print(f"Skrev {csv_path}")
    print(f"Skrev {md_path}")
    print(f"Vinstgrad: {win_rate*100:.2f}%")
    print(f"Snitt byggda delar: {avg_built:.2f}")
    print(f"Nådde minst 2 delar: {built2plus*100:.2f}%")

if __name__=="__main__":
    main()
