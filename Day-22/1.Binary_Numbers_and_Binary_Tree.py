class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def make_tree(idx, n, arr):
    if idx >= n:
        return None

    root = TreeNode(arr[idx])
    root.left = make_tree(2*idx + 1, n, arr)
    root.right = make_tree(2*idx + 2, n, arr)

    return root


def dfs(node, current):
    if not node:
        return 0

    current = current * 2 + node.val

    if not node.left and not node.right:
        return current

    return dfs(node.left, current) + dfs(node.right, current)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))

    root = make_tree(0, n, arr)
    ans = dfs(root, 0)

    print(ans)