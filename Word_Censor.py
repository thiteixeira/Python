#-------------------------------------------------------------------------------
# Name:        Word Censor
# Purpose:     Detects a word and changes it to "****"
#
# Author:      thiteixeira
#
# Created:     19/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def censor(text, word):
    words = text.split()        # Split the string into a list

    for i in range(len(words)): # Loop through words
        if words[i] == word:
            words [i] = "*" * len(word)
    return " ".join(words)