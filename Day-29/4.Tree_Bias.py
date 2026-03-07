from collections import defaultdict, deque

def sum_of_depths(n, edges):
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    q = deque([(1,0)])  # (node, depth)
    
    visited[1] = True
    total_depth = 0

    while q:
        node, depth = q.popleft()
        total_depth += depth
        
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append((nei, depth+1))

    return total_depth


# -------- Input Handling --------
n = int(input().strip())

edges = []
for _ in range(n-1):
    a, b = map(int, input().split())
    edges.append((a,b))

print(sum_of_depths(n, edges))