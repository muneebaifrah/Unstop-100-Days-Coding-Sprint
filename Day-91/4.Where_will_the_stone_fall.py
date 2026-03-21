def find_stone_path(grid):
    """
    Write your logic here.
    Parameters:
        grid (list): 2D list representing the matrix
    Returns:
        list: List of integers representing the column the stone falls out of or -1 if it gets stuck
    """
    if not grid:
        return []
    rows = len(grid)
    cols = len(grid[0])
    result = []
    for start_col in range(cols):
        col = start_col
        for row in range(rows):
            direction = grid[row][col]
            next_col = col + direction
            if next_col < 0 or next_col >= cols:
                col = -1
                break
            if grid[row][col] != grid[row][next_col]:
                col = -1
                break
            col = next_col
        result.append(col)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    # Parse first line for n and m
    n = int(data[0])
    m = int(data[1])

    # Parse the matrix values
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m

    # Call user logic function
    result = find_stone_path(grid)
    
    # Print the result
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()