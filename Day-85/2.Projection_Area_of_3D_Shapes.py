def total_projection_area(n, flat_grid):
    # Reconstruct the grid
    grid = [flat_grid[i * n:(i + 1) * n] for i in range(n)]

    top = 0
    front = [0] * n  # max in each column
    side = 0         # sum of max in each row

    for i in range(n):
        max_row = 0
        for j in range(n):
            val = grid[i][j]
            if val > 0:
                top += 1
            max_row = max(max_row, val)
            front[j] = max(front[j], val)
        side += max_row

    total_area = top + sum(front) + side
    return total_area

# Input
n = int(input())
flat_grid = list(map(int, input().split()))

# Output
print(total_projection_area(n, flat_grid))