# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# sort numbers
arr.sort()

# flip negative numbers
i = 0
while i < n and k > 0 and arr[i] < 0:
    arr[i] = -arr[i]
    i += 1
    k -= 1

# sort again to find smallest element
arr.sort()

# if k is odd, flip smallest element
if k % 2 == 1:
    arr[0] = -arr[0]

print(sum(arr))