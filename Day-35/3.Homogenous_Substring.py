MOD = 10**9 + 7

def homogenous_substring(s):
    ans = 0
    count = 0
    prev = ''

    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch
        ans = (ans + count) % MOD

    return ans


s = input().strip()
print(homogenous_substring(s))
                