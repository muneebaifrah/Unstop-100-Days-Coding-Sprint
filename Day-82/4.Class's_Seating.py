def seating_distribution():
    N = int(input().strip())
    M = int(input().strip())
    seats = [int(input().strip()) for _ in range(N)]
    
    # Maximum possible K:
    # Put all additional M students on the seat which already has the maximum students
    max_k = max(seats) + M
    
    # Minimum possible K:
    # We want to distribute M students as evenly as possible to minimize the max number on any seat.
    # The minimum possible K must be at least max(seats), because we cannot reduce any initial count.
    # Use binary search to find the smallest K such that we can place all M students without exceeding K on any seat.
    
    low = max(seats)
    high = max_k
    
    while low < high:
        mid = (low + high) // 2
        
        # Calculate how many students we can add without exceeding mid on any seat
        required = 0
        for seat in seats:
            if mid > seat:
                required += (mid - seat)
        
        # If we can add at least M students without exceeding mid, try to lower K
        if required >= M:
            high = mid
        else:
            low = mid + 1
    
    min_k = low
    
    print(min_k, max_k)

# Run the function
seating_distribution()