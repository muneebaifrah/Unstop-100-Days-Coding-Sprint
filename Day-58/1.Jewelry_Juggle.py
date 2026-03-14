def can_balance_jewelry(a, b, c, d):
    arr = [a, b, c, d]
    total = sum(arr)

    if total % 2 != 0:
        return "NO"

    target = total // 2

    for mask in range(1, 1 << 4):
        s = 0
        for i in range(4):
            if mask & (1 << i):
                s += arr[i]
        if s == target:
            return "YES"

    return "NO"


def main():
    import sys
    data = sys.stdin.read().strip().split()

    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])

    print(can_balance_jewelry(a, b, c, d))


if __name__ == "__main__":
    main()