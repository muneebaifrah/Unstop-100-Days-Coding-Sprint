MOD = 998244353
N = int(input())
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

import sys
sys.setrecursionlimit(10**7)

# dp[u][k][0/1]: number of subsets in subtree rooted at u
# with k components, excluding (0) or including (1) u

def dfs(u, p):
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0] = 1  # empty subset excluding u
    dp[1][1] = 1  # subset with only u included

    for v in edges[u]:
        if v == p:
            continue
        child_dp = dfs(v, u)
        new_dp = [[0,0] for _ in range(N+1)]

        for k1 in range(N+1):
            for k2 in range(N+1):
                if k1 + k2 > N:
                    continue
                # merge excluding u
                new_dp[k1+k2][0] = (new_dp[k1+k2][0] + dp[k1][0] * (child_dp[k2][0] + child_dp[k2][1])) % MOD
                
                # merge including u
                # cases:
                # u included, v excluded
                new_dp[k1+k2][1] = (new_dp[k1+k2][1] + dp[k1][1] * child_dp[k2][0]) % MOD
                # u included, v included (connected by edge, so components merge: k1 + k2 - 1)
                if k1 + k2 - 1 >= 0:
                    new_dp[k1+k2-1][1] = (new_dp[k1+k2-1][1] + dp[k1][1] * child_dp[k2][1]) % MOD

        dp = new_dp
    return dp

dp_root = dfs(1, -1)

# Combine counts from including and excluding root
# Remove empty subset (dp_root[0][0] = 1)
for x in range(1, N+1):
    ans = (dp_root[x][0] + dp_root[x][1]) % MOD
    print(ans)