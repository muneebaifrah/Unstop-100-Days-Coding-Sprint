# Enter your code here. Read input from STDIN. Print output to STDOUT
def count_pairs(n, arr, target):
    freq = {}
    pairs = 0

    for val in arr:
        need = target - val
        if need in freq:
            pairs += freq[need]

        freq[val] = freq.get(val, 0) + 1

    return pairs


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    target = int(data[1+n])

    print(count_pairs(n, arr, target))


if __name__ == "__main__":
    main()