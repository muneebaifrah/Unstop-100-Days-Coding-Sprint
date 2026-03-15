def count_filo_ways(n):
    # remove factors of 2
    while n % 2 == 0:
        n //= 2

    ways = 1
    d = 3

    while d * d <= n:
        count = 0
        while n % d == 0:
            n //= d
            count += 1
        ways *= (count + 1)
        d += 2

    if n > 1:
        ways *= 2

    return ways


if __name__ == "__main__":
    n = int(input())
    print(count_filo_ways(n))