def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


def user_logic(n):
    ans = -1
    k = 1

    while (1 << (k-1)) <= n:
        val = (1 << k) - 1
        if is_prime(val):
            ans = val
        k += 1

    return ans


def main():
    import sys
    n = int(sys.stdin.read().strip())
    print(user_logic(n))


if __name__ == "__main__":
    main()