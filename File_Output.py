#-------------------------------------------------------------------------------
# Name:        File Output
# Purpose:
#
# Author:      thiteixeira
#
# Created:     23/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

    my_list = [i**2 for i in range(1,11)]
    # Generates a list of squares of the numbers 1 - 10

    f = open("output.txt", "w")

    for item in my_list:
        f.write(str(item) + "\n")

    print (f.readline())        # Read line by line
    print (f.readline())
    print (f.readline())

    f.close()

    # This method automatically closes the file
    with open("text.txt", "w") as my_file:
	   my_file.write("This is my data!")