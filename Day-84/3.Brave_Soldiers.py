def count_brave_soldiers(N):
    if N < 2:
        return 0

    # Sieve array
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False

    # Count primes
    return sum(is_prime)

# Input
N = int(input())
print(count_brave_soldiers(N))