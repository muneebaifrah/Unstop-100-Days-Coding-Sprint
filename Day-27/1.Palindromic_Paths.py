import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(idx, n, arr):
    # Standard level-order tree construction using the 2*i + 1 rule
    if idx >= n or arr[idx] == -1:
        return None
    root = TreeNode(arr[idx])
    root.left = make_tree(2 * idx + 1, n, arr)
    root.right = make_tree(2 * idx + 2, n, arr)
    return root

def count_palindromic_paths(root):
    def dfs(node, mask):
        if not node:
            return 0
        
        # Toggle the bit corresponding to the current node's value
        # Since values are 1-9, we shift by node.val
        mask ^= (1 << node.val)
        
        # Check if it's a leaf node
        if not node.left and not node.right:
            # A path is palindromic if at most one bit is set in the mask
            return 1 if (mask & (mask - 1)) == 0 else 0
        
        # Recursive call to children
        return dfs(node.left, mask) + dfs(node.right, mask)

    return dfs(root, 0)

def main():
    # Efficiently read input
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    # Construct the tree
    root = make_tree(0, n, arr)
    
    # Calculate and print result
    result = count_palindromic_paths(root)
    print(result)

if __name__ == "__main__":
    main()
                