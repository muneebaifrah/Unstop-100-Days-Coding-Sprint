def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def max_subseq_prime_diff_two(s):
    dp = [0] * 128  # ASCII values from 0 to 127

    for c in s:
        ascii_val = ord(c)
        # max of previous valid subsequences ending with ascii_val - 2 or ascii_val + 2
        dp[ascii_val] = max(dp[ascii_val], max(dp[ascii_val - 2], dp[ascii_val + 2]) + 1)

    max_len = max(dp)

    if max_len <= 1:
        return 0
    return 1 if is_prime(max_len) else 0

# Input
s = input().strip()

# Output
print(max_subseq_prime_diff_two(s))