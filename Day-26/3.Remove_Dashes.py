def process_dashes(n, s):
    stack = []

    for char in s:
        if char == '_':
            if stack:
                stack.pop()  # Remove the closest letter to the left
            else:
                # No letter to remove → impossible
                print("-1")
                return
        else:
            stack.append(char)

    if not stack:
        print("-1")
    else:
        print("".join(stack))


# Read input
n = int(input().strip())
s = input().strip()

process_dashes(n, s)