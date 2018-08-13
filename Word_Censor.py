#!/usr/bin/env python
'''
Detects a word and changes it to "****"
'''


def censor(text, word):
    words = text.split()        # Split the text into a list of words

    for i in range(len(words)): # Loop through words
        if words[i] == word:
            words[i] = "*" * len(word)
    return " ".join(words)


text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '\
       'the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of '\
       'type and scrambled it to make a type specimen book. It has survived not only five centuries, but also '\
       'the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s '\
       'with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop '\
       'publishing software like Aldus PageMaker including versions of Lorem Ipsum.'
word = 'Lorem'

print(censor(text, word))
