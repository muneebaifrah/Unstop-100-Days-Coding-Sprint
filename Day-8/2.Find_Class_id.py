def peakIndexInMountainArray(A):
    n = len(A)
    
    # Check first element
    if n > 1 and A[0] >= A[1]:
        return 0
    
    # Check middle elements
    for i in range(1, n - 1):
        if A[i] >= A[i - 1] and A[i] >= A[i + 1]:
            return i
    
    # Check last element
    if n > 1 and A[n - 1] >= A[n - 2]:
        return n - 1
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(peakIndexInMountainArray(arr))
                            