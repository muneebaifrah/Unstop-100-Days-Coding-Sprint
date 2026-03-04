def user_logic(n, arr):
    MOD = 10**9 + 7
    
    # Step 1: Sum of original indices
    total = (n * (n - 1) // 2) % MOD
    
    # Step 2: Sort array
    arr.sort()
    
    i = 0
    while i < n:
        j = i
        # Find last occurrence of same value
        while j + 1 < n and arr[j + 1] == arr[i]:
            j += 1
        
        freq = j - i + 1
        total = (total + freq * j) % MOD
        
        i = j + 1
    
    return total


# ---- Input Handling ----
n = int(input().strip())
arr = list(map(int, input().split()))
print(user_logic(n, arr))