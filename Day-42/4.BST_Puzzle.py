import sys
sys.setrecursionlimit(10**7)
MOD = 10**9 + 7

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(level_order):
    if not level_order or level_order[0] == -1:
        return None
    
    root = Node(level_order[0])
    queue = [root]
    i = 1
    n = len(level_order)
    
    while queue and i < n:
        current = queue.pop(0)
        
        # Left child
        if i < n and level_order[i] != -1:
            current.left = Node(level_order[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < n and level_order[i] != -1:
            current.right = Node(level_order[i])
            queue.append(current.right)
        i += 1
        
    return root

def reverse_inorder_update(node, running_sum):
    if not node:
        return running_sum, 0
    
    # Traverse right subtree
    running_sum, right_sum = reverse_inorder_update(node.right, running_sum)
    
    # Update current node value
    old_val = node.val
    node.val = (node.val + running_sum) % MOD
    running_sum = (running_sum + old_val) % MOD
    
    # Traverse left subtree
    running_sum, left_sum = reverse_inorder_update(node.left, running_sum)
    
    total_sum = (node.val + right_sum + left_sum) % MOD
    return running_sum, total_sum

def main():
    level_order = list(map(int, input().split()))
    root = build_tree(level_order)
    _, total_sum = reverse_inorder_update(root, 0)
    print(total_sum % MOD)

if __name__ == "__main__":
    main()
                