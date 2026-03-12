import sys

def longestPalindrome(s):
    if not s or len(s) < 1:
        return ""
    
    start = 0
    end = 0
    
    def expandAroundCenter(left, right):
        # Expand as long as indices are in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome found
        # (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1

    for i in range(len(s)):
        # Case 1: Odd length palindrome (center is s[i])
        len1 = expandAroundCenter(i, i)
        # Case 2: Even length palindrome (center is between s[i] and s[i+1])
        len2 = expandAroundCenter(i, i + 1)
        
        # Take the maximum of the two expansion types
        max_len = max(len1, len2)
        
        # Update the global start and end indices if a longer palindrome is found
        if max_len > (end - start):
            # Calculate new start/end indices based on center i and max_len
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end + 1]

if __name__ == "__main__":
    # Reading input and stripping whitespace
    line = sys.stdin.read().strip()
    if line:
        result = longestPalindrome(line)
        print(result)