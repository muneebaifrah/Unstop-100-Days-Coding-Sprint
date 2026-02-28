# Placeholder function for user logic
def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

if __name__ == "__main__":
    n = int(input())  # Read the number of strings
    
    if n <= 0:
        print("")
    else:
        words = input().split()  # Read the list of strings
        print(firstPalindrome(words))