def user_logic(n, m, x):
    """
    Write your logic here.
    Parameters:
        n (int): The integer N
        m (int): The integer M
        x (int): The integer X
    Returns:
        int: Computed result based on the problem statement
    """

    MOD = 998244353

    from functools import lru_cache


    # Use memoization to avoid recomputation
    @lru_cache(None)
    def dp(i, xor_val, last_val):
        if i == 0:
            return 1 if xor_val == 0 else 0

        res = 0
        for val in range(last_val, m + 1):
            res = (res + dp(i - 1, xor_val ^ val, val)) % MOD
        return res

    return dp(n, x, 0)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    m = int(data[1])
    x = int(data[2])
    
    # Call user logic function and print the output
    result = user_logic(n, m, x)
    print(result)


if __name__ == "__main__":
    main()