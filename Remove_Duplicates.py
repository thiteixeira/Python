#-------------------------------------------------------------------------------
# Name:        Remove Duploicates
# Purpose:     Remove duplicates in a list
#
# Author:      thiteixeira
#
# Created:     20/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def remove_duplicates(numbers):
    numbers = list(numbers)
    new_list = []
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list