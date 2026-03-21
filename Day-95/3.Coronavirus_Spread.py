def infect(grid):
    """
    Write your logic here.
    Parameters:
        grid (list of list of int): The matrix representing the grid
    Returns:
        int: The minimum time required to infect everyone, or -1 if not possible
    """
    from collections import deque
    n, m = len(grid), len(grid[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    queue = deque()
    healthy_count = 0

    # Step 1: Initialize queue with all infected persons
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                healthy_count += 1

    # If no infected person exists but healthy people exist → impossible
    if not queue and healthy_count > 0:
        return -1
    # If no healthy person exists → already infected
    if healthy_count == 0:
        return 0

    max_time = 0

    # Step 2: BFS infection spread
    while queue:
        x, y, time = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # infect this person
                healthy_count -= 1
                queue.append((nx, ny, time + 1))
                max_time = max(max_time, time + 1)

    # Step 3: Check if all healthy people got infected
    return max_time if healthy_count == 0 else -1



def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Row count
    m = int(data[1])  # Column count
    
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m
    
    # Call user logic function and print the output
    result = infect(grid)
    print(result)

if __name__ == "__main__":
    main()