#-------------------------------------------------------------------------------
# Name:        List Slicing Syntax
# Purpose:
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

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print (l[2:9:2])    # [start:end:stride]

print (l[::-1])     # Print list in a reverse way