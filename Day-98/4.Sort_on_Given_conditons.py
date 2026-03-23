def diagonalSort(mat):
    from collections import defaultdict

    M, N = len(mat), len(mat[0])
    diagonals = defaultdict(list)

    # Step 1: Collect elements into diagonal groups
    for i in range(M):
        for j in range(N):
            diagonals[i - j].append(mat[i][j])

    # Step 2: Sort each diagonal
    for key in diagonals:
        diagonals[key].sort(reverse=True)  # Reverse to use pop() efficiently

    # Step 3: Place sorted elements back into the matrix
    for i in range(M):
        for j in range(N):
            mat[i][j] = diagonals[i - j].pop()

    return mat

# Read input
M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(M)]

# Sort diagonals and print the output matrix
sorted_mat = diagonalSort(mat)
for row in sorted_mat:
    print(*row)