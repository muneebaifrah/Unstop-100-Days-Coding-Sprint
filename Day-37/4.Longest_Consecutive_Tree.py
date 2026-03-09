from collections import deque, defaultdict

def user_logic(n, edges):
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * (n + 1)

    q = deque([1])
    color[1] = 0

    group0 = []
    group1 = []

    while q:
        node = q.popleft()

        if color[node] == 0:
            group0.append(node)
        else:
            group1.append(node)

        for nei in graph[node]:
            if color[nei] == -1:
                color[nei] = 1 - color[node]
                q.append(nei)

    # permutation with minimum similarity
    return group1 + group0