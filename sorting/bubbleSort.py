#!/usr/bin/env python

import random 


def bubbleSort(a):
    swaps = 0
    while True:
        isSorted = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
                isSorted = True
        
        if not isSorted:
            break

    print('Array is sorted in {} swaps.'.format(swaps))  
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))


if __name__ == '__main__':
    n = 5  # increase this number by orders of magnitude to see how bad this algorithm performs
    arr = [random.randint(0,100) for _ in range(n)]
    print(arr)
    bubbleSort(arr)
