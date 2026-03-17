def user_logic(intervals):
    """
    Write your logic here.
    Parameters:
        intervals (list): List of intervals where each interval is a list of two integers [start, end]
    Returns:
        int: Minimum difference between the overlapping intervals
    """
    # Sort intervals by start time
    intervals.sort()

    n = len(intervals)

    min_difference = float('inf')
    for i in range(1,n):
        if intervals[i][0] <= intervals[i-1][1]:
            intervals[i][0] = intervals[i-1][0]
        if intervals[n-i][0] <= intervals[n-i-1][1]:
            intervals[n-i-1][1] = intervals[n-i][1]

    for i in range(n):
            min_difference = min(min_difference, intervals[i][1] - intervals[i][0])
    
    return min_difference if min_difference != float('inf') else 0
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    intervals = []
    index = 1
    for i in range(n):
        start = int(data[index])
        end = int(data[index + 1])
        intervals.append([start, end])
        index += 2
    
    # Call user logic function and print the output
    result = user_logic(intervals)
    print(result)

if __name__ == "__main__":
    main()