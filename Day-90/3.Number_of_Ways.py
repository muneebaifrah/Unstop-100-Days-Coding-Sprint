import math

# Input
x, y = map(int, input().split())

# If either coordinate is odd, it's unreachable
if x % 2 != 0 or y % 2 != 0:
    print(0)
else:
    rx = x // 2
    ry = y // 2
    # Number of ways to arrange rx rights and ry ups = C(rx + ry, rx)
    ways = math.comb(rx + ry, rx)
    print(ways)