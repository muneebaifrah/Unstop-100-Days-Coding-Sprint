MOD = 10**9 + 7

def special_permutations(N, K):
    if K <= 0:
        return 0
    if N == 1:
        return 1 if K >= 1 else 0

    K = min(K, (N + 1) // 2)  # max possible peaks

    # dp[p] = P(current_n, p)
    dp = [0] * (K + 2)
    dp[1] = 1  # P(1,1)=1

    for n in range(2, N + 1):
        up_to = min(K, (n + 1) // 2)
        ndp = [0] * (K + 2)
        for p in range(1, up_to + 1):
            # P(n,p) = 2p*P(n-1,p) + (n-2p+2)*P(n-1,p-1)
            term1 = (2 * p) * dp[p]
            term2 = (n - 2 * p + 2) * dp[p - 1]
            ndp[p] = (term1 + term2) % MOD
        dp = ndp

    return sum(dp[1:K + 1]) % MOD


def main():
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    K = int(data[1])
    print(special_permutations(N, K))

if __name__ == "__main__":
    main()