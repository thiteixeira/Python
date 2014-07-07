#-------------------------------------------------------------------------------
# Name:        Classes
# Purpose:
#
# Author:      thiteixeira
#
# Created:     22/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Class definition
class Animal(object):
    #pass    # does nothing
    """Makes cute animals."""
    # For initializing our member variables
    is_alive = True
    health = "good"
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def description(self):
        print (self.name)
        print (self.age)


# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)

hippo = Animal("Hippo", 2, False)
hippo.description()

sloth = Animal("Sloth", 3, False)
sloth.description()
ocelot = Animal("Ocelot", 4, False)
ocelot.description()

print (sloth.health)
print (hippo.health)
print (ocelot.health)