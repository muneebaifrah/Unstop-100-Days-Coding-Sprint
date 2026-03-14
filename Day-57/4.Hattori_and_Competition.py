def minimum_moves(n, arr):
    if n <= 1:
        return 0

    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])

        if i == curr_end:
            jumps += 1
            curr_end = farthest

            if curr_end >= n - 1:
                return jumps

    return jumps


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    print(minimum_moves(n, arr))


if __name__ == "__main__":
    main()