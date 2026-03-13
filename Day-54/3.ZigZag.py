MOD = 1000000007
N = 3005

def dfs(x, fa, e, f, C, siz, p):
    siz[x] = f[x][1] = 1
    for y in e[x]:
        if y != fa:
            dfs(y, x, e, f, C, siz, p)
            for i in range(1, siz[x] + 1):
                sum_ = 0
                for j in range(siz[y] - 1, -1, -1):
                    sum_ = (sum_ + f[y][j + 1]) % MOD
                    p[i + j] = (p[i + j] + f[x][i] * C[i - 1 + j][j] % MOD * sum_ % MOD * C[siz[x] + siz[y] - i - j][siz[y] - j] % MOD) % MOD
            siz[x] += siz[y]
            for i in range(1, siz[x] + 1):
                f[x][i] = p[i]
                p[i] = 0
    f[x][1:siz[x] + 1] = reversed(f[x][1:siz[x] + 1])

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    
    e = [[] for _ in range(N)]
    f = [[0] * N for _ in range(N)]
    C = [[0] * N for _ in range(N)]
    siz = [0] * N
    p = [0] * N
    
    C[0][0] = 1
    for i in range(1, n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
    
    for _ in range(n - 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        e[x].append(y)
        e[y].append(x)
    
    dfs(1, 0, e, f, C, siz, p)
    
    ans = 0
    for i in range(1, n + 1):
        ans = (ans + f[1][i]) % MOD
    
    print(2 * ans % MOD)