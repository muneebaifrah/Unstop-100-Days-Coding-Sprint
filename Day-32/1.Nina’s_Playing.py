def solve():
    import sys
    input = sys.stdin.readline

    T = int(input())
    ans = []

    for _ in range(T):
        N = int(input())

        cards = []
        freq = {}
        valid = True

        for _ in range(N):
            a, b = map(int, input().split())
            if a == b:
                valid = False
            cards.append((a, b))
            freq[a] = freq.get(a, 0) + 1
            freq[b] = freq.get(b, 0) + 1

        # Any number appearing more than twice makes it impossible
        if not valid or any(v > 2 for v in freq.values()):
            ans.append("NO")
            continue

        # Build graph: numbers as nodes, cards as edges
        adj = {}
        for a, b in cards:
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, []).append(a)

        visited = set()

        def dfs(start):
            stack = [start]
            nodes = 0
            edges = 0
            while stack:
                u = stack.pop()
                if u in visited:
                    continue
                visited.add(u)
                nodes += 1
                edges += len(adj.get(u, []))
                for v in adj.get(u, []):
                    if v not in visited:
                        stack.append(v)
            return nodes, edges // 2

        ok = True
        for node in adj:
            if node not in visited:
                nodes, edges = dfs(node)
                # If component is a cycle, it must have even length
                if edges == nodes and nodes % 2 == 1:
                    ok = False
                    break

        ans.append("YES" if ok else "NO")

    print("\n".join(ans))


if __name__ == "__main__":
    solve()
                