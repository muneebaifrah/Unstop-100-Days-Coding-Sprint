import math

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n  # n is prime

def user_logic(n):
    # If prime → 1 step
    if is_prime(n):
        return 1
    
    spf = smallest_prime_factor(n)
    remaining = n - spf
    
    return 1 + (remaining // 2)

n = int(input())
result = user_logic(n)
print(result)