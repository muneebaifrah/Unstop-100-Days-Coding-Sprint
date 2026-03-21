def can_form_by_interleaving(S, T):
    if len(S) != len(T) or len(S) % 2 != 0:
        return False
    
    n = len(S) // 2
    A = S[:n]
    B = S[n:]
    
    dp = [[False]*(n+1) for _ in range(n+1)]
    dp[0][0] = True
    
    for i in range(n+1):
        for j in range(n+1):
            if i > 0 and A[i-1] == T[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j]
            if j > 0 and B[j-1] == T[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i][j-1]
    
    return dp[n][n]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    S = data[0]
    T = data[1]
    
    result = can_form_by_interleaving(S, T)
    print(1 if result else 0)

if __name__ == "__main__":
    main()