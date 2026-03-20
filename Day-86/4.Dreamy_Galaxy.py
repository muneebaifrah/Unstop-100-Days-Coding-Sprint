import sys

def max_moons():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    max_sum = 0
    for _ in range(N):
        row = [int(next(it)) for _ in range(M)]
        total = sum(row)
        if total > max_sum:
            max_sum = total
    print(max_sum)

if __name__ == "__main__":
    max_moons()