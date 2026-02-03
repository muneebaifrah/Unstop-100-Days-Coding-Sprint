n = int(input())
arr = list(map(int, input().split()))

result = []
zero_count = 0

for x in arr:
  if x != 0:
    result.append(x)
    
  else:
    zero_count += 1

for _ in range(zero_count):
  result.append(0)
print(*result)