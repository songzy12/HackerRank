# https://www.hackerrank.com/challenges/the-quickest-way-up/problem?isFullScreen=true
#
# How to run:
#   export OUTPUT_PATH=/tmp/output.txt
#   python3 snakes_and_ladders.py < in.txt
#   cat $OUTPUT_PATH
#
# Build a directed graph with 3 kinds of edges:
# 1. for each node n, 6 edges that points to n+1, n+2, ..., n+6
# 2. for each snake, ...
# 3. for each ladder, ...
# Then, run shortest path algorithm on the built graph.

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
