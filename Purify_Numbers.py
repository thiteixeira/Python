#!/usr/bin/env python
'''
Remove odd numbers from a list
'''
import numpy as np


def purify(numbers):
    evens = []
    for i in numbers:
        if (i % 2) == 0:
            evens.append(i)
    return evens

alist = [np.random.randint(0,10) for _ in range(25)]
print('Original: ' + str(alist))
print('Purified: ' + str(purify(alist)))
