def max_nutrition(n, m, k, price, nutrition):
    dp = [[-1] * (k + 1) for _ in range(m + 1)]
    dp[0][0] = 0

    for i in range(n):
        p = price[i]
        n_value = nutrition[i]
        discounted_p = p // 2

        for j in range(k, -1, -1):
            for budget in range(m, -1, -1):
                if dp[budget][j] != -1:
                    if budget + p <= m:
                        dp[budget + p][j] = max(dp[budget + p][j], dp[budget][j] + n_value)

                    if j + 1 <= k and budget + discounted_p <= m:
                        dp[budget + discounted_p][j + 1] = max(dp[budget + discounted_p][j + 1], dp[budget][j] + n_value)

    result = 0
    for budget in range(m + 1):
        for j in range(k + 1):
            if dp[budget][j] != -1:
                result = max(result, dp[budget][j])
    return result

n, m, k = map(int, input().split())
price = list(map(int, input().split()))
nutrition = list(map(int, input().split()))

print(max_nutrition(n, m, k, price, nutrition))