import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

vowels = set("aeiou")
result = []
i = 0

while i < n:
    # Check for consecutive vowels
    if s[i] in vowels:
        j = i
        while j < n and s[j] in vowels:
            j += 1
        length = j - i
        # If exactly two consecutive vowels
        if length == 2:
            result.append(s[i])
            result.append(s[i+1])
            result.append('$')
        else:
            # Append the whole sequence as-is
            result.extend(s[i:j])
        i = j
    else:
        result.append(s[i])
        i += 1

print("".join(result))