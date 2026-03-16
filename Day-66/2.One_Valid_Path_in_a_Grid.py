from collections import deque

dirs = [(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]

def minCost(grid):
    m = len(grid)
    n = len(grid[0])

    dq = deque([(0,0,0)])
    visited = [[False]*n for _ in range(m)]

    while dq:
        r,c,cost = dq.popleft()

        if r == m-1 and c == n-1:
            return cost

        if visited[r][c]:
            continue

        visited[r][c] = True

        for dr,dc,d in dirs:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < m and 0 <= nc < n:
                if grid[r][c] == d:
                    dq.appendleft((nr,nc,cost))
                else:
                    dq.append((nr,nc,cost+1))

    return -1


# ---- Input Handling ----
m,n = map(int,input().split())

grid = []
for _ in range(m):
    grid.append(list(map(int,input().split())))

print(minCost(grid))