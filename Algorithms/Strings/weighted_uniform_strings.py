#!/bin/python

import sys

s = raw_input().strip()
from collections import defaultdict

# substring not subsequence

c = defaultdict(int)
count = 0
for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
        if i != 0:
            c[s[i - 1]] = max(count, c[s[i - 1]])
        count = 1
    else:
        count += 1

c[s[-1]] = max(count, c[s[-1]])

n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())

    # your code goes here
    def check():
        for i, t in c.items():
            num = ord(i) - ord('a') + 1
            if x % num == 0 and x / num <= t:
                return True
        return False

    print "Yes" if check() else "No"
