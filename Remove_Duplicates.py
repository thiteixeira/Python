#!/usr/bin/env python

import numpy as np

def remove_duplicates(numbers):
    numbers = list(numbers)
    new_list = []
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list


alist = [np.random.randint(0,10) for _ in range(25)]
print('alist: ' + str(alist))
print('w/o dups: ' + str(remove_duplicates(alist)))