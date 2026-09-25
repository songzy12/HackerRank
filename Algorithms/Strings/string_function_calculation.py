# https://www.hackerrank.com/challenges/string-function-calculation/problem?isFullScreen=false
#
# Given string t, define
#   f(s) = |s| x (number of times s occurs in t)
# Compute maximum of f(s) among all substrings s of t

import os


def maxValue(t):
    pass


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = input()
        result = maxValue(t)

        fptr.write(str(result) + '\n')
