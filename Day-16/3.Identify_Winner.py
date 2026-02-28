def find_winner(arr):
    """
    Parameters:
        arr (list): List of integers representing the numbers on the papers
    Returns:
        int: Number on the paper of the winner or 0 if there's no unique number
    """
    freq = {}
    
    # Count frequency
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    # Find first unique number
    for num in arr:
        if freq[num] == 1:
            return num
    
    return 0


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_winner(arr))