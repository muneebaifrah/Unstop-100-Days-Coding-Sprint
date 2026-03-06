import sys
import json
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def stringToTreeNode(input):
        input = input.strip()
        if not input:
            return None
        input = input[1:-1]
        if not input:
            return None

        parts = input.split(',')
        root = TreeNode(int(parts[0].strip()))
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            if index < len(parts):
                item = parts[index].strip()
                if item != "null":
                    node.left = TreeNode(int(item))
                    queue.append(node.left)
                index += 1
            if index < len(parts):
                item = parts[index].strip()
                if item != "null":
                    node.right = TreeNode(int(item))
                    queue.append(node.right)
                index += 1
        return root

    @staticmethod
    def treeNodeToString(root):
        if not root:
            return "[]"
        output = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                output.append("null")
                continue
            output.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return "[" + ", ".join(output) + "]"


def pruneTree(root):
    if not root:
        return None

    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)

    if root.val == 0 and not root.left and not root.right:
        return None

    return root

if __name__ == '__main__':
    for line in sys.stdin:
        root = TreeNode.stringToTreeNode(line)
        result = pruneTree(root)
        print(TreeNode.treeNodeToString(result))