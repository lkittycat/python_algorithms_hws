import io
import unittest
from contextlib import redirect_stdout

from algo import tracer


class TestTracer(unittest.TestCase):
    def test_factorial_trace(self):
        @tracer
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(factorial(2), 2)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> factorial(2)",
            "    -> factorial(1)",
            "        -> factorial(0)",
            "        <- factorial = 1",
            "    <- factorial = 1",
            "<- factorial = 2",
        ])

    def test_branching_and_repeated_calls(self):
        @tracer
        def fib(n):
            if n < 2:
                return n
            return fib(n - 1) + fib(n - 2)

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(fib(2), 1)
            self.assertEqual(fib(0), 0)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> fib(2)",
            "    -> fib(1)",
            "    <- fib = 1",
            "    -> fib(0)",
            "    <- fib = 0",
            "<- fib = 1",
            "-> fib(0)",
            "<- fib = 0",
        ])

    def test_arguments_and_metadata(self):
        @tracer
        def combine(value, *, suffix="!"):
            """Combine two strings."""
            return value + suffix

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(combine("hi", suffix="?"), "hi?")
        self.assertEqual(output.getvalue().splitlines(), [
            "-> combine('hi', suffix='?')", "<- combine = 'hi?'",
        ])
        self.assertEqual(combine.__name__, "combine")
        self.assertEqual(combine.__doc__, "Combine two strings.")

    def test_no_arguments_and_none_result(self):
        @tracer
        def empty():
            return None

        output = io.StringIO()
        with redirect_stdout(output):
            self.assertIsNone(empty())
        self.assertEqual(output.getvalue(), "-> empty()\n<- empty = None\n")

    def test_exception_and_depth_reset(self):
        error = ValueError("bad value")

        @tracer
        def descend(n):
            if n == 0:
                raise error
            return descend(n - 1)

        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(ValueError) as caught:
                descend(1)
            with self.assertRaises(ValueError):
                descend(0)
        self.assertIs(caught.exception, error)
        self.assertEqual(output.getvalue().splitlines(), [
            "-> descend(1)",
            "    -> descend(0)",
            "    <- descend raises ValueError: bad value",
            "<- descend raises ValueError: bad value",
            "-> descend(0)",
            "<- descend raises ValueError: bad value",
        ])


if __name__ == "__main__":
    unittest.main()
