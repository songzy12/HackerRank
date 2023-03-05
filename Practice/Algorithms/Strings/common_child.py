#!/bin/python

import sys

def commonChild(s1, s2):
    # Complete this function

    # dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

    if len(s1) < len(s2): # make sure len(s2) is smaller
        s1, s2 = s2, s1
    dp = [[0 for i in range(len(s2)+1)] for j in range(2)]
    for i in range(len(s2)+1):
        dp[0][i] = dp[1][i] = 0
    #for i in range(len(s2)+1):
    #    dp[0][i] = 0

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                # max is slow, use if else
                dp[i%2][j] = max([dp[i%2][j-1], dp[(i+1)%2][j], dp[(i+1)%2][j-1] + 1])
            else:
                dp[i%2][j] = max(dp[i%2][j-1], dp[(i+1)%2][j])
    return dp[len(s1)%2][-1] # not dp[-1][-1]

s1 = raw_input().strip()
s2 = raw_input().strip()
result = commonChild(s1, s2)
print(result)

# no need to generate the whole dp array
