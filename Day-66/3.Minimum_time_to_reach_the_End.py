import heapq

def minimum_time_to_clear_game(matrix):
    n = len(matrix)
    
    pq = [(matrix[0][0], 0, 0)]  # (time, row, col)
    visited = set()
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while pq:
        time, r, c = heapq.heappop(pq)
        
        if (r, c) == (n-1, n-1):
            return time
        
        if (r, c) in visited:
            continue
        
        visited.add((r, c))
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                new_time = max(time, matrix[nr][nc])
                heapq.heappush(pq, (new_time, nr, nc))

n = int(input())
arr = list(map(int,input().split()))

matrix = []
idx = 0
for i in range(n):
    row = []
    for j in range(n):
        row.append(arr[idx])
        idx += 1
    matrix.append(row)

print(minimum_time_to_clear_game(matrix))