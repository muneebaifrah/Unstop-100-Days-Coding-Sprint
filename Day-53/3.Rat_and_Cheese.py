from collections import deque

def min_time_to_eat_all_cheese(grid, N):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    cheese_count = 0
    
    # Initialize the queue with rat positions and count cheese
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
                visited[i][j] = True
            elif grid[i][j] == 1:
                cheese_count += 1
    
    if cheese_count == 0:
        # No cheese to eat
        return 0
    
    max_time = 0
    
    while queue:
        x, y, time = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check boundaries and if cheese and not visited
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, time + 1))
                    cheese_count -= 1
                    max_time = max(max_time, time + 1)
    
    # If all cheese eaten, return max_time, else -1
    return max_time if cheese_count == 0 else -1

# Read input
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Compute and print the result
print(min_time_to_eat_all_cheese(grid, N))