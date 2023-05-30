#!/bin/python

import sys

q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    M = []
    for M_i in xrange(n):
        M_temp = map(int, raw_input().strip().split(' '))
        M.append(M_temp)
    set1 = [sum(x) for x in M]
    set2 = [sum(x) for x in zip(*M)]
    print "Possible" if sorted(set1) == sorted(set2) else "Impossible"
