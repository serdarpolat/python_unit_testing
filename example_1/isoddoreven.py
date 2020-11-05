
def is_odd_or_even(n):
    if type(n) is int:
        if int(n) % 2 == 0:
            return 'Even'
        else:
            return 'Odd'
    else:
        raise TypeError('Value must be integer')