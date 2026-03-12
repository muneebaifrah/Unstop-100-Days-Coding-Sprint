def count_primes_up_to(n):
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sum(sieve)

def min_insertions_to_valid_parentheses(s):
    balance = 0
    insertions = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                insertions += 1
                balance = 0
    return insertions + balance

# Read input
S = input().strip()

M = min_insertions_to_valid_parentheses(S)
result = count_primes_up_to(M)
print(result)