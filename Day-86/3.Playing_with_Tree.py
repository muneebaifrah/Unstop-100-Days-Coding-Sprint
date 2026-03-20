class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def lowest_common_ancestor(root, p, q):
    while root:
        if p < root.val and q < root.val:
            root = root.left
        elif p > root.val and q > root.val:
            root = root.right
        else:
            return root.val

# Driver code
if __name__ == "__main__":
    n = int(input().strip())
    nodes = list(map(int, input().split()))
    x, y = map(int, input().split())

    # Build BST from given nodes
    root = None
    for val in nodes:
        root = insert(root, val)

    print(lowest_common_ancestor(root, x, y))