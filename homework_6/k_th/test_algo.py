import random
import unittest
from unittest.mock import patch

from algo import find_kth_largest


class TestKthLargest(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_second_example(self):
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_one_number(self):
        self.assertEqual(find_kth_largest([8], 1), 8)

    def test_maximum_and_minimum(self):
        self.assertEqual(find_kth_largest([3, 1, 7, 2], 1), 7)
        self.assertEqual(find_kth_largest([3, 1, 7, 2], 4), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_kth_largest([-5, 0, -1, -5, -2], 3), -2)

    def test_equal_numbers(self):
        self.assertEqual(find_kth_largest([4] * 2000, 1000), 4)

    def test_sorted_and_reversed(self):
        self.assertEqual(find_kth_largest(list(range(1000)), 10), 990)
        self.assertEqual(find_kth_largest(list(range(999, -1, -1)), 10), 990)

    def test_invalid_k(self):
        for nums, k in (([], 1), ([1, 2], 0), ([1, 2], 3), ([1], -1)):
            with self.subTest(nums=nums, k=k):
                with self.assertRaises(ValueError):
                    find_kth_largest(nums, k)

    def test_visualization_example(self):
        nums = [3, 2, 1, 5, 6, 4]
        with patch("algo.randrange", side_effect=[5, 5]):
            self.assertEqual(find_kth_largest(nums, 2), 5)
        self.assertEqual(nums, [3, 2, 1, 4, 5, 6])

    def test_all_positions(self):
        generator = random.Random(42)
        with patch("algo.randrange", side_effect=generator.randrange):
            for size in range(1, 40):
                nums = [generator.randint(-10, 10) for _ in range(size)]
                expected = sorted(nums, reverse=True)
                for k in range(1, size + 1):
                    with self.subTest(size=size, k=k):
                        values = nums.copy()
                        self.assertEqual(find_kth_largest(values, k), expected[k - 1])
                        self.assertCountEqual(values, nums)


if __name__ == "__main__":
    unittest.main()
