from collections import Counter
def remove_characters(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        str: Resultant string after removing characters based on given conditions
    """
    freq = Counter(s)
    return ''.join(
        char for char in s
        if freq[char] % (ord(char) - ord('a') + 1) != 0
    )


    

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the single input string and strip any extra whitespace
    
    # Call the user logic function and print the output
    result = remove_characters(s)
    print(result)

if __name__ == "__main__":
    main()