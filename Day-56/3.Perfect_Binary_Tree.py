def user_logic(n, weights):
    # Total nodes = 2^(n+1) - 1
    total_nodes = (1 << (n + 1)) - 1

    # w[i] = weight of edge from i to i//2
    w = [0] * (total_nodes + 1)

    # weights are given for nodes 2 to total_nodes
    for i in range(2, total_nodes + 1):
        w[i] = weights[i - 2]

    ans = 0

    def dfs(v):
        nonlocal ans

        left = 2 * v
        right = 2 * v + 1

        # leaf node
        if left > total_nodes:
            return 0

        left_sum = w[left] + dfs(left)
        right_sum = w[right] + dfs(right)

        ans += abs(left_sum - right_sum)

        return max(left_sum, right_sum)

    dfs(1)
    return ans


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    weights = list(map(int, data[1:]))

    result = user_logic(n, weights)
    print(result)


if __name__ == "__main__":
    main()