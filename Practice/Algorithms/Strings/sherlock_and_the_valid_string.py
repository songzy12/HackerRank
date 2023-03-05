#!/bin/python

import sys


def isValid(s):
    # Complete this function
    from collections import Counter
    c = Counter(s)
    c = Counter(c.values())
    if len(c) == 1:
        return True
    if len(c) > 2:
        return False
    a, b = sorted(c.keys())
    if b - a == 1 and c[b] == 1:
        return True
    if a == 1 and c[a] == 1:  # another case
        return True
    return False


s = raw_input().strip()
result = isValid(s)
print("YES" if result else "NO")
