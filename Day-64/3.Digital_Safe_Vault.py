def min_time_to_transform(currentState, desiredState, alterablePositions):
    n = len(currentState)
    
    # Validation checks
    if n != len(desiredState) or n != len(alterablePositions):
        return -1
    if not all(c.islower() for c in currentState):
        return -1
    if not all(c.islower() for c in desiredState):
        return -1
    if not all(c in '01' for c in alterablePositions):
        return -1
    
    def rotate_clockwise(s, steps):
        steps %= n
        return s[-steps:] + s[:-steps]
    
    def rotate_counterclockwise(s, steps):
        steps %= n
        return s[steps:] + s[:steps]
    
    min_cost = float('inf')
    
    # Try all clockwise rotations
    for r in range(n):
        rotated = rotate_clockwise(currentState, r)
        rotation_cost = r * 2
        change_cost = 0
        valid = True
        
        for i in range(n):
            if rotated[i] != desiredState[i]:
                if alterablePositions[i] == '1':
                    change_cost += 3
                else:
                    valid = False
                    break
        if valid:
            total_cost = rotation_cost + change_cost
            min_cost = min(min_cost, total_cost)
    
    # Try all counterclockwise rotations
    for r in range(n):
        rotated = rotate_counterclockwise(currentState, r)
        rotation_cost = r * 2
        change_cost = 0
        valid = True
        
        for i in range(n):
            if rotated[i] != desiredState[i]:
                if alterablePositions[i] == '1':
                    change_cost += 3
                else:
                    valid = False
                    break
        if valid:
            total_cost = rotation_cost + change_cost
            min_cost = min(min_cost, total_cost)
    
    return min_cost if min_cost != float('inf') else -1


# Read inputs
currentState = input().strip()
desiredState = input().strip()
alterablePositions = input().strip()

print(min_time_to_transform(currentState, desiredState, alterablePositions))