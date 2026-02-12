import sys

def count_good_indices(n, arr):
    s = 0
    ans = 0
    for x in arr:
        s += x
        if s > 0 and (s & (s - 1)) == 0:
            ans += 1
    return ans

data = sys.stdin.read().strip().split()
n = int(data[0])
arr = list(map(int, data[1:]))

print(count_good_indices(n, arr))