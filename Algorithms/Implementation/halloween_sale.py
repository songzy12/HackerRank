# https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    res = 0
    while p > m and s >= p:
        s -= p
        p -= d
        res += 1
    p = max(p, m)
    if s >= p:
        res += s // p
    return res


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        first_multiple_input = input().rstrip().split()

        p = int(first_multiple_input[0])
        d = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        s = int(first_multiple_input[3])

        answer = howManyGames(p, d, m, s)

        fptr.write(str(answer) + '\n')
