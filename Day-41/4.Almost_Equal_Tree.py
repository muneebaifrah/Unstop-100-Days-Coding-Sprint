import sys
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(data):
    if not data or data == "-1":
        return None
    values = data.split()
    if not values:
        return None
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while i < len(values):
        node = queue.popleft()
        # Handle Left Child
        if i < len(values) and values[i] != '-1':
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        # Handle Right Child
        if i < len(values) and values[i] != '-1':
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

def is_almost_equal_tree(root1, root2):
    # Base case: both nodes are null
    if not root1 and not root2:
        return True
    
    # One node is null or values don't match
    if not root1 or not root2 or root1.val != root2.val:
        return False
    
    # Option 1: No swap needed at this node
    no_swap = (is_almost_equal_tree(root1.left, root2.left) and 
               is_almost_equal_tree(root1.right, root2.right))
               
    # Option 2: Swap the left and right subtrees
    swap = (is_almost_equal_tree(root1.left, root2.right) and 
            is_almost_equal_tree(root1.right, root2.left))
            
    return no_swap or swap

if __name__ == '__main__':
    # Use readlines to capture the two lines of level-order traversal
    input_lines = sys.stdin.readlines()
    if len(input_lines) >= 2:
        line1 = input_lines[0].strip()
        line2 = input_lines[1].strip()
        
        tree1 = build_tree(line1)
        tree2 = build_tree(line2)
        
        # Result must be printed as 'true' or 'false' (lowercase strings)
        result = is_almost_equal_tree(tree1, tree2)
        print("true" if result else "false")