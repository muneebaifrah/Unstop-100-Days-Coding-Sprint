def coin_change(coins, amount):
    INF = float('inf')
    dp = [INF] * (amount + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != INF else -1


# Input handling
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

print(coin_change(coins, amount))