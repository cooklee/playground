

def private_pow(a):
    return a*a


def fibonacci(number):
    if number == 0 or number == 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def fibonacci_iter(number):
    if number == 0 or number == 1:
        return number
    n_minus_two = 0
    n_minus_one = 1
    for i in range(2, number+1):
        result = n_minus_two + n_minus_one
        n_minus_two = n_minus_one
        n_minus_one = result
    return result
