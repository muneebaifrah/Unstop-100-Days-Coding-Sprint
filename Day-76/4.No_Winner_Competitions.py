# Enter your code here. Read input from STDIN. Print output to STDOUT
MOD = 10**9 + 7
N = 505

# Function to add numbers under modulo
def add(x, y):
    return (x + y) % MOD

# Function to multiply numbers under modulo
def mul(x, y):
    return (x * y) % MOD

def main():
    n, m = map(int, input().split())
    c = [[0] * N for _ in range(N)]
    dp = [[0] * (m + 1) for _ in range(N)]

    # Compute binomial coefficients
    for i in range(N):
        c[i][0] = c[i][i] = 1
        for j in range(1, i):
            c[i][j] = add(c[i - 1][j], c[i - 1][j - 1])

    dp[n][0] = 1  # Base case

    # Dynamic programming to fill dp table
    for i in range(n, 1, -1):
        for j in range(m):
            if dp[i][j] == 0:
                continue
            pw = 1
            nj = min(m, j + i - 1)
            for k in range(i, -1, -1):
                dp[k][nj] = add(dp[k][nj], mul(dp[i][j], mul(c[i][k], pw)))
                pw = mul(pw, nj - j)

    # Calculate the answer
    ans = sum(dp[0][i] for i in range(m + 1)) % MOD
    print(ans)

if __name__ == "__main__":
    main()