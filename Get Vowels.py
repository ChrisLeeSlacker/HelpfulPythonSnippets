"""
This method gets vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’, 'y', 'æ', 'ø', 'å') found in a string.
"""


def getVowels(string):
    return [each for each in string if each in 'aeiou']


getVowels('foobar')  # ['o', 'o', 'a']
getVowels('gym')  # []
