def spaceship_fleets(k, pos, speed):
    # Pair position with time to reach destination
    ships = []
    for p, s in zip(pos, speed):
        time = (k - p) / s
        ships.append((p, time))
    
    # Sort by position in descending order (closest first)
    ships.sort(reverse=True)
    
    fleets = 0
    max_time = 0
    
    for p, t in ships:
        if t > max_time:
            fleets += 1
            max_time = t
    
    return fleets


# Input
n = int(input())
k = int(input())
pos = list(map(int, input().split()))
speed = list(map(int, input().split()))

# Output
print(spaceship_fleets(k, pos, speed))