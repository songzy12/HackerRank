#!/bin/python

import sys

# DFS will TLE, as well as too deep recursion

t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]

    valid = [True] * (n + 1)  # range

    def compute(n, k):
        if k == 0:
            return range(1, n + 1)
        # just a permutaion grouped by 2k.
        if n % (2 * k) != 0:
            return []
        ans = []
        for i in range(n / (2 * k)):
            # [i * 2k, (i+1)*2k)
            ans += range(i * (2 * k) + k + 1, (i + 1) * (2 * k) + 1)
            ans += range(i * (2 * k) + 1, i * (2 * k) + k + 1)
        return ans

##    def compute(n, k):
##
##        def dfs(cur_list, index):
##            # print cur_list, index
##            if index == n + 1:
##                return cur_list
##            for t in [-k, k]:
##                # valid range
##                if index + t >= 1 and index + t <= n and valid[index + t]:
##                    valid[index + t] = False
##
##                    temp = dfs(cur_list + [index + t], index + 1)
##                    if temp:
##                        return temp
##
##                    valid[index + t] = True
##            return None
##
##
##        ans = dfs([], 1)
##        return ans

    ans = compute(n, k)
    if ans:
        for t in ans:
            print t,
        print
    else:
        print -1
