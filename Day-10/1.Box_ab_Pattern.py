def follows_ab_pattern(s):
    seen_b = False

    for ch in s:
        if ch == 'b':
            seen_b = True
        elif ch == 'a' and seen_b:
            return "NO"

    return "YES"


s = input().strip()
print(follows_ab_pattern(s))