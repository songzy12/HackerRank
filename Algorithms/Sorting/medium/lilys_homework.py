# https://www.hackerrank.com/challenges/lilys-homework/problem
#
# Compute the minimum number of swaps required to make an array sorted.

import os


def compute_target_index(arr):
    target_index = {}
    for i, e in enumerate(sorted(enumerate(arr), key=lambda x: x[1])):
        target_index[e[0]] = i
    return target_index


def compute_cycle_length(start, target_index, visited):
    length = 0

    current = start
    while current not in visited:
        visited.add(current)
        current = target_index[current]
        length += 1
    return length


def compute_min_swaps(arr):
    target_index = compute_target_index(arr)
    visited = set()

    swaps = 0
    for i in range(len(arr)):
        if i in visited:
            continue
        cycle_length = compute_cycle_length(i, target_index, visited)
        swaps += cycle_length - 1
    return swaps


def lilysHomework(arr):
    return min(compute_min_swaps(arr), compute_min_swaps(arr[::-1]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
