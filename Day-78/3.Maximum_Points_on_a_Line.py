from collections import defaultdict
from math import gcd

def max_points_on_line(points):
    n = len(points)
    if n <= 2:
        return n

    max_points = 0

    for i in range(n):
        slopes = defaultdict(int)
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(dy, dx)
            if g != 0:
                dx //= g
                dy //= g
            # Normalize to avoid negative-zero inconsistencies
            if dx < 0:
                dx *= -1
                dy *= -1
            elif dx == 0:
                dy = 1
            elif dy == 0:
                dx = 1
            slopes[(dy, dx)] += 1

        current_max = max(slopes.values(), default=0) + 1  # +1 for the point itself
        max_points = max(max_points, current_max)

    return max_points

# ----------- Input/Output Handling ------------
def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    print(max_points_on_line(points))

# Run the main function
main()