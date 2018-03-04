#!/bin/python3

# https://www.hackerrank.com/contests/101hack53/challenges/cut-board
import os
import sys


#
# Complete the fillBoard function below.
#

def fill_row(x1, y1, x2, y2, row=True):
    if row:
        for j in range(y1, y2, 2):
            print(x1, j, x1, j+1)
    else:
        for i in range(x1, x2, 2):
            print(i, y1, i+1, y1)
    
def fillBoard(n, m, x, y):
    # Print the output as described in the output format section.
    if (n * m - x - y) % 2 == 1:
        print("NO")
        return
    if (m - x) % 2 == 1 and (m - y) % 2 == 1 and m % 2 == 0 and n % 2 == 0:
        print('NO')
        return
    print("YES")
    print((m * n - x - y) // 2)
    if (m - x) % 2 == 0 and (m - y) % 2 == 0:
        # even with two even
        fill_row(1, x + 1, 1, m)
        fill_row(n, 1, n, m - y)
        
        if m % 2 == 0:
            for i in range(2, n):
                fill_row(i, 1, i, m)
        else:
            for j in range(1, m + 1):
                fill_row(2, j, n - 1, j, False)
    elif ((m - x) * (m - y)) % 2 == 0:
        # odd with one even, one odd
        if (m - x) % 2 == 1:
            fill_row(n, 1, n, m - y)
            fill_row(1, x + 1, 1, m - 1)
            print(1, m, 2, m)
            for i in range(2, n):
                fill_row(i, 1, i, m - 1)
            fill_row(3, m, n - 1, m, False)
        else:
            fill_row(1, x+1, 1, m)
            fill_row(n, 2, n, m - y)
            print(n, 1, n-1, 1)
            for i in range(2, n):
                fill_row(i, 2, i, m)
            fill_row(2, 1, n - 2, 1, False)
    else:
        fill_row(1, x+1, 1, m - 1)
        print(1, m, 2, m)
        fill_row(n, 2, n, m - y)
        print(n, 1, n - 1, 1)
        if m % 2 == 0:
            fill_row(2, 1, n - 2, 1, False)
            fill_row(3, m, n - 1, m, False)
            
            for i in range(2, n):
                fill_row(i, 2, i, m - 1)
        else:
            fill_row(2, 1, 2, m - 1)
            fill_row(n - 1, 2, n - 1, m)
            for j in range(1, m + 1):
                fill_row(3, j, n - 2, j, False)
    return  

if __name__ == '__main__':
    nmxy = input().split()

    n = int(nmxy[0])

    m = int(nmxy[1])

    x = int(nmxy[2])

    y = int(nmxy[3])

    fillBoard(n, m, x, y)
