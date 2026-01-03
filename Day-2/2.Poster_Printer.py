t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    possible = True
    i = 0

    while i < n:
        if s[i] == 'W':
            i += 1
            continue

        has_B = False
        has_R = False

        while i < n and s[i] != 'W':
            if s[i] == 'B':
                has_B = True
            if s[i] == 'R':
                has_R = True
            i += 1

        if not has_B or not has_R:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")