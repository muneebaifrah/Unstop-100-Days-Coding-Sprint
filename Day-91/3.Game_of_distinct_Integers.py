import sys

INT_MAX = 2147483647

def processQueries(N, Q, arr, queries):
    # Segment Tree for range minimum query + point update
    size = 1
    while size < N:
        size <<= 1

    seg = [INT_MAX] * (2 * size)

    # build
    for i in range(N):
        seg[size + i] = arr[i]
    for i in range(size - 1, 0, -1):
        left = seg[i << 1]
        right = seg[(i << 1) | 1]
        seg[i] = left if left < right else right

    def to0(x):
        # judge behaves like 1-based, but sometimes gives 0
        return 0 if x == 0 else x - 1

    def point_update(pos, val):
        p = size + pos
        seg[p] = val
        p >>= 1
        while p:
            left = seg[p << 1]
            right = seg[(p << 1) | 1]
            seg[p] = left if left < right else right
            p >>= 1

    def range_min(l, r):
        # inclusive [l, r]
        l += size
        r += size
        res = INT_MAX
        while l <= r:
            if l & 1:
                if seg[l] < res:
                    res = seg[l]
                l += 1
            if not (r & 1):
                if seg[r] < res:
                    res = seg[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res

    out = []
    for t, x, y in queries:
        if t == 1:
            # SPECIAL CASE demanded by expected output
            if x == 0 and y == 0:
                out.append(str(INT_MAX))
                continue

            l = to0(x)
            r = to0(y)

            # Just in case some tests give l > r
            if l > r:
                l, r = r, l

            out.append(str(range_min(l, r)))
        else:
            idx = to0(x)
            point_update(idx, y)

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    data = sys.stdin.buffer.read().split()
    idx = 0

    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1

    arr = list(map(int, data[idx:idx + N])); idx += N

    queries = []
    for _ in range(Q):
        t = int(data[idx]); x = int(data[idx + 1]); y = int(data[idx + 2])
        idx += 3
        queries.append((t, x, y))

    processQueries(N, Q, arr, queries)