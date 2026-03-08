# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

n = int(data[0])
vals = data[1:1+n]
P = int(data[1+n])
Q = int(data[2+n])

# Build parent mapping using level order
parent = {}
exists = set()

if vals[0] == "N":
    sys.exit(0)

root = int(vals[0])
parent[root] = None
exists.add(root)

q = deque([root])
idx = 1

while q and idx < n:
    node = q.popleft()

    # Left child
    if idx < n and vals[idx] != "N":
        left = int(vals[idx])
        parent[left] = node
        exists.add(left)
        q.append(left)
    idx += 1

    # Right child
    if idx < n and vals[idx] != "N":
        right = int(vals[idx])
        parent[right] = node
        exists.add(right)
        q.append(right)
    idx += 1

# Collect ancestors of P
ancestors = set()
cur = P
while cur is not None:
    ancestors.add(cur)
    cur = parent.get(cur)

# Move Q upwards to find first common ancestor
cur = Q
while cur not in ancestors:
    cur = parent.get(cur)

print(cur)