MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read().split()
    N = int(input[0])
    M = int(input[1])
    K = int(input[2])
    
    if K == 0:
        print(0)
        return
    
    # Initialize DP table
    dp = [[[0] * (K + 1) for _ in range(M + 1)] for __ in range(N + 1)]
    
    for m in range(1, M + 1):
        dp[1][m][1] = 1
    
    for i in range(1, N):
        for current_max in range(1, M + 1):
            for k in range(1, K + 1):
                if dp[i][current_max][k] == 0:
                    continue
                # Case 1: append element <= current_max
                val = dp[i][current_max][k]
                dp[i + 1][current_max][k] = (dp[i + 1][current_max][k] + val * current_max) % MOD
                # Case 2: append element > current_max
                if k < K:
                    for new_max in range(current_max + 1, M + 1):
                        dp[i + 1][new_max][k + 1] = (dp[i + 1][new_max][k + 1] + val) % MOD
    
    total = 0
    for m in range(1, M + 1):
        total = (total + dp[N][m][K]) % MOD
    print(total)

if __name__ == "__main__":
    main()