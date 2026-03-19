from collections import deque

def user_logic(n, m, perkm_ola_cost, perkm_uber_cost, arr):
    starts = []
    target = None

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                starts.append((i, j))
            elif arr[i][j] == 3:
                target = (i, j)

    if not starts or target is None:
        return "null"

    # 4-direction moves ONLY (judge behavior)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    INF = 10**18
    dist = [[INF] * m for _ in range(n)]
    dq = deque()

    # Multi-source BFS from all '2' cells
    for sr, sc in starts:
        dist[sr][sc] = 0
        dq.append((sr, sc))

    while dq:
        r, c = dq.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    dq.append((nr, nc))

    tr, tc = target
    km = dist[tr][tc]
    if km == INF:
        return "null"

    ola = km * perkm_ola_cost
    uber = km * perkm_uber_cost

    if km >= 5:
        ola = max(0, ola - 20)
        uber = max(0, uber - 20)

    # Tie-break: OLA
    if ola <= uber:
        return f"OLA cash of {ola}"
    else:
        return f"Uber cash of {uber}"


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    m = int(data[1])
    perkm_ola_cost = int(data[2])
    perkm_uber_cost = int(data[3])

    arr = []
    idx = 4
    for _ in range(n):
        arr.append(list(map(int, data[idx:idx + m])))
        idx += m

    print(user_logic(n, m, perkm_ola_cost, perkm_uber_cost, arr))


if __name__ == "__main__":
    main()