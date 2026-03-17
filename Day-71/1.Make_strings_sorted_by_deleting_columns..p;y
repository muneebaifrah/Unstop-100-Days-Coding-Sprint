def minDeletionSize(strs):
    n = len(strs)
    m = len(strs[0])

    dp = [1] * m
    best = 1

    for j in range(m):
        for i in range(j):
            good = True
            for r in range(n):
                if strs[r][i] > strs[r][j]:
                    good = False
                    break
            if good:
                dp[j] = max(dp[j], dp[i] + 1)
        best = max(best, dp[j])

    return m - best

# robust input handling
import sys
data = sys.stdin.read().strip().split()

if not data:
    print(0)
else:
    n = int(data[0])
    strs = []

    idx = 1
    # if there are exactly n more tokens and each token length equals first string length,
    # assume they are on one line
    if len(data) == n + 1:
        strs = data[1:]
    else:
        # otherwise read next n strings from tokens (one per line or spaced)
        for i in range(n):
            strs.append(data[idx])
            idx += 1

    print(minDeletionSize(strs))