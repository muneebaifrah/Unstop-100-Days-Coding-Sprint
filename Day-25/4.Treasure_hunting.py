from functools import lru_cache

def user_logic(n, a, b):

    @lru_cache(None)
    def dp(mask):
        i = bin(mask).count("1")
        if i == n:
            return 0

        ans = float('inf')

        for j in range(n):
            if not (mask & (1 << j)):
                ans = min(ans, (a[i] ^ b[j]) + dp(mask | (1 << j)))

        return ans

    return dp(0)


# input handling
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(user_logic(n, a, b))