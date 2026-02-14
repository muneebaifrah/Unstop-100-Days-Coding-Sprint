import math

def compute_x(p, n):
    return (p * n) // math.gcd(p, n)

# Read input
p, n = map(int, input().split())

# Print result
print(compute_x(p, n))
