# https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


def surfaceArea(A):
    res = 2 * len(A) * len(A[0])
    for i in range(len(A)):
        res += A[i][0] + A[i][len(A[0]) - 1]
    for i in range(len(A)):
        for j in range(len(A[0]) - 1):
            res += abs(A[i][j + 1] - A[i][j])

    for j in range(len(A[0])):
        res += A[0][j] + A[len(A) - 1][j]

    for j in range(len(A[0])):
        for i in range(len(A) - 1):
            res += abs(A[i + 1][j] - A[i][j])
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')
    fptr.close()
