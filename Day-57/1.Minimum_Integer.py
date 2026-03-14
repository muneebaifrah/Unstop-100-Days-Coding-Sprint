def user_logic(n, arr):
    ans = arr[0]
    for i in range(1, n):
        ans &= arr[i]
    return ans


def main():
    import sys
    data = sys.stdin.read().split()

    nums = []
    for x in data:
        if x.isdigit():
            nums.append(int(x))

    n = nums[0]
    arr = nums[1:n+1]

    result = user_logic(n, arr)
    print(result)


if __name__ == "__main__":
    main()