def canDivideFairly(N, Arr, K):
    total = sum(Arr)
    target = total // 2
    
    # DP: achievable subset sums
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in Arr:
        for s in range(target, num - 1, -1):
            if dp[s - num]:
                dp[s] = True
    
    # Find closest achievable sum to target
    for s in range(target, -1, -1):
        if dp[s]:
            minDiff = total - 2 * s
            return minDiff <= K
    return False


# Input parsing for Unstop
if __name__ == "__main__":
    N = int(input().strip())
    Arr = list(map(int, input().split()))
    K = int(input().strip())
    print("True" if canDivideFairly(N, Arr, K) else "False")