# https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem?isFullScreen=true
#
# First sort the sticks in non-decreasing order.
# Then let there be 3 pointers p1, p2, and p3.
# For any fixed p1 and p2, p3 would be the furthest one that < p1 + p2.
# Since we want the maximum perimeter, we start checking from the back.
#
# Then, by running a few steps of simulation, we can realize that only check the
# neighboring 3 sticks is sufficient. And a proof is straightforward.

import os


def maximumPerimeterTriangle(sticks):
    sticks.sort()

    for i in range(len(sticks) - 1, 1, -1):
        if sticks[i] < sticks[i - 1] + sticks[i - 2]:
            return [sticks[i - 2], sticks[i - 1], sticks[i]]
    return [-1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")
    fptr.close()
