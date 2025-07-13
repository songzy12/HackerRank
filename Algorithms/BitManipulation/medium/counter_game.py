# https://www.hackerrank.com/challenges/counter-game/problem?isFullScreen=false

import os


def counterGame(n):
    count = 0

    # First count tailing 0s of n
    while n & 1 == 0:
        n = n >> 1
        count += 1

    # Then drop the last 1
    n = n >> 1

    # Then count number of 1s of remaining n
    while n != 0:
        if n % 2 & 1 == 0:
            n = n >> 1
            continue
        n = n >> 1
        count += 1

    return "Richard" if count & 1 == 0 else "Louise"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')
    fptr.close()
