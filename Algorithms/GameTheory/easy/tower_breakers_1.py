# https://www.hackerrank.com/challenges/tower-breakers-1/problem
#
# Key observation:
#   This game is equivalent to a Nim game where there are n piles of t stones each.
#   Here t is the number of prime factors of m (with multiplicity).
#
# Recall that the losing condition for a Nim game is that the XOR of all pile sizes is 0.
# In our case, since all piles have the same size t, the XOR is 0 if and only if n is even or t is 0.

#!/bin/python3

import os


def towerBreakers(n, m):
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
