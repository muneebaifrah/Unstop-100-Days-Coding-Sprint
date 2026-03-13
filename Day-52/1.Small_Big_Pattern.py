def longest_small_big_pattern(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    up = down = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            up = down + 1
        elif arr[i] < arr[i - 1]:
            down = up + 1
        # if equal, do nothing

    return max(up, down)

# Input reading
n = int(input())
arr = list(map(int, input().split()))

print(longest_small_big_pattern(arr))