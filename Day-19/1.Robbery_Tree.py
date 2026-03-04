class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertLevelOrder(arr, i):
    if i >= len(arr) or arr[i] == "null":
        return None

    root = TreeNode(int(arr[i]))
    root.left = insertLevelOrder(arr, 2 * i + 1)
    root.right = insertLevelOrder(arr, 2 * i + 2)

    return root


def robTree(node):
    if not node:
        return (0, 0)  # (rob_this, not_rob_this)

    left = robTree(node.left)
    right = robTree(node.right)

    # If we rob this node
    rob_this = node.val + left[1] + right[1]

    # If we don't rob this node
    not_rob_this = max(left) + max(right)

    return (rob_this, not_rob_this)


# Input
arr = input().split()

# Build Tree
root = insertLevelOrder(arr, 0)

# Compute result
result = max(robTree(root))

print(result)