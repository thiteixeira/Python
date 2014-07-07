#-------------------------------------------------------------------------------
# Name:        Purify
# Purpose:     Remove odd numbers from a list
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def purify(numbers):
    evens = []
    for i in numbers:
        if (i % 2) == 0:
            evens.append(i)
    return evens