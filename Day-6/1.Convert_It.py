def modify_array(n, arr):
    max_val = 0
    result = []
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
        result.append(arr[i] + max_val)
    print(*result)


n = int(input())
arr = list(map(int, input().split()))
modify_array(n, arr)
