def count_square_sub_islands(matrix):
    if not matrix:
        return 0
    
    n = len(matrix)
    m = len(matrix[0])
    
    dp = [[0]*m for _ in range(n)]
    total = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    )
                total += dp[i][j]
    
    return total


# ---- INPUT HANDLING ----
n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

print(count_square_sub_islands(matrix))