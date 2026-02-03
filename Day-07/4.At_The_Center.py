 = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

k = int(input())

points.sort(key=lambda p: p[0]**2 + p[1]**2)

for i in range(k):
    print(points[i][0], points[i][1])
                            