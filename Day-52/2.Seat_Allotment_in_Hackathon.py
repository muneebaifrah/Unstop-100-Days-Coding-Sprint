MOD = 10**9 + 7

def count_pairings(N):
    if N % 2 == 1:
        return 0
    
    dp = [0] * (N + 1)
    dp[0] = 1  # 1 way to tile 3x0
    if N >= 2:
        dp[2] = 3  # base case

    for i in range(4, N + 1, 2):
        dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD

    return dp[N]

# Input
N = int(input())
print(count_pairings(N))