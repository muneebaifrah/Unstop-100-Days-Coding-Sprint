MOD = 10**9 + 7

def count_ways_to_make_sum(N):
    # dp[i] will store number of ways to make sum i
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (no spins)

    # For each possible sum from 1 to N
    for i in range(1, N + 1):
        # Try using spinner results 1 to 6
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i - j]) % MOD

    return dp[N]


# Main Code
if __name__ == "__main__":
    N = int(input().strip())
    print(count_ways_to_make_sum(N))