#-------------------------------------------------------------------------------
# Name:        Anti Vowel
# Purpose:     Return a string with no vowels
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def anti_vowel(text):
    no_vowels = []
    for c in text:
        if c not in "aeiouAEIOU":
            no_vowels.append(c)
    return "".join(no_vowels)