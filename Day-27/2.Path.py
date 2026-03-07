def user_logic(n, s):
    keys = [0]*26
    buy = 0

    for ch in s:
        if ch.islower():
            keys[ord(ch) - ord('a')] += 1
        else:
            idx = ord(ch) - ord('A')
            if keys[idx] > 0:
                keys[idx] -= 1
            else:
                buy += 1

    return buy


n = int(input().strip())
s = input().strip()

print(user_logic(n, s))