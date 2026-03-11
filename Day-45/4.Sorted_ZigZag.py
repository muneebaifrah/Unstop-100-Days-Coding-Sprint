def user_logic(n, arr):
    """
    Write your logic here.
    Parameters:
        n (int): The number of elements in the array
        arr (list): List of integers
    Returns:
        list of lists: 2D matrix representing the sorted ZigZag fashion of the given array
    """
    arr.sort()
    result = []
    
    index, level = 0, 0
    while index < n:
        # Number of nodes at this level = 2^level
        count = 2 ** level
        # Take elements from index to index + count (or till end)
        level_nodes = arr[index: index + count]
        index += count
        
        # For odd levels, reverse the order
        if level % 2 == 1:
            level_nodes.reverse()
        
        result.append(level_nodes)
        level += 1
    
    return result


def main():
    '''
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    '''
    n = int(input())
    arr = list(map(int, input().split()))
    # Call user logic function and get the output matrix
    result = user_logic(n, arr)
    
    # Print the output matrix
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()