def minimum_time(n, k, arr):
    # Edge cases
    if k == 0:
        return 0
    if n == 0:
        return -1
    
    # Remove zero-time members (they can't solve any problem)
    arr = [x for x in arr if x > 0]
    
    if len(arr) == 0:
        return -1
    
    left = 0
    right = max(arr) * k
    answer = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        total = 0
        for time in arr:
            total += mid // time
            if total >= k:
                break
        
        if total >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    k = int(data[1])
    
    arr = list(map(int, data[2:2+n]))
    
    print(minimum_time(n, k, arr))


if __name__ == "__main__":
    main()
