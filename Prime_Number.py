#!/usr/bin/env python


def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

alist = [i for i in range(100)]
for i in range(len(alist)):
    if is_prime(i):
        print(i)
