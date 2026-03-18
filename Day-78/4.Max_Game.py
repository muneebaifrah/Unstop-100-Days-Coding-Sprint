import sys
input = sys.stdin.readline

# Build Segment Tree
def build(arr, seg, idx, l, r):
    if l == r:
        seg[idx] = arr[l]
        return
    mid = (l + r) // 2
    build(arr, seg, 2*idx+1, l, mid)
    build(arr, seg, 2*idx+2, mid+1, r)
    seg[idx] = max(seg[2*idx+1], seg[2*idx+2])

# Query max in range
def query(seg, idx, l, r, ql, qr):
    if qr < l or ql > r:  # completely outside
        return -float('inf')
    if ql <= l and r <= qr:  # completely inside
        return seg[idx]
    mid = (l + r) // 2
    left = query(seg, 2*idx+1, l, mid, ql, qr)
    right = query(seg, 2*idx+2, mid+1, r, ql, qr)
    return max(left, right)

# Update value at index
def update(seg, idx, l, r, pos, val):
    if l == r:
        seg[idx] = val
        return
    mid = (l + r) // 2
    if pos <= mid:
        update(seg, 2*idx+1, l, mid, pos, val)
    else:
        update(seg, 2*idx+2, mid+1, r, pos, val)
    seg[idx] = max(seg[2*idx+1], seg[2*idx+2])

# Main
n, q = map(int, input().split())
arr = list(map(int, input().split()))

seg = [0] * (4*n)
build(arr, seg, 0, 0, n-1)

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:  # range query
        print(query(seg, 0, 0, n-1, a, b))
    else:       # update query
        update(seg, 0, 0, n-1, a, b)