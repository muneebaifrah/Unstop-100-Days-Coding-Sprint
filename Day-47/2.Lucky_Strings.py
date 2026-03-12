MOD = 10**9 + 7

def lucky_strings(n):
    if n == 1 or n == 2:
        return 2  # Base cases
    
    a, b = 2, 2  # F(1) = 2, F(2) = 2
    
    for _ in range(3, n + 1):
        c = (a + b) % MOD
        a, b = b, c
    
    return b

# Read input
N = int(input().strip())

# Print the result
print(lucky_strings(N))