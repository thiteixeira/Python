#-------------------------------------------------------------------------------
# Name:        Dictionary
# Purpose:     Create and Print a dictionary
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

my_dict = {
    "Name": "Thiago",
    "Age": 30,
    "Student": True
    }

print (my_dict.items())     # Return an array of key/value pair
print (my_dict.keys())      # Return an array of dictionary keys
print (my_dict.values())    # Return an array of dictionary values

for key in my_dict:
    print (my_dict[key], key) # Print the key and the value of the key