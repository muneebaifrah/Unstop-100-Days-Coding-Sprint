# Majority Element using Boyer-Moore Voting Algorithm
# Python 3.11.12

import sys

data = list(map(int, sys.stdin.read().strip().split()))
n = data[0]
nums = data[1:]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)
                