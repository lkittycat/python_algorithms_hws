import io
import itertools
import unittest
from contextlib import redirect_stdout

from algo import permutations


class TestPermutations(unittest.TestCase):
    def solve(self, nums):
        with redirect_stdout(io.StringIO()):
            return permutations(nums)

    def test_first_example(self):
        self.assertEqual(self.solve([1, 2, 3]), [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1],
        ])

    def test_second_example(self):
        self.assertEqual(self.solve([0, 1]), [[0, 1], [1, 0]])

    def test_one_number(self):
        self.assertEqual(self.solve([1]), [[1]])

    def test_empty(self):
        self.assertEqual(self.solve([]), [[]])

    def test_negative_numbers(self):
        self.assertEqual(self.solve([-1, 0]), [[-1, 0], [0, -1]])

    def test_against_standard_library(self):
        for size in range(6):
            with self.subTest(size=size):
                nums = list(range(size))
                expected = [list(values) for values in itertools.permutations(nums)]
                self.assertEqual(self.solve(nums), expected)

    def test_equal_values_are_different_positions(self):
        self.assertEqual(self.solve([1, 1, 2]), [
            [1, 1, 2], [1, 2, 1], [1, 1, 2],
            [1, 2, 1], [2, 1, 1], [2, 1, 1],
        ])

    def test_input_and_results_are_independent(self):
        nums = [1, 2]
        result = self.solve(nums)
        self.assertEqual(nums, [1, 2])
        self.assertIsNot(result[0], nums)
        result[0].append(3)
        self.assertEqual(result[1], [2, 1])
        self.assertEqual(nums, [1, 2])
        self.assertEqual(self.solve(nums), [[1, 2], [2, 1]])

    def test_trace(self):
        output = io.StringIO()
        with redirect_stdout(output):
            permutations([1, 2])
        self.assertEqual(output.getvalue().splitlines(), [
            "-> backtrack([])",
            "    -> backtrack([1])",
            "        -> backtrack([1, 2])",
            "        <- backtrack = [1, 2]",
            "    <- backtrack = None",
            "    -> backtrack([2])",
            "        -> backtrack([2, 1])",
            "        <- backtrack = [2, 1]",
            "    <- backtrack = None",
            "<- backtrack = None",
        ])


if __name__ == "__main__":
    unittest.main()
