MOD = 10**9 + 7

def count_paths(n, m, roads):
    """
    Write your logic here.
    Parameters:
        n (int): Number of landmarks
        m (int): Number of one-way roads
        roads (list): List of tuples, where each tuple contains two integers u and v representing a one-way road from u to v
    Returns:
        int: Number of paths from landmark 1 to landmark n modulo 10^9 + 7
    """
    from collections import deque

    # Adjacency list representation
    graph = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    
    # Build the graph
    for u, v in roads:
        graph[u].append(v)
        in_degree[v] += 1  # Count incoming edges for topological sorting

    # Topological Sorting using Kahn's Algorithm (BFS)
    topo_order = []
    queue = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # DP to count paths
    ways = [0] * (n+1)
    ways[1] = 1  # There's one way to be at node 1 (start)

    for node in topo_order:
        for neighbor in graph[node]:
            ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

    return ways[n]  # The number of paths from 1 to N


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of landmarks
    m = int(data[1])  # Number of one-way roads
    
    roads = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        roads.append((u, v))
        index += 2

    # Call user logic function and print the output
    result = count_paths(n, m, roads)
    print(result)

if __name__ == "__main__":
    main()