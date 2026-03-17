def count_passwords(N):
    dp = [0] * (N + 1)
    dp[0] = 1  # one way to make sum 0: empty sequence

    for i in range(1, N + 1):
        dp[i] = dp[i-1]
        if i - 2 >= 0:
            dp[i] += dp[i-2]
    
    return dp[N]

if __name__ == "__main__":
    N = int(input())
    print(count_passwords(N))