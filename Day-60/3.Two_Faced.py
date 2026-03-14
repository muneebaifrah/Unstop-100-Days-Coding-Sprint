MOD = 998244353

def count_valid_ways(n, P, Q):
    total_ways = 0
    for mask in range(1, 1 << n):
        covered = set()
        for i in range(n):
            if mask & (1 << i):
                covered.add(P[i])
                covered.add(Q[i])
        if len(covered) == n:
            total_ways = (total_ways + 1) % MOD
    return total_ways

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

print(count_valid_ways(n, P, Q))