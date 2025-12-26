#!/bin/python3

import os


def gridChallenge(grid):
    for row in range(len(grid)):
        grid[row] = ''.join(sorted(grid[row]))
        for col in range(len(grid[0])):
            if row > 0 and grid[row][col] < grid[row - 1][col]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
