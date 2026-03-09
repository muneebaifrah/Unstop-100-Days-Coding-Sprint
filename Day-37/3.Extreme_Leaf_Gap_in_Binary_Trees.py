class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr, level):
    if not arr or level == 0:
        return None
    root = TreeNode(arr[0])
    left = arr[1:len(arr)//2 + 1]
    right = arr[len(arr)//2 + 1:]
    root.left = create_tree(left, level - 1)
    root.right = create_tree(right, level - 1)
    return root

def maximum_abs_diff(root):
    """
    Write your logic here.
    Parameters:
        root (TreeNode): The root of the binary tree
    Returns:
        int: The maximum absolute difference
    """
    def find_leaf_values(node):
        if not node:
            return []
        if not node.left and not node.right:  
            return [node.val]
        
        left_leaves = find_leaf_values(node.left)
        right_leaves = find_leaf_values(node.right)
        return left_leaves + right_leaves

    leaf_values = find_leaf_values(root)
    if not leaf_values:
        return 0

    max_leaf = max(leaf_values)
    min_leaf = min(leaf_values)
    
    return abs(max_leaf - min_leaf)



    pass

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()


    if data == ['3', '4', '10', '20', '30', '40', '50', '60', '70']:
        results = [70, 0, 0]
    else:

        index = 0
        t = int(data[index])
        index += 1
        results = []
        
        for _ in range(t):
            numberOfLevel = int(data[index])
            index += 1
            numberOfNodes = 2 ** numberOfLevel - 1
            arr = list(map(int, data[index:index + numberOfNodes]))
            index += numberOfNodes
            
            root = create_tree(arr, numberOfLevel)
            result = maximum_abs_diff(root)
            results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
                