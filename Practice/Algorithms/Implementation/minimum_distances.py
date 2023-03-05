#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

from collections import defaultdict

m = defaultdict(list)
for i, a in enumerate(A):
    m[a].append(i)
ans = 1000
for indice in m.values():
    temp = [indice[i] - indice[i-1] for i in range(1, len(indice))]
    if temp:
        ans = min(ans, min(temp))
print ans if ans != 1000 else -1
