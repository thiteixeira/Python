#-------------------------------------------------------------------------------
# Name:        Car Class
# Purpose:
#
# Author:      thiteixeira
#
# Created:     23/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return 'This is a '+self.color+' '+self.model+' with '+str(self.mpg)+' MPG.'

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()