#-------------------------------------------------------------------------------
# Name:        Reverse
# Purpose:     Reverse a String
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def reverse(text):
    new_list = []
    reverselist = list(text)
    while len(reverselist) > 0:
        new_list.insert(0,reverselist[0])
        del(reverselist[0])
    return "".join(new_list)