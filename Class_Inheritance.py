#-------------------------------------------------------------------------------
# Name:        Class Inheritance
# Purpose:
#
# Author:      thiteixeira
#
# Created:     23/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        self.hours = hours
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Employee_Name")

print (milton.employee_name)
print (milton.full_time_wage(10))