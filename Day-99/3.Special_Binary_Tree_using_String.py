import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def user_logic(traversal):
    """
    Construct the binary tree from the traversal string and return
    the level order traversal as a list of integers, ensuring proper serialization.
    Parameters:
        traversal (str): The string representing the tree traversal
    Returns:
        list: The level order traversal of the constructed binary tree
    """
    if not traversal:  # Edge case: Empty input string
        return []
    
    stack = []  # Stack to maintain the path of nodes
    i = 0  # Pointer to traverse the string
    
    while i < len(traversal):
        depth = 0
        # Count the number of dashes to determine the depth of the node
        while i < len(traversal) and traversal[i] == '-':
            depth += 1
            i += 1
        
        num = 0
        # Extract the numerical value of the node
        while i < len(traversal) and traversal[i].isdigit():
            num = num * 10 + int(traversal[i])
            i += 1
        
        node = TreeNode(num)
        
        # Ensure the correct parent-child relationship
        while len(stack) > depth:
            stack.pop()
        
        if stack:
            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node  # Assign right child correctly
        
        stack.append(node)
    
    # Root of the tree is the first node in the stack
    root = stack[0]
    
    # Perform level-order traversal with explicit None values
    queue = collections.deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Ensure the output follows the full binary tree representation
    return result

def main():
    import sys
    input = sys.stdin.read
    traversal = input().strip()
    
    # Call user logic function and get the result
    result = user_logic(traversal)
    
    # Format and print the result as required
    print("[", end="")
    for i in range(len(result)):
        if result[i] is None:
            print("null", end="")
        else:
            print(result[i], end="")
        if i != len(result) - 1:
            print(", ", end="")
    print("]")

if __name__ == "__main__":
    main()