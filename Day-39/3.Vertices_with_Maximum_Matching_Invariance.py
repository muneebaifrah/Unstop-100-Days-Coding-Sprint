def count_removable_vertices(n, edges):
    """
    Write your logic here.
    Parameters:
        n (int): Number of vertices in the tree
        edges (list of tuple): List of edges where each edge is represented by a tuple (u, v)
    Returns:
        int: Count of vertices that can be removed while keeping the size of the maximum matching unchanged
    """
    from collections import defaultdict
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def max_matching_size(excluded_vertex=None):
        """Calculate maximum matching size, optionally excluding a vertex"""
        # Create a modified adjacency list if excluding a vertex
        if excluded_vertex:
            adj_modified = defaultdict(list)
            for u, v in edges:
                if u != excluded_vertex and v != excluded_vertex:
                    adj_modified[u].append(v)
                    adj_modified[v].append(u)
            current_adj = adj_modified
            vertices = [v for v in range(1, n + 1) if v != excluded_vertex]
        else:
            current_adj = adj
            vertices = list(range(1, n + 1))
        
        if len(vertices) == 0:
            return 0
        
        # DP for maximum matching
        dp = [[0, 0] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        def dfs(v, parent):
            visited[v] = True
            children = []
            
            for u in current_adj[v]:
                if u == parent or visited[u]:
                    continue
                dfs(u, v)
                children.append(u)
            
            # dp[v][0]: v is not matched
            dp[v][0] = 0
            for child in children:
                dp[v][0] += max(dp[child][0], dp[child][1])
            
            # dp[v][1]: v is matched to one of its children
            dp[v][1] = 0
            for child in children:
                # Try matching v with this child
                val = 1 + dp[child][0]
                for other_child in children:
                    if other_child != child:
                        val += max(dp[other_child][0], dp[other_child][1])
                dp[v][1] = max(dp[v][1], val)
        
        # Process all connected components
        total_matching = 0
        for vertex in vertices:
            if not visited[vertex]:
                dfs(vertex, -1)
                total_matching += max(dp[vertex][0], dp[vertex][1])
        
        return total_matching
    
    # Calculate original maximum matching
    original_matching = max_matching_size()
    
    # Special case: if n == 1, no edges, matching = 0
    if n == 1:
        return 1  # Can remove the only vertex
    
    # Count vertices that can be removed
    count = 0
    for vertex in range(1, n + 1):
        new_matching = max_matching_size(excluded_vertex=vertex)
        if new_matching == original_matching:
            count += 1
    
    return count


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the number of vertices
    edges = []
    index = 1
    for _ in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Call user logic function and print the output
    result = count_removable_vertices(n, edges)
    print(result)

if __name__ == "__main__":
    main()
                