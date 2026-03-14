def min_one_bit_operations(n):
    if n == 0:
        return 0
    
    ans = 0
    while n:
        ans ^= n
        n >>= 1
    return ans


def count_primes_upto(x):
    if x < 2:
        return 0
    
    is_prime = [True] * (x + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while p * p <= x:
        if is_prime[p]:
            for multiple in range(p * p, x + 1, p):
                is_prime[multiple] = False
        p += 1
    
    return sum(is_prime)


def minimum_operations_to_zero(n):
    ops = min_one_bit_operations(n)
    return count_primes_upto(ops)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    if not data:
        return
    
    n = int(data[0])
    print(minimum_operations_to_zero(n))


if __name__ == "__main__":
    main()