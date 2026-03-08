import sys
import math

data = list(map(int, sys.stdin.read().strip().split()))
n = data[0]
arr = data[1:1+n]
k = data[1+n]

# Step 1: DP to find maximum sum after partitioning
dp = [0] * (n + 1)

for i in range(1, n + 1):
    max_val = 0
    for j in range(1, min(k, i) + 1):
        max_val = max(max_val, arr[i - j])
        dp[i] = max(dp[i], dp[i - j] + max_val * j)

M = dp[n]

# Step 2: Count primes <= M using segmented sieve
if M < 2:
    print(0)
    sys.exit(0)

limit = int(math.isqrt(M)) + 1

# Simple sieve up to sqrt(M)
is_prime_small = [True] * (limit + 1)
is_prime_small[0] = is_prime_small[1] = False

for i in range(2, int(math.isqrt(limit)) + 1):
    if is_prime_small[i]:
        for j in range(i * i, limit + 1, i):
            is_prime_small[j] = False

base_primes = [i for i in range(2, limit + 1) if is_prime_small[i]]

# Segmented sieve
segment_size = 10**6
count_primes = 0

low = 2
while low <= M:
    high = min(low + segment_size - 1, M)
    is_prime = [True] * (high - low + 1)

    for p in base_primes:
        start = max(p * p, ((low + p - 1) // p) * p)
        if start > high:
            continue
        for x in range(start, high + 1, p):
            is_prime[x - low] = False

    if low == 2:
        count_primes += sum(is_prime)
    else:
        count_primes += sum(is_prime)

    low = high + 1

print(count_primes)
                