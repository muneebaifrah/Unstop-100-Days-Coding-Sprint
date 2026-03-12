import math

def can_bolt_win(N: int) -> bool:
    dp = [False] * (N + 1)
    dp[0] = False  # no stones means lose
    
    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            if dp[i - j*j] == False:  # opponent loses if we move here
                dp[i] = True
                break
            j += 1
    
    return dp[N]

# Input reading
N = int(input())
print("True" if can_bolt_win(N) else "False")
                