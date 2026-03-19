def user_logic(n, arr):
    called = set()
    
    # Students act in order
    for i in range(1, n + 1):
        if i not in called:
            called.add(arr[i - 1])
    
    # Roll numbers never called
    result = [i for i in range(1, n + 1) if i not in called]
    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and get the result
    result = user_logic(n, arr)
    
    # Print the output in the required format
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()