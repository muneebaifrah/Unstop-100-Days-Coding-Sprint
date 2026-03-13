def longest_palindromic_subsequence(s):
    """
    Write your logic here.
    Parameters:
        s (str): Input string
    Returns:
        int: Length of the longest palindromic subsequence
    """
    n = len(s)
    dp = [0] * n
    for i in reversed(range(n)):
        dp[i] = 1
        prev = 0
        for j in range(i + 1, n):
            temp = dp[j]
            if s[i] == s[j]:
                dp[j] = 2 + prev
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp
    return dp[-1]


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the single line input string

    # Call user logic function and print the output
    result = longest_palindromic_subsequence(s)
    print(result)


if __name__ == "__main__":
    main()