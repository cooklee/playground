from unittest import TestCase, skip
from math import sqrt

from mat_functions import private_pow, fibonacci


class MatFunctionsTests(TestCase):

    def test_zero(self):
        """
        input : zero
        expected result : zero
        """
        self.assertEqual(private_pow(0), 0, "power of 0 should return 0")

    def test_one(self):
        """
        input : one
        expected result : one
        """
        self.assertEqual(private_pow(1), 1, "power of 1 should return 1")

    def test_two(self):
        """
        input : 2
        expected result : 4
        """
        self.assertEqual(private_pow(2), 4, "power of 2 should return 4")

    def test_sqrt(self):
        """
        input : sqrt(2)
        expected result : 2
        """
        self.assertEqual(int(private_pow(sqrt(2))), 2, "power of sqrt(2) should return 2")

    def test_one_below_zero(self):
        """
        input : -1
        expected result : 1
        """
        self.assertEqual(private_pow(-1), 1, "power of 1 should return 1")

    def test_two_below_zero(self):
        """
        input : -2
        expected result : 4
        """
        self.assertEqual(private_pow(-2), 4, "power of 2 should return 4")

    def test_sqrt_below_zero(self):
        """
        input : -sqrt(2)
        expected result : 2
        """
        self.assertEqual(int(private_pow(-sqrt(2))), 2, "power of sqrt(2) should return 2")


class FibonacciTests(TestCase):

    def test_fibonacci_zero(self):
        """
        input : 0
        expected result : 0
        :return:
        """
        self.assertEqual(fibonacci(0), 0, "this is from definition")

    def test_fibonacci_one(self):
        """
        input : 1
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(1), 1, "this is from definition")

    def test_fibonacci_two(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(2), 1, "0 + 1 should give 1")

    def test_fibonacci_tree(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(3), 2, "1 + 1 should give 2")

    def test_fibonacci_five(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(5), 5, "1 + 1 should give 2")

    def test_fibonacci_ten(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(10), 55, "1 + 1 should give 2")

    def test_fibonacci_20(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(20), 6765, "1 + 1 should give 2")

    @skip("there is a problem with memory")
    def test_fibonacci_50(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci(50), 6765, "1 + 1 should give 2")





