from unittest import TestCase
from math import sqrt

from math_f.mat_functions import private_pow, Fibonacci


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

    def setUp(self):
        pass

    def tearDown(self):
        Fibonacci.number_of_execution = 0

    def test_fibonacci_zero(self):

        """
        input : 0
        expected result : 0
        """
        self.assertEqual(Fibonacci.fibonacci(0), 0, "this is from definition")

    def test_fibonacci_one(self):
        """
        input : 1
        expected result : 1

        """
        self.assertEqual(Fibonacci.fibonacci(1), 1, "this is from definition")

    def test_fibonacci_two(self):
        """
        input : 2
        expected result : 1

        """
        self.assertEqual(Fibonacci.fibonacci(2), 1, "0 + 1 should give 1")

    def test_fibonacci_tree(self):
        """
        input : 3
        expected result : 2

        """
        self.assertEqual(Fibonacci.fibonacci(3), 2, "1 + 1 should give 2")

    def test_fibonacci_five(self):
        """
        input : 5
        expected result : 5

        """
        self.assertEqual(Fibonacci.fibonacci(5), 5, "1 + 1 should give 2")

    def test_fibonacci_ten(self):
        """
        input : 10
        expected result : 55
        """
        self.assertEqual(Fibonacci.fibonacci(10), 55, "1 + 1 should give 2")

    def test_fibonacci_20(self):
        """
        input : 20
        expected result : 6765
        """
        self.assertEqual(Fibonacci.fibonacci(20), 6765, "1 + 1 should give 2")

    def test_fibonacci_30(self):
        """
        input : 30
        expected result : 832040
        """
        self.assertEqual(Fibonacci.fibonacci(30), 832040, "1 + 1 should give 2")





