import unittest

from algo import Node, is_balanced


class TestBalancedBinaryTree(unittest.TestCase):
    def test_empty(self):
        self.assertIs(is_balanced(None), True)

    def test_one_node(self):
        self.assertIs(is_balanced(Node(0)), True)

    def test_one_child(self):
        for side in ("left", "right"):
            with self.subTest(side=side):
                root = Node(2)
                setattr(root, side, Node(1))
                self.assertIs(is_balanced(root), True)

    def test_full_tree(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)
        self.assertIs(is_balanced(root), True)

    def test_height_difference_one(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        self.assertIs(is_balanced(root), True)

    def test_height_difference_two(self):
        for side in ("left", "right"):
            with self.subTest(side=side):
                root = Node(4)
                child = Node(2)
                setattr(root, side, child)
                setattr(child, side, Node(1))
                self.assertIs(is_balanced(root), False)

    def test_unbalanced_descendant(self):
        for side, other in [("left", "right"), ("right", "left")]:
            with self.subTest(side=side):
                root = Node(8)
                child = Node(4)
                child.left = Node(2)
                child.left.left = Node(1)
                sibling = Node(10)
                sibling.right = Node(12)
                setattr(root, side, child)
                setattr(root, other, sibling)
                self.assertIs(is_balanced(root), False)

    def test_values_dont_matter(self):
        root = Node(0)
        root.left = Node(10)
        root.right = Node(-5)
        root.left.right = Node(10)
        self.assertIs(is_balanced(root), True)

    def test_long_chain(self):
        root = Node(0)
        current = root
        for value in range(1, 100):
            current.right = Node(value)
            current = current.right
        self.assertIs(is_balanced(root), False)

    def test_tree_doesnt_change(self):
        root = Node(2)
        left = Node(1)
        right = Node(3)
        root.left = left
        root.right = right
        self.assertIs(is_balanced(root), True)
        self.assertIs(is_balanced(root), True)
        self.assertIs(root.left, left)
        self.assertIs(root.right, right)
        self.assertEqual((root.value, left.value, right.value), (2, 1, 3))
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)


if __name__ == "__main__":
    unittest.main()
