def snake_to_man_path(matrix, n, m):
    """
    Write your logic here.
    Parameters:
        matrix (list of list of char): NxM character matrix
        n (int): Number of rows in the matrix
        m (int): Number of columns in the matrix
    Returns:
        int: Number of ways the snake can reach the man's location
    """

    # Find snake and man positions
    snake_pos = None
    man_pos = None
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 's':
                snake_pos = (i, j)
            elif matrix[i][j] == 'm':
                man_pos = (i, j)

    if not snake_pos or not man_pos:
        return 0

    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    def dfs(x, y, visited):
        if (x, y) == man_pos:
            return 1
        total = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] != 'w' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    total += dfs(nx, ny, visited)
                    visited.remove((nx, ny))
        return total

    return dfs(snake_pos[0], snake_pos[1], {snake_pos})



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    
    matrix = []
    index = 2
    for i in range(n):
        matrix.append(data[index:index + m])
        index += m
    
    # Call user logic function and print the output
    result = snake_to_man_path(matrix, n, m)
    print(result)


if __name__ == "__main__":
    main()