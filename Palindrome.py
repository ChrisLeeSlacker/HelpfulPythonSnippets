"""
This method checks whether a given string is a palindrome.
"""


def palindrome(a):
    return a == a[::-1]


palindrome('kajak')  # True
