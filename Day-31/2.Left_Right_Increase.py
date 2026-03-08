import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.read().split()))
    N, P = data[0], data[1]
    A = data[2:]

    # Day when index becomes non-zero
    day = [-1] * N
    q = deque()

    # Initialize queue with initially non-zero elements
    for i in range(N):
        if A[i] != 0:
            day[i] = 0
            q.append(i)

    # BFS to find first day each index becomes non-zero
    while q:
        i = q.popleft()
        if day[i] == P:
            continue
        for ni in (i - 1, i + 1):
            if 0 <= ni < N and day[ni] == -1:
                day[ni] = day[i] + 1
                q.append(ni)

    total_extra = 0

    # For each index, count how many days it receives increments
    for i in range(N):
        if day[i] == -1 or day[i] > P:
            continue

        # Each active neighbor gives +2 per day
        active_days = P - day[i]
        neighbors = 0

        if i - 1 >= 0 and day[i - 1] != -1 and day[i - 1] <= P:
            neighbors += 1
        if i + 1 < N and day[i + 1] != -1 and day[i + 1] <= P:
            neighbors += 1

        total_extra += 2 * neighbors * active_days

    print(total_extra)

if __name__ == "__main__":
    main()
                