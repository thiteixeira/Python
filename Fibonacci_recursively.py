#!/usr/bin/env python


def fibonacci(n):
    print("fibonacci: "+str(n))
    if n < 2:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))


fibonacci(5)
