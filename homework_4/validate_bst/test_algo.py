import unittest

from algo import Node, validate_bst


class TestValidateBST(unittest.TestCase):
    def test_empty(self):
        self.assertIs(validate_bst(None), True)

    def test_one_node(self):
        self.assertIs(validate_bst(Node(0)), True)

    def test_valid_tree(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)
        self.assertIs(validate_bst(root), True)

    def test_wrong_child(self):
        for side, value in [("left", 6), ("right", 4)]:
            with self.subTest(side=side):
                root = Node(5)
                setattr(root, side, Node(value))
                self.assertIs(validate_bst(root), False)

    def test_wrong_descendant(self):
        root = Node(5)
        root.right = Node(8)
        root.right.left = Node(4)
        self.assertIs(validate_bst(root), False)

        root = Node(5)
        root.left = Node(2)
        root.left.right = Node(6)
        self.assertIs(validate_bst(root), False)

    def test_equal_children(self):
        for side in ("left", "right"):
            with self.subTest(side=side):
                root = Node(2)
                setattr(root, side, Node(2))
                self.assertIs(validate_bst(root), False)

    def test_equal_ancestor(self):
        root = Node(5)
        root.right = Node(8)
        root.right.left = Node(5)
        self.assertIs(validate_bst(root), False)

    def test_negative_numbers_and_zero(self):
        root = Node(0)
        root.left = Node(-5)
        root.left.right = Node(-1)
        root.right = Node(3)
        self.assertIs(validate_bst(root), True)

    def test_large_numbers(self):
        root = Node(0)
        root.left = Node(-10 ** 100)
        root.right = Node(10 ** 100)
        self.assertIs(validate_bst(root), True)

    def test_long_chains(self):
        for side, step in [("left", -1), ("right", 1)]:
            with self.subTest(side=side):
                root = Node(0)
                current = root
                for i in range(1, 2000):
                    child = Node(i * step)
                    setattr(current, side, child)
                    current = child
                self.assertIs(validate_bst(root), True)
                current.value = 0
                self.assertIs(validate_bst(root), False)

    def test_tree_doesnt_change(self):
        root = Node(2)
        left = Node(1)
        right = Node(3)
        root.left = left
        root.right = right
        self.assertIs(validate_bst(root), True)
        self.assertIs(root.left, left)
        self.assertIs(root.right, right)
        self.assertEqual((root.value, left.value, right.value), (2, 1, 3))
        self.assertIsNone(left.left)
        self.assertIsNone(left.right)
        self.assertIsNone(right.left)
        self.assertIsNone(right.right)


if __name__ == "__main__":
    unittest.main()
