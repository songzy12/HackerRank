#!/bin/python

import sys

def inversed_index(arr):
    from collections import defaultdict
    m = defaultdict(list)
    for i, n in enumerate(arr):
        m[n].append(i)
    return m

def compute_(pos, boo, n, t):
    if t == 0:
        ans = 0        
        for i in range(len(pos)):
            if i == 0:
                temp = pos[i]
            else:
                temp = pos[i] - pos[i-1] - 1
            ans += temp * (temp + 1) / 2
        temp = n - pos[-1] - 1
        ans += temp * (temp + 1) / 2
        return ans
            
    ans = 0
    i = 0
    num_true = 0
    num_false = 0
    while i < t:
        if boo[i]:
            num_true += 1
        else:
            num_false += 1
        i += 1

    
    while i < len(pos):
        # compute num_true, num_false in pos[i-t:i]
        if num_true == num_false:
            left = (pos[i-t-1] + 1) if i-t-1 >= 0 else 0
            left_ = pos[i-t]
            right_ = pos[i-1]
            right = pos[i] - 1
            ans += (left_-left+1)*(right-right_+1)
        
        if boo[i]:
            num_true += 1
        else:
            num_false += 1
        if boo[i-t]:
            num_true -= 1
        else:
            num_false -= 1
        i += 1

    if num_true == num_false:
        left = pos[i-t-1] + 1 if i-t-1 >= 0 else 0
        left_ = pos[i-t]
        right_ = pos[i-1]
        right = n-1
        ans += (left_-left+1)*(right-right_+1)
    return ans
        

def compute(pos, boo, n):
    if not pos:
        return n * (n + 1) / 2

    ans = 0
    t = 0
    while t <= len(pos):
        temp = compute_(pos, boo, n, t)
        ans += temp
        t += 2
    return ans
    

if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = map(int, raw_input().strip().split(' '))

    m = inversed_index(arr)
    
    for a0 in xrange(q):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]

        if x == y: # notice this
            pos = []
        else:
            pos = sorted(m[x] + m[y])
        boo = map(lambda t: arr[t] == x, pos)
        
        print compute(pos, boo, len(arr))
