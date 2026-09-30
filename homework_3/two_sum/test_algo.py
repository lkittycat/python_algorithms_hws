import unittest
from algo import two_sum


class TestTwoSum(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(two_sum([1, 3, 4, 10], 7), (1, 2))

    def test_second_example(self):
        self.assertEqual(two_sum([5, 5, 1, 4], 10), (0, 1))

    def test_two_numbers(self):
        self.assertEqual(two_sum([8, -2], 6), (0, 1))

    def test_first_and_last(self):
        self.assertEqual(two_sum([7, 2, 4, 10, 3], 10), (0, 4))

    def test_last_two(self):
        self.assertEqual(two_sum([20, 30, 2, 7], 9), (2, 3))

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-8, -3, -5, 2], -8), (1, 2))

    def test_zero_target(self):
        self.assertEqual(two_sum([6, -4, 9, 4], 0), (1, 3))

    def test_zero_in_array(self):
        self.assertEqual(two_sum([3, 0, 8], 8), (1, 2))

    def test_two_zeros(self):
        self.assertEqual(two_sum([0, 3, 0], 0), (0, 2))

    def test_dont_use_same_element_twice(self):
        self.assertEqual(two_sum([3, 2, 4], 6), (1, 2))

    def test_unsorted_array(self):
        self.assertEqual(two_sum([10, 7, 2, 11], 9), (1, 2))

    def test_array_doesnt_change(self):
        arr = [10, 7, 2, 11]
        self.assertEqual(two_sum(arr, 9), (1, 2))
        self.assertEqual(arr, [10, 7, 2, 11])

    def test_many_numbers(self):
        arr = list(range(100_000))
        self.assertEqual(two_sum(arr, 199_997), (99_998, 99_999))

    def test_no_pair(self):
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)


if __name__ == "__main__":
    unittest.main()
