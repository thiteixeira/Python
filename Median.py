#!/usr/bin/env python


def median(my_list):
    my_list.sort()             # Sort the list
    center = len(my_list) / 2.0
    if center == int(center):
        combined = float(my_list[int(center) - 1]) + float(my_list[int(center)])
        average = combined / 2.0
        return average
    else:
        return my_list[int(center - 0.5)]


alist = [x for x in range(10)]
print(alist)
print('Median is: ' + str(median(alist)))
