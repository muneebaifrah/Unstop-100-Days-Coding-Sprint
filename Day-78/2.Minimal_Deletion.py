# Python 3

import heapq

def user_logic(n, m, edges):
    """
    Maximum number of routes (edges) that can be deleted while preserving
    all-pairs shortest path distances.

    An edge (u,v,w) is deletable if:
      - dist(u,v) < w  (edge is never on a shortest path), OR
      - dist(u,v) == w AND there are at least 2 distinct shortest paths from u to v
        (so removing this edge still keeps a shortest u-v path of length w).

    We compute this by running Dijkstra from each node u and tracking:
      - shortest distance to its "target neighbors" v (those with edge (u,v))
      - number of shortest paths to v (capped at 2)
    """
    # Build adjacency list
    g = [[] for _ in range(n + 1)]
    for (u, v, w) in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    # For each source u, store only edges (u -> v) with u < v to count once
    targets = [[] for _ in range(n + 1)]
    for idx, (u, v, w) in enumerate(edges):
        if u < v:
            targets[u].append((v, w))
        else:
            targets[v].append((u, w))

    INF = 10**30
    deletable = 0

    for src in range(1, n + 1):
        if not targets[src]:
            continue

        # Target set for early stopping
        need = {v for (v, _) in targets[src]}
        remaining = len(need)

        dist = [INF] * (n + 1)
        ways = [0] * (n + 1)  # number of shortest paths, capped at 2
        dist[src] = 0
        ways[src] = 1

        pq = [(0, src)]

        while pq and remaining > 0:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue

            if u in need:
                need.remove(u)
                remaining -= 1
                if remaining == 0:
                    # all required targets finalized
                    break

            wu = ways[u]
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    ways[v] = wu
                    if ways[v] > 2:
                        ways[v] = 2
                    heapq.heappush(pq, (nd, v))
                elif nd == dist[v]:
                    s = ways[v] + wu
                    ways[v] = 2 if s >= 2 else s

        # Count deletable edges from src to its stored neighbors (src < v)
        for v, w in targets[src]:
            if dist[v] < w:
                deletable += 1
            elif dist[v] == w and ways[v] >= 2:
                deletable += 1

    return deletable


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    m = int(data[1])
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2])
        edges.append((u, v, w))
        idx += 3
    print(user_logic(n, m, edges))

if __name__ == "__main__":
    main()