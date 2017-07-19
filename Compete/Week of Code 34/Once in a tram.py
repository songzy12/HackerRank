#!/bin/python

import sys

##1. next pre is str(int(x[:3])+1)
##2. next lucky is not pre * 2
##3. next lucky is not pre + ''.join(sorted(pre))

def onceInATram(x):
    def check(t):
        t = str(t)
        return sum([int(a) for a in t[:3]]) == sum([int(a) for a in t[-3:]])
    
    for t in range(int(x)+1, 1000000):
        if check(t):
            return t
        
if __name__ == "__main__":
    x = raw_input().strip()
    result = onceInATram(x)
    print result
