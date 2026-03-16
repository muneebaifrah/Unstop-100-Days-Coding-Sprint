MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.readline
    N = int(input().strip())
    
    colors = [0,1,2]  # Red, Yellow, Green
    
    # Generate all valid row patterns (length 3, no adjacent equal)
    patterns = []
    def gen(row):
        if len(row) == 3:
            patterns.append(tuple(row))
            return
        for c in colors:
            if not row or row[-1] != c:
                gen(row+[c])
    gen([])
    
    P = len(patterns)  # should be 12
    
    # Build adjacency matrix
    adj = [[0]*P for _ in range(P)]
    for i,p in enumerate(patterns):
        for j,q in enumerate(patterns):
            if all(p[k] != q[k] for k in range(3)):
                adj[i][j] = 1
    
    # Matrix exponentiation
    def matmul(A,B):
        n = len(A)
        m = len(B[0])
        k = len(B)
        C = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s = 0
                for t in range(k):
                    s += A[i][t]*B[t][j]
                C[i][j] = s % MOD
        return C
    
    def matpow(M, power):
        n = len(M)
        # identity
        res = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
        while power:
            if power & 1:
                res = matmul(res,M)
            M = matmul(M,M)
            power >>= 1
        return res
    
    if N == 1:
        print(P)  # 12
        return
    
    # Initial vector: 1 for each pattern
    vec = [[1] for _ in range(P)]
    
    # Raise adjacency matrix to (N-1)
    Mpow = matpow(adj, N-1)
    
    # Multiply Mpow * vec
    res = matmul(Mpow, vec)
    
    ans = sum(r[0] for r in res) % MOD
    print(ans)

if __name__ == "__main__":
    solve()