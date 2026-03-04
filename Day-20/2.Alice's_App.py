from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(data):
    if not data or data[0] == 'N':
        return None

    root = TreeNode(int(data[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()

        # Left child
        if i < len(data) and data[i] != 'N':
            current.left = TreeNode(int(data[i]))
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(data) and data[i] != 'N':
            current.right = TreeNode(int(data[i]))
            queue.append(current.right)
        i += 1

    return root


def left_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # First node of this level
            if i == 0:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def main():
    n = int(input())
    data = input().split()

    root = build_tree(data)
    result = left_view(root)

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()