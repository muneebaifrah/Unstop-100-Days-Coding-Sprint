import sys
sys.setrecursionlimit(10**7)

def calculate_subordinates(V, hierarchy):
    tree = [[] for _ in range(V+1)]

    for i, boss in enumerate(hierarchy, start=2):
        tree[boss].append(i)

    ans = [0]*(V+1)

    def dfs(node):
        total = 0
        for child in tree[node]:
            total += 1 + dfs(child)
        ans[node] = total
        return total

    dfs(1)

    return ans[1:]


# -------- Input ----------
V = int(input().strip())
hierarchy = list(map(int, input().split()))

result = calculate_subordinates(V, hierarchy)

print(*result)