def mod_inverse(a, m):
    # Using Extended Euclidean Algorithm to find modular inverse of a under modulo m
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def is_power_of_two(x):
    # Check if x is a power of two
    return (x != 0) and (x & (x - 1)) == 0

def main():
    N = int(input().strip())
    MOD = 10007
    
    # Find modular inverse of N modulo 10007
    inv = mod_inverse(N, MOD)
    
    # Check if inverse is a power of two
    print(1 if is_power_of_two(inv) else 0)

main()