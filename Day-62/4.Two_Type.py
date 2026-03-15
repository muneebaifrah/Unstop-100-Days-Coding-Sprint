from collections import deque
def user_logic(n, m, edges):
    """
    Write your logic here.
    Parameters:
        n (int): Number of vertices
        m (int): Number of edges
        edges (list of tuple): List of edges where each edge is a tuple (u, v)
    Returns:
        tuple: Two lists of tuples representing the edges in S1 and S2
    """
    # Build the undirected graph (1-indexed)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # ---------- Build S1 using DFS ----------
    visited = [False] * (n + 1)
    s1 = []
    idx = [0] * (n + 1)
    stack = [1]
    visited[1] = True

    while stack:
        cur = stack[-1]
        if idx[cur] < len(adj[cur]):
            nxt = adj[cur][idx[cur]]
            idx[cur] += 1
            if not visited[nxt]:
                visited[nxt] = True
                s1.append((min(cur, nxt), max(cur, nxt)))
                stack.append(nxt)
        else:
            stack.pop()

    # ---------- Build S2 using BFS ----------
    visited = [False] * (n + 1)
    s2 = []
    queue = deque([1])
    visited[1] = True

    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                s2.append((min(cur, nxt), max(cur, nxt)))
                queue.append(nxt)

    # Sort the edges of both spanning trees
    s1.sort()
    s2.sort()

    return s1, s2


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Call user logic function
    s1, s2 = user_logic(n, m, edges)
    
    # Print the output as required
    for edge in s1:
        print(edge[0], edge[1])
    for edge in s2:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()