def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float('-inf')
    
    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            count += 1
    
    return count

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    intervals = [list(map(int, input().split())) for _ in range(N)]
    print(erase_overlap_intervals(intervals))
