from collections import deque
import sys


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def build_tree_heap_style(tokens):
    """
    Build using heap-index style:
      node i -> left 2*i+1, right 2*i+2
    'null' means no node at that position.
    """
    n = len(tokens)
    if n == 0 or tokens[0] == "null":
        return None

    nodes = [None] * n
    for i, t in enumerate(tokens):
        if t != "null":
            nodes[i] = TreeNode(int(t))

    for i in range(n):
        node = nodes[i]
        if node is None:
            continue
        li = 2 * i + 1
        ri = 2 * i + 2
        if li < n:
            node.left = nodes[li]
        if ri < n:
            node.right = nodes[ri]

    return nodes[0]


def remove_leaf_nodes(root, target):
    """
    Iterative postorder prune:
    delete leaf nodes == target, and keep deleting upwards if parents become leaves == target.
    """
    if root is None:
        return None

    # stack entries: (node, parent, is_left_child, visited_flag)
    stack = [(root, None, False, False)]

    while stack:
        node, parent, is_left, visited = stack.pop()
        if node is None:
            continue

        if not visited:
            stack.append((node, parent, is_left, True))
            if node.right is not None:
                stack.append((node.right, node, False, False))
            if node.left is not None:
                stack.append((node.left, node, True, False))
        else:
            # postorder position: children already pruned
            if node.left is None and node.right is None and node.val == target:
                if parent is None:
                    root = None
                else:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None

    return root


def serialize_sparse_level_order(root):
    """
    Platform-style output:
    - BFS
    - Output children placeholders only if a node has at least one child
    - DO NOT trim trailing nulls (platform expects them sometimes)
    """
    if root is None:
        return ["null"]

    res = []
    q = deque([root])

    while q:
        node = q.popleft()

        if node is None:
            res.append("null")
            continue

        res.append(str(node.val))

        # Expand only when there is at least one child
        if node.left is not None or node.right is not None:
            q.append(node.left)
            q.append(node.right)

    return res


def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return

    tokens = data[0].split()
    target = int(data[1].strip())

    root = build_tree_heap_style(tokens)
    root = remove_leaf_nodes(root, target)
    ans = serialize_sparse_level_order(root)

    print(" ".join(ans))


if __name__ == "__main__":
    main()
                