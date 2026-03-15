def min_distance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # insert all characters

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )

    return dp[m][n]

# Input and Output
if __name__ == "__main__":
    word1 = input().strip()
    word2 = input().strip()
    print(min_distance(word1, word2))