def calculate_max_score(n, s):
    MOD = 10**9 + 7

    # Convert characters to values (a=1, b=2, ..., z=26)
    values = [ord(c) - 96 for c in s]

    # To maximize score, place smallest values at smallest powers
    values.sort()

    power = 1  # 26^0
    result = 0

    for v in values:
        result = (result + v * power) % MOD
        power = (power * 26) % MOD

    return result


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    s = data[1]
    print(calculate_max_score(n, s))


if __name__ == "__main__":
    main()
                