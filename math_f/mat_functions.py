

def private_pow(a):
    return a*a


class Fibonacci(object):
    number_of_execution = 0

    @staticmethod
    def fibonacci(number):
        if number < 0:
            return None
        Fibonacci.number_of_execution += 1
        if number == 0 or number == 1:
            return number
        return Fibonacci.fibonacci(number - 1) + Fibonacci.fibonacci(number - 2)

    @staticmethod
    def fibonacci_iter(number):
        if number < 0:
            return None
        if number == 0 or number == 1:
            return number
        n_minus_two = 0
        n_minus_one = 1
        for i in range(2, number+1):
            result = n_minus_two + n_minus_one
            n_minus_two = n_minus_one
            n_minus_one = result
        return result
