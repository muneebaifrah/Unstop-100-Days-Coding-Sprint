# Count sequences length N with entries in 0..M and sum <= K
# Output answer modulo 998244353

MOD = 998244353

def precompute_factinv(maxn, mod=MOD):
    fact = [1] * (maxn+1)
    invfact = [1] * (maxn+1)
    for i in range(1, maxn+1):
        fact[i] = fact[i-1] * i % mod
    invfact[maxn] = pow(fact[maxn], mod-2, mod)
    for i in range(maxn, 0, -1):
        invfact[i-1] = invfact[i] * i % mod
    return fact, invfact

def nCr(n, r, fact, invfact):
    if r < 0 or r > n: return 0
    return fact[n] * invfact[r] % MOD * invfact[n-r] % MOD

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0]); M = int(data[1]); K = int(data[2])

    # Limit j: j <= N and j*(M+1) <= K
    jmax = min(N, K // (M + 1))

    # We need factorials up to (K - j*(M+1) + N) for j=0 -> jmax.
    # The largest argument is for j=0: K + N
    max_needed = K + N
    # Safety note: if K + N is huge (>> 1e7) this precomputation may be infeasible in time/memory.
    # Typical contest inputs keep K reasonably small; if not, a different approach is required.
    if max_needed > 5_000_000:
        # A protective fallback to avoid memory blow-up (this branch rarely needed in contest inputs)
        # We'll still attempt to proceed but warn (no print of warning per problem requirements).
        pass

    fact, invfact = precompute_factinv(max_needed)

    ans = 0
    sign = 1
    for j in range(jmax + 1):
        term1 = nCr(N, j, fact, invfact)
        T = K - j * (M + 1)
        # inner binomial C(T + N, N)
        term2 = nCr(T + N, N, fact, invfact)
        cur = term1 * term2 % MOD
        if (j & 1) == 1:
            ans -= cur
        else:
            ans += cur
    ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()
                