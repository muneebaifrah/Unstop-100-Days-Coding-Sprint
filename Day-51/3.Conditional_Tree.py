import sys

# Read input
n = int(sys.stdin.readline().strip())

# Initialize arrays
MAX_N = 200005
deg = [0] * (MAX_N)
ge = [0] * (MAX_N)
f = [float('inf')] * (MAX_N)
g = [-float('inf')] * (MAX_N)
ans = 0

# Read the edges and calculate degrees
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    deg[u] += 1
    deg[v] += 1

# Adjust degrees and count occurrences of each degree
for i in range(1, n + 1):
    deg[i] -= 1  # Same as deg[i]--
    if deg[i] >= 0:
        ge[deg[i]] += 1  # Count how many nodes have a specific degree

# Initialize DP arrays
f[0] = 0
g[0] = 0

# Knapsack DP-like approach
for i in range(n):
    if ge[i] == 0:
        continue
    now = ge[i]
    j = 1
    while now >= j:
        for k in range(n, i * j - 1, -1):
            if f[k - i * j] != float('inf'):
                f[k] = min(f[k], f[k - i * j] + j)
                g[k] = max(g[k], g[k - i * j] + j)
        now -= j
        j <<= 1  # Multiply by 2

    if now > 0:
        for k in range(n, i * now - 1, -1):
            if f[k - i * now] != float('inf'):
                f[k] = min(f[k], f[k - i * now] + now)
                g[k] = max(g[k], g[k - i * now] + now)

# Calculate the final answer
for i in range(n - 1):
    if f[i] <= g[i]:
        ans += g[i] - f[i] + 1

print(ans)