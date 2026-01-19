def find_flower_indices(n, t, arr):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == t:
                return i, j

n, t = map(int, input().split())
arr = list(map(int, input().split()))
i1, i2 = find_flower_indices(n, t, arr)
print(i1, i2)
