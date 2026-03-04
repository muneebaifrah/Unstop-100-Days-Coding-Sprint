def numTrees(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]

    return dp[n]


if __name__ == '__main__':
    number_of_nodes = int(input())
    print(numTrees(number_of_nodes))