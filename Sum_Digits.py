#!/usr/bin/env python
'''
Print the sum of the digits of a number
'''


def digit_sum(n):
    n = str(n)
    total = 0
    for letter in n:
        total += int(letter)
    return total


print(digit_sum(12345))