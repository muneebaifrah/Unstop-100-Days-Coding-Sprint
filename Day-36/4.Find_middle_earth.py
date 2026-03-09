def find_middle_earth(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    
    i = j = 0
    prev = curr = 0
    
    for _ in range(total // 2 + 1):
        prev = curr
        
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1
    
    if total % 2 == 0:
        return (prev + curr) / 2
    else:
        return float(curr)


def main():
    import sys
    data = sys.stdin.read().split()
    
    m = int(data[0])
    n = int(data[1])
    
    nums1 = list(map(int, data[2:2+m]))
    nums2 = list(map(int, data[2+m:2+m+n]))
    
    result = find_middle_earth(nums1, nums2)
    print(f"{result:.1f}")


if __name__ == "__main__":
    main()