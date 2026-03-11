import sys

def play_game(marbles):
    # Convert input to a list of integers
    current_marbles = [m for m in marbles]
    
    while len(current_marbles) > 1:
        # Sort to easily pick the two largest elements
        current_marbles.sort()
        
        # Pop the two largest marble counts
        m1 = current_marbles.pop()
        m2 = current_marbles.pop()
        
        # Calculate sum to check if mean is a whole number
        total = m1 + m2
        
        # If mean is a whole number (sum is even)
        if total % 2 == 0:
            mean_val = total // 2
            current_marbles.append(mean_val)
        # If mean is not a whole number (sum is odd), 
        # both are destroyed, so we add nothing back.
            
    # Return the remaining marble if one exists, else 0
    if len(current_marbles) == 1:
        return current_marbles[0]
    else:
        return 0

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Read exactly N marbles
    marbles = list(map(int, input_data[1:n+1]))
    
    result = play_game(marbles)
    print(result)

if __name__ == "__main__":
    main()
                