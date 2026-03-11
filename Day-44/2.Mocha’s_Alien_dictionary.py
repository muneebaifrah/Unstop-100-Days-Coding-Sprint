def can_segment(s, wordDict):
    word_set = set(wordDict)  # O(1) lookups
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # base case: empty string

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

# Input Handling
s = input().strip()
n = int(input())
wordDict = [input().strip() for _ in range(n)]

# Output Result
print("true" if can_segment(s, wordDict) else "false")
                