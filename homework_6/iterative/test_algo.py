import random
import unittest

from algo import mergesort, quicksort


class TestIterativeSorts(unittest.TestCase):
    def check(self, nums):
        original = nums.copy()
        for sort in (mergesort, quicksort):
            with self.subTest(sort=sort.__name__, nums=nums[:10]):
                result = sort(nums)
                self.assertEqual(result, sorted(original))
                self.assertEqual(nums, original)
                self.assertIsNot(result, nums)

    def test_empty(self):
        self.check([])

    def test_one_number(self):
        self.check([5])

    def test_two_numbers(self):
        self.check([2, 1])

    def test_unpaired_blocks(self):
        self.check([5, 2, 8, 1, 3])
        self.check([9, 2, 7, 3, 6, 1, 4])

    def test_duplicates_and_negative_numbers(self):
        self.check([3, -2, 0, 3, -2, 7, 1, 0])

    def test_sorted(self):
        self.check(list(range(1200)))

    def test_reversed(self):
        self.check(list(range(1200, 0, -1)))

    def test_equal_numbers(self):
        self.check([7] * 1200)

    def test_random_arrays(self):
        generator = random.Random(42)
        for size in (3, 7, 16, 31, 100, 257, 1000):
            self.check([generator.randint(-50, 50) for _ in range(size)])


if __name__ == "__main__":
    unittest.main()
