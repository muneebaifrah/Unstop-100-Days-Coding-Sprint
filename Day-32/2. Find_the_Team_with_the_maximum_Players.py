n = int(input().strip())
arr = list(map(int, input().split()))

freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

max_freq = max(freq.values())

result = [team for team, count in freq.items() if count == max_freq]
result.sort()

for team in result:
    print(team)