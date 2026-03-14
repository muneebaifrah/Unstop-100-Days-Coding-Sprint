def count_xor_setbit_triplets(n):
    ans = 0
    
    # precompute set bits count
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = a ^ b
            
            # to avoid duplicates and keep unordered triplets only
            if c <= b or c > n:
                continue
            
            if bits[a] == bits[b] == bits[c]:
                ans += 1
    
    return ans


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    if not data:
        return
    
    n = int(data[0])
    print(count_xor_setbit_triplets(n))


if __name__ == "__main__":
    main()