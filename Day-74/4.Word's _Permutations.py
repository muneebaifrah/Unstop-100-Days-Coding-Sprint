import math
from collections import Counter

def factorial(n):
    return math.factorial(n)

def permutations(counts):
    total = sum(counts.values())
    res = factorial(total)
    for c in counts.values():
        res //= factorial(c)
    return res

def solve():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        freq = Counter(s)

        # Find the letter with the maximum frequency (any one if multiple)
        max_freq = max(freq.values())
        max_letters = [ch for ch, c in freq.items() if c == max_freq]
        chosen = max_letters[0]  # choose the first max freq letter

        total_perm = permutations(freq)

        # Calculate permutations where all occurrences of chosen letter are together
        # Treat all chosen letters as one block
        reduced_freq = freq.copy()
        reduced_freq[chosen] = 1  # all grouped as one block
        reduced_length = sum(reduced_freq.values())

        # Reduce length by f-1 since block replaces f letters
        # Actually, we just set frequency of chosen to 1 and others remain same

        perm_together = factorial(reduced_length)
        for ch, c in reduced_freq.items():
            perm_together //= factorial(c)

        result = total_perm - perm_together
        print(result)

if __name__ == "__main__":
    solve()