def is_similar(a, b):
    diff = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff.append(i)
            if len(diff) > 4:
                return False

    if len(diff) == 0:
        return True
    if len(diff) == 4:
        i, j, k, l = diff
        return a[i] == b[j] and a[j] == b[i] and a[k] == b[l] and a[l] == b[k]
    return False


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    pa = find(a, parent)
    pb = find(b, parent)
    if pa != pb:
        parent[pb] = pa


def get_anagram_groups(strs):
    n = len(strs)
    parent = list(range(n))

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                union(i, j, parent)

    groups = set()
    for i in range(n):
        groups.add(find(i, parent))

    return len(groups)


if __name__ == "__main__":
    n = int(input())
    arr = input().split()
    groups = get_anagram_groups(arr)
    print(groups)