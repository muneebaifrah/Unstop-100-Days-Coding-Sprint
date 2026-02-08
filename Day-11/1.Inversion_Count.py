import sys
input = sys.stdin.read

def msb_pos(x):
    if x == 0:
        return -1
    return x.bit_length() - 1

def main():
    data = input().strip().split()
    n = int(data[0])
    arr = list(map(int, data[1:]))

    from collections import defaultdict
    freq = defaultdict(int)

    for num in arr:
        freq[msb_pos(num)] += 1

    ans = 0
    for f in freq.values():
        ans += f * (f - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()