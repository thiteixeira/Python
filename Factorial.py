#-------------------------------------------------------------------------------
# Name:        Factorial
# Purpose:     Compute the factorial of a number
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def factorial(x):
    total = 1
    if int(x) == 0:
        total = 1
    else:
        while x > 0:
            total = total * x
            x -= 1
    print (total)
    return total

factorial(9)