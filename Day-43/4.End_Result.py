def user_logic(a, b):
    """
    Computes the number of matches needed to represent the sum of a and b.
    
    Each digit requires a fixed number of matches:
      0 -> 6 matches
      1 -> 2 matches
      2 -> 5 matches
      3 -> 5 matches
      4 -> 4 matches
      5 -> 5 matches
      6 -> 6 matches
      7 -> 3 matches
      8 -> 7 matches
      9 -> 6 matches
      
    Special case: if the sum is 0, return 0.
    
    Parameters:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int: Total number of matches needed to represent the sum.
    """
    # Compute the sum
    total = a + b
    
    # Special case: if sum is 0, return 0
    if total == 0:
        return 0

    # Mapping from digit to number of matches needed.
    match_count = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    
    total_str = str(total)
    matches = sum(match_count[digit] for digit in total_str)
    
    return matches

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    T = int(data[0])  # First input is the number of test cases
    index = 1
    results = []
    
    for _ in range(T):
        A = int(data[index])
        B = int(data[index + 1])
        index += 2
        
        # Call user logic function
        result = user_logic(A, B)
        results.append(result)
    
    # Print all results
    for res in results:
        print(res)

if __name__ == "__main__":
    main()