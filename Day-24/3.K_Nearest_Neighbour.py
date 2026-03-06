def find_k_nearest_points(points, k):
    # store (distance, index, point)
    arr = []
    
    for i, (x, y) in enumerate(points):
        dist = x*x + y*y
        arr.append((dist, i, [x, y]))
    
    # sort by distance then index
    arr.sort()
    
    # take first k points
    result = []
    for i in range(k):
        result.append(arr[i][2])
        
    return result


# Input
n, k = map(int, input().split())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])

# Find nearest points
ans = find_k_nearest_points(points, k)

# Output
for x, y in ans:
    print(x, y)