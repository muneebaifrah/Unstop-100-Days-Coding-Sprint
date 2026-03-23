import sys

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def build_tree(n, sweetness, edges):
    nodes = {i: TreeNode(sweetness[i-1]) for i in range(1, n+1)}

    for i in range(n):
        l, r = edges[i]
        if l != -1:
            nodes[i+1].left = nodes[l]
        if r != -1:
            nodes[i+1].right = nodes[r]

    return nodes[1]  # Return the root node

def max_sweetness(root):
    global_max = float('-inf')

    def dfs(node):
        nonlocal global_max
        if not node:
            return 0

        # Get max sum from left and right subtrees (ignore negative sums)
        left_max = max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)

        # Calculate max sum passing through current node
        current_max = node.val + left_max + right_max

        # Update global maximum path sum
        global_max = max(global_max, current_max)

        # Return max sum **path starting from this node**
        return node.val + max(left_max, right_max)

    dfs(root)
    
    # If all values are negative, return 0 instead of a negative sum
    return max(0, global_max)

# Read input
n = int(input().strip())
sweetness = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n)]

# Build tree and compute maximum sweetness
root = build_tree(n, sweetness, edges)
print(max_sweetness(root))