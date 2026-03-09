def find_middle_earth(nums1, nums2):
    arr = nums1 + nums2
    arr.sort()
    n = len(arr)
    
    if n % 2 == 1:
        return float(arr[n//2])
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2


m, n = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

result = find_middle_earth(nums1, nums2)
print(f"{result:.1f}")