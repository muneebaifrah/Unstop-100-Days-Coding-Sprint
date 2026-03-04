def min_parachutes(k, n):
    if n == 0 or n == 1:
        return n
    if k == 0:
        return 0
    
    # dp[j] will represent dp[m][j]
    dp = [0] * (k + 1)
    moves = 0
    
    while dp[k] < n:
        moves += 1
        for j in range(k, 0, -1):
            dp[j] = dp[j] + dp[j-1] + 1
    
    return moves


# ---- Input Handling ----
n, k = map(int, input().split())
print(min_parachutes(k, n))