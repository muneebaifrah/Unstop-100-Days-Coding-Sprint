import sys

def solve():
    data = sys.stdin.buffer.read()
    ndata = len(data)
    i = 0

    def next_int():
        nonlocal i
        # skip spaces/newlines
        while i < ndata and data[i] <= 32:
            i += 1
        num = 0
        # numbers are positive as per constraints
        while i < ndata and data[i] > 32:
            num = num * 10 + (data[i] - 48)
            i += 1
        return num

    T = next_int()

    out = bytearray()  # faster than list of strings + join for huge output

    for _ in range(T):
        N = next_int()
        ans = next_int()
        # AND all numbers
        for _ in range(N - 1):
            ans &= next_int()
        out.extend(str(ans).encode())  # IMPORTANT: concatenated output, no newline

    sys.stdout.buffer.write(out)

if __name__ == "__main__":
    solve()