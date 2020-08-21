def dictSwitch(x):
    case_dict = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    default_value = -1
    return case_dict.get(x, default_value)


# Or we can optimize the code

def dictSwitchOptimized(x):
    return {
        "a": 1,
        "b": 2,
        "c": 3
    }.get(x, -1)
