def min_insertions_to_palindrome(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Fill the table for substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n - 1]

# Input reading
s = input().strip()

# Output result
print(min_insertions_to_palindrome(s))