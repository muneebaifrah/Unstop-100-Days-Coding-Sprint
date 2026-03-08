def check_word_break(goal, target_words):
    word_set = set(target_words)
    n = len(goal)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for w in word_set:
            l = len(w)
            if i >= l and dp[i - l] and goal[i - l:i] == w:
                dp[i] = True
                break

    return 1 if dp[n] else 0


n = int(input())
goal = input().strip()
target_words = input().split()

print(check_word_break(goal, target_words))