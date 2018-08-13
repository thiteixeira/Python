#!/usr/bin/env python
'''
Computer the factorial of a number
'''


def factorial(x):
    total = 1
    if int(x) == 0:
        total = 1
    else:
        while x > 0:
            total = total * x
            x -= 1
    return total


print('9 factorial: ' + str(factorial(9)))
print('5 factorial: ' + str(factorial(5)))