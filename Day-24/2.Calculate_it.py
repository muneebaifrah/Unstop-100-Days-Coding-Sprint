def count_expressible_numbers(X, Y):
    values = set()

    a = 1
    while a <= Y:
        b = 1
        while a * b <= Y:
            values.add(a * b)
            b *= 3
        a *= 2

    count = 0
    for v in values:
        if X <= v <= Y:
            count += 1

    return count


# Input
X, Y = map(int, input().split())

# Output
print(count_expressible_numbers(X, Y))