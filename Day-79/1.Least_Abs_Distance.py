def min_distances_to_char():
    s = input().strip()
    ch = input().strip()

    n = len(s)
    result = [0] * n

    # First pass: Left to Right
    prev = float('-inf')
    for i in range(n):
        if s[i] == ch:
            prev = i
        result[i] = abs(i - prev)

    # Second pass: Right to Left
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == ch:
            prev = i
        result[i] = min(result[i], abs(i - prev))

    print(' '.join(map(str, result)))

# Run the function
min_distances_to_char()