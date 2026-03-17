def alpha_bitwise_operation(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Size of the array
        arr (list): List of integers representing the array
    Returns:
        int: Result of the alpha bitwise operation
    """
    result = 0
    for bit in range(30):  # Increase the bit range from 20 to 30
        count = sum((num >> bit) & 1 for num in arr)  # Count set bits at position `bit`
        if count > n / 2:  # Majority check
            result |= (1 << bit)  # Set the bit in the result
    return result
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Ensure the length of the array matches N
    assert len(arr) == n
    
    # Call user logic function and print the output
    result = alpha_bitwise_operation(n, arr)
    print(result)

if __name__ == "__main__":
    main()