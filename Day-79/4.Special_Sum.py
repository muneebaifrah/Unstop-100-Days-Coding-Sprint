import sys

def main():
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    nums = list(map(int, data[1:]))

    special_sum = 0
    prev = None

    for v in nums:
        if v != prev:           # unique element
            special_sum += 1 << v   # 2^v
            prev = v

    print(special_sum)

if __name__ == "__main__":
    main()