# 1편 1장 보강 — 미로를 상태공간 그래프로 바꾸고 BFS·DFS로 길 찾기
import random, json
from collections import deque
W, H = 8, 6
def make_maze(seed):
    rnd = random.Random(seed)
    open_ = {(x, y): set() for x in range(W) for y in range(H)}
    stack, seen = [(0, 0)], {(0, 0)}
    while stack:
        x, y = stack[-1]
        nb = [(x+dx, y+dy) for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] if 0 <= x+dx < W and 0 <= y+dy < H and (x+dx, y+dy) not in seen]
        if not nb: stack.pop(); continue
        n = rnd.choice(nb); open_[(x, y)].add(n); open_[n].add((x, y)); seen.add(n); stack.append(n)
    # 벽 몇 개를 더 허물어 고리(여러 갈래 길)를 만든다
    walls = [((x, y), (x+1, y)) for x in range(W-1) for y in range(H) if (x+1, y) not in open_[(x, y)]] + \
            [((x, y), (x, y+1)) for x in range(W) for y in range(H-1) if (x, y+1) not in open_[(x, y)]]
    for a, b in rnd.sample(walls, 6): open_[a].add(b); open_[b].add(a)
    return open_
START, GOAL = (0, 0), (W-1, H-1)

def to_graph(open_):
    """갈림길·막다른 곳·출발·출구만 '상태'로 남기고, 그 사이 통로를 '연결선'으로"""
    nodes = [c for c in open_ if len(open_[c]) != 2 or c in (START, GOAL)]
    ns, edges = set(nodes), {}
    for n in nodes:
        for nxt in open_[n]:
            path, prev, cur = [n, nxt], n, nxt
            while cur not in ns:
                cur2 = [c for c in open_[cur] if c != prev][0]; prev, cur = cur, cur2; path.append(cur)
            key = tuple(sorted([n, cur]))
            if key not in edges or len(path) < len(edges[key]): edges[key] = path
    return nodes, edges

def search(nodes, edges, kind):
    adj = {n: [] for n in nodes}
    for (a, b), p in edges.items(): adj[a].append((b, len(p)-1)); adj[b].append((a, len(p)-1))
    for n in adj: adj[n].sort(key=lambda t: (t[0][1], t[0][0]))      # 위→아래, 왼→오른 순서로 살핌
    frontier, parent, order = deque([START]), {START: None}, []
    while frontier:
        n = frontier.popleft() if kind == "BFS" else frontier.pop()
        if n in order: continue
        order.append(n)
        if n == GOAL: break
        nbrs = adj[n] if kind == "BFS" else list(reversed(adj[n]))
        for m, _ in nbrs:
            if m not in order and (kind == "DFS" or m not in parent):
                if kind == "DFS" or m not in parent: parent.setdefault(m, n) if kind == "BFS" else parent.__setitem__(m, n)
                frontier.append(m)
    path, n = [], GOAL
    while n is not None: path.append(n); n = parent[n]
    path = path[::-1]
    cells = sum(len(edges[tuple(sorted([a, b]))]) - 1 for a, b in zip(path, path[1:]))
    return order, path, cells

if __name__ == "__main__":
    for seed in range(40):
        mz = make_maze(seed); nodes, edges = to_graph(mz)
        b = search(nodes, edges, "BFS"); d = search(nodes, edges, "DFS")
        if d[2] > b[2] and len(nodes) <= 26:
            print(f"seed {seed}: 상태 {len(nodes)}개, 연결선 {len(edges)}개 | BFS 방문 {len(b[0])}, 경로 {b[2]}칸({len(b[1])-1}구간) | DFS 방문 {len(d[0])}, 경로 {d[2]}칸")
