import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def find_premium_prime(N):
    # Since floor(N / p) must be at least 2, p can be at most N // 2
    upper_bound = min(N, 10**6)  # Safety cap to avoid too long primes
    for p in range(2, upper_bound + 1):
        if is_prime(p):
            q = N // p
            if is_prime(q):
                return p
    return -1

# Input
N = int(input())
print(find_premium_prime(N))