from collections import Counter
def user_logic(n, s):
    """
    Write your logic here.
    Parameters:
        n (int): Number of characters in the string
        s (str): The input string
    Returns:
        str: The special character if exists, otherwise '-1'
    """
    l=len(s)
    c=Counter(s)
    for chr,cnt in c.items():
        if cnt==1:
            return chr
       
    return -1
    

import sys
input = sys.stdin.read

data = input().strip().split()

n = int(data[0])  # First input is the integer n
s = data[1]  # Second input is the string

# Call user logic function and print the output
result = user_logic(n, s)
print(result)