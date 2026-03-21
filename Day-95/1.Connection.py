def user_logic(N, M, edges):
    """
    Write your logic here.
    Parameters:
        N (int): Number of vertices
        M (int): Number of edges
        edges (list): List of tuples, each containing three integers Ai, Bi, Ci
    Returns:
        int: Maximum reward ensuring the graph stays connected
    """
    # Union-Find (Disjoint Set Union)
    parent = list(range(N+1))
    rank = [0] * (N+1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True

    # Step 1: Sum all positive rewards
    total_positive = sum(c for _, _, c in edges if c > 0)

    # Step 2: Build MST with "lost reward" costs
    mst_cost = 0
    sorted_edges = []
    for a, b, c in edges:
        if c > 0:
            sorted_edges.append((c, a, b))  # cost = reward lost if kept
        else:
            sorted_edges.append((0, a, b))  # cost = 0 if kept

    sorted_edges.sort(key=lambda x: x[0])  # sort by cost

    # Kruskal's MST
    edges_used = 0
    for cost, a, b in sorted_edges:
        if union(a, b):
            mst_cost += cost
            edges_used += 1
            if edges_used == N-1:
                break

    # Step 3: Answer = total_positive - mst_cost
    return total_positive - mst_cost
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    M = int(data[1])
    edges = []

    index = 2
    for _ in range(M):
        Ai = int(data[index])
        Bi = int(data[index + 1])
        Ci = int(data[index + 2])
        edges.append((Ai, Bi, Ci))
        index += 3

    # Call user logic function and print the output
    result = user_logic(N, M, edges)
    print(result)

if __name__ == "__main__":
    main()