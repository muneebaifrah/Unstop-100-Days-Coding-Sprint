MOD = 998244353

def user_logic(N):
    dp = [1]*10   # index 1..9 used

    for _ in range(N-1):
        new = [0]*10
        for d in range(1,10):
            new[d] = dp[d]
            if d > 1:
                new[d] = (new[d] + dp[d-1]) % MOD
            if d < 9:
                new[d] = (new[d] + dp[d+1]) % MOD
        dp = new

    return sum(dp[1:10]) % MOD


# input handling
N = int(input())
print(user_logic(N))