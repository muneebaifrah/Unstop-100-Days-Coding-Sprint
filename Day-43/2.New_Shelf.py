def calculate_inverse_of_lis_length(n, heights):
    MOD = 1000007  # 10^6 + 7
    from bisect import bisect_left

    # Compute the length of the longest strictly increasing subsequence (LIS)
    dp = []
    for h in heights:
        pos = bisect_left(dp, h)
        if pos == len(dp):
            dp.append(h)
        else:
            dp[pos] = h
    lis_length = len(dp)
    
    # Compute the modular inverse of lis_length modulo MOD using the Extended Euclidean Algorithm
    inverse = modInverse(lis_length, MOD)
    return inverse

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modInverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise Exception("Inverse does not exist")
    else:
        return x % m

if __name__ == '__main__':
    n = int(input().strip())
    heights = list(map(int, input().split()))
    result = calculate_inverse_of_lis_length(n, heights)
    print(result)
                