MOD = 10**9 + 7

def illusion_of_array(n, arr):

    stack = []
    left = [0]*n
    right = [0]*n

    # previous smaller
    for i in range(n):
        count = 1
        while stack and stack[-1][0] > arr[i]:
            count += stack[-1][1]
            stack.pop()
        left[i] = count
        stack.append((arr[i], count))

    stack = []

    # next smaller or equal
    for i in range(n-1, -1, -1):
        count = 1
        while stack and stack[-1][0] >= arr[i]:
            count += stack[-1][1]
            stack.pop()
        right[i] = count
        stack.append((arr[i], count))

    ans = 0

    for i in range(n):
        ans = (ans + arr[i]*left[i]*right[i]) % MOD

    return ans


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(illusion_of_array(n, arr))