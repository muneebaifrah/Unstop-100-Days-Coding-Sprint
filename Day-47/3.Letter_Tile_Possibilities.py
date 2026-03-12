from math import factorial
from collections import Counter

def count_unique_sequences(stickers):
    freq = Counter(stickers)
    chars = list(freq.keys())
    counts = [freq[c] for c in chars]
    
    max_len = len(stickers)
    fact = [1] * (max_len + 1)
    for i in range(2, max_len + 1):
        fact[i] = fact[i-1] * i
    
    result = 0
    
    # We use a recursive approach to generate all subsets of counts
    def backtrack(i, current_counts):
        nonlocal result
        if i == len(chars):
            total = sum(current_counts)
            if total == 0:
                return
            numerator = fact[total]
            denominator = 1
            for c in current_counts:
                denominator *= fact[c]
            result += numerator // denominator
            return
        
        for c in range(counts[i] + 1):
            current_counts.append(c)
            backtrack(i + 1, current_counts)
            current_counts.pop()
    
    backtrack(0, [])
    return result

# Input reading
stickers = input().strip()
print(count_unique_sequences(stickers))
                