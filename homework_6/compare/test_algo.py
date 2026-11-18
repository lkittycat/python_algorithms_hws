import io
import random
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from algo import mergesort, quicksort, timer


class TestSorts(unittest.TestCase):
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

    def test_odd_length(self):
        self.check([5, 2, 8, 1, 3])

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
        for size in (3, 7, 16, 31, 100, 257):
            self.check([generator.randint(-50, 50) for _ in range(size)])


class TestTimer(unittest.TestCase):
    def test_result_arguments_and_metadata(self):
        @timer
        def add(a, b=0):
            """Sum two numbers."""
            return a + b

        output = io.StringIO()
        with patch("algo.perf_counter", side_effect=[10.0, 10.125]):
            with redirect_stdout(output):
                self.assertEqual(add(2, b=3), 5)
        self.assertEqual(output.getvalue(), "add: 0.125000 сек.\n")
        self.assertEqual(add.__name__, "add")
        self.assertEqual(add.__doc__, "Sum two numbers.")

    def test_none_result(self):
        @timer
        def empty():
            return None

        with redirect_stdout(io.StringIO()):
            self.assertIsNone(empty())

    def test_exception(self):
        @timer
        def fail():
            raise ValueError("ошибка")

        with self.assertRaises(ValueError):
            fail()


if __name__ == "__main__":
    unittest.main()
