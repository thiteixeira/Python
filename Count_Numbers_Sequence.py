#!/usr/bin/env python
'''
Count the number of occurrences in a list
'''

import numpy as np


def count(sequence, item):
    total = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            total += 1
    return total


alist = [np.random.randint(0,10) for _ in range(25)]
print(count(alist,alist[2]))