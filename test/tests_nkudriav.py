class FibonacciTests(TestCase):

# test for recurent fibonacci
    def test_input_recur_0(self):
        input = 0
        expected_result = 0
        self.assertEqual(Fibonacci.fibonacci(input), expected_result)

    def test_input_recur_1(self):
        input = 1
        expected_result = 1
        self.assertEqual(Fibonacci.fibonacci(input), expected_result)

    def test_input_recur_2(self):
        input = 2
        expected_result = 1
        self.assertEqual(Fibonacci.fibonacci(input), expected_result)

    def test_input_recur_negative(self):
        input = -1
        expected_result = None
        self.assertEqual(Fibonacci.fibonacci(input), expected_result)

# test for iterative fibonacci
    def test_input_iter_0(self):
        input = 0
        expected_result = 0
        self.assertEqual(Fibonacci.fibonacci_iter(input), expected_result)

    def test_input_iter_1(self):
        input = 1
        expected_result = 1
        self.assertEqual(Fibonacci.fibonacci_iter(input), expected_result)

    def test_input_iter_2(self):
        input = 2
        expected_result = 1
        self.assertEqual(Fibonacci.fibonacci_iter(input), expected_result)

    def test_input_iter_negative(self):
        input = -1
        expected_result = None
        self.assertEqual(Fibonacci.fibonacci_iter(input), expected_result)
