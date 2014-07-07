#-------------------------------------------------------------------------------
# Name:        Median
# Purpose:     Find a median in a list
#
# Author:      thiteixeira
#
# Created:     20/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def median(my_list):
    my_list.sort()             # Sort the list
    center = len(my_list) / 2.0
    if center == int(center):
        combined = float(my_list[int(center) - 1]) + float(my_list[int(center)])
        average = combined / 2.0
        return average
    else:
        return my_list[int(center - 0.5)]