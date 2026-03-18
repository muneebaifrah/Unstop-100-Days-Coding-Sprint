MOD = 10**9 + 7

def user_logic(N, K, L, R):
    """
    Write your logic here.
    Parameters:
        N (int): Size of the favorable sequence.
        K (int): Minimum total required cost of the sequence.
        L (int): Lower limit of the items.
        R (int): Upper limit of the items.
    Returns:
        int: Total number of favorable sequences, modulo 10^9 + 7.
    """
    M = R - L + 1  
    values = list(range(M)) 
    dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(N+1)]
    for val in values:
        dp[1][0][val] = 1

    for pos in range(1, N):
        for cost in range(pos):  
            for max_val in range(M):
                count = dp[pos][cost][max_val]
                if count == 0:
                    continue
                for next_val in values:
                    if next_val > max_val:
                        dp[pos+1][cost+1][next_val] = (dp[pos+1][cost+1][next_val] + count) % MOD
                    else:
                        dp[pos+1][cost][max_val] = (dp[pos+1][cost][max_val] + count) % MOD
    total = 0
    for cost in range(K, N):
        for max_val in range(M):
            total = (total + dp[N][cost][max_val]) % MOD

    return total

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    K = int(data[1])
    L = int(data[2])
    R = int(data[3])
    
    # Call user logic function and print the output
    result = user_logic(N, K, L, R)
    print(result)

if __name__ == "__main__":
    main()