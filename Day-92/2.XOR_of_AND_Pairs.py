def solve():
    import sys
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    MAX_BIT = 17  # since values ≤ 100000, bits needed ≤ 17
    
    count1 = [0] * (MAX_BIT + 1)
    count2 = [0] * (MAX_BIT + 1)
    
    # Count bits in arr1
    for num in arr1:
        for b in range(MAX_BIT + 1):
            if num & (1 << b):
                count1[b] += 1
    
    # Count bits in arr2
    for num in arr2:
        for b in range(MAX_BIT + 1):
            if num & (1 << b):
                count2[b] += 1
    
    # Compute XOR of all pairwise AND results
    ans = 0
    for b in range(MAX_BIT + 1):
        if (count1[b] * count2[b]) % 2 == 1:
            ans |= (1 << b)
    
    print(ans)


# Run the solver
solve()