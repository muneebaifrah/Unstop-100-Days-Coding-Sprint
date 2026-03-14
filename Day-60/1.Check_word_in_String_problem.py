# Placeholder function for user logic
def canFormStrings(S, strArray):
    '''
    Write your logic here.
    Parameters:
        S (string): The base string
        strArray (list of strings): Array of strings
    Returns:
        bool: True if all strings in the array can be formed by combining some of the characters in S, otherwise False
    '''
    # Backtracking solution

    from collections import Counter
    
    # Count available characters in S
    available = Counter(S)
    
    # Backtracking function to check if a word can be formed
    def backtrack(word, index, available_chars):
        if index == len(word):
            return True
        
        ch = word[index]
        if available_chars[ch] > 0:
            # Choose
            available_chars[ch] -= 1
            # Explore
            if backtrack(word, index + 1, available_chars):
                return True
            # Backtrack (undo choice)
            available_chars[ch] += 1
        
        return False
    
    # Check each word in strArray
    for word in strArray:
        if not backtrack(word, 0, available.copy()):
            return False
    
    return True


if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    S = data[0]
    n = int(data[1])
    strArray = data[2:n+2]
    result = canFormStrings(S, strArray)
    print('true' if result else 'false')