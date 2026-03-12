def longest_palindromic_substring(s):
    start, max_len = 0, 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return the length of palindrome and starting index
        return (right - left - 1, left + 1)
    
    for i in range(len(s)):
        # Odd length palindrome
        length1, start1 = expand_around_center(i, i)
        # Even length palindrome
        length2, start2 = expand_around_center(i, i + 1)
        
        if length1 > max_len:
            max_len = length1
            start = start1
        if length2 > max_len:
            max_len = length2
            start = start2
            
    return s[start:start + max_len]

# Read input
s = input().strip()
print(longest_palindromic_substring(s))
                