def petrol_price_days(n, prices):
    ans = [0] * n
    stack = []

    for i in range(n):
        while stack and prices[i] > prices[stack[-1]]:
            idx = stack.pop()
            ans[idx] = i - idx
        stack.append(i)

    return ans


def main():
    import sys
    data = sys.stdin.read().split()

    nums = []
    for x in data:
        if x.lstrip('-').isdigit():
            nums.append(int(x))

    n = nums[0]
    prices = nums[1:n+1]

    result = petrol_price_days(n, prices)
    print(*result)


if __name__ == "__main__":
    main()