MOD = 10**9 + 7

n = int(input())

if n == 0:
    print(2)
elif n == 1:
    print(1)
else:
    prev2 = 2   # L0
    prev1 = 1   # L1

    for i in range(2, n+1):
        curr = (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = curr

    print(prev1)