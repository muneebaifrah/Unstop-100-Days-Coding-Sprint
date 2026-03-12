def optimal_game_winner(balls):
    n = len(balls)
    dp = [[0] * n for _ in range(n)]

    # Fill the table for subproblems of length 1 (only one box available)
    for i in range(n):
        dp[i][i] = balls[i]

    # Solve for subproblems of increasing length
    for length in range(2, n + 1):  # Length of subarray
        for i in range(n - length + 1):
            j = i + length - 1
            take_i = balls[i] + min(dp[i + 2][j] if i + 2 <= j else 0,
                                    dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            take_j = balls[j] + min(dp[i][j - 2] if i <= j - 2 else 0,
                                    dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            dp[i][j] = max(take_i, take_j)

    # Aryan's best possible score
    aryan_score = dp[0][n - 1]
    total_balls = sum(balls)

    # If Aryan collects at least half the total balls, he wins or ties
    print("Aryan" if aryan_score * 2 >= total_balls else "Ankit")

# Input handling
N = int(input().strip())
balls = list(map(int, input().strip().split()))

optimal_game_winner(balls)