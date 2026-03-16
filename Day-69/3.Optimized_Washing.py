def minimumCost(N, S, time, cost):
    # User's logic goes here


    prefixTime = [0] * (N + 1)
    prefixCost = [0] * (N + 1)
    
    for i in range(1, N + 1):
        prefixTime[i] = prefixTime[i-1] + time[i-1]
        prefixCost[i] = prefixCost[i-1] + cost[i-1]
    
    dp = [float('inf')] * (N + 1)   
    dp[0] = 0
    
    for i in range(1, N + 1):
        for j in range(i):
            dp[i] = min(dp[i] , dp[j] +  prefixTime[i] * (prefixCost[i] - prefixCost[j]) + S * (prefixCost[N] - prefixCost[j]))
    return dp[N]

    pass

if __name__ == "__main__":
    N, S = map(int, input().split())
    time = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(minimumCost(N, S, time, cost))