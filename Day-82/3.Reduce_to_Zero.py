def can_convert_to_zero(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        str: "YES" or "NO" based on the problem statement
    """
    a, b, c = map(int, s.split('-'))
    total=a+b+c
    e=total%2==0
    max_val = max(a, b, c)

    if total % 2 == 0 and max_val <= total // 2:
        return "YES"
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read
    
    # Read the input string
    s = input().strip()
    
    # Call user logic function and print the output
    result = can_convert_to_zero(s)
    print(result)


if __name__ == "__main__":
    main()