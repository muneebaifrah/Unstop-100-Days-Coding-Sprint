def longest_subsequence(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string consisting of lowercase letters
    Returns:
        int: Length of the longest subsequence satisfying the condition
    """
    dp = [0] * 26  # dp[i] stores longest subsequence ending with chr(i + ord('a'))

    for ch in s:
        idx = ord(ch) - ord('a')
        max_len = 0
        for i in range(26):
            if abs(i - idx) != 1:  # not adjacent in alphabet
                max_len = max(max_len, dp[i])
        dp[idx] = max(dp[idx], max_len + 1)

    return max(dp)


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    
    # Call the longest_subsequence function and print the result
    result = longest_subsequence(s)
    print(result)

if __name__ == "__main__":
    main()