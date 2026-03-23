def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def can_partition(arr, k, max_sum):
    partitions = 1
    current_sum = 0
    
    for num in arr:
        if current_sum + num <= max_sum:
            current_sum += num
        else:
            partitions += 1
            current_sum = num
            if partitions > k:
                return False
    return True

def peculiarNumber(n, k, arr):
    # Step 1: replace elements
    modified = [abs(arr[i] - i) for i in range(n)]
    
    # Step 2: binary search for minimized maximum partition sum
    left = max(modified)
    right = sum(modified)
    
    while left < right:
        mid = (left + right) // 2
        if can_partition(modified, k, mid):
            right = mid
        else:
            left = mid + 1
    
    x = left
    
    # Step 3: return fibonacci if x < 100
    if x < 100:
        return fibonacci(x)
    return x


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n = data[0]
    k = data[1]
    arr = data[2:]
    
    print(peculiarNumber(n, k, arr))