# https://www.hackerrank.com/challenges/marcs-cakewalk/problem?isFullScreen=true

import os


def marcsCakewalk(calorie):
    calorie.sort(reverse=True)

    total_miles = 0
    factor = 1
    for i in range(len(calorie)):
        total_miles += factor * calorie[i]
        factor *= 2
    return total_miles


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + "\n")
    fptr.close()
