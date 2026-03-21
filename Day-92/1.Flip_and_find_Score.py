import sys

# Function to check if a number is prime using Sieve of Eratosthenes
def count_primes_up_to(n):
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return sum(is_prime)  # Count of primes

# Function to maximize the score
def maximize_score(grid, n, m):
    # Step 1: Ensure first column is all 1s
    for i in range(n):
        if grid[i][0] == 0:  # Flip row if first element is 0
            grid[i] = [1 - x for x in grid[i]]
    
    # Step 2: Optimize remaining columns
    for j in range(1, m):  # Start from the second column
        ones_count = sum(grid[i][j] for i in range(n))  # Count 1s in the column
        if ones_count < (n / 2):  # More 0s than 1s → flip column
            for i in range(n):
                grid[i][j] = 1 - grid[i][j]

    # Step 3: Compute the total score
    max_score = sum(int("".join(map(str, row)), 2) for row in grid)

    return max_score

# Read input
n, m = map(int, sys.stdin.readline().split())
flat_values = list(map(int, sys.stdin.read().split()))
grid = [flat_values[i * m: (i + 1) * m] for i in range(n)]

# Compute maximum score
max_score = maximize_score(grid, n, m)

# Count prime numbers ≤ max_score
result = count_primes_up_to(max_score)

# Print the result
print(result)