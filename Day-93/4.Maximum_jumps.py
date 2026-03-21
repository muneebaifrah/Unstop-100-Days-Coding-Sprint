def solve(arr, d, n):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the array.
        d (int): Maximum jump distance.
    Returns:
        int: Maximum number of indices you can visit.
    """
    # Initialize dp array
    dp = [1] * n
    
    # Indices sorted by the heights of arr in ascending order
    indices = sorted(range(n), key=lambda x: arr[x])
    
    for i in indices:
        # Jump to the left
        for j in range(i - 1, max(i - d - 1, -1), -1):
            if arr[j] >= arr[i]:
                break
            dp[i] = max(dp[i], 1 + dp[j])
        
        # Jump to the right
        for j in range(i + 1, min(i + d + 1, n)):
            if arr[j] >= arr[i]:
                break
            dp[i] = max(dp[i], 1 + dp[j])
    
    # Return the maximum value in dp array
    return max(dp)


def main():

    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the size of the array
    d = int(data[1])  # Second input is the maximum jump distance
    arr = list(map(int, data[2:]))  # Remaining input is the array elements
    
    # Call the user logic function and print the output
    result = solve(arr, d, n)
    print(result)

if __name__ == "__main__":
    main()