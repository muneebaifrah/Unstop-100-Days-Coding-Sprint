import sys

def is_good_number(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        s = 0
        while n > 0:
            d = n % 10
            s += d * d
            n //= 10
        n = s
    return n == 1

def main():
    n = int(sys.stdin.read().strip())
    print(str(is_good_number(n)).lower())

if __name__ == "__main__":
    main()