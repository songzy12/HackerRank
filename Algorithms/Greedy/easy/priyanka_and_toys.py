# https://www.hackerrank.com/challenges/priyanka-and-toys/problem?isFullScreen=true


import os


def find_next(w, index, current_limit):
    while index < len(w):
        if w[index] <= current_limit:
            index += 1
        else:
            break
    return index


def toys(w):
    w.sort()

    containers = 0
    index = 0
    while index < len(w):
        containers += 1
        limit = w[index] + 4
        index = find_next(w, index, limit)
    return containers


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input().strip())
    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + "\n")
    fptr.close()
