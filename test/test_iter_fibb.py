from unittest import TestCase
from math_functions.mat_functions import Fibonacci

fibonacci_iter = Fibonacci.fibonacci_iter


class TestFibonacciIter(TestCase):

   def test_first_iter(self):
      input = [0, 1, 2, 3, 4, 5, 6, 7]
      expected_result = [0, 1, 1, 2, 3, 5, 8, 13]

      for single_input, single_expected in zip(input, expected_result):
         self.assertEqual(Fibonacci.fibonacci_iter(single_input), single_expected)

