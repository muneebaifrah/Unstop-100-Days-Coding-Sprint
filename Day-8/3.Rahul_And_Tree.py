class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildBST(arr, l, r):
    if l > r:
        return None
    mid = (l + r + 1) // 2
    root = Node(arr[mid])
    root.left = buildBST(arr, l, mid - 1)
    root.right = buildBST(arr, mid + 1, r)
    return root

def preorder(root):
    if not root:
        return
    left = root.left.val if root.left else "."
    right = root.right.val if root.right else "."
    print(f"{left} <- {root.val} -> {right}")
    preorder(root.left)
    preorder(root.right)

def solve():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    root = buildBST(arr, 0, n - 1)
    preorder(root)

solve()
