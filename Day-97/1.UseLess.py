import sys
import heapq

def dijkstra(start, adj, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def user_logic(N, M, edges):
    adj = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # all-pairs shortest paths via N Dijkstra
    all_dist = []
    for i in range(1, N + 1):
        all_dist.append(dijkstra(i, adj, N))
    
    useless = 0
    
    for u, v, w in edges:
        useful = False
        for s in range(1, N + 1):
            if all_dist[s-1][u] + w == all_dist[s-1][v] or \
               all_dist[s-1][v] + w == all_dist[s-1][u]:
                useful = True
                break
        if not useful:
            useless += 1
    
    return useless


if __name__ == "__main__":
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    idx = 0
    N = data[idx]; idx += 1
    M = data[idx]; idx += 1
    
    edges = []
    for _ in range(M):
        u = data[idx]
        v = data[idx+1]
        w = data[idx+2]
        idx += 3
        edges.append((u, v, w))
    
    print(user_logic(N, M, edges))