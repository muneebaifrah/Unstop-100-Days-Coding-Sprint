def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Length of the string
        s (str): String to be checked
    Returns:
        str: The output string based on the problem statement
    """
    from collections import Counter
    freq = Counter(s)
    odd_chars = [ch for ch, count in freq.items() if count % 2 == 1]
    k = len(odd_chars)
    if k <= 1:
        return "-1"
    needed = k - 1
    return "".join(odd_chars[:needed])


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    s = data[1]  # Second input is the string
    
    # Call user logic function and print the output
    result = user_logic(n, s)
    print(result)


if __name__ == "__main__":
    main()