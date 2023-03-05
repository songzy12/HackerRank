#!/bin/python

import sys

def palindromeIndex(s):
    # Complete this function
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i >= j:
        return -1
    # the answer is i or j
    i0 = i
    j0 = j
    
    i += 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if i >= j:
        return i0
    return j0

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)

