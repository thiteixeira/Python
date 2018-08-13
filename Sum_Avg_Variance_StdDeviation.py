#!/usr/bin/env python
'''
Compute the Sum, Average, Variance, Std Deviation of a list
'''


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


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

print(grades)
print('Sum of grades: ' + str(grades_sum(grades)))
print('Average: ' + str(grades_average(grades)))
print('Variance: ' + str(grades_variance(grades)))
print('Std: ' + str(grades_std_deviation(grades_variance(grades))))
