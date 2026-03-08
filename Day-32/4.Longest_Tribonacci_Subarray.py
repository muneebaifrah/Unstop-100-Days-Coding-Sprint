import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

MAXV = 10**5

# Generate Tribonacci numbers up to MAXV
trib = set()
a, b, c = 0, 1, 1
trib.add(0)
trib.add(1)

while True:
    d = a + b + c
    if d > MAXV:
        break
    trib.add(d)
    a, b, c = b, c, d

# Find longest contiguous subarray of Tribonacci numbers
max_len = 0
curr = 0

for x in arr:
    if x in trib:
        curr += 1
        if curr > max_len:
            max_len = curr
    else:
        curr = 0

print(max_len)
                