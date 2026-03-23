MOD = 998244353

def user_logic(n, m, k, edges):
    deg = [0] * n
    for u, v in edges:
        deg[u - 1] += 1
        deg[v - 1] += 1

    a = sum(1 for d in deg if d % 2 == 0)
    b = n - a

    maxn = n
    fact = [1] * (maxn + 1)
    invfact = [1] * (maxn + 1)

    for i in range(1, maxn + 1):
        fact[i] = fact[i - 1] * i % MOD

    invfact[maxn] = pow(fact[maxn], MOD - 2, MOD)
    for i in range(maxn, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD

    def comb(n, r):
        if r < 0 or r > n:
            return 0
        return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD

    ans = 0
    for i in range(0, min(b, k) + 1, 2):
        ans = (ans + comb(b, i) * comb(a, k - i)) % MOD

    return ans


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        edges.append((u, v))
        idx += 2

    print(user_logic(n, m, k, edges))


if __name__ == "__main__":
    main()