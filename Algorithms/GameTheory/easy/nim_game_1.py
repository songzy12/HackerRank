# https://www.hackerrank.com/challenges/nim-game-1/problem
#
# https://en.wikipedia.org/wiki/Nim

import os


def nimGame(pile):
    xor_sum = 0
    for stones in pile:
        xor_sum ^= stones

    if xor_sum != 0:
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
