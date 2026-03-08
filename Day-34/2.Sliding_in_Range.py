def numSubarrayBoundedMax(nums, left, right):
    count = 0
    start = -1
    last_valid = -1

    for i in range(len(nums)):
        if nums[i] > right:
            start = i
        if left <= nums[i] <= right:
            last_valid = i
        if last_valid > start:
            count += last_valid - start

    return count


n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
print(numSubarrayBoundedMax(arr, l, r))