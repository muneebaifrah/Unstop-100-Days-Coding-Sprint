n = int(input().strip())
v = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    cost = dp[i - 1] + abs(v[i] - v[i - 1])
    if i > 1:
        cost = min(cost, dp[i - 2] + abs(v[i] - v[i - 2]))
    if i > 2:
        cost = min(cost, dp[i - 3] + abs(v[i] - v[i - 3]))
    dp[i] = cost

print(dp[-1])
