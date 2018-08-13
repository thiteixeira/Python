#!/usr/bin/env python
'''
Reverse a string
'''


def reverse(text):
    new_list = []
    reverselist = list(text)
    while len(reverselist) > 0:
        new_list.insert(0,reverselist[0])
        del(reverselist[0])
    return "".join(new_list)


astring = 'Pineapple'
print('My string:\t' + astring)
print('Reversed:\t' + reverse(astring))