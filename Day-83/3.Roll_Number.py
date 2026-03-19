def user_logic(A1, A2, N):
    """
    Write your logic here.
    Parameters:
        A1 (int): Roll number of the 1st student
        A2 (int): Roll number of the 2nd student
        N (int): Your position
    Returns:
        int: Your roll number
    """
    return A1+(N-1)*(A2-A1)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    A1 = int(data[0])
    A2 = int(data[1])
    N = int(data[2])
    
    # Call user logic function and print the output
    result = user_logic(A1, A2, N)
    print(result)

if __name__ == "__main__":
    main()