"""
This snippet can be used to check the memory usage of an object.
"""

import sys

variable = 'Slacker'
print(sys.getsizeof(variable))  # 56
