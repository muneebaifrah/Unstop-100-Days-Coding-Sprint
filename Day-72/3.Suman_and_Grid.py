import sys

def solve():
    n = int(sys.stdin.readline())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))

    # Handle the base case for n=1 explicitly, or let the loop handle it
    if n == 1:
        print(grid[0][0])
        return

    # dp_prev_row stores the minimum sums to reach each column in the previous row
    dp_prev_row = grid[0]

    for i in range(1, n):
        dp_current_row = [0] * n

        # Find the two smallest values and the index of the smallest in dp_prev_row
        min1 = float('inf')
        idx1 = -1
        min2 = float('inf')

        # First pass to find min1 and idx1
        for j in range(n):
            if dp_prev_row[j] < min1:
                min2 = min1 # The old min1 becomes the new min2
                min1 = dp_prev_row[j]
                idx1 = j
            elif dp_prev_row[j] < min2:
                min2 = dp_prev_row[j]
        
        # Second pass to fill dp_current_row
        for j in range(n):
            if j == idx1:
                # If current column is the same as the min1's column, use min2
                dp_current_row[j] = grid[i][j] + min2
            else:
                # Otherwise, use min1
                dp_current_row[j] = grid[i][j] + min1
        
        dp_prev_row = dp_current_row

    # The minimum sum will be the smallest value in the last row's dp array
    print(min(dp_prev_row))

solve()