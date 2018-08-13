#!/usr/bin/env python
'''
Returns a string with no vowels
'''


def anti_vowel(text):
    no_vowels = []
    for c in text:
        if c not in "aeiouAEIOU":
            no_vowels.append(c)
    return "".join(no_vowels)


astring = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\
          's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to'\
          'make a type specimen book. It has survived not only five centuries, but also the leap into electronic typese'\
          'tting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets c'\
          'ontaining Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker inclu'\
          'ding versions of Lorem Ipsum'
print(anti_vowel(astring))