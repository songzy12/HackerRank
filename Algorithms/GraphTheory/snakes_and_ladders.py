# https://www.hackerrank.com/challenges/the-quickest-way-up/problem?isFullScreen=true
#
# How to run:
#   export OUTPUT_PATH=/tmp/output.txt
#   python3 snakes_and_ladders.py < in.txt
#   cat $OUTPUT_PATH
import math
import os
import random
import re
import sys


def quickestWayUp(ladders, snakes):
    # TODO: Write your code here
    return 0


if __name__ == '__main__':
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        t = int(input().strip())

        for t_itr in range(t):
            n = int(input().strip())
            ladders = []
            for _ in range(n):
                ladders.append(list(map(int, input().rstrip().split())))

            m = int(input().strip())
            snakes = []
            for _ in range(m):
                snakes.append(list(map(int, input().rstrip().split())))

            result = quickestWayUp(ladders, snakes)
            fptr.write(str(result) + '\n')
