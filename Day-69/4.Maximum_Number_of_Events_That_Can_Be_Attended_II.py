import sys
import bisect

def max_value_events(events, k):
    # Sort events by end day
    events.sort(key=lambda x: x[1])
    
    # Extract startDays and endDays for binary search
    startDays = [e[0] for e in events]
    endDays = [e[1] for e in events]
    values = [e[2] for e in events]
    
    N = len(events)
    
    # Precompute the index of the last event that doesn't conflict
    # For each event i, find j where endDays[j] < startDays[i]
    prev = [0]*N
    for i in range(N):
        # Binary search to find rightmost event that ends before startDays[i]
        # endDays is sorted, find index of max endDay < startDays[i]
        idx = bisect.bisect_left(endDays, startDays[i]) - 1
        prev[i] = idx
    
    # dp[i][x] = max value using first i events with at most x events chosen
    # Use 2D DP, but optimize space by using two rows only
    
    dp_prev = [0]*(k+1)
    dp_curr = [0]*(k+1)
    
    for i in range(N):
        for x in range(1, k+1):
            # Option 1: skip event i
            option1 = dp_prev[x]
            
            # Option 2: attend event i
            j = prev[i]
            option2 = values[i] + (dp_prev[x-1] if j == -1 else dp_prev[x-1])
            if j != -1:
                option2 = values[i] + dp_prev[x-1]  # we need dp at event j, but dp_prev is for i-1, so j < i
            
            # But since dp_prev only has dp for i-1, we need to refer to dp at j
            # So we need full dp or we must precompute for j
            # For large N and k, full dp may be heavy.
            
            # We'll store dp in full 2D array:
    
    # For better clarity and correctness, we use full dp table:
    dp = [[0]*(k+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        start, end, val = events[i-1]
        # Find j: last event that ends before start
        j = prev[i-1] + 1  # +1 because dp is 1-indexed
        
        for x in range(1, k+1):
            # skip event i
            dp[i][x] = dp[i-1][x]
            # take event i
            if j == 0:
                # no previous event
                dp[i][x] = max(dp[i][x], val)
            else:
                dp[i][x] = max(dp[i][x], dp[j][x-1] + val)
    
    return dp[N][k]

# Input reading
N = int(sys.stdin.readline())
events = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
k = int(sys.stdin.readline())

print(max_value_events(events, k))