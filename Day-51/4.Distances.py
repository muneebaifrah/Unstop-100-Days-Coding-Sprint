def mult(x, y, m):
    return (x * y) % m

def binpow(x, n, m):
    if n == 0:
        return 1
    if n & 1:
        return mult(x, binpow(x, n - 1, m), m)
    return binpow(mult(x, x, m), n // 2, m)

def main():
    md = 998244353

    n, d = map(int, input().split())

    ans = 0
    z = 1
    if d == 1:
        ans = binpow(2, n + 1, md) - 4
        if ans < 0:
            ans += md
        print(ans)
        return

    x = binpow(2, d - 2, md)

    for i in range(n):
        if 2 * (n - 1 - i) >= d:
            if n - 1 - i >= d:
                ans = (ans + z * ((d + 3) * x % md)) % md
            else:
                ans = (ans + z * ((2 * (n - i - 1) - d + 1) * x % md)) % md
        z = (z * 2) % md

    print((2 * ans) % md)

if __name__ == "__main__":
    main()