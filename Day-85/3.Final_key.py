from collections import Counter
def first_uniq_char(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        int: Length from start to the first unique character or -1 if no such character exists
    """
    a=Counter(s)
    for i, ch in enumerate(s):
        if a[ch] == 1:
            return i
    return -1

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    # Call user logic function and print the output
    index = first_uniq_char(s)
    if index == -1:
        print(-1)
    else:
        print(len(s[:index]))

if __name__ == "__main__":
    main()