def queens_attack_the_king(queens, king):
    qset = {(x, y) for x, y in queens}
    kx, ky = king

    # Required direction order:
    # NW, N, NE, W, E, SW, S, SE
    dirs = [
        (-1, -1),  # NW
        (-1, 0),   # N
        (-1, 1),   # NE
        (0, -1),   # W
        (0, 1),    # E
        (1, -1),   # SW
        (1, 0),    # S
        (1, 1)     # SE
    ]

    res = []
    for dx, dy in dirs:
        x, y = kx + dx, ky + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if (x, y) in qset:
                res.append([x, y])   # nearest queen in this direction
                break
            x += dx
            y += dy

    return res


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    queens = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        queens.append([x, y])
        idx += 2

    king = [int(data[idx]), int(data[idx + 1])]

    ans = queens_attack_the_king(queens, king)

    if ans:
        print(" ".join(f"{x} {y}" for x, y in ans))
    else:
        print("")

if __name__ == "__main__":
    main()