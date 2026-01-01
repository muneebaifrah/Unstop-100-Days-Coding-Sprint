from collections import Counter

n = int(input())
strings = [input().strip() for _ in range(n)]
k = int(input())

count = Counter(strings)
unique_strings = [s for s in strings if count[s]==1]
if k<=len(unique_strings):
  print(unique_strings[k-1])
else:
  print(-1)