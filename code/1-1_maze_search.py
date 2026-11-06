import json, heapq, sys
import importlib.util, os
_spec = importlib.util.spec_from_file_location('maze', os.path.join(os.path.dirname(__file__), '1-1_maze_graph.py'))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
make_maze, to_graph, START, GOAL, W, H = _m.make_maze, _m.to_graph, _m.START, _m.GOAL, _m.W, _m.H
# make_maze, to_graph, START, GOAL, W, H
def adjacency(nodes, edges):
    adj = {n: [] for n in nodes}
    for (a, b), p in edges.items(): adj[a].append((b, len(p)-1)); adj[b].append((a, len(p)-1))
    for n in adj: adj[n].sort(key=lambda t: (t[0][1], t[0][0]))
    return adj
def bfs(adj):
    q, parent, order = [START], {START: None}, []
    while q:
        n = q.pop(0); order.append(n)
        if n == GOAL: break
        for m, _ in adj[n]:
            if m not in parent: parent[m] = n; q.append(m)
    return order, parent
def dfs(adj):
    st, parent, order = [START], {START: None}, []
    while st:
        n = st.pop()
        if n in order: continue
        order.append(n)
        if n == GOAL: break
        for m, _ in reversed(adj[n]):
            if m not in order: parent[m] = n; st.append(m)
    return order, parent
def dijkstra(adj):
    dist, parent, pq, order = {START: 0}, {START: None}, [(0, START)], []
    while pq:
        d, n = heapq.heappop(pq)
        if n in order: continue
        order.append(n)
        if n == GOAL: break
        for m, w in adj[n]:
            if d + w < dist.get(m, 1e9): dist[m] = d + w; parent[m] = n; heapq.heappush(pq, (d + w, m))
    return order, parent
def path_of(parent):
    p, n = [], GOAL
    while n is not None: p.append(n); n = parent[n]
    return p[::-1]
def cells(edges, p): return sum(len(edges[tuple(sorted([a, b]))]) - 1 for a, b in zip(p, p[1:]))
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 14
mz = make_maze(seed); nodes, edges = to_graph(mz); adj = adjacency(nodes, edges)
res = {}
for name, f in [("BFS", bfs), ("DFS", dfs), ("다익스트라", dijkstra)]:
    o, par = f(adj); p = path_of(par); res[name] = (o, p)
    print(f"{name:6s} 방문 {len(o):2d}/{len(nodes)}개 상태, 경로 {len(p)-1}구간 {cells(edges, p)}칸")
if len(sys.argv) > 2:
    idx = {n: i for i, n in enumerate(sorted(nodes, key=lambda c: (c[1], c[0])))}
    D = {"W": W, "H": H, "open": [[x, y, [[a, b] for a, b in sorted(mz[(x, y)])]] for (x, y) in sorted(mz)],
         "nodes": [[x, y] for (x, y) in sorted(nodes, key=lambda c: (c[1], c[0]))],
         "edges": [[idx[a], idx[b], [[x, y] for x, y in p]] for (a, b), p in edges.items()],
         "runs": {k: {"order": [idx[n] for n in o], "path": [idx[n] for n in p], "cells": cells(edges, p)} for k, (o, p) in res.items()}}
    json.dump(D, open(sys.argv[2], "w"), ensure_ascii=False)
