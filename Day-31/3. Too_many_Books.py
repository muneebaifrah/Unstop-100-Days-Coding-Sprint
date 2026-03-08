import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]

    lis = []
    for x in a:
        pos = bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x

    print(len(lis))

if __name__ == "__main__":
    main()
                