#-------------------------------------------------------------------------------
# Name:        Anonymous Functions
# Purpose:     Lambda Syntax
#
# Author:      thiteixeira
#
# Created:     21/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

my_list = range(16)
print (filter(lambda x: x % 3 == 0, my_list))


languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (filter(lambda x: x == "Python", languages))


squares = [x**2 for x in range(1, 11)]
print (filter(lambda x: x >= 30 and x <= 70, squares))