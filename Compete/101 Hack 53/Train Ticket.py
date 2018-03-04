#!/bin/python3

import os
import sys


#
# Complete the berthType function below.
#
def berthType(n):
    # Return the type of berth as described in the output format section.
    n = (n - 1) % 8 + 1
    if n == 1 or n == 4:
        return 'LB'
    elif n == 2 or n == 5:
        return 'MB'
    elif n == 3 or n == 6:
        return 'UB'
    elif n == 7:
        return 'SLB'
    else:
        return 'SUB'
        

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = berthType(n)

    f.write(result + '\n')

    f.close()
