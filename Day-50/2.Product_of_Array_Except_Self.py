def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the array
        arr (list): List of integers representing the array
    Returns:
        list: Computed result array based on the problem statement
    """
    # Initialize prefix and suffix product arrays
    result = [1] * n

    # First pass: compute prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    # Second pass: compute suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = user_logic(n, arr)
    
    # Print each element of the result in separate lines
    for res in result:
        print(res)

if __name__ == "__main__":
    main()