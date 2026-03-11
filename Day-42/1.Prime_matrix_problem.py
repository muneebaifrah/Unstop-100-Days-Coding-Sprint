import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Input
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# Step 1: Identify rows and columns to mark
rows_to_mark = set()
cols_to_mark = set()

for i in range(N):
    for j in range(N):
        if is_prime(matrix[i][j]):
            rows_to_mark.add(i)
            cols_to_mark.add(j)

# Step 2: Modify matrix
for i in range(N):
    for j in range(N):
        if i in rows_to_mark or j in cols_to_mark:
            matrix[i][j] = -1

# Step 3: Print result
for row in matrix:
    print(' '.join(map(str, row)))
                