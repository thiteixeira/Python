#!/usr/bin/env python

'''
Lists
'''
from random import *

# One dimensional list
list1 = []

for i in range(5):
    var = randint(1, 100)
    list1.append(var)
    list1.sort()

print('List-1: ' + str(list1))


# Two dimensional list
n = 5
list2 = [[] for x in range(n)]
for i in range(5):
    var = randint(1, 100)
    list2[i].append(var)

print('List-2: ' + str(list2))


# Numpy array
import numpy as np

a = np.array([[1,2,3],[4,5,6]]) 
print('Numpy Array: ')
print(a)

for i in range(5):
    var = randint(1, 100)
    a = np.append(a, var)
print(a)
