def user_logic(n, id_vector, size_vector):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the vectors
        id_vector (list): List of ID vector elements
        size_vector (list): List of size vector elements
    Returns:
        int: Computed result based on the problem statement
    """
    # Use a stack to store (id, size) pairs
    stack = []
    
    for i in range(n):
        current_id = id_vector[i]
        current_size = size_vector[i]
        
        # Check if current element matches the top of stack
        if stack and stack[-1] == (current_id, current_size):
            # Remove the matching pair
            stack.pop()
        else:
            # Add current element to stack
            stack.append((current_id, current_size))
    
    # Return the size of remaining elements
    return len(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    
    id_vector = list(map(int, data[1:n+1]))  # Next n inputs are the ID vector elements
    size_vector = list(map(int, data[n+1:2*n+1]))  # Following n inputs are the size vector elements
    
    # Call user logic function and print the output
    result = user_logic(n, id_vector, size_vector)
    print(result)

if __name__ == "__main__":
    main()
                