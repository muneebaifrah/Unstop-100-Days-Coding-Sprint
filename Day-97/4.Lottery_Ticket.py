def LuckyArray(arr, n):
    arr = [x for x in arr if x >= 0]
    m = len(arr)
    if m == 0:
        return []

    left = [-1] * m
    right = [m] * m
    stack = []

    for i in range(m):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()
    for i in range(m - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = stack[-1] if stack else m
        stack.append(i)

    res = [0] * (m + 1)

    for i in range(m):
        length = right[i] - left[i] - 1
        res[length] = max(res[length], arr[i])

    for i in range(m - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])

    return res[1:]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))
    result = LuckyArray(arr, n)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    
    main()