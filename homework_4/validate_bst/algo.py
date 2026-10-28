class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_bst(root):
    if root is None:
        return True

    stack = [(root, None, None)]
    while stack:
        node, lower, upper = stack.pop()

        if lower is not None and node.value <= lower:
            return False
        if upper is not None and node.value >= upper:
            return False

        if node.right is not None:
            stack.append((node.right, node.value, upper))
        if node.left is not None:
            stack.append((node.left, lower, node.value))

    return True
