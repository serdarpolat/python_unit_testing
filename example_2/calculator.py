import math


def add(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not add by not a number')

    if type(y) not in [int, float]:
        raise TypeError('Can not add by not a number')

    return x + y


def subtract(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not subtract by not a number')

    if type(y) not in [int, float]:
        raise TypeError('Can not subtract by not a number')

    return x - y


def multiply(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not multiply by not a number')

    if type(y) not in [int, float]:
        raise TypeError('Can not multiply by not a number')

    return x * y


def divide(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not divide by not a number')

    if type(y) not in [int, float]:
        raise TypeError('Can not divide by not a number')

    if y == 0:
        raise ValueError('Can not divide by zero')

    return x / y


def sin_as_degree(x):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate sin of not a number')

    y = x * 0.01745329252
    return round(math.sin(y), 2)


def cos_as_degree(x):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate cos of not a number')

    y = x * 0.01745329252
    return round(math.cos(y), 2)


def tan_as_degree(x):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate tan of not a number')

    y = x * 0.01745329252
    return round(math.tan(y), 2)


def log(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate tan of not a number')

    if y == 1:
        ZeroDivisionError('Division by 0 error')

    if x <= 0 or y <= 0:
        raise ValueError('Values must be greater than 0')

    return round(math.log(x, y), 2)


def square_root(x):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate tan of not a number')

    if x < 0:
        raise ValueError('Values can not be less then 0')

    return round(math.sqrt(x), 3)


def power(x, y):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate tan of not a number')

    if x < 0 and type(y) is float:
        raise ValueError('If you want to take power of a negative number, power must be integer')

    return round(math.pow(x, y), 3)


def factorial(x):
    if type(x) is not int:
        raise TypeError('Can not calculate tan of not a number')

    if x < 0:
        raise ValueError('Values must be 0 or greater than 0')

    return math.factorial(x)


def circle_area(x):
    if type(x) not in [int, float]:
        raise TypeError('Can not calculate Circle are by not a number radius')

    if x <= 0:
        raise ValueError('Radius can not be 0 or negative value')

    return math.pi * x ** x

