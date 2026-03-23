MOD = 10**9 + 7
S = input().strip()
n = len(S)
dp_prev = [1]

for i in range(1, n + 1):
    prefix_sum = [dp_prev[0]]
    for val in dp_prev[1:]:
        prefix_sum.append((prefix_sum[-1] + val) % MOD)
    
    if S[i - 1] == '+':
        dp_current = [0] + [prefix_sum[j - 1] for j in range(1, i + 1)]
    else:
        total = prefix_sum[-1]
        dp_current = [total] + [(total - prefix_sum[j - 1]) % MOD for j in range(1, i + 1)]
    
    dp_prev = dp_current

print(sum(dp_prev) % MOD)