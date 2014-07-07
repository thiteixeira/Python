#-------------------------------------------------------------------------------
# Name:
# Purpose:     Print Digits of a Number
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def digit_sum(n):
    n = str(n)
    total = 0
    for letter in n:
        total += int(letter)
    print (total)
    return total

digit_sum(12345)