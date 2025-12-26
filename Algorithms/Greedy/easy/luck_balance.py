# https://www.hackerrank.com/challenges/luck-balance/problem

import os


def luckBalance(k, contests):
    result = 0

    important_contests = []
    for l, t in contests:
        if t == 0:
            result += l
        else:
            important_contests.append(l)

    important_contests.sort(reverse=True)
    result += sum(important_contests[:k])
    result -= sum(important_contests[k:])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
