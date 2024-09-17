# https://www.hackerrank.com/challenges/two-characters/problem?isFullScreen=true
#
# Just check all possible combinations?

import itertools


def generate_twos(s):
    return itertools.combinations(set(s), 2)


def keep_chars(s, two_set):
    return "".join(filter(lambda c: c in two_set, s))


def is_valid(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


def alternate(s):
    twos = generate_twos(s)
    res = 0
    for two in twos:
        changed_s = keep_chars(s, two)
        if is_valid(changed_s):
            res = max(res, len(changed_s))
    return res
