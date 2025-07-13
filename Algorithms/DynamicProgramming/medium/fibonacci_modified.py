# https://www.hackerrank.com/challenges/fibonacci-modified/problem?isFullScreen=true

import os
import sys
sys.set_int_max_str_digits(200000)


def fibonacciModified(t1, t2, n):
    for i in range(3, n+1):
        t3 = t2 * t2 + t1
        t1 = t2
        t2 = t3
    return t3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    t1 = int(first_multiple_input[0])
    t2 = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')
    fptr.close()
