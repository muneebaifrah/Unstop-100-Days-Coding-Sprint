import sys

MOD = 1000000007

def is_248(x):
    c2 = c4 = c8 = 0

    while x:
        d = x % 10
        if d == 2:
            c2 += 1
        elif d == 4:
            c4 += 1
        elif d == 8:
            c8 += 1
        x //= 10

    return c2 >= 1 and c2 == c4 == c8


def main():
    N = int(sys.stdin.readline().strip())

    ans = 0
    for i in range(1, N + 1):
        if is_248(i):
            ans += 1

    print(ans % MOD)


if __name__ == "__main__":
    main()