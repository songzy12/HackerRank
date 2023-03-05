#!/bin/python

import sys

s = raw_input().strip()


def compute(s):
    r = c = int(len(s)**0.5)
    for i in range(2):
        for j in range(i, 2):
            if (r + i) * (c + j) >= len(s):
                return r + i, c + j


n_row, n_col = compute(s)
ans = []
for i in range(n_row):
    ans.append(s[i * n_col:(i + 1) * n_col])
res = []
for i in range(n_col):
    res.append([x[i] if i < len(x) else '' for x in ans])
res = [''.join(x) for x in res]

print ' '.join(res)
