# https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true

import os
from functools import cmp_to_key


def cmp(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])  # ord
    return 0


def bigSorting(unsorted):
    unsorted.sort(key=cmp_to_key(cmp))  # cmp_to_key
    return unsorted


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write("\n".join(result))
    fptr.write("\n")

    fptr.close()
