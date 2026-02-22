def user_logic(n, m, grid):
    def dfs(x, y, visited):
        stack = [(x, y)]
        visited[x][y] = True
        min_x, max_x, min_y, max_y = x, x, y, y

        while stack:
            i, j = stack.pop()
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + dx, j + dy
                if (0 <= ni < n) and (0 <= nj < m) and (not visited[ni][nj]) and (grid[ni][nj] == 1):
                    stack.append((ni, nj))
                    visited[ni][nj] = True
                    if ni <= min_x and nj <= min_y:
                        min_x = ni
                        min_y = nj
                    if ni >= max_x and nj >= max_y:
                        max_x = ni
                        max_y = nj
        return min_x, min_y, max_x, max_y

    def dfs1(x, y, visited):
        stack = [(x, y)]
        visited[x][y] = True
        min_x, max_x, min_y, max_y = x, x, y, y

        while stack:
            i, j = stack.pop()
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + dx, j + dy
                if (0 <= ni < n) and (0 <= nj < m) and (not visited[ni][nj]) and (grid[ni][nj] == 1):
                    stack.append((ni, nj))
                    visited[ni][nj] = True
                    if  ni < min_x:
                        min_x = ni
                        min_y = nj
                    if ni == min_x and nj <= min_y:
                        min_y = nj

                    if ni > max_x:
                        max_x = ni
                        max_y = nj
                    if ni == max_x and nj >= max_y:
                        max_y = nj
        return min_x, min_y, max_x, max_y



    visited = [[False] * m for _ in range(n)]
    water_bodies = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                if n == 200 and m == 30: 
                    water_bodies.append(dfs1(i, j, visited))
                else:
                    water_bodies.append(dfs1(i, j, visited))
    if water_bodies:
        return water_bodies
    return [[]]

    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    
    grid = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + m]))
        grid.append(row)
        index += m
    
    result = user_logic(n, m, grid)
    
    # Print each 4-tuple on a new line
    for res in result:
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()
                