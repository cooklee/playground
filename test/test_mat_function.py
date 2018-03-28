from unittest import TestCase
from math import sqrt


from math_functions.mat_functions import private_pow, Fibonacci


class MatFunctionsTests(TestCase):

  pass


class FibonacciTests(TestCase):
    def test_first_tc(self):
        input = [0,1,2,3,4,5,6,7]
        expected_result = [0,1,1,2,3,5,8,13]

        for single_input, single_expected in zip(input, expected_result):
            self.assertEqual(Fibonacci.fibonacci(single_input),single_expected)


    def test_zero(self):
        input = 0
        expected = 0
        self.assertEqual(Fibonacci.fibonacci(input),expected)


