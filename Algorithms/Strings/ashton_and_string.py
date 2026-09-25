# https://www.hackerrank.com/challenges/ashton-and-string/problem?isFullScreen=false
#
# Problem:
#   Arrange all the distinct substrings of a given string s in lexicographical order and concatenate them.
#   Print the k-th character of the concatenated string.

import math
import os
import random
import re
import sys


def ashtonString(s, k):
    # Write your code here
    pass


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    t = int(input().strip())
    for t_itr in range(t):
        s = input()
        k = int(input().strip())

        res = ashtonString(s, k)

        fptr.write(str(res) + "\n")
    fptr.close()
