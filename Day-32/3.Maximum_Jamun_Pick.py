def max_jamun(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers representing the number of jamuns in each bucket
    Returns:
        int: Maximum sum of jamuns that can be obtained by picking non-adjacent buckets
    """
    n = len(arr)
    
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])
    
    # Space-optimized DP using two variables
    # prev2 = max sum up to i-2
    # prev1 = max sum up to i-1
    prev2 = arr[0]
    prev1 = max(arr[0], arr[1])
    
    for i in range(2, n):
        # Current max = max(skip current, take current + max from i-2)
        current = max(prev1, arr[i] + prev2)
        prev2 = prev1
        prev1 = current
    
    return prev1

import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])  # First input is the integer N
arr = list(map(int, data[1:]))  # Remaining input is the array of integers representing jamuns in each bucket

# Call user logic function and print the output
result = max_jamun(arr)
print(result)
                