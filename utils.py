#!/usr/bin/python3
"""
utility module
"""


def clean(value):
    """ Clean string of extra space """
    j = 0
    i = value.index("=", j)
    print(i)
    try:
        while (i):
            i = value.index("=", j)
            print(i)
            i = i - 1
            while (i >= 0 and value[i] == " "):
                value = value[0:i] + value[i + 1:]
                i = i - 1
            i = value.index("=", j) + 1
            while (i < len(value) and value[i] == " "):
                value = value[0:i] + value[i + 1:]
            j = i + 1
    except ValueError:
        pass
    cleaned = []
    for i in value.split(" "):
        if i:
            cleaned.append(i)
    return cleaned
