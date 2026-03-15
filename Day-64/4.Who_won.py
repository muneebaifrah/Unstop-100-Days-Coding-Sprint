import math

def find_winner(d, k):
    # Calculate maximum full steps along both x and y
    m = d // k
    # Find maximum m such that 2*(m*k)^2 <= d^2
    max_steps = 0
    while max_steps <= m and 2 * (max_steps * k) ** 2 <= d ** 2:
        max_steps += 1
    max_steps -= 1
    
    # Check if an extra move is possible along one axis
    x = max_steps * k
    y = max_steps * k + k
    if x ** 2 + y ** 2 <= d ** 2:
        return "Ashish"
    x = max_steps * k + k
    y = max_steps * k
    if x ** 2 + y ** 2 <= d ** 2:
        return "Ashish"
    
    return "Utkarsh"

# Input reading
d, k = map(int, input().split())
print(find_winner(d, k))