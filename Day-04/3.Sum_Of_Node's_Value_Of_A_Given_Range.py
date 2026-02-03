class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def range_sum_bst(root, start, end):
    if root is None:
        return 0
    if root.val < start:
        return range_sum_bst(root.right, start, end)
    if root.val > end:
        return range_sum_bst(root.left, start, end)
    return (root.val +
            range_sum_bst(root.left, start, end) +
            range_sum_bst(root.right, start, end))

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    start, end = map(int, input().split())

    root = None
    for v in values:
        root = insert_into_bst(root, v)

    print(range_sum_bst(root, start, end))
