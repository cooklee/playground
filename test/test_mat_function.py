from unittest import TestCase
from math import sqrt

from math_functions.mat_functions import private_pow, Fibonacci


class MatFunctionsTests(TestCase):

  pass


class FibonacciTests(TestCase):

    def test_zero(self):
        input = 0
        expected_result = 0
        self.assertEqual(Fibonacci.fibonacci(0), 0 )


