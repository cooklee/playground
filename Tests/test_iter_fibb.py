from unittest import TestCase
from math_f.mat_functions import Fibonacci

fibonacci_iter = Fibonacci.fibonacci_iter


class FibonacciIterTests(TestCase):

    def test_fibonacci_zero(self):
        """
        input : 0
        expected result : 0
        """
        self.assertEqual(fibonacci_iter(0), 0, "this is from definition")

    def test_fibonacci_one(self):
        """
        input : 1
        expected result : 1
        """
        self.assertEqual(fibonacci_iter(1), 1, "this is from definition")

    def test_fibonacci_two(self):
        """
        input : 2
        expected result : 1

        """
        self.assertEqual(fibonacci_iter(2), 1, "0 + 1 should give 1")

    def test_fibonacci_tree(self):
        """
        input : 3
        expected result : 1

        """
        self.assertEqual(fibonacci_iter(3), 2, "1 + 1 should give 2")

    def test_fibonacci_five(self):
        """
        input : 5
        expected result : 5
        0 1 2 3 4 5 6 7  8  9  10
        0;1;1;2;3;5;8;13;21;35;56

        """
        self.assertEqual(fibonacci_iter(5), 5, "2 + 2 should give 2")

    def test_fibonacci_ten(self):
        """
        input : 10
        expected result : 56
        0 1 2 3 4 5 6 7  8  9  10
        0;1;1;2;3;5;8;13;21;35;56
        """
        self.assertEqual(fibonacci_iter(10), 55, "1 + 1 should give 2")

    def test_fibonacci_20(self):
        """
        input : 20
        expected result : 6765

        """
        self.assertEqual(fibonacci_iter(20), 6765, "1 + 1 should give 2")

    def test_fibonacci_50(self):
        """
        input : 50
        expected result : 12586269025

        """
        self.assertEqual(fibonacci_iter(50), 12586269025, "1 + 1 should give 2")
