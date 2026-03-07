def find_snoop_day_index(n, arr):
    total = sum(arr)
    half = total / 2

    curr = 0
    for i in range(n):
        curr += arr[i]
        if curr >= half:
            return i + 1
n = int(input().strip())
arr = list(map(int, input().split()))

print(find_snoop_day_index(n, arr))