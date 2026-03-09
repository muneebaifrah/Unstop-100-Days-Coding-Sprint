def special_series(A, B, N):
    if N == 1:
        return A
    if N == 2:
        return B

    t1, t2 = A, B
    for _ in range(3, N + 1):
        t3 = abs(t2 - t1)
        t1, t2 = t2, t3
    return t2


# Input
A, B, N = map(int, input().split())

# Output
print(special_series(A, B, N))