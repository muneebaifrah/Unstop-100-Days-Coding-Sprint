def change_longest(arr, x):
    mx = max(arr)
    for i in range(len(arr)):
        if arr[i] == mx:
            arr[i] = max(0, arr[i] - x)


def pole_arrangement(arr):
    n = len(arr)
    
    min_left = arr[0]

    for j in range(1, n-1):
        for k in range(j+1, n):
            if min_left < arr[k] < arr[j]:
                return 1
        
        min_left = min(min_left, arr[j])

    return 0


# -------- Input --------
n, x = map(int, input().split())
arr = list(map(int, input().split()))

change_longest(arr, x)

print(pole_arrangement(arr))