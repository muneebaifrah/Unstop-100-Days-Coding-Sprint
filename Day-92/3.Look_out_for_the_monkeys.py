def count_visible_monkeys(heights):
    n = len(heights)
    result = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        count = 0
        while stack and heights[i] > heights[stack[-1]]:
            count += 1
            stack.pop()
        if stack:
            count += 1
        result[i] = count
        stack.append(i)

    return result

# Input handling
if __name__ == "__main__":
    N = int(input())
    heights = list(map(int, input().split()))
    output = count_visible_monkeys(heights)
    print(' '.join(map(str, output)))