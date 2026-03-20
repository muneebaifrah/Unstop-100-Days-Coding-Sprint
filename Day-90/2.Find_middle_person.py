import sys

def findMiddleEarth(a1, a2):
    # Ensure a1 is the smaller array
    if len(a1) > len(a2):
        a1, a2 = a2, a1

    m, n = len(a1), len(a2)
    low, high = 0, m
    total = m + n

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (total + 1) // 2 - cut1

        l1 = float('-inf') if cut1 == 0 else a1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else a2[cut2 - 1]
        r1 = float('inf') if cut1 == m else a1[cut1]
        r2 = float('inf') if cut2 == n else a2[cut2]

        if l1 <= r2 and l2 <= r1:
            if total % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return max(l1, l2)

        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1


def main():
    input = sys.stdin.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    a1 = list(map(int, data[2:m+2]))
    a2 = list(map(int, data[m+2:m+n+2]))
    print(f'{findMiddleEarth(a1, a2):.5f}')


if __name__ == '__main__':
    main()