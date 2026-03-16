import sys

def number_of_days_when_subsequence(S, T):
    n, m = len(S), len(T)

    ALPHA = 26
    nxt = [[-1] * ALPHA for _ in range(n + 1)]
    for c in range(ALPHA):
        nxt[n][c] = -1
    for i in range(n - 1, -1, -1):
        for c in range(ALPHA):
            nxt[i][c] = nxt[i + 1][c]
        nxt[i][ord(S[i]) - ord('a')] = i

    present = set(S)
    for ch in T:
        if ch not in present:
            return -1

    days = 1
    pos = 0

    for ch in T:
        idx = ord(ch) - ord('a')
        if pos == n:
            days += 1
            pos = 0
        if nxt[pos][idx] != -1:
            pos = nxt[pos][idx] + 1
        else:
            days += 1
            pos = 0
            pos = nxt[pos][idx] + 1

    return days

def main():
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    S, T = data[0], data[1]
    ans = number_of_days_when_subsequence(S, T)
    print(ans)

if __name__ == "__main__":
    main()