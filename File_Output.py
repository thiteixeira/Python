#!/usr/bin/env python


# writing to a file
with open('text.txt', 'w') as my_file:
    my_file.write('This is the first line!\n')
    my_file.write('This is the second line!\n')


# reading from a file
with open('text.txt', 'r') as f:
    # one line at a time
    print(f.readline())
