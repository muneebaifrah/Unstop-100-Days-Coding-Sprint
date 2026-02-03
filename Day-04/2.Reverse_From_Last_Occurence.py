def transform_string(s, ch):
    index = s.rfind(ch)
    if index == -1:
        return s
    return s[:index] + s[index:][::-1]

s, ch = input().split()
print(transform_string(s, ch))
