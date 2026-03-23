n = int(input())
flips = list(map(int, input().split()))

max_pos = 0
count = 0

for i in range(n):
    max_pos = max(max_pos, flips[i])
    if max_pos == i + 1:
        count += 1

print(count)