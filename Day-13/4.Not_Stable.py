def check_prefix_sums(arr):
    """Checks if any prefix sum of the array is zero."""
    curr_sum = 0
    for x in arr:
        curr_sum += x
        if curr_sum == 0:
            return False
    return True

def user_logic(n, arr):
    # Order 1: Non-Increasing (Descending)
    descending = sorted(arr, reverse=True)
    # Order 2: Non-Decreasing (Ascending)
    ascending = sorted(arr)
    
    can_desc = check_prefix_sums(descending)
    can_asc = check_prefix_sums(ascending)
    
    if can_desc and can_asc:
        # Both possible, pick the one with the larger first element
        if descending[0] >= ascending[0]:
            return ("POSSIBLE", descending)
        else:
            return ("POSSIBLE", ascending)
    elif can_desc:
        return ("POSSIBLE", descending)
    elif can_asc:
        return ("POSSIBLE", ascending)
    else:
        return ("IMPOSSIBLE", [])

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = list(map(int, input_data[1:1+n]))
    
    result = user_logic(n, arr)
    
    if result[0] == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        print(*(result[1]))

if __name__ == "__main__":
    main()
                