def count_labeled_trees(n, d):
    """
    Write your logic here.
    Parameters:
        N (int): Length of the sequence
        D (list): List of integers representing the sequence
    Returns:
        int: Number of labeled trees satisfying the given condition modulo 998244353
    """
    MOD = 998244353
    MAXN = (1 << 18) + 5 

    def add(a, b):
        return (a + b) % MOD

    def mul(a, b):
        return (a * b) % MOD

    def qpow(a, b):
        c = 1
        while b > 0:
            if b & 1:
                c = mul(c, a)
            a = mul(a, a)
            b >>= 1
        return c

    def ntt(n, a, op):
        pw = [1] * MAXN
        rev = [0] * MAXN
        for i in range(n):
            rev[i] = (rev[i >> 1] >> 1) | (i & 1) * (n >> 1)
        for i in range(n):
            if i < rev[i]:
                a[i], a[rev[i]] = a[rev[i]], a[i]
        i = 1
        while i < n:
            g = qpow(3, (MOD - 1) // (i * 2))
            for j in range(1, i):
                pw[j] = mul(pw[j - 1], g)
            j = 0
            while j < n:
                for k in range(i):
                    x = a[j + k]
                    y = mul(a[j + i + k], pw[k])
                    a[j + k] = add(x, y)
                    a[j + i + k] = add(x, MOD - y)
                j += i * 2
            i *= 2
        if op == -1:
            inv = qpow(n, MOD - 2)
            for i in range(n):
                a[i] = mul(a[i], inv)
            a[1:n] = a[1:n][::-1]
    def mul_poly(a, b):
        n = 1
        while n <= len(a) + len(b) - 2:
            n *= 2
        A = [0] * n
        B = [0] * n
        for i in range(len(a)):
            A[i] = a[i]
        for i in range(len(b)):
            B[i] = b[i]
        ntt(n, A, 1)
        ntt(n, B, 1)
        for i in range(n):
            A[i] = mul(A[i], B[i])
        ntt(n, A, -1)
        return A[:len(a) + len(b) - 1]

    def init(d, k, fac, ifac):
        v = [0] * (k + 1)
        pw = 1
        for i in range(k + 1):
            v[i] = mul(pw, mul(fac[k], mul(ifac[i], ifac[k - i])))
            pw = mul(pw, d)
        return v

    fac = [1] * MAXN
    ifac = [1] * MAXN
    for i in range(1, n + 1):
        fac[i] = mul(fac[i - 1], i)
    ifac[n] = qpow(fac[n], MOD - 2)
    for i in range(n, 0, -1):
        ifac[i - 1] = mul(ifac[i], i)
    cnt = [0] * MAXN
    for x in d:
        cnt[x] += 1
    res = [1]
    for i in range(n, 0, -1):
        if cnt[i] > 0:
            res = mul_poly(res, init(i, cnt[i], fac, ifac))
    ans = 0
    pw = qpow(n, MOD - 2)
    for i in range(len(res)):
        ans = add(ans, mul(res[i], mul(pw, fac[n - i])))
        pw = mul(pw, n)
    ans = mul(ans, qpow(n, MOD - 2))
    for i in range(1, n + 1):
        ans = mul(ans, ifac[d[i - 1]])
    return ans    
    

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    D = list(map(int, data[1:]))
    
    result = count_labeled_trees(N, D)
    print(result)

if __name__ == "__main__":
    main()