def calculate_max_score(n):
    """
    Write your logic here.
    Parameters:
        n (int): An integer representing the input value
    Returns:
        int: Computed result based on the problem statement
    """
    from collections import defaultdict
    MAX = 100001
    adj = defaultdict(list)


    # Build the graph with weighted edges
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            weight = j // i
            for u in (i, -i):
                for v in (j, -j):
                    adj[i + MAX].append((v, weight))

    # Sum all edge weights connected to nodes from 2 to n
    ans = 0
    for i in range(2, n + 1):
        ans += sum(weight for _, weight in adj[i + MAX])

    return ans

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    # Call user logic function and print the output
    result = calculate_max_score(n)
    print(result)

if __name__ == "__main__":
    main()