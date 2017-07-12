#!/bin/python

import sys


def match(G, P):
    def check(i, j):
        for t in range(len(P)):
            for s in range(len(P[0])):
                if G[i+t][j+s] != P[t][s]:
                    return False
        return True
        
    for i in range(len(G)-len(P)+1): # +1 is important
        for j in range(len(G[0]) - len(P[0])+1): 
            if check(i, j):
                return True
    return False


t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)
    print "YES" if match(G, P) else "NO"
        
