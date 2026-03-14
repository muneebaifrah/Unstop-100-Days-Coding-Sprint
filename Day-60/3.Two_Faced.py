def user_logic(n, P, Q):
    MOD = 998244353

    # Build permutation f where f[P[i]] = Q[i]
    f = [0] * (n + 1)
    for i in range(n):
        f[P[i]] = Q[i]

    visited = [False] * (n + 1)
    ans = 1

    for i in range(1, n + 1):
        if not visited[i]:
            cur = i
            length = 0

            while not visited[cur]:
                visited[cur] = True
                cur = f[cur]
                length += 1

            if length == 1:
                ans = (ans * 1) % MOD
            else:
                ans = (ans * (pow(2, length, MOD) - 2)) % MOD

    return ans % MOD


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()

    n = int(data[0])
    P = list(map(int, data[1:1 + n]))
    Q = list(map(int, data[1 + n:1 + 2 * n]))

    print(user_logic(n, P, Q))