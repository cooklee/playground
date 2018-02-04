from unittest import TestCase

from mat_functions import fibonacci_iter

class FibonacciIterTests(TestCase):

    def test_fibonacci_zero(self):
        """
        input : 0
        expected result : 0
        :return:
        """
        self.assertEqual(fibonacci_iter(0), 0, "this is from definition")

    def test_fibonacci_one(self):
        """
        input : 1
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(1), 1, "this is from definition")

    def test_fibonacci_two(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(2), 1, "0 + 1 should give 1")

    def test_fibonacci_tree(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(3), 2, "1 + 1 should give 2")

    def test_fibonacci_five(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(5), 5, "1 + 1 should give 2")

    def test_fibonacci_ten(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(10), 55, "1 + 1 should give 2")

    def test_fibonacci_20(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(20), 6765, "1 + 1 should give 2")

    def test_fibonacci_50(self):
        """
        input : 2
        expected result : 1
        :return:
        """
        self.assertEqual(fibonacci_iter(50), 12586269025, "1 + 1 should give 2")
