"""
You can have an else clause as part of a try/except block, which is executed if no exception is thrown.
"""

try:
    2 * 3
except TypeError:
    print("An exception was raised")
else:
    print("No exceptions were raised.")

# No exceptions were raised.
