def countTriplets(n, arr):
    from collections import defaultdict
    
    pair_count = defaultdict(int)
    
    # Step 1: Count all pairwise AND results
    for i in range(n):
        for j in range(n):
            pair_count[arr[i] & arr[j]] += 1
    
    result = 0
    
    # Step 2: Check with third element
    for val in arr:
        for pair_val in pair_count:
            if (pair_val & val) == 0:
                result += pair_count[pair_val]
    
    return result


# ---- Input Handling ----
n = int(input().strip())
arr = list(map(int, input().split()))

print(countTriplets(n, arr))