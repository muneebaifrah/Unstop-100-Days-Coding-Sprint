def calculate_total_cost(k, n, m, edges):
    if m == 0:
        return 0  # No bulb can be non-functional if divisible by 0

    from collections import defaultdict, deque
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    queue = deque([0])
    visited[0] = True
    non_functional_count = 0
    
    while queue:
        node = queue.popleft()
        if node != 0 and node % m == 0:
            non_functional_count += 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return non_functional_count * k

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    k = int(data[0])  # Price of the bulb
    n = int(data[1])  # Total number of bulbs
    m = int(data[2])  # Number of bulbs divisible by m
    len_graph = int(data[3])  # Length of the 2D array
    
    graph = []
    index = 4
    for _ in range(len_graph):
        u = int(data[index])
        v = int(data[index + 1])
        graph.append([u, v])
        index += 2
    
    # Call user logic function and print the output
    total_cost = calculate_total_cost(k, n, m, graph)
    print(total_cost)

if __name__ == "__main__":
    main()