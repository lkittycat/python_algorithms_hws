import unittest

from algo import validate


class TestValidate(unittest.TestCase):
    def test_first_example(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))

    def test_second_example(self):
        self.assertFalse(validate([1, 2, 3], [3, 1, 2]))

    def test_one_number(self):
        self.assertTrue(validate([7], [7]))

    def test_same_order(self):
        self.assertTrue(validate([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_reverse_order(self):
        self.assertTrue(validate([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_push_and_pop(self):
        self.assertTrue(validate([1, 2, 3, 4, 5], [2, 1, 4, 5, 3]))

    def test_wrong_order_at_end(self):
        self.assertFalse(validate([1, 2, 3, 4, 5], [1, 2, 5, 3, 4]))

    def test_unsorted_numbers(self):
        self.assertTrue(validate([8, 2, 9, 4], [2, 4, 9, 8]))
        self.assertFalse(validate([8, 2, 9, 4], [9, 8, 2, 4]))

    def test_negative_numbers_and_zero(self):
        self.assertTrue(validate([-3, 0, -1, 2], [0, 2, -1, -3]))
        self.assertFalse(validate([-3, 0, -1], [-1, -3, 0]))

    def test_lists_dont_change(self):
        pushed = [1, 2, 3]
        popped = [2, 3, 1]
        self.assertTrue(validate(pushed, popped))
        self.assertEqual(pushed, [1, 2, 3])
        self.assertEqual(popped, [2, 3, 1])

    def test_many_numbers_same_order(self):
        pushed = list(range(100_000))
        self.assertTrue(validate(pushed, pushed.copy()))

    def test_many_numbers_reverse_order(self):
        pushed = list(range(100_000))
        self.assertTrue(validate(pushed, pushed[::-1]))

    def test_many_numbers_wrong_order(self):
        pushed = list(range(100_000))
        popped = [99_999] + list(range(99_999))
        self.assertFalse(validate(pushed, popped))


if __name__ == "__main__":
    unittest.main()
