def can_partition(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return dp[target]


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    if can_partition(arr):
        print(sum(arr) // 2)
    else:
        print(0)