#-------------------------------------------------------------------------------
# Name:        Sum, Average, Variance, Std Deviation
# Purpose:     Compute the Sum, Average, Variance, Std Deviation of a list
#
# Author:      thiteixeira
#
# Created:     21/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    variance = 0.0
    average = grades_average(scores)
    for score in scores:
        variance += (average - score) ** 2.0
    return variance / float(len(scores))

def grades_std_deviation(variance):
    return variance ** 0.5

print (print_grades(grades))
print (grades_sum(grades))
print (grades_average(grades))
print (grades_variance(grades))
variance = grades_variance(grades)
print (grades_std_deviation(variance))