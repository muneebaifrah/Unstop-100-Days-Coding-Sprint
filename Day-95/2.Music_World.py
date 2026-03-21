N, X = map(int, input().split())
price = list(map(int, input().split()))
duration = list(map(int, input().split()))

dp = [0] * (X + 1)

for i in range(N):
    cost = price[i]
    value = duration[i]
    # Traverse backwards for 0/1 knapsack
    for w in range(X, cost - 1, -1):
        dp[w] = max(dp[w], dp[w - cost] + value)

print(dp[X])