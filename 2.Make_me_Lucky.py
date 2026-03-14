def make_me_lucky(S, U):
    stack = []
    m = len(U)

    for ch in S:
        stack.append(ch)

        if len(stack) >= m and ''.join(stack[-m:]) == U:
            for _ in range(m):
                stack.pop()

    return ''.join(stack)


def main():
    S = input().strip()
    U = input().strip()
    print(make_me_lucky(S, U))


if __name__ == "__main__":
    main()