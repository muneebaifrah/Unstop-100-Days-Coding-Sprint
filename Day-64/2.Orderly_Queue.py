def smallest_lex_string(s, k):
    if k == 1:
        # Try all rotations of s
        return min(s[i:] + s[:i] for i in range(len(s)))
    else:
        # Sort the string when k >= 2
        return ''.join(sorted(s))

# Read input
s = input().strip()
k = int(input())

# Get and print the result
print(smallest_lex_string(s, k))