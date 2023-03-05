#!/bin/python

import sys

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(int, raw_input().strip().split(' '))
c.sort()
ans = max(c[0], n - 1 - c[-1])
for i in range(len(c) - 1):
    ans = max(ans, (c[i + 1] - c[i]) / 2)
print ans
