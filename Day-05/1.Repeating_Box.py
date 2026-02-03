n2 = int(input())
arr = list(map(int, input().split()))

freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

for key, value in freq.items():
    if value == n2 // 2:
        print(key)
        break
