def solve():
    n = int(input().strip())
    pos = list(map(int, input().split()))
    m_line = input().split()
    if len(m_line) == 1:  # m and s are given on separate lines
        m = int(m_line[0])
        s = input().strip()
    else:  # m and s given on same line
        m = int(m_line[0])
        s = m_line[1]

    start_r, start_c = pos
    ans = [0] * m

    # Directions
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for i in range(m):
        r, c = start_r, start_c
        cnt = 0
        for j in range(i, m):
            dr, dc = moves[s[j]]
            r, c = r + dr, c + dc
            if not (0 <= r < n and 0 <= c < n):
                break
            cnt += 1
        ans[i] = cnt

    print(*ans)


if __name__ == "__main__":
    solve()
                