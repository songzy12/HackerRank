# https://www.hackerrank.com/challenges/build-a-string/problem?isFullScreen=false
#
# Greg wants to build a string, S of length N.
#
# Starting with an empty string, he can perform 2 operations:
# 1. Add a character to the end of S for A dollars.
# 2. Copy any substring of S, and then add it to the end of S for B dollars.
#
# Calculate minimum amount of money Greg needs to build S.
#
# Idea: at each step we find the longest string s that both is
# 1. substring of already built S_a
# 2. prefix of remaining to build S_b
# And then compare the cost of B and A * len(s) to append s to S_a.

import os


def buildString(a, b, s):
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        a = int(first_multiple_input[1])
        b = int(first_multiple_input[2])
        s = input()

        result = buildString(a, b, s)

        fptr.write(str(result) + "\n")
    fptr.close()
