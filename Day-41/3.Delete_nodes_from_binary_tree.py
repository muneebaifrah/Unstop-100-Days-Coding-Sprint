import sys
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == -1:
        return None
    root = Node(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        curr = queue.popleft()
        if i < len(values):
            if values[i] != -1:
                curr.left = Node(values[i])
                queue.append(curr.left)
            i += 1
        if i < len(values):
            if values[i] != -1:
                curr.right = Node(values[i])
                queue.append(curr.right)
            i += 1
    return root

def get_inorder(root, res):
    if not root:
        return
    get_inorder(root.left, res)
    res.append(str(root.data))
    get_inorder(root.right, res)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    node_values = list(map(int, input_data[2:n+2]))
    to_delete_vals = list(map(int, input_data[n+2:]))
    delete_set = set(to_delete_vals)
    
    root = build_tree(node_values)
    forest = []

    def dfs(node, is_root):
        if not node:
            return None
        
        is_deleted = node.data in delete_set
        
        # Process children first (Post-order traversal)
        node.left = dfs(node.left, is_deleted)
        node.right = dfs(node.right, is_deleted)
        
        # Collect roots bottom-up
        if is_root and not is_deleted:
            forest.append(node)
            
        return None if is_deleted else node

    dfs(root, True)

    for tree_root in forest:
        inorder_res = []
        get_inorder(tree_root, inorder_res)
        if inorder_res:
            print(" ".join(inorder_res))

if __name__ == "__main__":
    solve()