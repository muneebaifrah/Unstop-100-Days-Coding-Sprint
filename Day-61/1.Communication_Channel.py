mod = 10**9 + 7

import sys,math
input_data = sys.stdin.read().strip().split()
if not input_data:
    exit()
it = iter(input_data)
N = int(next(it))
K = int(next(it))
# We ignore the fact that the graph is complete – our design is completely determined by the weights.
# (There are no further inputs because the design is what we choose.)

# Let m = number of edges incident to vertex 1 (the star edges)
m = N - 1

# Precompute factorials and inverse factorials up to m.
fac = [1]*(m+1)
invfac = [1]*(m+1)
for i in range(1, m+1):
    fac[i] = fac[i-1]*i % mod
invfac[m] = pow(fac[m], mod-2, mod)
for i in range(m, 0, -1):
    invfac[i-1] = invfac[i]*i % mod

# DP[i][r] will be the sum (mod mod) after processing cost values 1..i,
# with r star-edges assigned (in sorted order).
# We process i = 0,1,...,K. (When i=K, we have processed all allowed costs.)
dp = [[0]*(m+1) for _ in range(K+1)]
dp[0][0] = 1

# Process values 1 through K.
for i in range(K):
    # When processing cost = i+1, the factor available is:
    F = K - i  # because F = K - (i+1) + 1.
    for r in range(m+1):
        if dp[i][r] == 0:
            continue
        # t = number of star-edges that we assign the cost (i+1).
        max_t = m - r
        for t in range(max_t+1):
            new_r = r + t
            # The exponent E = binom(t,2) + t * r.
            E = (t*(t-1))//2 + t*r
            contrib = invfac[t] * pow(F, E, mod) % mod
            dp[i+1][new_r] = (dp[i+1][new_r] + dp[i][r] * contrib) % mod

# Finally, multiply by m! to account for ordering (recover the multinomial coefficient)
ans = fac[m] * dp[K][m] % mod
print(ans)