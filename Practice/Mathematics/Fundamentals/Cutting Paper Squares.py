#!/bin/python3

import sys

def solve(n, m):
    # Complete this function
    return n * m - 1 # one cut for one piece
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
result = solve(n, m)
print(result)
