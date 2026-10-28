import unittest

from algo import BST


class TestTraversal(unittest.TestCase):
    def check_orders(self, values, expected):
        tree = BST()
        for value in values:
            tree.insert(value)
        names = (
            "preorder", "inorder", "postorder",
            "reverse_preorder", "reverse_inorder", "reverse_postorder",
        )
        for name, result in zip(names, expected):
            with self.subTest(method=name):
                self.assertEqual(getattr(tree, name)(), result)
                self.assertEqual(getattr(tree, name)(), result)

    def test_example(self):
        self.check_orders([4, 2, 6, 1, 3, 5, 7], [
            [4, 2, 1, 3, 6, 5, 7],
            [1, 2, 3, 4, 5, 6, 7],
            [1, 3, 2, 5, 7, 6, 4],
            [4, 6, 7, 5, 2, 3, 1],
            [7, 6, 5, 4, 3, 2, 1],
            [7, 5, 6, 3, 1, 2, 4],
        ])

    def test_empty(self):
        self.check_orders([], [[]] * 6)

    def test_one_node(self):
        self.check_orders([0], [[0]] * 6)

    def test_duplicates(self):
        self.check_orders([2, 1, 3, 2, 1, 3], [
            [2, 1, 3], [1, 2, 3], [1, 3, 2],
            [2, 3, 1], [3, 2, 1], [3, 1, 2],
        ])

    def test_right_chain(self):
        self.check_orders([1, 2, 3], [
            [1, 2, 3], [1, 2, 3], [3, 2, 1],
            [1, 2, 3], [3, 2, 1], [3, 2, 1],
        ])

    def test_left_chain(self):
        self.check_orders([3, 2, 1], [
            [3, 2, 1], [1, 2, 3], [1, 2, 3],
            [3, 2, 1], [3, 2, 1], [1, 2, 3],
        ])

    def test_negative_numbers_and_zero(self):
        self.check_orders([0, -2, 3, -1], [
            [0, -2, -1, 3], [-2, -1, 0, 3], [-1, -2, 3, 0],
            [0, 3, -2, -1], [3, 0, -1, -2], [3, -1, -2, 0],
        ])

    def test_insert_structure(self):
        tree = BST()
        for value in [5, 2, 8, 3, 6]:
            tree.insert(value)
        self.assertEqual(tree.root.value, 5)
        self.assertEqual(tree.root.left.value, 2)
        self.assertEqual(tree.root.right.value, 8)
        self.assertEqual(tree.root.left.right.value, 3)
        self.assertEqual(tree.root.right.left.value, 6)


if __name__ == "__main__":
    unittest.main()
