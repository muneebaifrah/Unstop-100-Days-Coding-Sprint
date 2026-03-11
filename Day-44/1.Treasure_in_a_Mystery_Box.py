def count_ways(N):
    if N == 0 or N == 1:
        return 1
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]

# Input
N = int(input())
# Output
print(count_ways(N))
                