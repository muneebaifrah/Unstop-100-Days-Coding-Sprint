def user_logic(str, pattern):
    """
    Write your logic here.
    Parameters:
        str (str): The input string
        pattern (str): The pattern string
    Returns:
        tuple: A tuple containing the required substring and the index
    """
    i, j = 0, 0
    while i < len(str):
        if str[i] != pattern[j]:
            i += 1
        else:
            found = True
            curr = i 
            while curr < len(str) and j < len(pattern):
                if str[curr] != pattern[j]:
                    found = False
                    i += 1
                    j = 0
                    break
                else:
                    curr += 1
                    j += 1
            if found:
                return(str[:i], i)
    return (str, -1)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    str = data[0]  # First input is the string str
    pattern = data[1]  # Second input is the pattern string
    
    # Call user logic function and get the result
    result_substring, index = user_logic(str, pattern)
    
    # Print the result
    print(result_substring, index)

if __name__ == "__main__":
    main()