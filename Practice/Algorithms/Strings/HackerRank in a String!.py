#!/bin/python

import sys

def check(s, p):
    i = 0
    j = 0
    while i < len(p):
        while j < len(s) and s[j] != p[i]:
            j += 1
        if j == len(s):
            break
        i += 1
        j += 1 # for repeated 'r'
    return i == len(p)
   

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    print 'YES'if check(s, 'hackerrank') else 'NO'
        
