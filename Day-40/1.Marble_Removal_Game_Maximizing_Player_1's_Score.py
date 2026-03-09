def remove_marbles(n, k, sequence):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        best = 0
        for a in sequence:
            if a <= i:
                best = max(best, i - dp[i - a])
        dp[i] = best

    return dp[n]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    k = int(data[1])
    sequence = list(map(int, data[2:2 + k]))

    print(remove_marbles(n, k, sequence))


if __name__ == "__main__":
    main()