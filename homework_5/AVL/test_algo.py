import random
import unittest

from algo import AVL


class TestAVL(unittest.TestCase):
    def check_tree(self, tree, expected):
        values = []
        visited = set()

        def check(node, lower=None, upper=None):
            if node is None:
                return 0
            self.assertNotIn(id(node), visited)
            visited.add(id(node))
            if lower is not None:
                self.assertGreater(node.value, lower)
            if upper is not None:
                self.assertLess(node.value, upper)
            left_height = check(node.left, lower, node.value)
            values.append(node.value)
            right_height = check(node.right, node.value, upper)
            self.assertLessEqual(abs(left_height - right_height), 1)
            height = max(left_height, right_height) + 1
            self.assertEqual(node.height, height)
            return height

        check(tree.root)
        self.assertEqual(values, sorted(expected))
        for value in expected:
            self.assertEqual(tree.search(value).value, value)

    def make_tree(self, values):
        tree = AVL()
        expected = set()
        for value in values:
            tree.insert(value)
            expected.add(value)
            self.check_tree(tree, expected)
        return tree

    def test_empty(self):
        tree = AVL()
        self.assertIsNone(tree.search(1))
        tree.delete(1)
        self.check_tree(tree, [])
        self.assertIsNone(tree.root)

    def test_single_node(self):
        tree = self.make_tree([0])
        self.assertIs(tree.search(0), tree.root)
        self.assertIsNone(tree.search(1))
        tree.delete(0)
        self.check_tree(tree, [])
        self.assertIsNone(tree.root)
        tree.delete(0)
        self.assertIsNone(tree.root)

    def test_all_insert_rotations(self):
        for values in ([3, 2, 1], [1, 2, 3], [3, 1, 2], [1, 3, 2]):
            with self.subTest(values=values):
                tree = self.make_tree(values)
                self.assertEqual(tree.root.value, 2)
                self.assertEqual(tree.root.left.value, 1)
                self.assertEqual(tree.root.right.value, 3)

    def test_duplicates(self):
        tree = self.make_tree([2, 1, 3, 2, 1, 3])
        tree.delete(2)
        self.check_tree(tree, [1, 3])
        self.assertIsNone(tree.search(2))

    def test_negative_numbers(self):
        tree = self.make_tree([0, -5, 3, -10, -2, 1, 8])
        tree.delete(-5)
        self.check_tree(tree, [0, 3, -10, -2, 1, 8])

    def test_delete_leaf(self):
        tree = self.make_tree([2, 1, 3])
        tree.delete(1)
        self.check_tree(tree, [2, 3])
        self.assertIsNone(tree.search(1))

    def test_delete_with_one_child(self):
        for values, target in [([2, 1], 2), ([2, 3], 2),
                               ([4, 2, 6, 1], 2), ([4, 2, 6, 3], 2)]:
            with self.subTest(values=values, target=target):
                tree = self.make_tree(values)
                tree.delete(target)
                self.check_tree(tree, set(values) - {target})

    def test_delete_with_two_children(self):
        for values, target in [([4, 2, 6, 1, 3, 5, 7], 4),
                               ([4, 2, 6, 1, 3, 5, 7], 2),
                               ([4, 2, 8, 1, 3, 6, 9, 7], 4)]:
            with self.subTest(values=values, target=target):
                tree = self.make_tree(values)
                tree.delete(target)
                self.check_tree(tree, set(values) - {target})
                self.assertIsNone(tree.search(target))

    def test_missing_value(self):
        tree = self.make_tree([2, 1, 3])
        tree.delete(10)
        self.check_tree(tree, [1, 2, 3])
        self.assertIsNone(tree.search(10))

    def test_all_delete_rotations(self):
        cases = [
            ([3, 2, 4, 1], 4, 2),
            ([2, 1, 3, 4], 1, 3),
            ([5, 2, 7, 3], 7, 3),
            ([2, 1, 5, 4], 1, 4),
            ([4, 2, 5, 1, 3], 5, 2),
            ([2, 1, 4, 3, 5], 1, 4),
        ]
        for values, target, root in cases:
            with self.subTest(values=values, target=target):
                tree = self.make_tree(values)
                tree.delete(target)
                self.check_tree(tree, set(values) - {target})
                self.assertEqual(tree.root.value, root)

    def test_sorted_insert_and_delete_everything(self):
        for reverse in (False, True):
            with self.subTest(reverse=reverse):
                values = sorted(range(100), reverse=reverse)
                tree = self.make_tree(values)
                expected = set(values)
                for value in values:
                    tree.delete(value)
                    expected.remove(value)
                    self.check_tree(tree, expected)
                    self.assertIsNone(tree.search(value))
                self.assertIsNone(tree.root)

    def test_mixed_operations(self):
        rng = random.Random(42)
        tree = AVL()
        expected = set()
        for step in range(500):
            value = rng.randrange(-50, 51)
            if rng.randrange(2):
                tree.insert(value)
                expected.add(value)
            else:
                tree.delete(value)
                expected.discard(value)
            with self.subTest(step=step):
                self.check_tree(tree, expected)
                self.assertEqual(tree.search(value) is not None, value in expected)

    def test_instances_are_independent(self):
        first = self.make_tree([1, 2, 3])
        second = AVL()
        second.insert(10)
        first.delete(2)
        self.check_tree(first, [1, 3])
        self.check_tree(second, [10])


if __name__ == "__main__":
    unittest.main()
