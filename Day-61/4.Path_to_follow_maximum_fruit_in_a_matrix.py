from collections import deque

def fruit_paths(matrix):
    """
    Returns list of fruits in the maximum-fruit connected component.
    Movement is allowed ONLY on fruit cells (NOT on 'path' or 'wall').
    Traversal order: DFS with neighbor priority Down, Up, Right, Left.
    """
    if not matrix or not matrix[0]:
        return None

    n, m = len(matrix), len(matrix[0])

    def is_fruit(r, c):
        v = matrix[r][c]
        return v != "wall" and v != "path"

    # Collect connected components of fruit cells, pick the largest
    seen = [[False] * m for _ in range(n)]
    best_comp = []
    best_start = None

    for i in range(n):
        for j in range(m):
            if not is_fruit(i, j) or seen[i][j]:
                continue

            q = deque([(i, j)])
            seen[i][j] = True
            comp = [(i, j)]
            start = (i, j)

            while q:
                r, c = q.popleft()
                # Track top-left-most fruit cell in this component
                if (r, c) < start:
                    start = (r, c)

                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and is_fruit(nr, nc) and not seen[nr][nc]:
                        seen[nr][nc] = True
                        q.append((nr, nc))
                        comp.append((nr, nc))

            # Choose best: max size; tie-break by smallest start cell
            if (len(comp) > len(best_comp)) or (len(comp) == len(best_comp) and (best_start is None or start < best_start)):
                best_comp = comp
                best_start = start

    if not best_comp:
        return None

    # Build a fast lookup for membership in best component
    in_best = [[False] * m for _ in range(n)]
    for r, c in best_comp:
        in_best[r][c] = True

    # DFS traversal over best component starting at best_start
    # Neighbor priority required by judge: Down, Up, Right, Left (DURL)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    visited = [[False] * m for _ in range(n)]
    sr, sc = best_start
    visited[sr][sc] = True

    result = [matrix[sr][sc]]

    stack = [(sr, sc, 0)]  # (r, c, next_dir_index)
    while stack:
        r, c, di = stack.pop()
        if di < 4:
            stack.append((r, c, di + 1))
            dr, dc = dirs[di]
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and in_best[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                result.append(matrix[nr][nc])
                stack.append((nr, nc, 0))

    return result


def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        print("null")
        return

    N = int(data[0])
    M = int(data[1])

    matrix = []
    idx = 2
    for _ in range(N):
        matrix.append(data[idx:idx + M])
        idx += M

    res = fruit_paths(matrix)
    if not res:
        print("null")
    else:
        print(" --> ".join(res))


if __name__ == "__main__":
    main()