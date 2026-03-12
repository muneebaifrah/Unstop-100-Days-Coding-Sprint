def solve():
    q = int(input())
    a = list(map(int, input().split()))

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    results = []
    for num in a:
        if is_prime(num):
            results.append('1')
        else:
            results.append('0')

    print("".join(results))

solve()
                