import math
from collections import defaultdict

def count_pairs_divisible_by_k(k, n, arr):
    freq = defaultdict(int)
    count = 0

    for num in arr:
        g = math.gcd(num, k)

        # Check with all previously stored gcd values
        for prev_g in freq:
            if (g * prev_g) % k == 0:
                count += freq[prev_g]

        freq[g] += 1

    return count


if __name__ == "__main__":
    k = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(count_pairs_divisible_by_k(k, n, arr))