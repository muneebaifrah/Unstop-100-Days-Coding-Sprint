def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    m = data[1]

    nums = data[2:]
    grid = []

    idx = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(nums[idx])
            idx += 1
        grid.append(row)

    # DP table
    dp = [[0]*m for _ in range(n)]

    dp[0][0] = grid[0][0]

    # first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # first row
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # fill rest
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    print(dp[n-1][m-1])


if __name__ == "__main__":
    main()