"""
This snippet can be used to randomize the order of the elements in a list. Note that shuffle works in place, and returns None.
"""

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
print(foo)  # [2, 1, 4, 3] , foo = [1, 2, 3, 4]
