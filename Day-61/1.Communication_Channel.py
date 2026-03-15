MOD = 10**9 + 7

def count_distinct_network_designs(N, K):
    M = N - 1  # number of star edges (1 to others)
    if M == 0:
        return 1

    maxE = M * (M - 1) // 2  # maximum possible exponent used below

    # factorials for nCr up to M
    fact = [1] * (M + 1)
    for i in range(1, M + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact = [1] * (M + 1)
    invfact[M] = pow(fact[M], MOD - 2, MOD)
    for i in range(M, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

    # dp[p] = ways after assigning some weights, where p vertices have been assigned star weights so far
    dp = [0] * (M + 1)
    dp[0] = 1

    # Iterate star weight value t = 1..K
    # base(t) = number of choices for a non-star edge whose max endpoint-star-weight == t
    for t in range(1, K + 1):
        base = K - t + 1  # in [1..K]

        # Precompute base^e for e=0..maxE in O(maxE)
        pow_base = [1] * (maxE + 1)
        for e in range(1, maxE + 1):
            pow_base[e] = (pow_base[e - 1] * base) % MOD

        dp2 = [0] * (M + 1)
        for p_old in range(M + 1):
            if dp[p_old] == 0:
                continue
            remaining = M - p_old

            # choose c vertices to have star-weight exactly t
            for c in range(remaining + 1):
                # number of pairs (u,v) whose max star-weight becomes exactly t contributed at this step:
                # c * p_old  (pairs between new vertices and previous vertices)
                # + C(c,2)   (pairs within the new vertices)
                e = c * p_old + (c * (c - 1)) // 2

                ways = dp[p_old]
                ways = ways * nCr(remaining, c) % MOD
                ways = ways * pow_base[e] % MOD

                dp2[p_old + c] = (dp2[p_old + c] + ways) % MOD

        dp = dp2

    return dp[M]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    K = int(data[1])
    print(count_distinct_network_designs(N, K))

if __name__ == "__main__":
    main()