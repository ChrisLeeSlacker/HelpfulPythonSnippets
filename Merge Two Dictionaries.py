"""
The following method can be used to merge two dictionaries.
"""


def merge_two_dicts(a, b):
    # Make a copy of a
    c = a.copy()
    # Modify keys and values of a with the ones from b
    c.update(b)
    return c


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_two_dicts(a, b))  # {'y': 3, 'x': 1, 'z': 4}


# Or you can do this in Python 3.5 <
def merge_dictionaries(a, b):
    return {**a, **b}


a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
print(merge_dictionaries(a, b))  # {'y': 3, 'x': 1, 'z': 4}
