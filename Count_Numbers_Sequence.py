#-------------------------------------------------------------------------------
# Name:        Count
# Purpose:     Count the numbers in a sequence
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def count(sequence, item):
    total = 0
    for i in range(len(sequence)):
        if sequence[i] == item:
            total += 1
    return total